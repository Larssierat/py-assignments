def text_to_unique_words(text):
    words=text.split()
    words = cleanup(words)
    unique_words= []
    for word in words:                                                   #for i in range(0, len(unique_words)):
        if word not in unique_words:
            unique_words.append(word)
    sorted_list= sorted(unique_words)
    return (sorted_list)

def cleanup(words):
    empty_list = []
    for i in range(0, len(words)):
        lowercase_word= words[i].lower()
        lowercase_stripped_word= lowercase_word.strip('.,:;?!')
        empty_list.append(lowercase_stripped_word)
    return empty_list



source_text= "The apple doesn't fall far from the tree. "

b= text_to_unique_words(source_text)
print (*b, sep= "\n")
