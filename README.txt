GROUP4 Project on Song Classification Based on Lyrics

This is an academic project as part of the course: Tools for Analytics under the guidance of Professor Paul Logston.

SUMMARY:
To create a tool to categorize the songs based on their lyrics. There are 1000 text files each containing the lyrics of wide genre of music. The input to the code is a  path to the directory holding the song files. The output of the command is a JSON object (sent to standard out, StdOut) that contains a list of characterizations; one for each song. Five different dimensions were tested: Kid Safe, Love, Mood, Length and Complexity for each song.
The project contains several files like load.py, main.py, classify.py and tests.py which run through a single command.

File Details and Project Workflow:

MAIN.PY
This is the main file that triggers all other logic in the program. 
The argument passed to main.py is a path (relative or absolute). That 'path' is a path of a directory. That directory contains flat .txt files.

First step is sorting all the files in the given path by alphabetical order for better processing efficiency for further steps.
Next, the TextBlob package converts the lyrics strings into a format it can understand and it interprets the language of the song. If the language is not English, our function will assign an avergae value to the kid_safe index, love and mood index. It will only give back to the length of the non-english song.

Song Name, Artist name and Song Title are extracted from the File Name. Kid_safe, love, mood, length and complexity index are found when classify.py file is called with 'lyrics' as the argument for each song respectively.

The output of the program is of the form of a nested dictionary. This is then exported as a JSON object using json package. 

if __name__ == '__main__':
The Argeparse package ensures a non-empty path argument is passed to the function to set it rolling.


LOAD.PY
This file loads (reads) the lyrics of each song from the given path.

CLASSIFY.PY
This file contains all the code for the actual classification and index calculation for each song for the above mentioned dimensions.
Regular Expression (REGEX) is used to identify the pattern in the filename and extract the Song id, Song artist, and Song Title. 
Kid_safe count is checked by matching several cuss words from a list. A count is defined based on our results.
Similar concept is used for love_index and Mood index.
Word count is done to find the length of each song.
For complexity, the calculations are not straight forward. Textstat package was imported. A set of commonly used easy words were compared from the package and the lyrics of each song. If there are very few words matching, then the song obtained a higher value on the complexity index.


TESTS.PY
This file contains unit tests for the overall code for the project. It tests the overall project code for correct values, missing valeus, incorrect arguments, paths, methods, classes, errors and other assertions. The code coverage for the tests can be check using coverage.py
