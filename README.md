# tensorflow-checkpoints

## Preparing Training Data from Videos

1. Place your **.mp4** video files in [frame-extraction/videos/](./frame-extraction/videos/)
2. `docker build -t frame-extraction frame-extraction/`
3. `docker run -it -v $(pwd)/frame-extraction:/data frame-extraction`
4. Retrieve the split video frames from [frame-extraction/frames/](./frame-extraction/frames), and place in the appropriate [training-images/](./training-images) subdirectory.

