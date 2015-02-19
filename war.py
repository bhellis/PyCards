__author__ = 'benellis'
import deck
import hand


class War(object):
    def __init__(self):
        self.__size_of_hand = deck.N_CARDS // 2
        my_deck = deck.Deck()
        my_deck.shuffle_deck()
        self.player1 = hand.Hand()
        self.player2 = hand.Hand()
        self.__deal_card(my_deck, self.player1)
        self.__deal_card(my_deck, self.player2)
        #myDeck.add_card(self.player1._myDeck[0])
        if my_deck.size_of_deck() == 0:
            del my_deck
        else:
            raise AttributeError('Size of deck, after being dealt, should be zero')

    def __deal_card(self, total_deck, player_deck):
        while player_deck.size_of_deck() < self.__size_of_hand:
            player_deck.add_card(total_deck.remove_card())
