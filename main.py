import os
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
	for name in filename_list:
		filepath = f"{path}/{name}"
		lyrics = load.extract_lyrics(filepath)
		
		song_id = classify.song_id(name)
		artist = classify.song_artist(name)
		title = classify.song_title(name)
		kid_safe_index = classify.kid_safe(lyrics)
		love_index = classify.love(lyrics)
		mood_index = classify.mood(lyrics)
		length_index = classify.length(lyrics)
		complexity_index = classify.complexity(lyrics)

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
		
		total_list.append(song_classification)
	
	classified_songs = {'characterizations': total_list[0:10]}

	print(json.dumps(classified_songs, indent=4))

if __name__ == '__main__':
	import argparse

	parser = argparse.ArgumentParser(description='Classify songs by their lyrics!')
	parser.add_argument('path', help='Please provide a path to a diretory containing lyrics files')

	args = parser.parse_args()
	main(args.path)
