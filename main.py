import os
import load

filename = os.fsdecode('/home/mts2180/Project4/lyrics/000~Jerry-Harrison~No-More-Reruns.txt')
load.extract_lyrics(filename)
