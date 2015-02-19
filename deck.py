__author__ = 'benellis'
import sys
import card as CD
import random as RD

N_SUITS = len(CD.SUITS)
N_VALS  = len(CD.VALS)
N_CARDS = N_SUITS * N_VALS


class Deck(object):
    def __init__(self):
        self._this_deck = []
        for suit in range(N_SUITS):
            for val in range(N_VALS):
                self._this_deck.append(CD.Card(val, suit))

    def print_deck(self):
        for i, icard in enumerate(self._this_deck):
            print('[' + str(i + 1) + ']', icard.display_card())

    def shuffle_deck(self):
        for i in range(len(self._this_deck)):
            j = RD.randrange(len(self._this_deck))
            self.__swap_cards(i, j)

    def sort_deck(self):
        while not self.__sorted():
            for i in range(len(self._this_deck)):
                for j in range(i + 1, len(self._this_deck)):
                    if not self._this_deck[i].is_lower(self._this_deck[j]):
                        self.__swap_cards(i, j)

    def __swap_cards(self, i, j):
        tmp = self._this_deck[i]
        self._this_deck[i] = self._this_deck[j]
        self._this_deck[j] = tmp

    def __sorted(self):
        for i in range(0, N_CARDS):
            for j in range(i + 1, N_CARDS):
                if not self._this_deck[i].is_lower(self._this_deck[j]):
                    return False
        return True

    def remove_card(self, i=0):
        try:
            removed = self._this_deck.pop(i)
        except IndexError:
            print('Removing a card that isn\'t there! %s' % i)
            sys.exit()
        return removed

    def add_card(self, card, i=0):
        self._this_deck.append(card)

    def remove_rand_card(self):
        irand = RD.randrange(len(self._this_deck))
        return self.remove_card(irand)

    def find_card(self, val, suit):
        translator = {1: 'ace', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six',
                      7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten'}
        if val not in CD.VALS and val in translator:
            val = translator[val]
        mysearch = val.lower() + ' of ' + suit.lower()
        for idx, card in enumerate(self._this_deck):
            if card.display_card() == mysearch:
                return idx
        else:
            return False

    def fancy_print(self):
        step = 4
        plist = []
        for idx, iCard in enumerate(self._this_deck):
            plist.append(' '.join(['[' + str(idx + 1) + ']', iCard.display_card()]))
            if (idx + 1) % 4 == 0:
                print(self.__make_fancy_line(plist))
                plist = []
        if len(plist) > 0:
            print(self.__make_fancy_line(plist))

    def merge_decks(self, other):
        for card in other._this_deck:
            self._this_deck.append(card)

    def check_deck_size(self):
        if self is type(Deck):
            if len(self._this_deck) == N_CARDS:
                return True
            else:
                return False
        else:
            print('Can\'t check outside of Deck')
            return False

    def size_of_deck(self):
        return len(self._this_deck)

    def __make_fancy_line(self, the_list):
        line = ''
        for sub in the_list:
            line += '{:<30}'.format(sub)
        return line

    def get_card_from_deck(self, i=0):
        return self._this_deck[i]



