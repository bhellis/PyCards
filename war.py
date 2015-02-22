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
        if my_deck.size_of_deck() == 0:
            del my_deck
        else:
            raise AttributeError('Size of deck, after being dealt, should be zero')

    def __deal_card(self, total_deck, player_deck):
        while player_deck.size_of_deck() < self.__size_of_hand:
            player_deck.add_card(total_deck.remove_card())

    def play_game(self):
        nhands = 0
        while not self.__game_over():
            nhands += 1
            print('Hand Numer %s' % nhands)
            #print('Press C to continue or Q to quit')
            #pacer = input('>> ')
            #if pacer.lower() == 'q':
            #    print('-- exiting --')
            #    sys.exit()
            #elif pacer.lower() not in ['q', 'c']:
            #    print(' -- invalid command.  continuing anyway.')
            self.__play_round()
            print('\n')

    def __play_round(self):
        print('Number of cards for Player 1: ', self.player1.size_of_deck())
        print('Number of cards for Player 2: ', self.player2.size_of_deck())
        self.__declare_winning_hand()

    def __declare_winning_hand(self, i=0):
        p1card = self.player1.get_card_from_deck(i)
        p2card = self.player2.get_card_from_deck(i)
        print('Player 1 card: ', p1card.display_card())
        print('Player 2 card: ', p2card.display_card())
        if p2card.is_lower_val(p1card):
            print('Player 1 wins!')
            self.__winning_hand(self.player2, self.player1, i)
        elif p1card.is_lower_val(p2card):
            print('Player 2 wins!')
            self.__winning_hand(self.player1, self.player2, i)
        else:
            if not self.player1.size_of_deck() > i + 1:
                print('Player 1 has run out of cards!')
                for i in range(self.player1.size_of_deck()):
                    self.player1.remove_card()
            elif not self.player2.size_of_deck() > i + 1:
                print('Player 2 has run out of cards!')
                for i in range(self.player2.size_of_deck()):
                    self.player2.remove_card()
            else:
                self.__declare_winning_hand(i + 1)

    def __game_over(self):
        if self.player1.size_of_deck() == 0:
            print('Player 2 WINS IT ALL!')
            return True
        elif self.player2.size_of_deck() == 0:
            print('Player 1 WINS IT ALL!')
            return True
        else:
            return False

    def __winning_hand(self, give_from, give_to, i=0):
        ## modifies list while iterating - generally a bad idea
        for j in range(i + 1):
            give_to.add_card(give_from.remove_card(), give_to.size_of_deck())
            give_to.add_card(give_to.remove_card())





