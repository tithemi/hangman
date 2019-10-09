from hangman.game import Game

def test_easy_win():
    """
    Check if we won the game the current_word is the rigth one
    """
    game = Game()
    game.set_dict(['win'])
    game.input_stream = ['w', 'i', 'n']
    result = game.start()

    assert result
    assert game.current_word == 'win'

test_easy_win()

