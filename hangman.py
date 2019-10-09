import argparse

from hangman import Game


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dict_path', type=str, default='default_dict.csv',
                        required=False,
                        help='Full path to *.txt file')
    parser.add_argument('--max_tries', type=int, default=5,
                        required=False,
                        help='The amount of wrong tries')

    args = parser.parse_args()

    game = Game(dict_path=args.dict_path, max_tries=args.max_tries)
    game.start()


if __name__ == '__main__':
    main()
