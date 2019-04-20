import re

def song_id(filename):
	
def song_artist(filename):

def song_title(filename):

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
	complexity_count = 0
	for word in lyrics.splitlines():
		if word in ['is like','yo yo yo','uptown funk']: #we need to split in lines instead of words and check metaphors, alliterations,etc
			complexity_count +=1
	
	return complexity_count
