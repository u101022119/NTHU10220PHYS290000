fruit='banana'

"""
index=-1
while index>=-len(fruit):
    letter=fruit[index]
    print letter
    index=index-1
"""

"""
def find(word, letter):
    index=0
    while index<len(word):
        if word[index]==letter:
            return index
        index=index+1
    return -1

print find("dghfghfghfthb", "b")
"""

"""
word='banana'
count=0
for letter in word:
    if letter=='a':
        count=count+1
        print count
"""
"""
word='banana'
word.find('na',3)

name='bob'
print name.find('b',1,2)
"""
"""
def in_both(w1 ,w2):
    for letter in w1:
        if letter in w2:
            print letter

in_both('apples','oranges')
"""

numbers = [2,4,6,8]
print len(numbers)
for i in range(len(numbers)):
    numbers[i]=numbers[i]*2

print numbers
