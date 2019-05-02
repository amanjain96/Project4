import re
import textstat

def song_id(filename):
	pattern = re.compile(r'(\S+)~(\S+)~(\S+)[.]')
	match = pattern.match(filename)
	song_id = int(match.group(1))
	return song_id
	
def song_artist(filename):
	pattern = re.compile(r'(\S+)~(\S+)~(\S+)[.]')
	match = pattern.match(filename)
	artist_raw = match.group(2)
	artist = artist_raw.replace('-', ' ')
	return artist

def song_title(filename):
	pattern = re.compile(r'(\S+)~(\S+)~(\S+)[.]')
	match = pattern.match(filename)
	title_raw = match.group(3)
	title = title_raw.replace('-', ' ')
	return title

def kid_safe(lyrics):
	kid_count = 0
	bad_words = ['***', '****', '*****', 'a**', 'ass', 'asshole', 'b****', 'bitch', 'boner', 'boob', 'boobs', 'booty', 'butt', 'butthole', 'clit', 'clitoris', 'cock', 'cocks', 'cum', 'cumming', 'cunt', 'dick', 'erotic', 'fag', 'faggot', 'fingering', 'f***', 'fuck', 'fucker', 'fucking', 'fucks', 'genitals', 'hooker', 'jizz', 'juggs', 'kike', 'kink', 'kinky', 'negro', 'n****', 'nigga', 'nigger', 'nipple', 'nipples', 'nude', 'nudity', 'orgasm', 'orgy', 'paedophile', 'panties', 'panty', 'pedophile', 'penis', 'pissing', 'playboy', 'porn', 'porno', 'pornography', 'pubes', 'pussy', 'rape', 'raping', 'rapist','ruined', 'semen', 'sex', 'sexy', 's***', 'shit', 'slut', 'tit', 'tits', 'titties', 'titty', 'topless', 'twat', 'vagina', 'whore', 'whores']
	for word in lyrics.split():
		if word.lower() in bad_words:
			kid_count += 1
	if kid_count == 0:
		return 1
	elif kid_count >= 10:
		return 0
	else:
		return 1 - kid_count / 10

def love(lyrics):
	love_count = 0
	love_words = ['adorable', 'adore', 'affection', 'amour', 'angel', 'bliss', 'caring', 'chocolate', 'companion', 'compassion', 'darling', 'dear', 'desire', 'fond', 'forever','habibi', 'heart', 'husband', 'intimacy', 'intimate', 'kiss', 'kisses', 'kissing', 'love', 'lover', 'loving', 'marriage', 'married', 'marry', 'passion', 'relationship', 'romance', 'romantic', 'sex', 'sweetheart', 'tender', 'warmth', 'wife']
	for word in lyrics.split():
		if word.lower() in love_words:
			love_count += 1
	if love_count == 0:
		return 0
	elif love_count >= 10:
		return 1
	else:
		return love_count / 10

def mood(lyrics):
	mood_count = 0
	for word in lyrics.split():
		if word.lower() in ['upbeat', 'happy', 'brilliant', 'energetic', 'enthusiastic']:
			mood_count += 1
	return mood_count

def length(lyrics):
	length_count = 0
	for word in lyrics.split():
		length_count += 1
	return length_count

def complexity(lyrics):
	return textstat.difficult_words(lyrics)
