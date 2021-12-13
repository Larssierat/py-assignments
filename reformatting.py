# Name: Lars Sierat
# Date: 25-11-2021
# Description:  This program neatly formats the given text into lines of a maximal length.
#               Words are not cut off, but moved to the next line when necessary.


# this function counts the words on a line and creates a new line when the max_length
# of words on a line is reached
def text_to_lines(text, max_length):
    words= text.split()
    seperate_lines= ''
    count = 0
    for word in words:
        if count+len(word)<= max_length:              # adds a word to a line
            seperate_lines= seperate_lines+word
            seperate_lines = seperate_lines+' '
            count = count + len(word) + 1
        else:                                         # creates a new line and adds the first word
            seperate_lines=seperate_lines.rstrip(' ')
            seperate_lines= seperate_lines +'\n'
            seperate_lines= seperate_lines+word
            seperate_lines = seperate_lines+' '
            count= len(word)+1
    seperate_lines=seperate_lines.rstrip(' ')
    return seperate_lines
