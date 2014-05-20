fruit = 'banana'
letter = fruit[1]
print letter

len(fruit)
last = fruit[-1]
print last

print fruit[-2]

index = 0
while index < len(fruit) :
    letter = fruit[index]
    print letter
    index = index + 1

index = 5
while 0 <= index <= len(fruit) :
    letter = fruit[index]
    print letter
    index = index - 1

for char in fruit :
    print char

s = 'Monty Python'
print s[0:5]
print s[6:12]

fruit[3:3]

greeting = 'Hello, world!'
new_greeting = 'J' + greeting[1:]
print new_greeting

def find(word, letter) :
    index = 0
    while index < len(word) :
        if word[index] == letter :
            return index
        index =index + 1
    return -1
print find(fruit, letter)

def find(word, letter) :
    index = 0
    while index < len(word) :
        if word[index] == letter :
            return index
        index =index + 1
    return -1
print find(fruit, letter)

word = 'banana'
count = 0
for letter in word :
    if letter == 'a':
        count = count + 1
print count

word = 'banana'
new_word = word.upper()
print new_word

def in_both(word1,word2):
    for letter in word1:
        if letter in word2:
            print letter
in_both('apples', 'oranges')

numbers = [17,123]
numbers[1] = 5
print numbers

numbers = [17,123]
for i in range(len(numbers)) :
    numbers[i] = numbers[i] * 2
print numbers[i]

t = ['a', 'b', 'c', 'd', 'e', 'f']
t[1:3] = ['x', 'y']
print t
t.append('123')
print t

def add_all(l) :
    total = 0
    for x in l :
        total += x
    return total
l = [1, 2, 3, 4, 5]
s = [3, 4, 5, 6, 7]

print add_all(l+s)

def only_upper(t) :
    res = []
    for s in t:
        if s.isupper() :
            res.append(s)
    return res
t = ['a', 'b', 'c', 'd', 'e', 'f']
s = ['1', 'y', '3', 'd', 'e', 'f']
print only_upper(t)

s = 'spam'
t = list(s)
print t


def middle(f):
    return f [1:len(f)-1]
f = ['a', 'b', 'c', 'd', 'e', 'f']
print middle(f)
    
    


    







    

