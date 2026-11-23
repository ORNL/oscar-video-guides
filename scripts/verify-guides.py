#!/usr/bin/env python3
"""Validate NVENC H.264 workflow video guides, 4-language (en, es, fr, el) captions, HTML5 tracks, and hygiene invariants."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

EXPECTED_GUIDE_COUNT = 31
LOCALIZED_LANGS: tuple[tuple[str, str], ...] = (
    ("es", "Español"),
    ("fr", "Français"),
    ("el", "Ελληνικά"),
)

FORBIDDEN_PATTERNS: tuple[re.Pattern[str], ...] = (
    re.compile(r"\b192\.168\.\d{1,3}\.\d{1,3}\b"),
    re.compile(r"\b10\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"),
    re.compile(r"\b172\.(?:1[6-9]|2\d|3[01])\.\d{1,3}\.\d{1,3}\b"),
    re.compile(r"\braven\b", re.IGNORECASE),
    re.compile(r"\bharrisnt\.com\b", re.IGNORECASE),
    re.compile(r"\bnimo(?:-MME3L)?\b", re.IGNORECASE),
    re.compile(r"\bLAP124441\b", re.IGNORECASE),
    re.compile(r"\b0129372\b"),
    re.compile(r"\btyroneharris\b", re.IGNORECASE),
    re.compile(r"/home/tyrone\b", re.IGNORECASE),
    re.compile(r"\bUbuntu\s+Gate\s+57\b", re.IGNORECASE),
    re.compile(r"\bWindows\s+Gate\s+170\b", re.IGNORECASE),
    re.compile(r"\b(?:we|our|ours|ourselves|us)\b", re.IGNORECASE),
)

LITERAL_PRESERVE_RE = re.compile(
    r"(?:Code 999[89]|SCFU8572724|EMCU 141779-0|EGHU3972694)"
)

VTT_CUE_RE = re.compile(
    r"^(\d+)\n(\d{2}:\d{2}:\d{2}\.\d{3}\s*-->\s*\d{2}:\d{2}:\d{2}\.\d{3})\n([\s\S]+)$"
)
SRT_CUE_RE = re.compile(
    r"^(\d+)\n(\d{2}:\d{2}:\d{2},\d{3}\s*-->\s*\d{2}:\d{2}:\d{2},\d{3})\n([\s\S]+)$"
)
MD_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


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


def parse_caption_file(
    cap_path: Path, is_vtt: bool
) -> tuple[list[tuple[str, str, list[str]]], list[str]]:
    errors: list[str] = []
    label = cap_path.as_posix()
    if not cap_path.is_file() or cap_path.stat().st_size < 20:
        return [], [f"{label}: missing or empty caption file"]

    try:
        raw = cap_path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        return [], [f"{label}: invalid UTF-8 ({exc})"]

    for pat in FORBIDDEN_PATTERNS:
        m = pat.search(raw)
        if m:
            errors.append(
                f"{label}: matched forbidden pattern {pat.pattern!r} ({m.group(0)!r})"
            )

    parts = re.split(r"\r?\n\s*\r?\n", raw.strip())
    if is_vtt:
        if not parts or parts[0].strip() != "WEBVTT":
            errors.append(f"{label}: missing WEBVTT header")
            return [], errors
        cue_blocks = parts[1:]
        cue_re = VTT_CUE_RE
    else:
        cue_blocks = parts
        cue_re = SRT_CUE_RE

    if not cue_blocks:
        errors.append(f"{label}: zero caption cues parsed")
        return [], errors

    cues: list[tuple[str, str, list[str]]] = []
    for expected_idx, blk in enumerate(cue_blocks, start=1):
        norm_blk = "\n".join(ln.rstrip("\r") for ln in blk.strip().splitlines())
        m = cue_re.match(norm_blk)
        if not m:
            errors.append(f"{label}: malformed cue block #{expected_idx}")
            continue
        cue_id, cue_ts, body = m.groups()
        if cue_id != str(expected_idx):
            errors.append(
                f"{label}: expected cue index {expected_idx}, got {cue_id}"
            )
        lines = [ln.strip() for ln in body.splitlines() if ln.strip()]
        if not lines:
            errors.append(f"{label}: empty cue text at cue #{expected_idx}")
        elif len(lines) > 2:
            errors.append(
                f"{label}: cue #{expected_idx} has {len(lines)} lines (expected 1-2 lines)"
            )
        for ln in lines:
            if len(ln) > 160:
                errors.append(
                    f"{label}: cue #{expected_idx} line exceeds readable length ({len(ln)} chars)"
                )
        cues.append((cue_id, cue_ts, lines))

    return cues, errors


def verify_captions_for_stem(stem: str, captions_dir: Path) -> list[str]:
    errors: list[str] = []
    en_vtt = captions_dir / f"{stem}.vtt"
    en_srt = captions_dir / f"{stem}.srt"

    en_vtt_cues, vtt_errs = parse_caption_file(en_vtt, is_vtt=True)
    en_srt_cues, srt_errs = parse_caption_file(en_srt, is_vtt=False)
    errors.extend(vtt_errs)
    errors.extend(srt_errs)
    if not en_vtt_cues or not en_srt_cues:
        return errors

    if len(en_vtt_cues) != len(en_srt_cues):
        errors.append(
            f"{stem}: English VTT ({len(en_vtt_cues)}) and SRT ({len(en_srt_cues)}) cue counts differ"
        )
        return errors

    for idx, ((v_id, v_ts, v_lines), (s_id, s_ts, s_lines)) in enumerate(
        zip(en_vtt_cues, en_srt_cues), start=1
    ):
        if v_id != s_id or v_ts.replace(".", ",") != s_ts:
            errors.append(f"{stem}: English VTT/SRT timestamp mismatch at cue #{idx}")
        if " ".join(v_lines) != " ".join(s_lines):
            errors.append(f"{stem}: English VTT/SRT text mismatch at cue #{idx}")

    for lang_code, _lang_label in LOCALIZED_LANGS:
        loc_vtt = captions_dir / lang_code / f"{stem}.vtt"
        loc_srt = captions_dir / lang_code / f"{stem}.srt"

        loc_vtt_cues, lv_errs = parse_caption_file(loc_vtt, is_vtt=True)
        loc_srt_cues, ls_errs = parse_caption_file(loc_srt, is_vtt=False)
        errors.extend(lv_errs)
        errors.extend(ls_errs)
        if not loc_vtt_cues or not loc_srt_cues:
            continue

        if len(loc_vtt_cues) != len(en_vtt_cues):
            errors.append(
                f"captions/{lang_code}/{stem}.vtt: cue count {len(loc_vtt_cues)} != English {len(en_vtt_cues)}"
            )
            continue
        if len(loc_srt_cues) != len(en_srt_cues):
            errors.append(
                f"captions/{lang_code}/{stem}.srt: cue count {len(loc_srt_cues)} != English {len(en_srt_cues)}"
            )
            continue

        for idx, (
            (ev_id, ev_ts, ev_lines),
            (es_id, es_ts, _),
            (lv_id, lv_ts, lv_lines),
            (ls_id, ls_ts, ls_lines),
        ) in enumerate(
            zip(en_vtt_cues, en_srt_cues, loc_vtt_cues, loc_srt_cues), start=1
        ):
            if lv_id != ev_id or lv_ts != ev_ts:
                errors.append(
                    f"captions/{lang_code}/{stem}.vtt: cue #{idx} timestamp {lv_ts!r} != English {ev_ts!r}"
                )
            if ls_id != es_id or ls_ts != es_ts:
                errors.append(
                    f"captions/{lang_code}/{stem}.srt: cue #{idx} timestamp {ls_ts!r} != English {es_ts!r}"
                )
            lv_flat = " ".join(lv_lines)
            ls_flat = " ".join(ls_lines)
            ev_flat = " ".join(ev_lines)
            if lv_flat != ls_flat:
                errors.append(
                    f"captions/{lang_code}/{stem}: VTT and SRT cue #{idx} text differ"
                )
            if not lv_flat.strip():
                errors.append(
                    f"captions/{lang_code}/{stem}: cue #{idx} has empty translated text"
                )
            elif lv_flat == ev_flat:
                errors.append(
                    f"captions/{lang_code}/{stem}: cue #{idx} is untranslated (identical to English)"
                )
            for ln in lv_lines:
                if len(ln) > 95:
                    errors.append(
                        f"captions/{lang_code}/{stem}: cue #{idx} line too wide for 1080p ({len(ln)} chars)"
                    )
            for literal_tok in set(LITERAL_PRESERVE_RE.findall(ev_flat)):
                if literal_tok not in lv_flat:
                    errors.append(
                        f"captions/{lang_code}/{stem}: cue #{idx} missing required literal {literal_tok!r}"
                    )

    return errors


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
        errors.append(
            f"{mp4_path.name}: expected h264_nvenc encoder tag, got '{encoder_tag}'"
        )
    if vs.get("codec_name") != "h264" or vs.get("codec_tag_string") != "avc1":
        errors.append(
            f"{mp4_path.name}: expected h264/avc1, got {vs.get('codec_name')}/{vs.get('codec_tag_string')}"
        )
    if (vs.get("width"), vs.get("height")) != (1920, 1080):
        errors.append(
            f"{mp4_path.name}: expected 1920x1080, got {vs.get('width')}x{vs.get('height')}"
        )
    if vs.get("pix_fmt") != "yuv420p":
        errors.append(
            f"{mp4_path.name}: expected yuv420p (4:2:0 from nv12), got {vs.get('pix_fmt')}"
        )
    if vs.get("color_space") != "bt709":
        errors.append(
            f"{mp4_path.name}: expected bt709 color_space, got {vs.get('color_space')}"
        )
    if vs.get("r_frame_rate") != "30/1":
        errors.append(
            f"{mp4_path.name}: expected peak r_frame_rate 30/1, got {vs.get('r_frame_rate')}"
        )

    duration = float(info.get("format", {}).get("duration", 0.0))
    if duration <= 3.0 or duration >= 120.0:
        errors.append(
            f"{mp4_path.name}: duration {duration:.2f}s outside (3s, 120s) limit"
        )

    nb_frames = int(vs.get("nb_frames", 0))
    if nb_frames < 10:
        errors.append(f"{mp4_path.name}: suspiciously low nb_frames={nb_frames}")

    keyframes = get_keyframes(mp4_path)
    if not keyframes or keyframes[0] > 0.1:
        errors.append(
            f"{mp4_path.name}: missing initial keyframe at 0.0s ({keyframes[:2]})"
        )
    for a, b in zip(keyframes, keyframes[1:]):
        if (b - a) > 10.5:
            errors.append(
                f"{mp4_path.name}: keyframe gap {b - a:.2f}s exceeds ~10s GOP target"
            )

    if len(s_streams) != 1 or s_streams[0].get("codec_name") != "mov_text":
        errors.append(f"{mp4_path.name}: expected embedded mov_text subtitle stream")

    if captions_dir is not None:
        errors.extend(verify_captions_for_stem(mp4_path.stem, captions_dir))

    return errors


def verify_docs_and_tracks(target: Path, stems: list[str]) -> list[str]:
    errors: list[str] = []
    for doc in list(target.glob("*.md")) + list(target.glob("*.html")):
        try:
            text = doc.read_text(encoding="utf-8")
        except UnicodeDecodeError as exc:
            errors.append(f"{doc.name}: invalid UTF-8 ({exc})")
            continue
        for pat in FORBIDDEN_PATTERNS:
            m = pat.search(text)
            if m:
                errors.append(
                    f"{doc.name}: matched forbidden pattern {pat.pattern!r} ({m.group(0)!r})"
                )

    index_html = target / "index.html"
    if index_html.is_file():
        html = index_html.read_text(encoding="utf-8")
        for stem in stems:
            expected_tracks = [
                f'<track kind="captions" srclang="en" label="English" src="captions/{stem}.vtt" default>',
                *(
                    f'<track kind="captions" srclang="{code}" label="{label}" src="captions/{code}/{stem}.vtt">'
                    for code, label in LOCALIZED_LANGS
                ),
            ]
            for snippet in expected_tracks:
                if snippet not in html:
                    errors.append(f"index.html: missing expected track tag {snippet}")

    readme_md = target / "README.md"
    if readme_md.is_file():
        md = readme_md.read_text(encoding="utf-8")
        for m in MD_LINK_RE.finditer(md):
            raw_target = m.group(1).strip().split()[0]
            if (
                raw_target.startswith("http://")
                or raw_target.startswith("https://")
                or raw_target.startswith("mailto:")
                or raw_target.startswith("#")
            ):
                continue
            rel_path = raw_target.split("#")[0].split("?")[0]
            if rel_path and not (target / rel_path).exists():
                errors.append(f"README.md: broken relative link -> {raw_target}")

    return errors


def main() -> int:
    if len(sys.argv) > 2:
        print(f"Usage: {sys.argv[0]} [guides-root-or-mp4]", file=sys.stderr)
        return 64

    default_root = Path(__file__).resolve().parent.parent
    target = Path(sys.argv[1]).resolve() if len(sys.argv) == 2 else default_root
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
        if (target / "videos").is_dir() and len(mp4_files) != EXPECTED_GUIDE_COUNT:
            all_errors.append(
                f"Expected {EXPECTED_GUIDE_COUNT} .mp4 guides in {videos_dir}, found {len(mp4_files)}"
            )
        for mp4 in mp4_files:
            all_errors.extend(verify_mp4(mp4, captions_dir))
        all_errors.extend(verify_docs_and_tracks(target, [p.stem for p in mp4_files]))

    total_bytes = sum(p.stat().st_size for p in mp4_files)
    if all_errors:
        for err in all_errors:
            print(f"FAIL: {err}", file=sys.stderr)
        return 1

    print(
        f"PASS: Verified {len(mp4_files)} NVENC H.264 MP4 guide(s) + 4-language (en, es, fr, el) "
        f"WebVTT/SRT captions ({len(mp4_files) * 8} subtitle files), total video size "
        f"{total_bytes / (1024 * 1024):.2f} MiB."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
