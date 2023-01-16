import io
from unittest.mock import patch
from textwrap import dedent

import pytest

from src.main.tic_tac_game import TicTacGame


@patch('sys.stdout', new_callable=io.StringIO)
def assert_stdout_show_board(expected_output, mock_stdout):
    game = TicTacGame()
    game.show_board()
    assert expected_output == mock_stdout.getvalue(), (
        f"expected:\n{expected_output}, result:\n{mock_stdout.getvalue()}"
    )


def test_show_board():
    value = dedent("""\
    | | | |
    +++++++
    | | | |
    +++++++
    | | | |
    +++++++
    """)
    assert_stdout_show_board(value)


@pytest.mark.parametrize("x,y,value", [
    (1.0, 1.0, 'x'),
    ('1', '1', 'x')],
                         ids=["float_coord", "string_coord"])
def test_validate_input_check_type_coordinates(x, y, value):
    game = TicTacGame()
    with pytest.raises(TypeError):
        game.validate_input(x=x, y=y, value=value)


@pytest.mark.parametrize("x,y,value", [
    (1, 1, "X"),
    (1, 1, "O"),
    (1, 1, "1"),
    (1, 1, "0")],
                         ids=["value=X", "value=O", "value=1", "value=0"])
def test_validate_input_check_value(x, y, value):
    game = TicTacGame()
    with pytest.raises(ValueError):
        game.validate_input(x=x, y=y, value=value)


@pytest.mark.parametrize("x,y,value,last_value", [
    (0, 0, 'x', 'x'),
    (0, 0, 'o', 'o')],
                         ids=["last_value=x, value=x",
                              "last_value=o, value=o"])
def test_validate_input_check_last_value_not_equal_to_new_value(x, y, value, last_value):
    game = TicTacGame()
    game.last_value = last_value
    with pytest.raises(ValueError):
        game.validate_input(x=x, y=y, value=value)


@pytest.mark.parametrize("x,y,value,hist_coord", [
    (0, 0, 'x', {(0, 0)})],
                         ids=["add (x=0, y=0), hist_coord={(0, 0)}"])
def test_validate_input_check_new_coord_is_really_new(x, y, value, hist_coord):
    game = TicTacGame()
    game.hist_coord = hist_coord
    with pytest.raises(ValueError):
        game.validate_input(x=x, y=y, value=value)


@pytest.mark.parametrize("x,y,value", [
    (-1, 0, 'x'),
    (3, 0, 'x')],
                         ids=["x=-1", "x=3"])
def test_validate_input_check_coord_x_in_range_0_2(x, y, value):
    game = TicTacGame()
    with pytest.raises(ValueError):
        game.validate_input(x=x, y=y, value=value)


@pytest.mark.parametrize("x,y,value", [
    (0, -1, 'x'),
    (0, 3, 'x')],
                         ids=["y=-1", "y=3"])
def test_validate_input_check_coord_y_in_range_0_2(x, y, value):
    game = TicTacGame()
    with pytest.raises(ValueError):
        game.validate_input(x=x, y=y, value=value)


@pytest.fixture(params=[
    ([['x', 'x', 'x'],
      ['o', 'o', ''],
      ['', '', '']], (True, 'x')),
    ([['o', 'o', ''],
      ['x', 'x', 'x'],
      ['', '', '']], (True, 'x')),
    ([['', '', ''],
      ['o', 'o', ''],
      ['x', 'x', 'x']], (True, 'x')),
    ([['x', 'o', 'o'],
      ['', 'x', ''],
      ['', '', 'x']], (True, 'x')),
    ([['o', 'o', 'x'],
      ['', 'x', ''],
      ['x', '', '']], (True, 'x')),
    ([['x', 'o', ''],
      ['x', 'o', ''],
      ['x', '', '']], (True, 'x')),
    ([['o', 'x', ''],
      ['o', 'x', ''],
      ['', 'x', '']], (True, 'x')),
    ([['', 'o', 'x'],
      ['', 'o', 'x'],
      ['', '', 'x']], (True, 'x')),
    ([['x', 'o', 'x'],
      ['o', '', ''],
      ['', 'o', 'x']], (False, str(None)))],
    ids=["winner_x_1st_row",
         "winner_x_2nd_row",
         "winner_x_3rd_row",
         "winner_x_1st_col",
         "winner_x_2nd_col",
         "winner_x_3rd_col",
         "winner_x_main_diagonal",
         "winner_x_side_diagonal",
         "winner_x_draw"])
def param_test(request):
    return request.param


def test_check_winner(param_test):
    (input, expected_output) = param_test
    game = TicTacGame()
    game.board = input
    result = game.check_winner()
    assert expected_output == result, (
        f"expected: {expected_output}, result: {result}"
    )


@patch('builtins.input', lambda: '1 2 x o')
def test_start_game_number_input_more_values():
    game = TicTacGame()
    with pytest.raises(ValueError):
        game.start_game()


@patch('builtins.input', lambda: '1 2')
def test_start_game_number_input_less_values():
    game = TicTacGame()
    with pytest.raises(ValueError):
        game.start_game()
