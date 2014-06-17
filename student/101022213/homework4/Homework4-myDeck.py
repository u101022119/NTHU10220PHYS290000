# -*- coding: utf-8 -*-
"""
Created on Tue Jun 17 12:31:32 2014

@author: USER
"""
import random

class Card(object):
    """Represents a standard playing card."""

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7','8', '9', '10', 'Jack', 'Queen', 'King']

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],Card.suit_names[self.suit])


    def cmp(self, other):
        # check the suits
        if self.suit > other.suit: return 'ther first is bigger'
        if self.suit < other.suit: return 'ther second is bigger'
        # suits are the same... check ranks
        if self.rank > other.rank: return 'ther first is bigger'
        if self.rank < other.rank: return 'ther second is bigger'
        # ranks are the same... it's a tie
        return 'equal'
        

card1 = Card(2, 11)
card2 = Card(0,1)
print card1
print card2
cmp(card1,card2)


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
        d = self.cards
        for i in range(1,len(d)):
            valueToInsert = d[i]
            holePos = i
            while holePos > 0 and valueToInsert > d[holePos-1]:
                d[holePos] = d[holePos-1]
                holePos = holePos - 1
            d[holePos] = valueToInsert
        self.cards = d
        return self
        
deck = Deck()
card3 = deck.pop_card()
print '-------------------------------------------------'
print card3
print '-------------------------------------------------'
print deck
print '-------------------------------------------------'
deck.add_card(card3)
print deck
print '-------------------------------------------------'

deck.shuffle()
print deck
print '-------------------------------------------------'

class Hand(Deck):
    """Represents a hand of playing cards."""
    
    def __init__(self, label=''):
        self.cards = []
        self.label = label
  
      

   
