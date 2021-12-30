import random

SUITS = ["Diamonds", "Spades", "Hearts", "Clubs"]
VALUES = ["A", "2" , "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

class Card:
    # initialize the instance (automatic)
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    # represent the object as a string
    def __repr__(self):
        return "{} of {}".format(self.value, self.suit)
    
    def suit(self):
        return self.suit
    
    def value(self):
        return self.value

class Deck:
    
    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for value in VALUES:
                card = Card(suit, value)
                self.cards.append(card)
    
    def num_cards(self):
        return len(self.cards)
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def peek(self):
        return self.cards[-1]
    
    def draw(self):
        return self.cards.pop()
    
    def add_card(self, card):
        if(self.num_cards() >= 52):
            raise ValueError("A deck cannot contain more than 52 cards!")
        else:
            self.cards.append(card)
    
    def print_deck(self):
        print(self.cards)