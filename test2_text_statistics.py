def number_of_letters_in(text):
    count =0
    for char in range(0, len((text))):
        if text[char].isalpha():
            count =count +1
    return count



def number_of_words_in(text):
    words_list= text.split(" ")
    words= len(words_list)
    return words

def number_of_sentences_in(text):
    sentences_list= text.split('.')
    sentences= len(sentences_list)-1
    return sentences

def average_word_length(text):
    count = 0
    word_list = text.split(' ')
    for i in range(0, len(word_list)):
        for char in word_list[i]:
            if char.isalpha():
                count = count+1
    average_letters_word= count/number_of_words_in(text)
    return round(average_letters_word, 2)


text = "ASDF is the sequence of letters that appear on the first four keys on the home row of a QWERTY or QWERTZ keyboard. They are often used as a sample or test case or as random, meaningless nonsense. It is also a common learning tool for keyboard classes, since all four keys are located on Home row."
print (number_of_letters_in(text))