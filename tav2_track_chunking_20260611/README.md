# TAv2 track chunking + visibility regeneration — inspection artifacts (2026-06-11)

Branch: `ericwang/tav2-track-chunking` (stacked on samli/po-chunking-optimization, PR #117962).
Nothing uploaded to Azure yet — all artifacts below come from local SKIP_UPLOAD sample runs.

## chunk_overlays/
Tracks read back **from the offline chunk tree** (t001/k000) drawn onto RGB frames fetched
at `frame_start + relative_index` — visual proof the chunk-relative frame mapping is right.
- `tav2_P001/`: TartanAir-V2 AbandonedCable/Data_easy/P001 (frame_start=296)
- `vk2_scene20/`: Virtual KITTI 2 Scene20/clone Camera_0 (frame_start=279)

## visibility/
TAv2 visibility regeneration overlays (green = visible, red = newly marked occluded),
depth-reprojection occlusion check (0.1 m + 0.5 % thresholds, amodal: valids untouched).

| sequence | visible (old -> new) | flipped | drift px (median / p90) | anchor fallback |
|---|---|---|---|---|
| AbandonedCable P001 (industrial) | 1.000 -> 0.938 | 6.2 % | 0.34 / 2.1 | 26 % |
| ForestEnv P000 (vegetation)      | 1.000 -> 0.936 | 6.4 % | 0.19 / 5.6 | 50 % |
| AmericanDiner P000 (indoor)      | 1.000 -> 0.967 | 3.3 % | 0.27 / 0.7 | 0.4 % |
| Downtown P000 (urban)            | 1.000 -> 0.924 | 7.6 % | 0.21 / 3.3 | 20 % |

"Anchor fallback" tracks (no reliable depth anchor: sky / depth edges) keep their old
degenerate visibility. Drift = reprojection error of the static world point vs the stored
2D track — sub-pixel medians validate the static-scene assumption.
