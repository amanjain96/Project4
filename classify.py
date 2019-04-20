import re
import textstat

def song_id(filename):
	pass
	
def song_artist(filename):
	pass

def song_title(filename):
	pass

def kid_safe(lyrics):
	kid_count = 0
	for word in lyrics.split():
		if word in ['fuck', 'bitch', 'shit', 'ass', 'asshole', 'fag', 'jerkoff', 'whore', 'cunt', 'pussy', 'arse']:
			kid_count += 1

	return kid_count

def love(lyrics):
	love_count = 0
	for word in lyrics.split():
		if word in ['love', 'kiss', 'dream', 'amour', 'yearning', 'sex', 'like', 'babe', 'baby', 'girlfriend', 'boyfriend']:
			love_count += 1

	return love_count

def mood(lyrics):
	mood_count = 0
	for word in lyrics.split():
		if word in ['upbeat', 'happy', 'brilliant', 'energetic', 'enthusiastic']:
			mood_count += 1

	return mood_count

def length(lyrics):
	length_count = 0
	for word in lyrics.split():
		length_count += 1

	return length_count

def complexity(lyrics):
	return textstat.difficult_words(lyrics)
