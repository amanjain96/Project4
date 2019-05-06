# This file contains the Unit-testing required to test our code
import unittest
import main
import classify

# Unit testing for non-english song
# class TestNonEnglish(unittest.TestCase):
#    def test_kidsafe(self):
#        for song_id in non_english:
#            self.assertDictEqual(song_classification,{'kid_safe':0.5,'love':0.5,'mood',0.5,'complexity':0.5})    

class TestClassifyMethods(unittest.TestCase):
    
    def test_song_id(self):
        self.assertEqual(classify.song_id('45~Michael-Jackson~Billie-Jean.txt'), 45)

    def test_song_artist(self):
        self.assertEqual(classify.song_artist('45~Michael-Jackson~Billie-Jean.txt'), 'Michael Jackson')

    def test_song_title(self):
        self.assertEqual(classify.song_title('45~Michael-Jackson~Billie-Jean.txt'), 'Billie Jean')
        
    def test_kid_safe(self):
        self.assertEqual(classify.kid_safe('This is a kid friendly song with good words'), 1)
        self.assertEqual(classify.kid_safe('I am so ruined, fuck life sucks'), 0.7)
        self.assertEqual(classify.kid_safe('Cuss words include fuck, fucking, fucker, shit, bitch, bitches, ass, asshole, mothafucka, and whore'), 0)
                         
    def test_love(self):
        self.assertEqual(classify.love('This is a kid friendly song with good words'), 0)
        self.assertEqual(classify.love('Habibi, I love you, I miss you, I wanna kiss you. Oh babe'), 0.5)
    
    def test_mood(self):
        self.assertEqual(classify.mood('I am so happy and energetic but dead'), 0.6)
    
    def test_length(self):
        self.assertEqual(classify.length('This is a short seven word song'), 0)

    def test_instrumental(self):
        lyrics = '[Instrumental]'
        self.assertEqual(classify.kid_safe(lyrics), 0.5)
        self.assertEqual(classify.love(lyrics), 0.5)
        self.assertEqual(classify.length(lyrics), 0.5)
        self.assertEqual(classify.mood(lyrics), 0.5)
        self.assertEqual(classify.complexity(lyrics), 0.5)

#class TestInputOutput(unittest.TestCase):
#    
#    def test_output(self):
#        self.assertIsInstance(main.main('lyrics'), str)
#
#    def test_input(self):
#        with self.assertRaises(TypeError):
#            main.main()

if __name__ == '__main__':
    unittest.main()