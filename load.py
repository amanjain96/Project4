# This function reads the entire contents of a file and returns those contents
# as a single string

def extract_lyrics(path):
    with open(path, 'r') as myfile:
        lyrics = myfile.read()
        return lyrics