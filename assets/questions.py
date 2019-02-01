import random
words ={'film':['CZTEREJ PANCERNI I PIES', 'KARMAZYNOWY PRZYPŁYW', 'CZTERY WESELA I POGRZEB', 'OGNIEM I MIECZEM'],
        'geografia': ['PUSZCZA BIAŁOWIESKA', 'GÓRY STOŁOWE', 'KORDYLIERY', 'OCEAN ATLANTYCKI', 'KOŁO PODBIEGUNOWE POŁUDNIOWE'],
        'muzyka': ['TINA TURNER', 'THE BEATLES', 'METALLICA']}

random_word = random.choice(list(words))
category_pick = 'Kategoria: ' + random_word
word = random.choice(words[random_word])
word_shuffle = ''.join(('*' if i != ' ' else ' ' for i in word))

