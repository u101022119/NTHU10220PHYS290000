import random

list = []
print 'aaa'

def random_list( N, a, b):
    #cleanlist
    del list[:]
    #create a list
    randnumber = [None] * N                     
    for i in range( 0, N):
        #Return a random integer x such that a <= x <= b
        randnumber[i] = random.randint( a, b)
    #extend takes a list as an argument and appends all of the elements
    list.extend(randnumber)

def insertion_sort(list):
    for i in range( 1, len(list)):
        j = i
        while j > 0 and list[j - 1] > list[j]:
            list[j - 1], list[j] = list[j], list[j - 1]
            j = j - 1

def selection_sort(list):
    for i in range( 0, len(list)):
        min = i
        for j in range( i+1,len(list)): 
            if list[j] < list[min]:
                min = j
        list[i], list[min] = list[min], list[i]
            
    
def bubble_sort(list):
    for i in range( 0, len(list)):
        for j in range( 1, len(list)-i):
            if list[j] < list[j-1]:
                list[j], list[j-1] = list[j-1], list[j]
                
