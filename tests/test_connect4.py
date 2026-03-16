from pprint import pprint

import connect4

def test_create_game():
    """Testing that we can create a game"""
    # When
    game = connect4.Connect4()


def test_display_board__empty():
    """Testing the display of an empty board"""
    # Given
    game = connect4.Connect4()
    expected_board = """
|      |
|      |
|      |
|      |
|      |
|      |
|      |
"""

    # When
    board = game.display_board()

    # Then
    assert board == expected_board


def tst_play_column():
    # Given
    game = connect4.Connect4()
    expected_board = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
    ]

    # When
    game.play_column(2)

    # Then
    assert game._board == expected_board


def tst_play_column__2_plays():
    # Given
    game = connect4.Connect4()
    expected_board = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
    ]

    # When
    game.play_column(2)
    game.play_column(2)

    # Then
    assert game._board == expected_board


def tst_display_board__after_some_plays():
    """Testing the display of after 3 plays
    Player 1 will put a coin in col 2
    Player 2 will put a coin in col 3
    and Player 1 will put a coin in col 2 again
    """
    # Given
    game = connect4.Connect4()
    expected_board = """
|      |
|      |
|      |
|      |
|      |
| O    |
| OX   |
"""

    # When
    game.play_column(2)
    game.play_column(3)
    game.play_column(2)
    board = game.display_board()

    # Then
    assert board == expected_board


def tst_get_winner_id__vertical_case():
    """Player 1 will play 4 times in column 2,
    Player 2 will play 3 times in column 3,
    -> Player 1 wins
    """
    
    # Given
    game = connect4.Connect4()

    # When
    # Each player played 3 times
    game.play_column(2)
    game.play_column(3)
    game.play_column(2)
    game.play_column(3)
    game.play_column(2)
    game.play_column(3)

    # No winner for now
    winner = game.get_winner_id()
    assert winner == 0

    game.play_column(2)
    # Player 1 wone
    winner = game.get_winner_id()
    assert winner == 1

