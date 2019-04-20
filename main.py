import os
import load
import classify
import statistics

def main(path):
	length_list = []
	for filename in os.listdir(path)[0:1]:
		filepath = f"{path}/{filename}"
		lyrics = load.extract_lyrics(filepath)
		
		kid_safe_index = classify.kid_safe(lyrics)
		love_index = classify.love(lyrics)
		mood_index = classify.mood(lyrics)
		length_index = classify.length(lyrics)
		complexity_index = classify.complexity(lyrics)

		song_classification = [kid_safe_index, love_index, mood_index, length_index, complexity_index]

		print(song_classification)

		#length_list.append(int(classify.length(lyrics)))
	
	#print(max(length_list))
	#print(min(length_list))
	#print(statistics.mean(length_list))

if __name__ == '__main__':
	import argparse

	parser = argparse.ArgumentParser(description='Classify songs by their lyrics!')
	parser.add_argument('path', help='Please provide a path to a diretory containing lyrics files')

	args = parser.parse_args()
	main(args.path)
