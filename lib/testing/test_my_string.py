# tests/test_my_string.py

import unittest
from my_string import MyString

class TestMyString(unittest.TestCase):
    def test_is_sentence(self):
        string = MyString("This is a sentence.")
        self.assertTrue(string.is_sentence())

    def test_is_not_sentence(self):
        string = MyString("This is not a sentence")
        self.assertFalse(string.is_sentence())

    def test_is_question(self):
        string = MyString("Is this a question?")
        self.assertTrue(string.is_question())

    def test_is_not_question(self):
        string = MyString("This is not a question")
        self.assertFalse(string.is_question())

    def test_is_exclamation(self):
        string = MyString("Wow!")
        self.assertTrue(string.is_exclamation())

    def test_is_not_exclamation(self):
        string = MyString("This is not an exclamation")
        self.assertFalse(string.is_exclamation())

    def test_count_sentences(self):
        string = MyString("This is a string! It has three sentences. Right?")
        self.assertEqual(string.count_sentences(), 3)

    def test_count_sentences_complex(self):
        string = MyString("This, well, is a sentence. This is too!! And so is this, I think? Woo...")
        self.assertEqual(string.count_sentences(), 5)

if __name__ == '__main__':
    unittest.main()
