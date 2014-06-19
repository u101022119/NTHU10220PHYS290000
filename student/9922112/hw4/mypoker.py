# -*- coding: utf-8 -*-
"""
Created on Tue Jun 10 11:35:18 2014

@author: Administrator
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Jun 09 16:15:32 2014

@author: Administrator
"""
import random

class Card(object):
    """Represents a standard playing card."""
    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7','8', '9', '10', 'Jack', 'Queen', 'King']
    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],Card.suit_names[self.suit])
    def __cmp__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return cmp(t1, t2)

def kind(n,ranks):
    for r in ranks:
        if ranks.count(r) >=n:
            return 'True'
    return 'False'
                        
class Deck(object):
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
    def pop_card(self):
        return self.cards.pop()
    def add_card(self, card):
        self.cards.append(card)
    def shuffle(self):
        random.shuffle(self.cards)
    def sort(self):
        self.cards.sort()
        
    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())
    def deal_hands(self,n1,n2): #n1,n2 represent:the number of hands and the number of cards per hand
        H=[]
        for i in range(n1):
            hand=Hand()
            self.move_cards(hand,n2)
            H.append(hand)
        return H #會是一個list, 每一個element是發出去的手牌
    def rank_list(self): #將Hand的rank轉為list
        L=[]
        for x in self.cards:
            L.append(x.rank)
        return L               
    def has_pair(self):
        R=self.rank_list()
        return kind(2,R)
    def has_two_pairs(self):
        R=self.rank_list()
        n=0
        for r in R:
            if R.count(r)>=2:
                n=n+1
        return n/2>=2
    def has_three_of_a_kind(self):
        R=self.rank_list()
        return kind(3,R)
    def has_flush(self):
        R=self.rank_list()
        p=0
        q=0
        for r in R:
            if R.count(r) >=3:
               p=r
            elif R.count(r)==2:
               q=r
        return p!=q and p>0 and q>0
    def classify(self):
        if self.has_flush()==True:
            return 'flush'
        else:
            if self.has_three_of_a_kind()=="True":
                return 'three of a kind'
            else:
                if self.has_two_pairs()==True:
                    return 'two pairs'
                else:
                    if self.has_pair()=="True":
                        return 'pairs'       
        
class Hand(Deck):
    """Represents a hand of playing cards."""
    def __init__(self,cards=[], label=''):
        self.cards = []
        self.label = label
         
def probability(category,n):#計算某種牌型(category)，發牌n次，平均發牌一次拿到的機率
    d=Deck()
    h=Hand()
    s=0
    for i in range(n):
        d=Deck()
        hand=Hand()
        d.shuffle()
        d.move_cards(hand,5)
        if hand.classify()==category:
            s=s+1
    return float(s)/n*100         


print probability('flush',10000),"%"

