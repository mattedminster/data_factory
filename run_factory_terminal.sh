#! /bin/bash

nvidia-docker run -it -v /home/robot/data_factory/youtube_downloads:/youtube_downloads -v /home/robot/data_factory/egs:/opt/kaldi/egs -v /home/robot/data_factory/data:/data data_factory /bin/bash
