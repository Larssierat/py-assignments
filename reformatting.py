def text_to_lines(text, max_length):
    words= text.split()
    seperate_lines= ''
    count = 0
    for word in words:
        if count+len(word)<= max_length:
            seperate_lines= seperate_lines+word
            seperate_lines = seperate_lines+' '
            count = count + len(word) + 1
        else:
            seperate_lines=seperate_lines.rstrip(' ')
            seperate_lines= seperate_lines +'\n'
            seperate_lines= seperate_lines+word
            seperate_lines = seperate_lines+' '
            count= len(word)+1
    seperate_lines=seperate_lines.rstrip(' ')
    return seperate_lines
