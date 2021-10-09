import matplotlib.pyplot as plt

def load_words(words):
    content = open(words)
    lines = content.read().splitlines()
    content.close()
    return lines

def load_positive_words():
    return load_words('pos_words.txt')

def load_negative_words():
   return load_words("neg_words.txt")

pos_words = load_positive_words()
neg_words = load_negative_words()

def sentiment_of_word(word):
    score = 0
    word = word.lower().rstrip('.,')
    if word in pos_words:
        score = 1
    elif word in neg_words:
        score = -1
    return score


def sentiment_of_text(text):
    text = text.split()
    total_score = 0
    for word in text:
        total_score = total_score + sentiment_of_word(word)
    return total_score
