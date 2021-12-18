# Name: Lars Sierat
# Date: 25-11-2021
# Description: this program calculates the sentiment score of a text by dividing the words in the text in positive, negative and neutral words.

# this is a function that reads a text and returns the different lines in a text
def load_words(words):
    content = open(words)
    lines = content.read().splitlines()
    content.close()
    return lines

# returns positive words
def load_positive_words():
    return load_words('pos_words.txt')

# returns negative words
def load_negative_words():
   return load_words("neg_words.txt")

pos_words = load_positive_words()
neg_words = load_negative_words()

# this function cleans the word of non-alphabetical signs and determines if it is a positive or negative word
def sentiment_of_word(word):
    score = 0
    word= word.lower().rstrip('.,?!:;')
    if word in pos_words:
        score+= 1
    elif word in neg_words:
        score+=-1
    return score

# this function determines for all words in a text if the total sentiment is negative or positive
def sentiment_of_text(text):
    text= text.split()
    total_score= 0
    for word in text:
        total_score= total_score+sentiment_of_word(word)
    return total_score

example_text=("Pastel-colored 1980s day cruisers from Florida are nice, nice, admire.")
a= sentiment_of_text(example_text)
print(a)
