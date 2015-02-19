__author__ = 'benellis'

SUITS = ['hearts', 'diamonds', 'clubs', 'spades']
VALS  = ['ace', 'two', 'three', 'four', 'five', 'six',
         'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king']


class Card(object):
    def __init__(self, val, suit):
        self.__val = val
        self.__suit = suit

    def display_card(self):
        the_suit = self.__get_suit()
        the_val = self.__get_val()
        return the_val + ' of ' + the_suit

    def __get_suit(self):
        return SUITS[self.__suit]

    def __get_val(self):
        return VALS[self.__val]

    def is_lower(self, other):
        lower_suit = self.is_lower_suit(other)
        lower_val = self.is_lower_val(other)
        if lower_suit:
            return True
        elif lower_val and self.__suit == other.__suit:
            return True
        else:
            return False

    def is_lower_suit(self, other):
        if self.__suit < other.__suit:
            return True
        else:
            return False

    def is_lower_val(self, other):
        if self.__val < other.__val:
            return True
        else:
            return False
