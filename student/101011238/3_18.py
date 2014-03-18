# -*- coding: cp950 -*-
def letter_backward(word):
        index=len(word)-1
        while index>-1:
                letter=word[index]
                print letter
                index=index-1
#如何不換行

fruit = 'counter strike'

for char in fruit:
        print char


word = 'BanAna'
new_word = word.lower()
print new_word


def in_both(word1, word2):
        for letter in word1:
                if letter in word2:
                        print letter


x=fruit[::-1]

def is_palindrome(word1):
        word2=word1[::-1]
        if word1==word2:
                print 'True'
        else :
                print 'False'
Lagrange=1
Newton=2
Laplace=3
math = ['Lagrange','Newton','Laplace']

for x in math:
        print x





























