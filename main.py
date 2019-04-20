import os
import load
import classify
import statistics

def main(path):
	filename_list = []
	for filename in os.listdir(path):
		filename_list.append(filename)
	filename_list.sort()

	total_list = []
	for name in filename_list:
		filepath = f"{path}/{name}"
		lyrics = load.extract_lyrics(filepath)
		
		kid_safe_index = classify.kid_safe(lyrics)
		love_index = classify.love(lyrics)
		mood_index = classify.mood(lyrics)
		length_index = classify.length(lyrics)
		complexity_index = classify.complexity(lyrics)

		song_classification = [kid_safe_index, love_index, mood_index, length_index, complexity_index]
		
		total_list.append(song_classification)
	
	print(total_list[192])

	#print(max(total_list))
	#print(min(length_list))
	#print(statistics.mean(length_list))

if __name__ == '__main__':
	import argparse

	parser = argparse.ArgumentParser(description='Classify songs by their lyrics!')
	parser.add_argument('path', help='Please provide a path to a diretory containing lyrics files')

	args = parser.parse_args()
	main(args.path)
