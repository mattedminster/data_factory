#!/usr/bin/env python3
import os 
import glob

#test_audio_path = '/data/test'
#train_audio_path = '/data/train'
train_path = '/data/train'
test_path = '/data/test'


#test_audio_path
f = open("./input_corpus/test_audio_path","w+")
f.write(test_path)
f.close()


#train_audio_path
f = open("./input_corpus/train_audio_path","w+")
f.write(train_path)
f.close()

#transcripts.train
f = open("./input_corpus/transcripts.train","w+")

for root, dirs, files in os.walk(train_path):
    for file in files:
        if file == "transcript.txt":
            #read the file
            path = "{}/{}".format(root, file)
            with open(path) as fp:
                f.write(fp.read())
f.close()

#transcripts.test
f = open("./input_corpus/transcripts.test","w+")

for root, dirs, files in os.walk(test_path):
    for file in files:
        if file == "transcript.txt":
            #read the file
            path = "{}/{}".format(root, file)
            with open(path) as fp:
                f.write(fp.read())
f.close()
