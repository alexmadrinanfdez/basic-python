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
    # define equality between the object of the class
    def __eq__(self, other):
        if(self.suit == other.suit and self.value == other.value):
            return True
        else:
            return False
    
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
            raise Exception("A deck cannot contain more than 52 cards!")
        elif(card.suit not in SUITS or card.value not in VALUES):
            raise ValueError(f"The {card} does belong to this deck.")
        elif(card in self.cards):
            raise ValueError("A deck can't have duplicate cards!")
        else:
            self.cards.append(card)
    
    def print_deck(self):
        for card in self.cards:
            print(card, end=', ')
        # remove last comma
        print('\b\b ')

if __name__ == "__main__":
    deck = Deck()
    print("The ordered deck:")
    deck.print_deck()   
    deck.shuffle()
    print("\nAfter being shuffled:")
    deck.print_deck()

    print("\nDraw thrice from the deck:")
    deck.draw()
    deck.draw()
    deck.draw()
    deck.print_deck()

    card = Card('Swords', 'King') # raises an exception
    deck.add_card(card)