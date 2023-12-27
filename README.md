# tensorflow-checkpoints

## Preparing Training Data from Videos

1. Place your **.mp4** video files in [frame-extraction/videos/](./frame-extraction/videos/)
2. Build the frame extraction image: `docker build -t frame-extraction frame-extraction/`
3. Run frame extraction: `docker run -it -v $(pwd)/frame-extraction:/data frame-extraction`
4. Retrieve the split video frames from [frame-extraction/frames/](./frame-extraction/frames), and place in the appropriate [training-images/](./training-images) subdirectoryso that each subdirectory represents a class you want to train/predict. 

## Train & Predict

1. Build the training image: `docker build -t tf-checkpoint .` 
2. Run tarining: `docker run -it tf-checkpoint`

