"""
tic_tac_game.py - реализует логику игры крестики-нолики
"""
from typing import Tuple, Set

from logger import get_logger

RUS_TINY_O = 1086
RUS_TINY_X = 1093
EN_TINY_O = 111
EN_TINY_X = 120

logger = get_logger("tic_tac_game.py")


class TicTacGame:
    """
    TicTacGame - класс, реализующий логику игры крестики-нолики
    """

    def __init__(self):
        self.board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        self.hist_coord: Set[Tuple[int, int]] = set()
        self.last_value: str = ''
        self.is_winner: bool = False
        self.available_coords: Set[Tuple[int, int]] = {(x, y) for x in range(3) for y in range(3)}

    def show_board(self) -> None:
        """
        Функция, которая отображает игровую доску
        :return: None
        """
        for row in self.board:
            print("|", end='')
            for cell in row:
                print(cell, end="|")
            print()
            print("+" * 7)

    def validate_input(self, x: int, y: int, value: str) -> None:
        """
        Функция проверяет куда вставляется значение и само значение.
        Оно должно быть либо 'х', либо 'o'
        :param x: int - координата поля по оси абсцисс
        :param y: int - координата поля по оси ординат
        :param value: str - значение 'x' или 'o'
        :return: None
        """
        if not isinstance(x, int) or not isinstance(y, int):
            logger.exception("Тип координат должен быть целочисленный(int), "
                             "предоставлен: x=%s, y=%s", type(x), type(y))
            raise TypeError

        if value not in ["x", "o"]:
            logger.exception("Вставляемое значение должно быть 'o' или 'х', "
                             "предоставлено: value=%s", value)
            raise ValueError

        if value == self.last_value:
            logger.exception("Вставляемое значение должно быть отлично от предыдущего, "
                             "предоставлено: value=%s", value)
            raise ValueError

        if (x, y) in self.hist_coord:
            logger.exception("Координаты должны быть отличны от используемых ранее, "
                             "предоставлены координаты: (x=%s, y=%s)", x, y)
            raise ValueError

        if x not in [0, 1, 2]:
            logger.exception("Координата x должна быть от 0 до 2, "
                             "предоставлена координата: x=%s", x)
            raise ValueError

        if y not in [0, 1, 2]:
            logger.exception("Координата y должна быть от 0 до 2, "
                             "предоставлена координата: y=%s", y)
            raise ValueError

    def start_game(self):
        """
        Функция, являющаяся входной точкой для запуска игры
        :return: None
        """
        cnt = 0
        while not self.is_winner and cnt < 9:
            print("Доступны следующие поля: "
                  f"{sorted(self.available_coords.difference(self.hist_coord))}")
            print("Введите 3 значения через пробел: "
                  "координата х (значения от 0 до 2), "
                  "координата y (значения от 0 до 2), "
                  "значение x или o")
            print("Пример ввода: 0 1 x")
            try:
                x, y, value = map(str, (input().split()))
                x = int(x)
                y = int(y)
            except ValueError:
                logger.exception("Ошибка при вводе параметров")
                raise

            if ord(value.lower()) == RUS_TINY_X or ord(value.lower()) == EN_TINY_X:
                value = chr(EN_TINY_X)
            elif ord(value.lower()) == RUS_TINY_O or ord(value.lower()) == EN_TINY_O:
                value = chr(EN_TINY_O)

            self.validate_input(x=x, y=y, value=value)
            self.last_value = value
            self.hist_coord.add((x, y))
            self.board[x][y] = value
            self.show_board()

            self.is_winner, value = self.check_winner()
            cnt += 1

        self.is_winner, self.last_value = self.check_winner()
        if self.is_winner:
            print(f"ПОБЕДИЛ ИГРОК, ИГРАЮЩИЙ ЗА {self.last_value}!")
        else:
            print("НИЧЬЯ!")

    def check_winner(self) -> Tuple[bool, str]:
        """
        Функция проверяет есть ли победитель на поле
        :return: Tuple[bool, str]
        """
        list_of_direct = [
            [self.board[0][0], self.board[0][1], self.board[0][2]],  # первая строка
            [self.board[1][0], self.board[1][1], self.board[1][2]],  # вторая строка
            [self.board[2][0], self.board[2][1], self.board[2][2]],  # третья строка
            [self.board[0][0], self.board[1][0], self.board[2][0]],  # первый столбец
            [self.board[0][1], self.board[1][1], self.board[2][1]],  # второй столбец
            [self.board[0][2], self.board[1][2], self.board[2][2]],  # третий столбец
            [self.board[0][0], self.board[1][1], self.board[2][2]],  # главная диагональ
            [self.board[0][2], self.board[1][1], self.board[2][0]]  # побочная диагональ
        ]

        for direct in list_of_direct:
            for value in ['x', 'o']:
                if all([value == item for item in direct]):
                    return True, value
        return False, str(None)


if __name__ == "__main__":
    game = TicTacGame()
    game.show_board()
    game.start_game()
