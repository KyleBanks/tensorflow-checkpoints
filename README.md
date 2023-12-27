# tensorflow-checkpoints

This repository demonstrates how you could possibly use a neural network classifier to determine checkpoints from a video game screenshot, allow screenshots and photo mode to be used as save files. This is ultimately impractical for a number of reasons, but was a fun technical deep dive along with other topics such as Steganography to see how save file screenshots might be implemented. 

For a video walkthrough of this project and the alternative approaches that were taken, see: TODO: youtube link

## Preparing Training Data from Videos

1. Place your **.mp4** video files in [frame-extraction/videos/](./frame-extraction/videos/)
2. Build the frame extraction image: `docker build -t frame-extraction frame-extraction/`
3. Run frame extraction: `docker run -it -v $(pwd)/frame-extraction:/data frame-extraction`
4. Retrieve the split video frames from [frame-extraction/frames/](./frame-extraction/frames), and place in the appropriate [training-images/](./training-images) subdirectoryso that each subdirectory represents a class you want to train/predict. 

## Train & Predict

1. Build the training image: `docker build -t tf-checkpoint .` 
2. Run tarining: `docker run -it tf-checkpoint`

