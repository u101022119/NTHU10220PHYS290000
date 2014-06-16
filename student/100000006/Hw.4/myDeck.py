import random  as rand

suit_dict = {0:"S",1:"H",2:"D",3:"C"} 
num_dict = {i:str(i) for i in range(2,11)}
num_dict[1]  = 'A'
num_dict[11] = 'J'
num_dict[12] = 'Q'
num_dict[13] = 'K'

class Card():
    def __init__(self,suit,num):
        if suit in range(4) and num in range(1,14):
            self.suit = suit
            self.num = num
            self.get_order()
        else:
            print "ERROR"
    def get_order(self):
        if self.num == 1:
            num = 14
        else:
            num = self.num
        self.order = self.suit*13 + (15 - num)
        return self.order
    def get_name(self):
        self.suit = int(self.order/13)
        self.num = int(self.order%13)
        if self.num == 14:
            self.num = 1
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

            
d = Deck()
h_dict = d.deal_hands(4,5)
                
            
