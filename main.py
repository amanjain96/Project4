import os
import load
import classify
import json

def main(path):
    filename_list = []
    for filename in os.listdir(path):
        filename_list.append(filename)
    filename_list.sort()

    total_list = []
    language_dict = {}
    for filename in filename_list[752:754]:
        filepath = f"{path}/{filename}"
        lyrics = load.extract_lyrics(filepath)
        
        song_id = classify.song_id(filename)
        artist = classify.song_artist(filename)
        title = classify.song_title(filename)
        
        language = classify.song_language(lyrics)
        
        language_dict[song_id] = language
    
    print(language_dict)
        
#        if language == 'en' and lyrics != '[Instrumental]':
#            kid_safe_index = classify.kid_safe(lyrics)
#            love_index = classify.love(lyrics)
#            mood_index = classify.mood(lyrics)
#            length_index = classify.length(lyrics)
#            complexity_index = classify.complexity(lyrics)
#            
#            song_classification = {
#                    'id': song_id,
#                    'artist': artist,
#                    'title': title,
#                    'kid_safe': kid_safe_index,
#                    'love': love_index,
#                    'mood': mood_index,
#                    'length': length_index,
#                    'complexity': complexity_index
#                    }
#        elif lyrics == '[Instrumental]':
#            song_classification = {
#                    'id': song_id,
#                    'artist': artist,
#                    'title': title,
#                    'kid_safe': 0.5,
#                    'love': 0.5,
#                    'mood': 0.5,
#                    'length': 0.5,
#                    'complexity': 0
#                    }
#        else:
#            song_classification = {
#                    'id': song_id,
#                    'artist': artist,
#                    'title': title,
#                    'kid_safe': 0.5,
#                    'love': 0.5,
#                    'mood': 0.5,
#                    'length': length_index,
#                    'complexity': 0.5
#                    }
#        
#        total_list.append(song_classification)
#        
#    classified_songs = {'characterizations': total_list}
#    
#    print(json.dumps(classified_songs, indent=4))

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Classify songs by their lyrics!')
    parser.add_argument('path', help='Please provide a path to a diretory containing lyrics files')
    
    args = parser.parse_args()
    main(args.path)