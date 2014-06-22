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
        card.sort()
    def num_dict(card):
        l = [c.num for c in card.cards]
        l.sort()
        d = dict()
        for i in l :
            if d.get(i) is None:
                d[i] = 0
            d[i] += 1
        return d
    def suit_dict(card):
        l = [c.suit for c in card.cards]
        l.sort()
        d = dict()
        for i in l :
            if d.get(i) is None:
                d[i] = 0
            d[i] += 1
        return d
    def has_pair(card):
        d = card.num_dict()
        for i in d.values():
            if i is 2:
                return True
        return False
    def has_two_pair(card):
        d = card.num_dict()
        p = 0
        for i in d.values():
            if i is 2:
                p += 1
        if p >= 2:
            return True
        else:
            return False
    def has_three_of_a_kind(card):
        d = card.num_dict()
        for i in d.values():
            if i is 3:
                return True
        return False
    def has_straight(card):
        d = card.num_dict()
        for i in d.keys():
            test = True
            for j in range(5):
                if i+j not in d.keys():
                    test = False
            if test is True:
                return True
        return False
    def has_flush(card):
        d = card.suit_dict()
        for i in d.values():
            if i >= 5:
                return True
        return False
    def has_full_house(card):
        pair = card.has_pair()
        three = card.has_three_of_a_kind()
        ans = pair and three        
        return ans
    def has_four_of_a_kind(card):
        d = card.num_dict()
        for i in d.values():
            if i is 4:
                return True
        return False
    def has_straight_flush(card):
        card.sort()        
        for s in range(4):
            l = []
            for c in card.cards:
                if c.suit is s:
                    l.append(c.num)
            for i in l:
                test = True
                for j in range(5):
                    if i+j not in l:
                        test = False
                if test is True:
                    return True
        return False
    def classify(card):
        if card.has_straight_flush():
            return "has_straight_flush",1
        elif card.has_four_of_a_kind():
            return "has_four_of_a_kind",2
        elif card.has_full_house():
            return "has_full_house",3
        elif card.has_flush():
            return "has_flush",4
        elif card.has_straight():
            return "has_straight",5
        elif card.has_three_of_a_kind():
            return "has_three_of_a_kind",6
        elif card.has_two_pair():
            return "has_two_pair",7
        elif card.has_pair():
            return "has_pair",8
        else:
            return "has_nothing",9
        
        
        
        
h = Hand(7)
print h
print h.suit_dict()
print h.num_dict()
print h.classify()

num_test = 10000
count = {t:0 for t in range(1,10)}
for i in range(1,num_test):
    h = Hand(5)
    msg, test = h.classify()
    count[test] += 1
result = {t:count[t]*100.0/num_test for t in range(1,10)}
for t,i in  result.iteritems():
    print t,":",i,"%"
