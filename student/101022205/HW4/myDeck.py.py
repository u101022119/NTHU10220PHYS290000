import random
class Card():
    suit=['clubs', 'heart', 'diamond', 'spades']
    rank=['1', '2', '3', '4', '5', '6','7', '8', '9', '10', 'J', 'Q', 'K']
    def __init__(self, suit, rank):
        self.suit= suit
        self.rank= rank
    def __str__(self):
        return str(self.suit)+str(self.rank)
    def __cmp__(self, other):
        if self.rank < other.rank:
            return 1
        elif self.suit< other.suit:
            return 1
        elif self.rank > other.rank:
            return -1
        elif self.suit < other.suit:
            return -1
        else:
            return 0

class Deck():
    def __init__(self):
        self.card=[]
        for i in range(4):
            for j in range(13):
                card=Card(i, j)
                self.card.append(card)
    def pop_card(self, position):
        self.card.pop(position)
    def add_card(self, position):
        self.card.append(position)
    def shuffle(self):
        random.shuffle(self.card)
    def deal_hands(self, player, card):
        hand_list= []
        for a in range(player):
            h=Hand()
            for b in range(card):
                h.card.append(Card(random.randint(0,3),random.randint(0,12)))
            hand_list.append(h)
        return hand_list
                


class Hand(Deck):
    def __init__(self, label=''):
        self.card = []
        self.label = label
    
        
deck=Deck()
y=deck.deal_hands(2, 3)
for i in range(3):
    print y[0].card[i]





