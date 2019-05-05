# Group 4: Song Classification Based on Lyrics

This is an academic project as part of IEOR 4501: Tools for Analytics under the guidance of Professor Paul Logston. Our goal is to classify 1001 songs by analyzing their lyrics, which are given as text files. Song classifications are made along five dimensions: kid safeness, love, mood, length and complexity.

## Contributors

Mitchell Sitzer (UNI: mts2180)

Aman Jain (UNI: akj2137)

## Usage

To use this program, this repository must be cloned to a local location. Calling main.py executes all of the program logic required to classify lyrics files in a directory. A directory path must be provided as a command line argument to main.py in order for the program to execute properly.

```bash
$ git clone git@github.com:mts2180/Project4.git
$ pip install -r requirements.txt # Install all dependencies, which for this project, is only the textstat package

# To execute:
$ python main.py <path to directory with lyrics files>/
```

## Project Workflow

Our program relies on 3 Python scripts to execute. First, main.py is called, which obtains a list of file names from the given directory. Then, for each file in the directory, main.py calls load.py to load the text file's contents, and passes those contents to classify.py for song classification. For each song, a dictionary is created containing the following keys: id, artist, title, kid_safe, love, mood, length and complexity. Once each song is classified, the program outputs a JSON object (sent to standard out, StdOut) that contains a list of songs and their characterizations.

## main.py

This is the main Python script that triggers all other logic in the program. The argument passed to main.py is a path (relative or absolute). That 'path' is a path of a directory. That directory must contain flat .txt files. The first step is to obtain a list of all files in the given directory. The script then sorts the files and iterates over each file one at a time. For each file, load.py is called to 'load' the text content (lyrics) within the file. These lyrics are then passed to classify.py for each of the classification dimensions.

#### Non-English Songs

To handle non-English songs, we used a package called TextBlob, which has a language detection function. We identified the language of each of the 1001 songs, and recorded which songs were not English into a list. Since our classification functions cannot classify non-English songs, we assign a midpoint value of 0.5 to each dimension for these songs.

## classify.py

For instrumental songs, classify.py returns a value of 0.5 for the 5 characterizations, a midpoint value.

### List of Functions

#### Song ID

```python
classify.song_id(filename)
```

Returns the id of the song by using RegEx.

#### Song Artist

```python
classify.song_artist(filename)
```

Returns the artist of the song by using RegEx.

#### Song Title

```python
classify.song_title(filename)
```

Returns the title of the song by using RegEx.

#### Characterization: Kid Safe

```python
classify.kid_safe(lyrics)
```

Returns a value between 0 (is not kid safe) to 1 (is very kid safe) based on the number of bad words detected.

#### Characterization: Love

```python
classify.love(lyrics)
```

Returns a value between 0 (is not a love song) to 1 (is a love song) based on the number of words associated with 'love' detected.

#### Characterization: Mood

```python
classify.mood(lyrics)
```

Returns a value between 0 (is a dark song) to 1 (is a very happy song) based on the number of words associated with positivity or negativity detected.

#### Characterization: Length

```python
classify.length(lyrics)
```

Returns a value between 0 (is a short song) to 1 (is a very long song) based on the number of words present in the lyrics.

#### Characterization: Complexity

```python
classify.complexity(lyrics)
```

Returns a value between 0 (is a very simple song) to 1 (is a very complex song) based on the number of uncommonly used words. This is tested by importing an easy word set from the textstat package, which contains approximately 3000 of the most commonly used words.

## load.py

```python
load.extract_lyrics(path)
```

Returns the lyrics of each song from a given path to a flat .txt file.

## tests.py

Contains unit tests for the overall code for the project. It tests the overall project code for correct values, missing valeus, incorrect arguments, paths, methods, classes, errors and other assertions. The code coverage for the tests can be checked using coverage.py.