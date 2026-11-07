#!/usr/bin/env bash
# Encode or remux a 1080p workflow screen recording using NVIDIA RTX 5060 Ti
# hardware NVENC H.264 (nv12 / 4:2:0, BT.709, GOP 300 @ 30fps, differential VFR)
# and embed synchronized mov_text soft subtitles.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if [[ -f "${SCRIPT_DIR}/ensure_nvenc_env.sh" ]]; then
  # shellcheck source=/dev/null
  source "${SCRIPT_DIR}/ensure_nvenc_env.sh"
fi

if [[ "$#" -lt 2 || "$#" -gt 3 ]]; then
  echo "Usage: $0 <input-video> [captions.srt] <output.mp4>" >&2
  exit 64
fi

INPUT_VIDEO="$1"
if [[ "$#" -eq 3 ]]; then
  CAPTIONS_SRT="$2"
  OUTPUT_MP4="$3"
else
  CAPTIONS_SRT=""
  OUTPUT_MP4="$2"
fi

TMP_MP4="$(mktemp --suffix=.mp4)"
trap 'rm -f "${TMP_MP4}"' EXIT

ffmpeg -hide_banner -loglevel warning -y \
  -i "${INPUT_VIDEO}" \
  -vf "mpdecimate=hi=256:lo=64:frac=0.001:max=300,scale=1920:1080:flags=lanczos:out_color_matrix=bt709:out_range=tv,format=nv12,setparams=colorspace=bt709:color_primaries=bt709:color_trc=bt709:range=tv" \
  -fps_mode vfr \
  -c:v h264_nvenc \
  -preset p7 \
  -tune hq \
  -multipass fullres \
  -profile:v high \
  -level:v 4.1 \
  -rc vbr \
  -cq 22 \
  -qmin 16 \
  -qmax 28 \
  -b:v 0 \
  -g 300 \
  -forced-idr 1 \
  -force_key_frames "expr:gte(t,n_forced*10)" \
  -bf 3 \
  -b_ref_mode middle \
  -rc-lookahead 20 \
  -spatial-aq 1 \
  -temporal-aq 1 \
  -colorspace bt709 \
  -color_primaries bt709 \
  -color_trc bt709 \
  -color_range tv \
  -an \
  "${TMP_MP4}"

if [[ -n "${CAPTIONS_SRT}" && -f "${CAPTIONS_SRT}" ]]; then
  ffmpeg -hide_banner -loglevel warning -y \
    -i "${TMP_MP4}" -i "${CAPTIONS_SRT}" \
    -map 0:v:0 -map 1:0 \
    -c:v copy -c:s mov_text \
    -metadata:s:v:0 language=eng \
    -metadata:s:s:0 language=eng \
    -metadata:s:s:0 title="English" \
    -disposition:s:0 default \
    -movflags +faststart \
    "${OUTPUT_MP4}"
else
  ffmpeg -hide_banner -loglevel warning -y \
    -i "${TMP_MP4}" \
    -c:v copy \
    -movflags +faststart \
    "${OUTPUT_MP4}"
fi
