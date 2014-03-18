fruit = 'apple'
print len(fruit)
index = 0
while index < len(fruit):
    letter = fruit[index]
    print letter
    index = index + 1
print 'exercise:Write a function that takes a string as an argument and displays the letters backward, one per line.'
index = len(fruit)
while index > 0:
    letter = fruit[index - 1]
    print letter
    index = index - 1
