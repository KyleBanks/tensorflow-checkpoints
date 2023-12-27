FROM jrottenberg/ffmpeg
MAINTAINER Kyle Banks

ENV MAX_PROCS 4
ENV VIDEO_FOLDER /data/videos
ENV FRAMES_FOLDER /data/frames
ENV IMAGE_SIZE 224 

VOLUME /data

ENTRYPOINT ls $VIDEO_FOLDER/ | grep '\.mp4$' | xargs -P $MAX_PROCS -n 1 -- bash -c 'ffmpeg -i $VIDEO_FOLDER/$0 -r 20  -vf scale=$IMAGE_SIZE:$IMAGE_SIZE $FRAMES_FOLDER/$0_%05d.jpg' 
