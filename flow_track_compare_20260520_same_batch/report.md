# Same-batch sparse-flow checkpoint comparison

Date: 2026-05-20

## Setup

- Baseline checkpoint: `session_2026_05_11_05_41_40_mfssl_flow_po_tracks_baseline_bs8_p3_100k_nanfix_20260511_0541/checkpoints/model-checkpoint-000035000.ckpt`
- SSL frozen checkpoint: `session_2026_05_11_05_41_57_mfssl_flow_po_tracks_ssl90k_frozen_bs8_p3_20k_nanfix_20260511_0541/checkpoints/model-checkpoint-000020000.ckpt`
- SSL pretrain checkpoint: `session_2026_05_09_01_07_00_mfssl_dino_idm_rgb_fdm_t16_gen2_po_vk2_ta_p2_100k/checkpoints/model-checkpoint-000090000.ckpt`
- Evaluation: 50 validation batches per dataset, batch size 1, 16 frames, 1024 tracks, same dataloader batch shared by baseline and SSL frozen.

## Results

| Dataset | Baseline EPE | SSL frozen EPE | SSL - baseline | Baseline better batches | SSL better batches | Finite batches |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| PointOdyssey | 0.9040 | 1.7481 | +0.8441 | 49 | 1 | 50/50 |
| Virtual KITTI 2 | 2.7211 | 4.4682 | +1.7470 | 39 | 11 | 50/50 |
| TartanAir V2 | 9.8382 | 17.6512 | +7.8130 | 49 | 1 | 50/50 |

## Notes

- Previous TartanAir V2 one-sample comparison was not reliable because independent baseline/SSL validation runs did not necessarily see the same samples.
- The comparison script forwards both checkpoints on the same preprocessed batch and same sparse ground truth.
- PointOdyssey NaNs were caused by invalid/non-finite sparse coordinates reaching grid sampling and then being multiplied by a zero mask; the fix sanitizes invalid coordinates/flows and masks non-finite sampled predictions before reduction.
- TartanAir V2 scene ordering was made deterministic by sorting scene names when all scenes are used; otherwise Python hash randomization can change the sequence pool order across processes.
- Current result does not support the hypothesis that SSL frozen is better in OOD flow readout for this head/checkpoint pair. The most likely explanation is optimization/capacity mismatch: the baseline trains the backbone end to end for 35k steps, while SSL frozen trains only the flow head for 20k steps. The frozen SSL representation may not expose the adjacent-frame flow signal strongly enough for this head.

## Files

- `point_odyssey/point_odyssey_summary.json`
- `point_odyssey/point_odyssey_per_batch.csv`
- `virtual_kitti2/virtual_kitti2_summary.json`
- `virtual_kitti2/virtual_kitti2_per_batch.csv`
- `tartanair_v2/tartanair_v2_summary.json`
- `tartanair_v2/tartanair_v2_per_batch.csv`
