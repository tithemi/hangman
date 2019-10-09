import argparse

from hangman.game import Game


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dict_path', type=str, default='default_dict.csv',
                        required=False,
                        help='Full path to *.csv file with 1 column words for game.')
    parser.add_argument('--max_tries', type=int, default=5,
                        required=False,
                        help='The amount of wrong tries before a end of the game')

    args = parser.parse_args()

    game = Game(dict_path=args.dict_path, max_tries=args.max_tries)
    game.start()


if __name__ == '__main__':
    main()
