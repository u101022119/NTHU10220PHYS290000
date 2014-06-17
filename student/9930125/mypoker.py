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

class PokerHand(Hand):
 
	def suit_hist(self):
		self.suits = {}
		for card in self.cards:
			self.suits[card.suit] = self.suits.get(card.suit, 0) + 1
		return self.suits
 
	def rank_hist(self):
		self.ranks = {}
		for card in self.cards:
			self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1
		return self.ranks
 
	def P(self):
		self.rank_hist()
		for val in self.ranks.values():
			if val >= 2:
				return True
		return False
 
	def TP(self):
		self.rank_hist()
		count = 0
		for val in self.ranks.values():
			if val == 4:
				return True
			elif val >= 2 and val < 4:
				count += 1
		return count >= 2
 
	def TOAK(self):
		self.rank_hist()
		for val in self.ranks.values():
			if val >= 3:
				return True
		return False
 
	def STRseq(self):
		seq = []
		l = STRlist()
		self.rank_hist()
		h = self.ranks.keys()
		h.sort()
		if len(h) < 5:
			return []
 
		#high Aces:
		if 1 in h:
			h.append(1)
 
		for i in range(5, len(h)+1):
			if h[i-5:i] in l:
				seq.append(h[i-5:i])
		return seq
 
	def STR(self):
		seq = self.STRseq()
		return seq != []
 
	def FL(self):
		self.suit_hist()
		for val in self.suits.values():
			if val >= 5:
				return True
		return False
 
	def FH(self):
		d = self.rank_hist()
		keys = d.keys()
 
		for key in keys:
			if d[key] >= 3:
				keys.remove(key)
				for key in keys:
					if d[key] >= 2:
						return True
		return False
 
	def FOAK(self):
		self.rank_hist()
		for val in self.ranks.values():
			if val >= 4:
				return True
		return False
 
	def SFL(self):
		seq = self.STRseq()
		if seq == []:
			return False
		for list in seq:
			list_suits = []
			for index in list:
				for card in self.cards:
					if card.rank == index:
						list_suits.append(card.suit)
			list_hist = histogram(list_suits)
			for key in list_hist.keys():
				if list_hist[key] >= 5:
					return True
		return False
 
	def classify(self):
		self.scores = []
		hands = ['Pair', 'Two-Pair', 'Three of a Kind', 'Straight', 'Flush', 'Full House', 'Four of a Kind', 'Straight Flush']
		if self.P():
			self.scores.append(1)
		if self.TP():
			self.scores.append(2)
		if self.TOAK():
			self.scores.append(3)
		if self.STR():
			self.scores.append(4)
		if self.FL():
			self.scores.append(5)
		if self.FH():
			self.scores.append(6)
		if self.FOAK():
			self.scores.append(7)
		if self.SFL():
			self.scores.append(8)
		if self.scores != []:
			return hands[max(self.scores)-1]
 
def STRlist():
	s = []
	for i in range(0,9):
		s.append(range(1,14)[i:i+5])
	s.append([10,11,12,13,1])	
	return s
 
def histogram(l):
	d = dict()
	for k in range(len(l)):
		d[l[k]] = 1 + d.get(l[k],0)
	return d

