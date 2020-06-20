#!/usr/bin/env python3.7
import youtube_dl
from youtube_transcript_api import YouTubeTranscriptApi
from pydub import AudioSegment
import re
import argparse
from youtube_search import YoutubeSearch
import json
import os


def download_youtube(youtube_id, target_saying):
	folder = './data/{}'.format(target_saying)
	if not os.path.exists(folder):
		os.makedirs(folder)

	if os.path.exists('./data/{}/{}.wav'.format(target_saying, youtube_id)):
		print("{} already exsists...skipping".format(youtube_id))
		return False

	f=open("./data/{}/transcript.txt".format(target_saying), "a+")
	#print("youtube id: {}".format(youtube_id))
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

	try:
		transcript = YouTubeTranscriptApi.get_transcript(youtube_id)
	except Exception as e:
		print("Transcript doesn't exist for video: {}".format(e))
		return False




	
	
	for x in range(0, len(transcript)):
		text = transcript[x]['text']
		if target_saying.lower() in text.lower():
			print("{} was detected in transcript. Downloading Video".format(target_saying))
			with youtube_dl.YoutubeDL(ydl_opts) as ydl:
				ydl.download(['http://www.youtube.com/watch?v={}'.format(youtube_id)])
			print("download complete")
			
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
			#clean_line = clean_line.encode('utf-8')

			

			newAudio = AudioSegment.from_wav("wav")
			newAudio = newAudio[t1:t2]
			newAudio.export('./data/{}/{}.wav'.format(target_saying, youtube_id), format="wav")

			
			annotation_text = "{} {}\n".format(youtube_id, clean_line.upper())
			f.write(annotation_text)
			f.close()
			return True

	return False


parser = argparse.ArgumentParser(prog="dataCollector")
parser.add_argument('--target_saying', default="turn on the lights")
parser.add_argument('--search_term', default="smart home tests")
parser.add_argument('--num_of_samples', type=int, default=3)
parser.add_argument('--max_searches', type=int, default=10)

args = parser.parse_args()

print("Target Saying: {}".format(args.target_saying))
print("Search Term: {}".format(args.search_term))
print("Number of Samples: {}".format(args.num_of_samples))
print("Max Searches: {}".format(args.max_searches))


f = open("search_terms.txt", "r")
for term in f:
	search_terms = term
	results = YoutubeSearch(search_terms, max_results=args.max_searches).to_json()
	results = json.loads(results)
	print("results: {}".format(results))
			
	found_count = 0

	for x in range(0, len(results['videos'])):
		video_id = results['videos'][x]['id']
		found_target = download_youtube(video_id, args.target_saying)
		if found_target is True:
			found_count += 1
		
	print("number of found samples: {}".format(found_count))


#get the num of samples youtube ids 

#grab the transcript
#create the MP3

