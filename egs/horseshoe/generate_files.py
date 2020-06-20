#!/usr/bin/env python3
import os 
import glob

#test_audio_path = '/data/test'
#train_audio_path = '/data/train'
train_path = './data/train'
#test_path = '/data/test'


#text
f = open("text","w+")

for root, dirs, files in os.walk(train_path):
    for file in files:
        if file == "transcript.txt":
            #read the file
            path = "{}/{}".format(root, file)
            with open(path) as fp:
                f.write(fp.read())
f.close()


