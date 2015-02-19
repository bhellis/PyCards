__author__ = 'benellis'
#import card
#import deck
#import hand
import war


def main():
    war_game = war.War()
    war_game.player1.fancy_print()
    print('-' * 20)
    war_game.player2.fancy_print()

if __name__ == '__main__':
    main()