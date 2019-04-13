import os
import load
import classify

def main():
    for filename in os.listdir('/home/mts2180/Project4/lyrics')[0:10]:
        filepath = f"/home/mts2180/Project4/lyrics/{filename}"
        lyrics = load.extract_lyrics(filepath)
        love_index = classify.love(lyrics)
        print(love_index)

if __name__ == '__main__':
    main()
