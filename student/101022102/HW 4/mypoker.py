import random  as rand

suit_dict = {0:"S",1:"H",2:"D",3:"C"}  
num_dict = {i:str(i) for i in range(1,14)}


class Card():
    def __init__(self,suit,num):
        if suit in range(4):
            if num in range(1,14):
                self.suit = suit
                self.num = num
                self.get_order()
        else:
            print "ERROR"
    def get_order(self):
        self.order = self.suit*13 + self.num
        return self.order
    
    def get_name(self):
        self.suit = int(self.order/13)
        self.num = int(self.order%13)
        return self
    def __str__(self):
        s = suit_dict[self.suit]
        n = num_dict[self.num]
        return s+'_'+n
    def __cmp__(self,C2):
        o1, o2 = self.get_order(), C2.get_order()
        if o1 < o2:
            return 1
        elif o1 > o2:
            return -1
        else:
            return 0
            

class Deck():
    def __init__(self):
        self.cards = []
        for i in range(4):
            for j in range(1,13):
                self.cards.append(Card(i,j))
    def __str__(self):
        str_list = ''
        for i in self.cards:
            s = suit_dict[i.suit]
            n = num_dict[i.num]
            str_list += s + "_" + n + ' '
        return str_list
    def pop_card(self,n):
        c = self.cards.pop(n)
        return c
    def add_card(self,c):
        if c in self.cards:
            print "ERROR"
        else:
            self.cards.append(c)
            return self
    def shuffle(self,n,m):
        if 0 <= n < len(self.cards) and 0 <= m < len(self.cards):
            c_temp = self.cards.pop(n)
            self.cards.insert(m,c_temp)
            return self
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
    def deal_hands(self,n_h,n_c):
        h_dict = dict()
        for i in range(n_h):
            h_temp = Hand()
            for j in range(n_c):
                r = rand.randint(0,len(self.cards)-1)
                c_temp = self.pop_card(r)
                h_temp.add_card(c_temp)
            h_dict[i] = h_temp.sort()
        for i in h_dict.values():
            print i
        return h_dict
        
        
class Hand(Deck):
    def __init__(self,n = 0):
        self.cards = []
        for i in range(n):
            test = False
            while test is False:
                test = True
                suit = rand.randint(0,3)
                num = rand.randint(1,13)
                c_temp = Card(suit,num)
                for i in self.cards:
                    if c_temp == i:
                        test = False
            self.cards.append(Card(suit,num))
        self.sort()
    def num_dict(self):
        l = [c.num for c in self.cards]
        l.sort()
        d = dict()
        for i in l :
            if d.get(i) is None:
                d[i] = 0
            d[i] += 1
        return d
    def suit_dict(self):
        l = [c.suit for c in self.cards]
        l.sort()
        d = dict()
        for i in l :
            if d.get(i) is None:
                d[i] = 0
            d[i] += 1
        return d
    def has_pair(self):
        d = self.num_dict()
        for i in d.values():
            if i is 2:
                return True
        return False
    def has_two_pair(self):
        d = self.num_dict()
        p = 0
        for i in d.values():
            if i is 2:
                p += 1
        if p >= 2:
            return True
        else:
            return False
    def has_three_of_a_kind(self):
        d = self.num_dict()
        for i in d.values():
            if i is 3:
                return True
        return False
    def has_straight(self):
        d = self.num_dict()
        for i in d.keys():
            test = True
            for j in range(5):
                if i+j not in d.keys():
                    test = False
            if test is True:
                return True
        return False
    def has_flush(self):
        d = self.suit_dict()
        for i in d.values():
            if i >= 5:
                return True
        return False
    def has_full_house(self):
        pair = self.has_pair()
        three = self.has_three_of_a_kind()
        ans = pair and three        
        return ans
    def has_four_of_a_kind(self):
        d = self.num_dict()
        for i in d.values():
            if i is 4:
                return True
        return False
    def has_straight_flush(self):
        self.sort()        
        for s in range(4):
            l = []
            for c in self.cards:
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
    def classify(self):
        if self.has_straight_flush():
            return "has_straight_flush",1
        elif self.has_four_of_a_kind():
            return "has_four_of_a_kind",2
        elif self.has_full_house():
            return "has_full_house",3
        elif self.has_flush():
            return "has_flush",4
        elif self.has_straight():
            return "has_straight",5
        elif self.has_three_of_a_kind():
            return "has_three_of_a_kind",6
        elif self.has_two_pair():
            return "has_two_pair",7
        elif self.has_pair():
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
