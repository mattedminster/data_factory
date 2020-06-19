#! /bin/bash

docker run -v /home/robot/data_factory/youtube_downloads:/youtube_downloads data_factory bash -c "cd /youtube_downloads && ./download_youtube_video.py"