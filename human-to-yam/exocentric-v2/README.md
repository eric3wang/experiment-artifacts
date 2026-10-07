# Human → YAM: exocentric showcase

[Open the presentation](https://eric3wang.github.io/experiment-artifacts/human-to-yam/exocentric-v2/).

Three newly recorded Isaac demonstrations using the official YAM robot:
mug to plate, stacking bowls, and placing the first block into a box.
All three single trials passed their simulator checks. Approximate scenes were
reconstructed by hand and controlled with scripted waypoints. They are not
learned policies or metrically calibrated reconstructions.

The gallery streams third-person **human** references directly from
[H2RBench](https://h2rbench.github.io/), credited to its authors. It does not host
copies of their human footage or use their robot simulation results.

- `yam-showcase.mp4`: shareable 24-second 1080p video of our YAM simulations.
- `media/`: three actual 1280×960/24 fps Isaac recordings and result files.
- `manifest.json`: source URLs, hashes, measured results and scope.
- `scenes-and-trajectories.zip`: initial USD scenes, configurations, object
  trajectories, commanded/measured joints and result JSONs.

The human/robot comparison plays each trial in eight seconds (Isaac 2.25×), with
human footage retimed for comparison. The packing clip covers the first block
only. The earlier 12-example gallery remains in `../12-pairs-v1`, including
partial and failed cable/cloth attempts.
