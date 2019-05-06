import os
import load
import classify
import json

def main(path):
    """The main file that triggers all other logic"""
    filename_list = []
    for filename in os.listdir(path):
        filename_list.append(filename)
    filename_list.sort()

    total_list = []
    non_english = [16, 23, 26, 32, 51, 74, 82, 93, 106, 110, 111, 152, 154, 155, 170, 177, 191, 194, 215, 226, 232, 252, 256, 262, 266, 274, 300, 307, 325, 329, 348, 350, 359, 363, 367, 372, 380, 385, 389, 391, 393, 409, 428, 438, 456, 465, 480, 484, 493, 513, 515, 519, 524, 535, 536, 547, 551, 580, 582, 588, 590, 608, 614, 617, 624, 645, 647, 651, 653, 666, 669, 673, 697, 704, 714, 717, 725, 741, 759, 761, 784, 787, 797, 798, 808, 823, 828, 832, 833, 858, 864, 878, 890, 893, 913, 914, 920, 945, 951, 959, 964, 965, 966, 976, 979, 986]

    for filename in filename_list:
        filepath = f"{path}/{filename}"
        lyrics = load.extract_lyrics(filepath)
        
        song_id = classify.song_id(filename)
        artist = classify.song_artist(filename)
        title = classify.song_title(filename)
        length_index = classify.length(lyrics)
        
        if song_id not in non_english:
            kid_safe_index = classify.kid_safe(lyrics)
            love_index = classify.love(lyrics)
            mood_index = classify.mood(lyrics)
            complexity_index = classify.complexity(lyrics)
            
            song_classification = {
                    'id': song_id,
                    'artist': artist,
                    'title': title,
                    'kid_safe': kid_safe_index,
                    'love': love_index,
                    'mood': mood_index,
                    'length': length_index,
                    'complexity': complexity_index
                    }
        else:
            song_classification = {
                    'id': song_id,
                    'artist': artist,
                    'title': title,
                    'kid_safe': 0.5,
                    'love': 0.5,
                    'mood': 0.5,
                    'length': length_index,
                    'complexity': 0.5
                    }
        
        total_list.append(song_classification)
        
    classified_songs = {'characterizations': total_list}
    
    json_output = json.dumps(classified_songs, ensure_ascii=False, indent=4)
    print(json_output)
    return json_output
    
if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Classify songs by their lyrics!')
    parser.add_argument('path', help='Please provide a path to a directory containing lyrics files')
    
    args = parser.parse_args()
    main(args.path)