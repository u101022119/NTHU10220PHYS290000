def find(word, letter , wherestart):
    index = start
    while index < len(word):
        if word[index] == letter:
            return index+1
        index = index + 1
    return -1

