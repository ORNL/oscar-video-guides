#!/usr/bin/env python3
"""Validate NVENC H.264 workflow video guides, captions, and hygiene invariants."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

FORBIDDEN_PATTERNS = [
    re.compile(r"\b192\.168\.\d{1,3}\.\d{1,3}\b"),
    re.compile(r"\b10\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"),
    re.compile(r"\b172\.(?:1[6-9]|2\d|3[01])\.\d{1,3}\.\d{1,3}\b"),
]


def run_ffprobe(mp4_path: Path) -> dict:
    cmd = [
        "ffprobe",
        "-hide_banner",
        "-loglevel",
        "error",
        "-show_format",
        "-show_streams",
        "-of",
        "json",
        str(mp4_path),
    ]
    out = subprocess.check_output(cmd, text=True)
    return json.loads(out)


def get_keyframes(mp4_path: Path) -> list[float]:
    cmd = [
        "ffprobe",
        "-hide_banner",
        "-loglevel",
        "error",
        "-select_streams",
        "v:0",
        "-skip_frame",
        "nokey",
        "-show_entries",
        "frame=pts_time",
        "-of",
        "csv=p=0",
        str(mp4_path),
    ]
    out = subprocess.check_output(cmd, text=True)
    pts = []
    for line in out.splitlines():
        val = line.strip().rstrip(",")
        if val:
            pts.append(float(val))
    return pts


def verify_mp4(mp4_path: Path, captions_dir: Path | None) -> list[str]:
    errors: list[str] = []
    info = run_ffprobe(mp4_path)
    streams = info.get("streams", [])
    v_streams = [s for s in streams if s.get("codec_type") == "video"]
    s_streams = [s for s in streams if s.get("codec_type") == "subtitle"]

    if len(v_streams) != 1:
        return [f"{mp4_path.name}: expected 1 video stream, found {len(v_streams)}"]

    vs = v_streams[0]
    encoder_tag = vs.get("tags", {}).get("encoder", "")
    if "h264_nvenc" not in encoder_tag:
        errors.append(f"{mp4_path.name}: expected h264_nvenc encoder tag, got '{encoder_tag}'")
    if vs.get("codec_name") != "h264" or vs.get("codec_tag_string") != "avc1":
        errors.append(f"{mp4_path.name}: expected h264/avc1, got {vs.get('codec_name')}/{vs.get('codec_tag_string')}")
    if (vs.get("width"), vs.get("height")) != (1920, 1080):
        errors.append(f"{mp4_path.name}: expected 1920x1080, got {vs.get('width')}x{vs.get('height')}")
    if vs.get("pix_fmt") != "yuv420p":
        errors.append(f"{mp4_path.name}: expected yuv420p (4:2:0 from nv12), got {vs.get('pix_fmt')}")
    if vs.get("color_space") != "bt709":
        errors.append(f"{mp4_path.name}: expected bt709 color_space, got {vs.get('color_space')}")
    if vs.get("r_frame_rate") != "30/1":
        errors.append(f"{mp4_path.name}: expected peak r_frame_rate 30/1, got {vs.get('r_frame_rate')}")

    duration = float(info.get("format", {}).get("duration", 0.0))
    if duration <= 3.0 or duration >= 120.0:
        errors.append(f"{mp4_path.name}: duration {duration:.2f}s outside (3s, 120s) limit")

    nb_frames = int(vs.get("nb_frames", 0))
    if nb_frames < 10:
        errors.append(f"{mp4_path.name}: suspiciously low nb_frames={nb_frames}")

    keyframes = get_keyframes(mp4_path)
    if not keyframes or keyframes[0] > 0.1:
        errors.append(f"{mp4_path.name}: missing initial keyframe at 0.0s ({keyframes[:2]})")
    for a, b in zip(keyframes, keyframes[1:]):
        if (b - a) > 10.5:
            errors.append(f"{mp4_path.name}: keyframe gap {b - a:.2f}s exceeds ~10s GOP target")

    if len(s_streams) != 1 or s_streams[0].get("codec_name") != "mov_text":
        errors.append(f"{mp4_path.name}: expected embedded mov_text subtitle stream")

    if captions_dir is not None:
        stem = mp4_path.stem
        for ext in (".vtt", ".srt"):
            cap = captions_dir / f"{stem}{ext}"
            if not cap.is_file() or cap.stat().st_size < 20:
                errors.append(f"{mp4_path.name}: missing or empty caption file {cap.name}")
            else:
                text = cap.read_text(encoding="utf-8")
                for pat in FORBIDDEN_PATTERNS:
                    if pat.search(text):
                        errors.append(f"{cap.name}: matched forbidden pattern {pat.pattern}")

    return errors


def main() -> int:
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <guides-root-or-mp4>", file=sys.stderr)
        return 64

    target = Path(sys.argv[1]).resolve()
    all_errors: list[str] = []

    if target.is_file():
        all_errors.extend(verify_mp4(target, None))
        mp4_files = [target]
    else:
        videos_dir = target / "videos" if (target / "videos").is_dir() else target
        captions_dir = target / "captions" if (target / "captions").is_dir() else None
        mp4_files = sorted(videos_dir.glob("*.mp4"))
        if not mp4_files:
            print(f"No .mp4 files found in {videos_dir}", file=sys.stderr)
            return 1
        for mp4 in mp4_files:
            all_errors.extend(verify_mp4(mp4, captions_dir))

        for doc in list(target.glob("*.md")) + list(target.glob("*.html")):
            text = doc.read_text(encoding="utf-8")
            for pat in FORBIDDEN_PATTERNS:
                if pat.search(text):
                    all_errors.append(f"{doc.name}: matched forbidden pattern {pat.pattern}")

    total_bytes = sum(p.stat().st_size for p in mp4_files)
    if all_errors:
        for err in all_errors:
            print(f"FAIL: {err}", file=sys.stderr)
        return 1

    print(
        f"PASS: Verified {len(mp4_files)} NVENC H.264 MP4 guide(s), "
        f"total size {total_bytes / (1024 * 1024):.2f} MiB."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
