#EX1----------------------------------------------
def back_string(t):
    number = 1
    while number < len(t)+1:
        print t[-number]
        number = number +1

L='fuck'
back_string(L)
#EX end-------------------------------------------
#EX2----------------------------------------------

def find(word,letter,index):
    num = 0
    while index<len(word):
        if word[index]==letter:
            num = num+1 
        index = index +1
    print letter,'in',word,'count from',index,'have',num

word = raw_input("please give me a word!")
letter = raw_input("give a a letter you want to find in word.")
index = input("you want to find the letter from which position ?give me a number")
find(word,letter,index)

#end
#EX3
#def count(word,alphabeta,num):
#    word = raw_input("please give me a word!")
#    alphabeta = raw_input("give a a letter you want to find in word.")
#    num=0
#    for letter in word :
#        if letter==alphabeta :
#            num =num +1
#    print count


