import random  as rand

suit_dict = {0:"S",1:"H",2:"D",3:"C"}  ## S = Spade , H = Heart , D = Diamond , C = Club
num_dict = {i:str(i) for i in range(2,11)}
num_dict[1] = 'A'
num_dict[11] = 'J'
num_dict[12] = 'Q'
num_dict[13] = 'K'

class Card():
    def __init__(card,suit,num):
        if suit in range(4) and num in range(1,14):
            card.suit = suit
            card.num = num
            card.get_order()
        else:
            print "ERROR"
    def get_order(card):
        if card.num == 1:
            num = 14
        else:
            num = card.num
        card.order = card.suit*13 + (15 - num)
        return card.order
    def get_name(card):
        card.suit = int(card.order/13)
        card.num = int(card.order%13)
        if card.num == 14:
            card.num = 1
        return card
    def __str__(card):
        s = suit_dict[card.suit]
        n = num_dict[card.num]
        return s+'_'+n
    def __cmp__(card,C2):
        o1, o2 = card.get_order(), C2.get_order()
        if o1 < o2:
            return 1
        elif o1 > o2:
            return -1
        else:
            return 0
            
#c1 = Card(0,1)
#print c1
#c2 = Card(1,1)
#print c1.order,c2.order,c1 > c2, c1 == c2, c1 < c2

class Deck():
    def __init__(card):
        card.cards = []
        for i in range(4):
            for j in range(1,13):
                card.cards.append(Card(i,j))
    def __str__(card):
        str_list = ''
        for i in card.cards:
            s = suit_dict[i.suit]
            n = num_dict[i.num]
            str_list += s + "_" + n + ' '
        return str_list
    def pop_card(card,n):
        c = card.cards.pop(n)
        return c
    def add_card(card,c):
        if c in card.cards:
            print "ERROR"
        else:
            card.cards.append(c)
            return card
    def shuffle(card,n,m):
        if 0 <= n < len(card.cards) and 0 <= m < len(card.cards):
            c_temp = card.cards.pop(n)
            card.cards.insert(m,c_temp)
            return card
    def sort(card):
        d = card.cards
        for i in range(1,len(d)):
            valueToInsert = d[i]
            holePos = i
            while holePos > 0 and valueToInsert > d[holePos-1]:
                d[holePos] = d[holePos-1]
                holePos = holePos - 1
            d[holePos] = valueToInsert
        card.cards = d
        return card
    def deal_hands(card,n_h,n_c):
        h_dict = dict()
        for i in range(n_h):
            h_temp = Hand()
            for j in range(n_c):
                r = rand.randint(0,len(card.cards)-1)
                c_temp = card.pop_card(r)
                h_temp.add_card(c_temp)
            h_dict[i] = h_temp.sort()
        for i in h_dict.values():
            print i
        return h_dict
        
        
#d = Deck()
#print d
##d.add_card(0,1)
##print d
##d.shuffle(1,1)
##print d
#d.sort()
#print d
        
class Hand(Deck):
    def __init__(card,n = 0):
        card.cards = []
        for i in range(n):
            test = False
            while test is False:
                test = True
                suit = rand.randint(0,3)
                num = rand.randint(1,13)
                c_temp = Card(suit,num)
                for i in card.cards:
                    if c_temp == i:
                        test = False
            card.cards.append(Card(suit,num))
#h = Hand()
#print h.sort()
            
d = Deck()
h_dict = d.deal_hands(4,5)
                
            