FROM kaldiasr/kaldi:gpu-latest


RUN apt-get update && apt-get install -y \
    software-properties-common

RUN add-apt-repository ppa:deadsnakes/ppa

RUN apt-get update && apt-get install --no-install-recommends -y \
    flac \
    python3.7-dev \
    dirmngr \
    g++ \
    gnupg2 \
    lsb-release \
    python3-pip \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

RUN python3.7 -m pip install --upgrade youtube_dl youtube_transcript_api pydub youtube_search


#COPY ./download_youtube_video.py /download_youtube_video.py

