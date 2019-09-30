import pandas as pd
import random
import numpy as np


class Game:
    def __init__(self, dict_path='default_dict.csv', max_tries=5):
        words = pd.read_csv(dict_path)
        words = list(words[words.columns[0]])
        self.initial_word = random.choice(words)
        self.letters = np.array(list(self.initial_word))
        self.max_tries = max_tries

    def start(self):
        tries = 0

        current_word = np.array(list('*' * len(self.initial_word)))

        while tries < self.max_tries:
            print('Guess a letter:')
            guess = input()

            if guess in self.letters:
                print('Hit!')

                idx = np.where(self.letters == guess)
                current_word[idx] = guess
            else:
                tries += 1

                print(f"Missed, mistake {tries} out of {self.max_tries}.")

            print(f"\nThe word: {''.join(current_word)}\n")
            if not '*' in current_word:
                print('You won!')
                return

        print('You lost!')
        return

