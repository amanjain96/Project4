def extract_lyrics(path):
    with open(path, 'r') as myfile:
        lyrics = myfile.read()
        print(lyrics)
