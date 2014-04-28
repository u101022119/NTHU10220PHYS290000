def find(word,letter):   #word and letter is string!
    index=0
    while index<len(word):
        if word[index]==letter:
            return index
        index=index+1
    return -1
