# my_string.py

class MyString:
    def __init__(self, value=''):
        if not isinstance(value, str):
            raise ValueError("Value must be a string")
        self.value = value

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        # Split the string based on punctuation marks
        sentences = [sentence.strip() for sentence in self.value.split('.') if sentence.strip()]
        sentences = [sentence.strip() for s in sentences for sentence in s.split('!') if sentence.strip()]
        sentences = [sentence.strip() for s in sentences for sentence in s.split('?') if sentence.strip()]
        return len(sentences)
