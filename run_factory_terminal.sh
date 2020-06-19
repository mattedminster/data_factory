#! /bin/bash

nvidia-docker run -it -v /home/robot/data_factory/youtube_downloads:/youtube_downloads -v /home/robot/data_factory/mini_librispeech:/opt/kaldi/egs/mini_librispeech data_factory /bin/bash