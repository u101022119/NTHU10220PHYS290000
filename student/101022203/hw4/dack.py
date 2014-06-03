Python 2.7.6 (default, Nov 10 2013, 19:24:18) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
>>> 
import random
class Card(object):
    suit_names = ['Clubs', 'Diamonds', 'Heart', 'Spades']
    rank_names = ['None','Ace', '2', '3', '4', '5', '6',
                  '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])                    
                  
    def __init__(self, suit = 0, rank = 2):
        self.suit = suit
        self.rank = rank

    def __cmp__(self, other):
        if self.suit > other.suit:
            return 1
        if self.suit < other.suit:
            return -1
        if self.rank > other.rank:
            return 1
        if self.rank < other.rank:
            return -1
        return 0

class Deck(object):
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit, rank)
                self.cards.append(card)

    def pop_card(self):
        return self.cards.pop()

+	    def add_card(self, card):
+	        self.cards.append(card)
+	
+	    def shuffle(self):
+	        random.shuffle(self.cards)
+	
+	class Hand(Deck):
+	    def __init__(self, label = ''):
+	        self.cards = []
+	        self.label = label
+	
+	    def move_cards(self, hand, num):
+	        for i in range(num):
+	            hand.add_card(self.pop_card())
+	            
+	deck = Deck()
+	hand = Hand()
+	for i in range(52):
+	    print hand.cards[i]
