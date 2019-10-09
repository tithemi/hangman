import pandas as pd
import random
import numpy as np
import sys

class Game:
    def __init__(self, dict_path='hangman/default_dict.txt', max_tries=5):
        self.words = [line.rstrip('\n') for line in open(dict_path)]
        self.initial_word = random.choice(self.words)
        self.letters = np.array(list(self.initial_word))
        self.max_tries = max_tries
        self.input_stream = sys.stdin
        self.current_word = np.array(list('*' * len(self.initial_word)))

    def set_dict(self, wordlist):
        self.words = wordlist

    def start(self):
        tries = 0

        current_word = np.array(list('*' * len(self.initial_word)))

        lines = self.input_stream

        while tries < self.max_tries:
            print('Guess a letter:')
            for line in lines:
                guess = line

                if guess in self.letters:
                    print('Hit!')

                    idx = np.where(self.letters == guess)
                    current_word[idx] = guess
                else:
                    tries += 1

                    print("Missed, mistake " + str(tries) + "out of " + str(self.max_tries) + ".")

                print("\nThe word: " + ''.join(current_word) + "\n")
                if not '*' in current_word:
                    print('You won!')
                    return True

        print('You lost!')
        return False

