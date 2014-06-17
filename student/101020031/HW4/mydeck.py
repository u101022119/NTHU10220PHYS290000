import random
class Card(object):
    suit_names = ['Clubs','Diamonds','Hearts','Spades']
    rank_names = [None,'Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
    def __init__(self,suit=0,rank=2):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return '%s of %s' % (self.rank_names[self.rank],self.suit_names[self.suit])
    def __cmp__(self, other):
        ns = self.suit+self.rank*4
        if ns<=7:
            ns+=52
        no = other.suit+other.rank*4
        if no<=7:
            no+=52
        if ns>no:
            return 1
        if ns<no:
            return -1
        return 0
class Deck(object):
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit,rank)
                self.cards.append(card)
    def __str__(self):
        self.res = []
        for card in self.cards:
            self.res.append(card.__str__())
        return '\n'.join(self.res)
    def pop_card(self):
        return self.cards.pop()
    def add_card(self,card):
        self.cards.append(card)
    def shuffle(self):
            random.shuffle(self.cards)
    def sort(self):
        so=[]
        for i in range(len(self.cards)):
            m = min(self.cards)
            so.append(m)
            self.cards.remove(m)
        self.cards=so
    def deal_hands(self,nh,nc):
        hl=[]
        self.shuffle()
        for i in range(nh):
            h=Hand()
            for j in range(nc):
                h.cards.append(self.pop_card())
            hl.append(h)
        return hl
class Hand(Deck):
    def __init__(self,label=''):
        self.cards=[]
        self.label=label

c1 = Card(1,10)
c2 = Card(0,1)
print c2>c1
d = Deck()
print d

print '\npopcard:'
for i in range(13):
    d.pop_card()
print d

print '\naddcard'
d.add_card(Card(3,13))
print d

d.shuffle()
print '\nshuffle'
print d

d.sort()
print '\nsort'
print d

hl=d.deal_hands(4,5)
print'\ndeal_hand'
for i in range(len(hl)):
    print 'hand%d' % (i+1)
    print hl[i]
