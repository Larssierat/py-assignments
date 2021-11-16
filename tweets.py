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

with open("trump.txt", encoding="utf8") as tweet_file:
    tweets = tweet_file.read().splitlines()
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

total_count= pos_count+neg_count+neutral_count
pos_percentage= (pos_count/total_count)*100
neg_percentage= (neg_count/total_count)*100
neutral_percentage= (neutral_count/total_count)*100
labels = 'positive', 'negative', 'neutral',
sizes = [pos_percentage, neg_percentage, neutral_percentage]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()

tweet_file.close()