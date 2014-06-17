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
            h=PokerHand()
            for j in range(nc):
                h.cards.append(self.pop_card())
            hl.append(h)
        return hl
class Hand(Deck):
    def __init__(self,label=''):
        self.cards=[]
        self.label=label
class PokerHand(Hand):
    def devide_suit(self):
        self.li_suit=[[],[],[],[]]
        self.n_suit=[]
        for i in self.cards:
            self.li_suit[i.suit].append(i)
        for i in self.li_suit:
            self.n_suit.append(len(i))
    def devide_rank(self):
        self.li_rank=[[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
        self.n_rank=[]
        for i in self.cards:
            self.li_rank[i.rank].append(i)
        for i in self.li_rank:
            self.n_rank.append(len(i))
    def has_pair(self):
        self.devide_rank()
        for i in self.n_rank:
            if i>=2:
                return True
        return False
    def has_two_pair(self):
        self.devide_rank()
        for i in range(14):
            if self.n_rank[i]>=2:
                for j in self.n_rank[i+1:]:
                    if j>=2:
                        return True
                return False
        return False
    def has_three_of_a_kind(self):
        self.devide_rank()
        for i in self.n_rank:
            if i>=3:
                return True
        return False
    def has_straight(self):
        self.devide_rank()
        n=0
        if (self.n_rank[1]!=0 and self.n_rank[10]!=0 and self.n_rank[11]!=0 and self.n_rank[12]!=0 and self.n_rank[13]!=0):
            return True
        for i in self.n_rank:
            n+=1
            if i==0:
                n=0
            if n==5:
                return True
        return False
    def has_flush(self):
        self.devide_suit()
        for i in self.n_suit:
            if i>=5:
                return True
        return False
    def has_full_house(self):
        self.devide_rank()
        for i in range(14):
            if self.n_rank[i]>=3:
                for j in self.n_rank[0:i-1]:
                    if j>=2:
                        return True
                for j in self.n_rank[i+1:]:
                    if j>=2:
                        return True
                return False
        return False
    def has_four_of_a_kind(self):
        self.devide_rank()
        for i in self.n_rank:
            if i>=4:
                return True
        return False
    def has_straight_flush(self):
        self.devide_suit()
        self.clubs_hand=PokerHand()
        self.diamonds_hand=PokerHand()
        self.hearts_hand=PokerHand()
        self.spades_hand=PokerHand()
        for i in self.li_suit[0]:
            self.clubs_hand.add_card(i)
        for i in self.li_suit[1]:
            self.diamonds_hand.add_card(i)
        for i in self.li_suit[2]:
            self.hearts_hand.add_card(i)
        for i in self.li_suit[3]:
            self.spades_hand.add_card(i)
        return (self.clubs_hand.has_straight() or self.diamonds_hand.has_straight() or self.hearts_hand.has_straight() or self.spades_hand.has_straight())
    def classify(self):
        self.label = 'high card'
        if self.has_pair():
            self.label = 'pair'
        if self.has_two_pair():
            self.label = 'two pair'
        if self.has_three_of_a_kind():
            self.label = 'three of a kind'
        if self.has_straight():
            self.label = 'straight'
        if self.has_flush():
            self.label = 'flush'
        if self.has_full_house():
            self.label = 'full house'
        if self.has_four_of_a_kind():
            self.label = 'four of a kind'
        if self.has_straight_flush():
            self.label = 'straight flush'

n_straight_flush=0
n_four_of_a_kind=0
n_full_house=0
n_flush=0
n_straight=0
n_three_of_a_kind=0
n_two_pair=0
n_pair=0
n_high_card=0
for i in range(100000):
    d=Deck()
    ph=d.deal_hands(10,5)
    for i in ph:
        i.classify()
        if i.label == 'straight flush':
            n_straight_flush+=1
        if i.label == 'four of a kind':
            n_four_of_a_kind+=1
        if i.label == 'full house':
            n_full_house+=1
        if i.label == 'flush':
            n_flush+=1
        if i.label == 'straight':
            n_straight+=1
        if i.label == 'three of a kind':
            n_three_of_a_kind+=1
        if i.label == 'two pair':
            n_two_pair+=1
        if i.label == 'pair':
            n_pair+=1
        if i.label == 'high card':
            n_high_card+=1
print 'straight flush %d' % n_straight_flush
print 'four of a kind %d' % n_four_of_a_kind
print 'full house %d' % n_full_house
print 'flush %d' % n_flush
print 'straight %d' % n_straight
print 'three of a kind %d' % n_three_of_a_kind
print 'two pair %d' % n_two_pair
print 'pair %d' % n_pair
print 'high card %d' % n_high_card
