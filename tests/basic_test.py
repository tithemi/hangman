from hangman.game import Game

def test_easy_win():
    """
    Check if we won the game the current_word is the rigth one
    """
    game = Game()
    game.set_dict(['test'])
    game.input_stream = ['t', 'e', 's', 't']
    result = game.start()

    assert result
    assert game.current_word == 'test'

test_easy_win()

