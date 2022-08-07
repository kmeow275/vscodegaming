from hi import words
import random

def get_valid_words():
    word = random.choice(words)
    while '-' or ' ' in word:
        word = random.choice(words)

    return word