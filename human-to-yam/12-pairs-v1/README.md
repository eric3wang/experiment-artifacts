# Human → YAM: 12 paired examples

A 4-column × 3-row comparison of **real human demonstrations** and recorded **YAM attempts in Isaac Sim**. The tasks range from simple placement to cups, books, lids, sweeping, cables and fabric.

**Measured outcomes: 5 completed the stated action, 3 partial attempts, 4 failed attempts.** The viewer preserves failures. See [validation.json](validation.json) for each task's scope, checks and measurements.

## View the pairs

Download and extract [gallery.zip](gallery.zip). With Python 3 and ffmpeg installed, run in the extracted directory:

```bash
python3 fetch_sources.py human
python3 -m http.server 8766
```

Open `http://localhost:8766`, then choose **Play all pairs**. This fetches the twelve original human clips directly from the EgoDex publisher and verifies their hashes; no full dataset download is required. It preserves the originals and makes H.264 playback copies for browser compatibility. Simulated videos are already included. The original footage is not redistributed in this public bundle.

Human source credit: [EgoDex / Apple AIML Research](https://github.com/apple-aiml-research/ml-egodex). Dataset license: CC BY-NC-ND 4.0, distinct from the project's code license. These are publisher-hosted human clips, not YouTube downloads.

## Use the scenes

[Scenes and recorded trajectories](scenes-and-recordings.zip) contains twelve initial `scene.usdc` files, measured object/cloth/cable trajectories, commanded joint targets, measured robot joint positions, and outcome JSON. A USD file shows the initial scene; running the controller is necessary to replay its action.

[Implementation and reproduction instructions — PR #5](https://github.com/wayveai/robot-expert-flywheel/pull/5) are in the team's robot repository under `showcase/human_yam`. Robot assets use the official I2RT YAM model; the archive includes the asset license.

## What the demo establishes

Scenes and task-space waypoints were authored manually after inspecting the human clips. Geometry, scale, materials and camera placement are approximate. YAM follows inverse-kinematics joint targets, and the images are recorded from actual Isaac physics steps. This is not an automatic video reconstruction model, learned robot policy, or validated digital twin.

Rigid props use physical finger contact. Cloth and cable use explicitly idealized grasp attachments. Cloth/table/self-collision is simulated, but cloth/robot collision is disabled. Cable connector fit is not validated. The yellow cloth shows a first-fold attempt; the shirt example reproduces only one fold. Source and simulation playback durations are normalized for comparison, without precise event alignment.
