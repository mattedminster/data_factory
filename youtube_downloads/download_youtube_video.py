#!/usr/bin/env python3
import youtube_dl
from youtube_transcript_api import YouTubeTranscriptApi
from pydub import AudioSegment
import re

youtube_id = 'd5XTDmm0KUQ'
wav_file_name = '{}.wav'.format(youtube_id)

ydl_opts = {
    'outtmpl': youtube_id,
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'wav',
        'preferredquality': '192'
    }],
    'postprocessor_args': [
        '-ar', '16000'
    ],
    'prefer_ffmpeg': True,
    'keepvideo': False
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['http://www.youtube.com/watch?v={}'.format(youtube_id)])

transcript = YouTubeTranscriptApi.get_transcript(youtube_id)
print("got transcript: {}".format(transcript[0]))
for x in range(0, len(transcript)):
    text = transcript[x]['text']
    start = float(transcript[x]['start'])
    duration = float(transcript[x]['duration'])

    
    t1 = start * 1000 #Works in milliseconds
    if x+1 < len(transcript):
        next_start = transcript[x+1]['start'] * 1000
        t2 = next_start #the start of the next one
    else:
        t2 = t1 + (duration * 1000)

    print("{} - start: {}({}) duration: {} end time:{} ".format(text, start, t1, duration, t2))
    
    clean_line = re.sub(r'([^a-zA-Z ]+?)', '', text)
    clean_line = clean_line.lower() #lowercase 
    clean_line = clean_line.encode('utf-8')

    newAudio = AudioSegment.from_wav("wav")
    newAudio = newAudio[t1:t2]
    newAudio.export('{}.wav'.format(clean_line), format="wav")
    #get path of wav file
    #split up eav

#for speech in transcript[0]:
#    print(speech.text)
#make folder
#move videos
#download transcript
#crop the files
#create annotation files
