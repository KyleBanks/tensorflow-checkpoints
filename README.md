# tensorflow-checkpoints

This repository demonstrates how you could potentially use a convolutional neural network classifier to determine game save checkpoints from a video game screenshot, allow screenshots and photo mode to be used as save files. This was a fun technical experiement but is ultimately impractical for a number of reasons.

For more on why it's impractical and a video walkthrough of this project, as well as the alternative approaches that were taken including steganography, EXIF tags and QR codes, [check out my YouTube video on the subject here.](https://youtu.be/0aBy8wLnpQ8)

## Preparing Training Data from Videos

1. Place your **.mp4** video files in [frame-extraction/videos/](./frame-extraction/videos/)
2. Build the frame extraction image: `docker build -t frame-extraction frame-extraction/`
3. Run frame extraction: `docker run -it -v $(pwd)/frame-extraction:/data frame-extraction`
4. Retrieve the split video frames from [frame-extraction/frames/](./frame-extraction/frames), and place in the appropriate [training-images/](./training-images) subdirectory such that each subdirectory represents a class you want to train/predict. 

## Train & Predict

1. Build the training image: `docker build -t tf-checkpoint .` 
2. Run tarining: `docker run -it tf-checkpoint`

