class Card(object):
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

    def __init__(self, suit = 0, rank = 2):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])

    def __cmp__(self, other):
        c1 = (self.suit, self.rank)
        c2 = (other.suit, other.rank)
        return cmp(c1, c2)
    def is_valid(self):
        return self.rank > 0

class Deck(object):
    def __init__(self, label = 'Deck'):
        self.label = label
        self.cards = []
        for i in range(4):
            for k in range(1, 14):
                card = Card(i, k)
                self.cards.append(card)
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
            print self.label
            return '\n'.join(res)

    def deal_card(self):
        return self.cards.pop(0)

    def add_card(self, card):
        self.cards.append(card)

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def sort(self):
        self.cards.sort()

    def move_cards(self, other, num):
        for i in range(num):
            other.add_card(self.deal_card())
    def deal_hands(self, num_hands, num_cards):
        if num_hands*num_cards > 52:
            return 'Not enough cards.'
        l = []
        for i in range(1, num_hands + 1):
            hand_i = Hand('Hand %d' % i)
            self.move_cards(hand_i, num_cards)
            l.append(hand_i)
            return l

class Hand(Deck):
    def __init__(self, label = ''):
        self.cards = []
        self.label = label

 
