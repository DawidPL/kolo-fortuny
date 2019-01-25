import random
words ={'film':['CZTEREJ PANCERNI I PIES', 'KARMAZYNOWY PRZYPŁYW', 'CZTERY WESELA I POGRZEB', 'OGNIEM I MIECZEM'],
        'geografia': ['PUSZCZA BIAŁOWIESKA', 'GÓRY STOŁOWE', 'KORDYLIERY', 'OCEAN ATLANTYCKI', 'KOŁO PODBIEGUNOWE POŁUDNIOWE'],
        'muzyka': ['TINA TURNER', 'THE BEATLES', 'METALLICA']}


class Titles:
    def __init__(self, random_word, word = ''):
        self.random_word = random_word
        self.word = word
    def word_shuffle(self):
        self.random_word = random.choice(list(words))
        return 'Kategoria: ' + self.random_word
    def word_pick(self):
        self.word = random.choice(words[self.random_word])
        self.word.replace(word, '*****')
        return self.word

title = Titles(words)

