# Name: Lars Sierat
# Date: 25-11-2021
# Description: This program reads a selection of texts, calculates each text’s sentiment and summarizes the results in a pie chart.


import matplotlib.pyplot as plt

# this is a function that reads a text and returns the different lines in a text
def load_words(words):
    content = open(words)
    lines = content.read().splitlines()
    content.close()
    return lines

def load_positive_words():              # returns positive words
    return load_words('pos_words.txt')

def load_negative_words():             # returns negative words
   return load_words("neg_words.txt")

pos_words = load_positive_words()
neg_words = load_negative_words()

# this function cleans the word of non-alphabetical signs and determines if it is a positive or negative word
def sentiment_of_word(word):
    score = 0
    word = word.lower().rstrip('.,!?;:')
    if word in pos_words:
        score = 1
    elif word in neg_words:
        score = -1
    return score

# this function determines for all words in a text if the total sentiment is negative or positive
def sentiment_of_text(text):
    text = text.split()
    total_score = 0
    for word in text:
        total_score = total_score + sentiment_of_word(word)
    return total_score

with open("trump.txt", encoding="utf8") as tweet_file:
    tweets = tweet_file.read().splitlines()   # separate tweets
    neutral_count= 0
    neg_count= 0
    pos_count=0
for tweet in tweets:
    if sentiment_of_text(tweet)==0:
        neutral_count=neutral_count+1
    elif sentiment_of_text(tweet)<0:
        neg_count=neg_count+1
    elif sentiment_of_text(tweet)>0:
        pos_count=pos_count+1

total_count= pos_count+neg_count+neutral_count   # amount of tweets
pos_percentage= (pos_count/total_count)*100
neg_percentage= (neg_count/total_count)*100
neutral_percentage= (neutral_count/total_count)*100
labels = 'positive', 'negative', 'neutral',    # labels of the graph
sizes = [pos_percentage, neg_percentage, neutral_percentage] # positions of percentages in the graph
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()

tweet_file.close()