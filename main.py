import os
from textblob import TextBlob
import load
import classify
import statistics
import json

def main(path):
	filename_list = []
	for filename in os.listdir(path):
		filename_list.append(filename)
	filename_list.sort()

	total_list = []
	for name in filename_list[0:20]:
		filepath = f"{path}/{name}"
		lyrics = load.extract_lyrics(filepath)
		b = TextBlob(lyrics)
		print(b.detect_language())

		song_id = classify.song_id(name)
		artist = classify.song_artist(name)
		title = classify.song_title(name)
		kid_safe_index = classify.kid_safe(lyrics)
		love_index = classify.love(lyrics)
		mood_index = classify.mood(lyrics)
		length_index = classify.length(lyrics)
		complexity_index = classify.complexity(lyrics)

		if b.detect_language() == 'en':
			song_classification = {
								'id': song_id,
								'artist': artist,
								'title': title,
								'kid_safe': kid_safe_index,
								'love': love_index,
								'mood': mood_index,
								'length': length_index,
								'complexity': complexity_index
			}
		else:
			song_classification = {
								'id': song_id,
								'artist': artist,
								'title': title,
								'kid_safe': 0.5,
								'love': 0.5,
								'mood': 0.5,
								'length': length_index,
								'complexity': 0.5
			}
		
		total_list.append(song_classification)
	
	classified_songs = {'characterizations': total_list}

	print(json.dumps(classified_songs, indent=4))

if __name__ == '__main__':
	import argparse

	parser = argparse.ArgumentParser(description='Classify songs by their lyrics!')
	parser.add_argument('path', help='Please provide a path to a diretory containing lyrics files')

	args = parser.parse_args()
	main(args.path)
