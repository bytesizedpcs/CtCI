#!/usr/bin/python3
import random
# deck of cards
# 4 suits, diamonds, hearts, clubs, spades
# numbers: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13
# each suit has all of the numbers

class Card: 
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    suit = [
        'Diamond',
        'Heart',
        'Club',
        'Spade'
    ]

    def __init__(self):
        self.value = random.randint(1, 13)
        self.suit = random.choice(Card.suit)

    def __str__(self):
        return f'Card is: {self.value}, {self.suit}'


class Deck:
    cards = [] * 52

    def __init__(self):
        self.card = Card()
        cards.append(self.card)


    def lookUp(self, card):
        return

    def __str__(self):
        return f'Deck is: {Deck.cards}'


card = Card()
deck = Deck()
print (card)
print (deck)
