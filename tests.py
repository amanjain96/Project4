
#This file contains the Unit-testing required to test our code
import unittest


#Unit testing for non-english song
class TestNonEnglish(unittest.TestCase):
   # def test_kidsafe(self):
#    for song_id in non_english:
#            self.assertDictEqual(song_classification,{'kid_safe':0.5,'love':0.5,'mood',0.5,'complexity':0.5})
    pass    

class TestClassify(unittest.TestCase):

    def test_id(self):
        self.assertEqual(classify.song_id('45~Michael-Jackson~Billie-Jean'),45)

    def test_artist(self):
        self.assertEqual(classify.song_artist('45~Michael-Jackson~Billie-Jean'),'Michael Jackson')

    def test_title(self):
        self.assertEqual(classify.song_title('45~Michael-Jackson~Billie-Jean'),'Billie Jean')

    def test_kidsafe1(self):
        self.assertEqual(classify.kid_safe('This is a kid friendly song with good words',1)

    def test_kidsafe2(self):
        self.assertEqual(classify.kid_safe('I am so ruined, fucked. **** Life sucks.',0.6)
   
    def test_love1(self):
        self.assertEqual(classify.love('This is a kid friendly song with good words',0)

    def test_love2(self):
        self.assertEqual(classify.love('Habibi, I love you, I need you, I miss you,I wanna kiss you. Oh babe!',0.6)

    
class TestInputOutput(unittest.TestCase):

    def test_output(self):
        pass


    def test_input(self):

        with self.assertRaises():
            main()

        with self.assertRaises():
            main('incorrect path format')


class TestArgeParser(unittest.TestCase):

    def test_argeparse(self):
        self.assertIn('ArgumentParser', main.py)

    def test_ifname(self):
        self.assertIn("if __name__ == '__main__':", main.py)




if __name__ == '__main__':
    unittest.main()


