import random  as rand

shape_dict = {0:"S",1:"H",2:"D",3:"C"}  ## S = Spade , H = Heart , D = Diamond , C = Club
number_dict = {i:str(i) for i in range(2,11)}
number_dict[1] = 'A'
number_dict[11] = 'J'
number_dict[12] = 'Q'
number_dict[13] = 'K'

class Card():
    def __init__(self,shape,number):
        if shape in range(4) and number in range(1,14):
            self.shape = shape
            self.number = number
            self.get_order()
        else:
            print "false"
    def get_order(self):
        if self.number == 1:
            number = 14
        else:
            number = self.number
        self.order = self.shape*13 + (15 - number)
        return self.order
    def get_name(self):
        self.shape = int(self.order/13)
        self.number = int(self.order%13)
        if self.number == 14:
            self.number = 1
        return self
    def __str__(self):
        s = shape_dict[self.shape]
        n = number_dict[self.number]
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
        for x in range(4):
            for y in range(1,13):
                self.cards.append(Card(x,y))
    def __str__(self):
        str_list = ''
        for x in self.cards:
            s = shape_dict[x.shape]
            n = number_dict[x.number]
            str_list += s + "_" + n + ' '
        return str_list
    def pop_card(self,n):
        c = self.cards.pop(n)
        return c
    def add_card(self,c):
        if c in self.cards:
            print "false"
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
        for x in range(1,len(d)):
            valuetoinsert = d[x]
            holeposition = x
            while holeposition > 0 and valuetoinsert > d[holeposition-1]:
                d[holeposition] = d[holeposition-1]
                holeposition = holeposition - 1
            d[holeposition] = valuetoinsert
        self.cards = d
        return self
    def deal_hands(self,n_h,n_c):
        h_dict = dict()
        for x in range(n_h):
            h_temp = Hand()
            for y in range(n_c):
                r = rand.randint(0,len(self.cards)-1)
                c_temp = self.pop_card(r)
                h_temp.add_card(c_temp)
            h_dict[x] = h_temp.sort()
        for x in h_dict.values():
            print x
        return h_dict
                
class Hand(Deck):
    def __init__(self,n = 0):
        self.cards = []
        for x in range(n):
            test = False
            while test is False:
                test = True
                suit = rand.randint(0,3)
                num = rand.randint(1,13)
                c_temp = Card(suit,num)
                for x in self.cards:
                    if c_temp == x:
                        test = False
            self.cards.append(Card(suit,num))
    def number_dict(self):
        l=[c.number for c in self.cards]
        l.sort()
        d=dict()
        for x in l:
            if d.get(x) is None:
                d[x]=0
            d[x] += 1
        return d
    def shape_dict(self):
        l=[c.shape for c in self.cards]
        l.sort()
        d=dict()
        for x in l:
            if d.get(x) is None:
                d[x]=0
            d[x] += 1
        return d
    def has_pair(self):
        d=self.number_dict()
        for x in d.values():
            if x is 2:
                return True
        return False
    def has_two_pair(self):
        d=self.number_dict()
        p=0
        for x in d.values():
            if x is 2:
                p+=1
        if p>=2:
            return True
        return False
    def has_three_of_a_kind(self):
        d=self.number_dict()
        for x in d.values():
            if x is 3:
                return True
        return False
    def has_straight(self):
        d = self.number_dict()
        for x in d.keys():
            test = True
            for y in range(5):
                if x+y not in d.keys():
                    test = False
            if test is True:
                return True
        return False
    def has_flush(self):
        d = self.shape_dict()
        for x in d.values():
            if x >= 5:
                return True
        return False
    def has_full_house(self):
        pair = self.has_pair()
        three = self.has_three_of_a_kind()
        ans = pair and three        
        return ans
    def has_four_of_a_kind(self):
        d = self.number_dict()
        for x in d.values():
            if x is 4:
                return True
        return False
    def has_straight_flush(self):
        self.sort()        
        for s in range(4):
            l = []
            for c in self.cards:
                if c.shape is s:
                    l.append(c.number)
            for x in l:
                test = True
                for y in range(5):
                    if x+y not in l:
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
        
        
        
        
h = Hand(14)
print h
print h.shape_dict()
print h.number_dict()
print h.classify()


