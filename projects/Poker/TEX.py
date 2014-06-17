from deck import deck
import sys

class Poker:
    
    
    def __init__(self, number_of_players, debug = False):
        self.deck = deck()
        if number_of_players < 2 or number_of_players > 10:
            sys.exit("*** ERROR ***: Invalid number of players. It must be between 2 and 10.")
        self.number_of_players = number_of_players
        self.debug = debug      
    def shuffle(self):
        self.deck.shuffle()    
        
   
    def cut(self, amount):
        return self.deck.cut(amount)
      
    def getFlop(self):  
        if not self.deck.deal(3):
            return False
        return self.deck.deal(3)
    
   
    def getOne(self):
        if not self.deck.deal(1):
            return False    
        return self.deck.deal(1)
    
  
    def distribute(self):
        number_of_cards = 2 
        if(number_of_cards*self.number_of_players > self.deck.cards_left() ):
            return False
        
        inplay = []
        for i in range(0, self.number_of_players):
            inplay.append( [] )            
        
       
        for i in range(0, number_of_cards):
            for j in range(0, self.number_of_players):
                inplay[j].append( self.deck.deal(1).pop() )
                    
        
        return inplay
    
  
    def name_of_hand(self, type_of_hand):
        if type_of_hand == 0:
            return "High Card"
        elif type_of_hand == 1:
            return "Pair"
        elif type_of_hand == 2:
            return "2 Pair"
        elif type_of_hand == 3:
            return "3 of a Kind"
        elif type_of_hand == 4:
            return "Straight"
        elif type_of_hand == 5:
            return "Flush"
        elif type_of_hand == 6:
            return "Full House"
        elif type_of_hand == 7:
            return "Four of a Kind"
        elif type_of_hand == 8:
            return "Straight Flush"
        else:
            return "Royal Flush"

   
    def score(self, hand):
        
        score = 0
        kicker = []
       
        pairs = {}
        prev = 0
        
       
        for card in hand:
            if prev == card.value:
                key = card.value
                if key in pairs:
                    pairs[key] += 1
                else:
                    pairs[key] = 2
            prev = card.value
        
      
        nop = {}
        for k, v in pairs.iteritems():
            if v in nop:
                nop[v] += 1
            else:
                nop[v] = 1
        
       
        
        if 4 in nop:         
            score = 7
            kicker = pairs.keys()
            
            kicker = [key for key in kicker if pairs[key] == 4] 
            key = kicker[0]
            temp = [card.value for card in hand if card.value != key]
            card_value = temp.pop()
            kicker.append(card_value)
            
            return [score, kicker] 
            
        elif 3 in nop:      
            if nop[3] == 2 or 2 in nop:     
                score = 6
                
                
                kicker = pairs.keys()
                kicker.reverse()
                temp = kicker
                
               
                kicker = [key for key in kicker if pairs[key] == 3]
                if( len(kicker) > 1):   
                    kicker.pop() 
                
                
                temp.remove(kicker[0])
                card_value = temp[0]
                kicker.append(card_value)
                
            else:           
                score = 3
                
                kicker = pairs.keys()       
                key = kicker[0]
                
                
                temp = [card.value for card in hand if card.value != key]
                card_value = temp.pop()
                kicker.append(card_value)
                
                card_value = temp.pop()
                kicker.append(card_value)
    
        elif 2 in nop:      
            if nop[2] >= 2:     
                score = 2
                
                kicker = pairs.keys()   
                
                if ( len(kicker) == 3 ):   
                    kicker.pop()
                    
                key1 = kicker[0]
                key2 = kicker[1]
                
                
                temp = [card.value for card in hand if card.value != key1 and card.value != key2]
                card_value = temp.pop()
                kicker.append(card_value)
                
            else:          
                score = 1 
                
                kicker = pairs.keys()   
                key = kicker[0] 
     
             
                temp = [card.value for card in hand if card.value != key]

                card_value = temp.pop()
                kicker.append(card_value)
                
                card_value = temp.pop()
                kicker.append(card_value)
                
                card_value = temp.pop()
                kicker.append(card_value)
                
        
       
        counter = 0
        high = 0
        straight = False
        
       
        if (hand[6].value == 14): 
            prev = 1
        else: 
            prev = None
            
       
        for card in hand:
            if prev and card.value == (prev + 1):
                counter += 1
                if counter == 4: 
                    straight = True
                    high = card.value
            elif prev and prev == card.value: 
                pass
            else:
                counter = 0
            prev = card.value
        
      
        if (straight or counter >= 4) and score < 4:
            straight = True  
            score = 4
            kicker = [high]
            
        flush = False
        total = {}
        
      
        for card in hand:
            key = card.symbol
            if key in total:
                total[key] += 1
            else:
                total[key] = 1
        
        
        key = -1
        for k, v in total.iteritems():
            if v >= 5:
                key = int(k)
        
   
        if key != -1 and score < 5:
            flush = True
            score = 5
            kicker = [card.value for card in hand if card.symbol == key]        
        
        
    
        if flush and straight:
            
          
            counter = 0
            high = 0
            straight_flush = False
            if (kicker[len(kicker)-1] == 14): 
                prev = 1
            else: 
                prev = None
                
            
            for card in kicker:
                if prev and card == (prev + 1):
                    counter += 1
                    if counter >= 4: 
                        straight_flush = True
                        high = card
                elif prev and prev == card: 
                    pass
                else:
                    counter = 0
                prev = card
          
            if straight_flush:
                if high == 14:
                    score = 9
                else:
                    score = 8
                kicker = [high]
                return [score, kicker]
        
        if flush:    
            kicker.reverse()
            
           
            length = len(kicker) - 5
            for i in range (0,length):
                kicker.pop()
                
        if score == 0:
            
            kicker = [int(card.value) for card in hand]
           
            kicker.reverse()
           
            kicker.pop()

            kicker.pop()       
         
        return [score, kicker]
    
    
  
    def determine_score(self, community_cards, players_hands):
        
        for hand in players_hands:
            hand.extend(community_cards)
            hand.sort()
    
        results = []
        if self.debug:      
            print "---- Determining Scores----"
        for hand in players_hands:
                     
            overall = self.score(hand)
            results.append([overall[0], overall[1]])    
            
            
            if self.debug:               
                text = "Hand -- " 
                for c in hand:
                    text += str(c) + "  "
    
                kicker = ""
                for c in overall.pop(1):
                    try:
                        kicker += str(c) + "  "
                    except:
                        kicker += str(c) + "  "
                print text + "Score: " + str(overall.pop(0)) + ", Kicker: " + kicker
        
        
        return results
        
 
    def determine_winner(self, results):
        if self.debug:
            print "---- Determining Winner----"
            
     
        high = 0
        for r in results:
            if r[0] > high:
                high = r[0]
            
            if self.debug:
                print r
        
        kicker = {}    
        counter = 0
     
        for r in results:
            if r[0] == high:
                kicker[counter] = r[1]
                
            counter += 1
        
      
        if(len(kicker) > 1):
            
            if self.debug: 
                print "---- Tie Braker ----"
                print "---- Kicker ----"
                for k, v in kicker.items():
                    print str(k) + " : " + str(v)
            
           
            number_of_kickers = len(kicker[kicker.keys().pop()])
            for i in range (0, number_of_kickers):
                high = 0
                for k, v in kicker.items():
                    if v[i] > high:
                        high = v[i]
                
           
                kicker = {k:v for k, v in kicker.items() if v[i] == high}
                
                if self.debug: 
                    print "---- " + "Round " + str(i) + " ----"
                    for k in kicker:
                        print k
                        
              
                if( len(kicker) <= 1):
                    return kicker.keys().pop()
                
        else: 
            return kicker.keys().pop()
        
       
        return kicker.keys()
