import random
suit=['clubs', 'heart', 'diamond', 'spades']
rank=['1', '2', '3', '4', '5', '6','7', '8', '9', '10', 'J', 'Q', 'K']
class Card():

    def __init__(self, suit, rank):
        self.suit= suit
        self.rank= rank
    def __str__(self):
        return '%s of %s' % (suit[self.suit], rank[self.rank])
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
    def __str__(self):
        for i in range(len(self.card)):
            print self.card[i]
        return ''


class Hand(Deck):
    def __init__(self, label=''):
        self.card = []
        self.label = label
    def has_pair(self):
        for i in range(13):
            a=0
            for j in range(5):
                if self.card[j].rank == i:
                    a+=1
            if a == 2:
                return True
        return False
        return False    
    def has_two_pair(self):
        for i in range(13):
            a=0
            b=0
            for j in range(5):
                if self.card[j].rank == i:
                    a+=1
                    for k in range(13):
                        if self.card[j].rank == k and i!=k:
                            b+=1
            if a == 2 and b==2:
                return True
        return False

    def has_three_of_a_kind(self):
        for i in range(13):
            a=0
            for j in range(5):
                if self.card[j].rank == i:
                    a+=1
            if a == 3:
                return True
        return False

    def flush(self):
        for i in range(4):
            suit1=self.card[i].suit
            suit2=self.card[i+1].suit
            if suit1 != suit2:
                return False
        return True
    def full_house(self):
        if self.has_three_of_a_kind == True:
            if self.has_pair == True:
                return True
        return False
        
    def four_of_a_kind(self):
        for i in range(13):
            a=0
            for j in range(5):
                if self.card[j].rank == i:
                    a+=1
            if a == 4:
                return True
        return False
    def straight(self):
        ranka=[]
        for i in range(5):
            ranka.append(self.card[i].rank)
        ranka.sort()

        for j in range(4):
            if ranka[j+1]-ranka[j]==1:
                return True
        return False
    def straight_flush(self):
        if self.straight == True:
            if self.flush == True:
                return True
        return False
        
                        
    
deck=Deck()
y=deck.deal_hands(1,5)

print y[0]
print y[0].straight_flush()
