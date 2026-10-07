# Real → Sim / YAM: 12 paired examples

A 4 × 3 gallery comparing eight rigid-object actions, two towel half-folds and two cable actions with YAM simulations rendered in Isaac Sim 5.1.

**Approximate, manually reconstructed scenes and scripted actions.** Rigid objects use physical contact grasps. Cloth and cables use idealized grip attachments; cloth uses native PhysX particle physics with robot collision shapes disabled, and cables use articulated rigid links. The cable loop is simplified. Original cable robots are retargeted to YAM. This is not an automatic video-to-sim model or hardware validation.

## Open the comparison

- [Download the interactive 12-pair gallery](yam12-gallery.zip), unzip, and open `yam12-gallery/index.html` in a browser. Internet access is needed for the real clips.
- [Download Isaac scenes and recorded trajectories](yam12-scenes-and-recordings.zip) (39 MB). Run instructions and model license are included.
- [Provenance, source ranges and simulation checks](gallery/manifest.json).

The gallery contains our simulation videos and streams real footage from the researchers’ original project hosts. It does not bundle or redistribute the original source videos. YouTube downloads were blocked by a sign-in/bot check, so accessible project-hosted footage was selected instead. Playback uses a normalized 20-second comparison cycle, not precise event synchronization.

## Examples

| # | Action | Real source | Isaac / YAM recording |
|---|---|---|---|
| 1 | Cube → red pad | [Original](https://dreamzero0.github.io/yam_gallery/videos/episode_000002_processed_small.mp4#t=0,4.541667) | [Simulation](gallery/media/000002.mp4) |
| 2 | Cube → red pad | [Original](https://dreamzero0.github.io/yam_gallery/videos/episode_000006_processed_small.mp4#t=0,4.65) | [Simulation](gallery/media/000006.mp4) |
| 3 | Cube → red pad | [Original](https://dreamzero0.github.io/yam_gallery/videos/episode_000007_processed_small.mp4#t=0,5.9) | [Simulation](gallery/media/000007.mp4) |
| 4 | Cube → red pad | [Original](https://dreamzero0.github.io/yam_gallery/videos/episode_000009_processed_small.mp4#t=0,4.866016) | [Simulation](gallery/media/000009.mp4) |
| 5 | Two-arm bar → pad | [Original](https://dreamzero0.github.io/yam_gallery/videos/episode_000017_processed_small.mp4#t=0,5.466667) | [Simulation](gallery/media/000017.mp4) |
| 6 | Two-arm bar → pad | [Original](https://dreamzero0.github.io/yam_gallery/videos/episode_000021_processed_small.mp4#t=0,6.4) | [Simulation](gallery/media/000021.mp4) |
| 7 | Two-arm bar → pad | [Original](https://dreamzero0.github.io/yam_gallery/videos/episode_000022_processed_small.mp4#t=0,4.916016) | [Simulation](gallery/media/000022.mp4) |
| 8 | Two-arm bar → pad | [Original](https://dreamzero0.github.io/yam_gallery/videos/episode_000024_processed_small.mp4#t=0,6.075) | [Simulation](gallery/media/000024.mp4) |
| 9 | Towel → half fold | [Original](https://dreamzero0.github.io/yam_gallery/videos/episode_000010_processed_small.mp4#t=0,1.9) | [Simulation](gallery/media/000010.mp4) |
| 10 | Towel → half fold | [Original](https://dreamzero0.github.io/yam_gallery/videos/episode_000013_processed_small.mp4#t=0,2.1) | [Simulation](gallery/media/000013.mp4) |
| 11 | Cable → grasp | [Original](https://remodel-project.eu/wp-content/uploads/2023/05/ariadne_grasp.mp4#t=9,16.56) | [Simulation](gallery/media/000101.mp4) |
| 12 | Cable → change bend | [Original](https://remodel-project.eu/wp-content/uploads/2023/05/demo5.3.mp4#t=33,43) | [Simulation](gallery/media/000102.mp4) |

Validation: **12/12 rollouts and 83 simulation checks pass**. Browser validation loaded and advanced all **24 videos**, opened the comparison dialog and reported no JavaScript errors. These checks verify behavior within the simulation, not real-world accuracy.

Source credits: [DreamZero YAM gallery](https://dreamzero0.github.io/yam_gallery/) and [REMODEL](https://remodel-project.eu/content/videos/). YAM model: I2RT, under its included upstream license.
