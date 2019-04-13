import zipfile

lyrics = zipfile.ZipFile('/home/mts2180/Project4/lyrics/Lyrics.zip', mode='r')
lyrics.extractall()
lyrics.close()
