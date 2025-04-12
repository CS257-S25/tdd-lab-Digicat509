import unittest
import sys
from io import StringIO
from production import reverse_word
from production import reverse_all_words
sys.argv = ['production.py', 'this is a test'] #setting the command-line argument "this is a test"

class TestReverseWord(unittest.TestCase):
    def test_reverse_word(self):
        self.assertEqual(reverse_word("hello"), "olleh", "should be olleh")
    def test_reverse_word_same(self):
        self.assertEqual(reverse_word("aaa"), "aaa", "should be aaa")
    def test_reverse_word_empty(self):
        self.assertEqual(reverse_word(""), "", "should be nothing")

class TestReverseAllWord(unittest.TestCase):
    def test_reverse_words(self):
        self.assertEqual(reverse_all_words("this is a test"), "siht si a tset", "should be siht si a tset")
    def test_reverse_word_same(self):
        self.assertEqual(reverse_all_words("aaa"), "aaa", "should be aaa")
    def test_reverse_word_empty(self):
        self.assertEqual(reverse_all_words(""), "", "should be nothing")
    def test_reverse_word_comand_line(self):
        sys.stdout = StringIO() #make a StringIO object and have sys.stdout point to it instead of the usual spot
        print(reverse_all_words(sys.argv[1]))
        printed_output = sys.stdout.getvalue().strip() #I can get what is printed as a normal string!
        self.assertEqual(printed_output, "siht si a tset", "should be siht si a tset")


if __name__ == '__main__':
    unittest.main()