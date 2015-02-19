__author__ = 'benellis'
import sys
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

    def play_game(self):
        while not self.__game_over():
            p1card = self.player1.get_card_from_deck()
            p2card = self.player2.get_card_from_deck()
            print('Number of cards for Player 1: ', self.player1.size_of_deck())
            print('Number of cards for Player 2: ', self.player2.size_of_deck())
            print('Player 1 card: ', p1card.display_card())
            print('Player 2 card: ', p2card.display_card())
            if p1card.is_lower_val(p2card):
                print('Player 2 wins!')
                self.player2.add_card(self.player1.remove_card(), self.player2.size_of_deck())
                self.player2.add_card(self.player2.remove_card())
            elif p2card.is_lower_val(p1card):
                print('Player 1 wins!')
                self.player1.add_card(self.player2.remove_card(), self.player1.size_of_deck())
                self.player1.add_card(self.player1.remove_card())
            else: ## TIE
                pass
            pacer = input('Press C to continue or Q to quit')
            if pacer.lower() == 'q':
                print('-- exiting --')
                sys.exit()
            elif pacer.lower() not in ['q', 'c']:
                print(' -- invalid command.  continuing anyway.')
            print('\n')

    def __game_over(self):
        if self.player1.size_of_deck() == 0:
            print('Player 2 WINS IT ALL!')
            return True
        elif self.player2.size_of_deck() == 0:
            print('Player 1 WINS IT ALL!')
            return True
        else:
            return False