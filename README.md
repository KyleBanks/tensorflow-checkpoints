# tensorflow-checkpoints

## Preparing Training Data from Videos

1. Place your **.mp4** video files in [frame-extraction/videos/](./frame-extraction/videos/)
2. `docker build -t frame-extraction frame-extraction/`
3. `docker run -it -v $(pwd)/frame-extraction:/data frame-extraction`
4. Retrieve the split video frames from [frame-extraction/frames/](./frame-extraction/frames), and place in the appropriate [training-images/](./training-images) subdirectory.

## Install

**TODO: setup a docker image to avoid local installation**

The following assumes you have Python installed (I'm using v3.11.7, v3.12 has issues) as well as Pip.

Install dependencies:

```
pip install -r requirements.txt
```

Execute: 

```
python main.py
```