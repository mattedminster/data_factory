#! /bin/bash

docker run -v /home/robot/data_factory/youtube_downloads:/youtube_downloads -v /home/robot/data_factory/mini_librispeech:/opt/kaldi/egs/mini_librispeech data_factory bash -c "cd /youtube_downloads && ./create_data.py --target_saying \"turn off the lights\" --search_term \"turn off the lights smart home\" --num_of_samples 3 --max_searches 50"