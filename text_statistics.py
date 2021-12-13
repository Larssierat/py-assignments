# Name: Lars Sierat
# Date: 25-11-2021
# Description: In this program, the following text statistics will be calculated.
#              The number of letters in the text are counted.
#              The number of words are counted.
#              The number of sentences are counted.
#              The average word length is computed.

# this function counts alphabetical characters(letters) in a given text
def number_of_letters_in(text):
    count =0
    for char in range(0, len((text))):
        if text[char].isalpha():
            count =count +1
    return count


# this function counts words in a given text
def number_of_words_in(text):
    words_list= text.split(" ")
    words= len(words_list)
    return words

# this function counts sentences in a given text
def number_of_sentences_in(text):
    sentences_list= text.split('.')
    sentences= len(sentences_list)-1
    return sentences

# this function calculates the average length of words in a given text
def average_word_length(text):
    average_letters_word= number_of_letters_in(text)/number_of_words_in(text)
    return average_letters_word

text = "It did quite literally; he burned up pretty quick."
print (number_of_letters_in(text))

