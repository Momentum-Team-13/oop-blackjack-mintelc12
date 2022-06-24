import random

CARDVALUE_PAIRS = {"Ace":[1,11], "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, 
        "eight":8, "nine":9, "ten":10, "Jack":10, "Queen":10, "King":10}
SUITS = ["♥️", "♦️", "♣️", "♠️"]


class Card():
    def __init__(self, suit, value_rank):
        self.suit = suit
        self.value_rank = value_rank


    def __str__(self):
        return f"{self.value_rank[0]} of {self.suit}  is worth {self.value_rank[1]} points."
        
class Deck():
    def __init__(self):
        self.cards = []
        self.create_deck(SUITS, CARDVALUE_PAIRS)

    def create_deck(self, suits, cardvalue_pairs):
        for suit in suits:
            for pair in cardvalue_pairs.items():
                card = Card(suit, pair)
                self.cards.append(card)

deck = Deck()
for card in deck.cards:
    print(card)


    def show_suits(self):
        return f""

    def get_suits(self):
        pass

    def show_keyvalue_ranks(self):
        pass
    
    def get_keyvalue_ranks(self):
        pass


class Player():
    pass

class Dealer():
    pass

class Game():
    pass
