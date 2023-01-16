"""
custom_list.py - модуль, реализующий класс CustomList, отнаследованный от списка
"""
from __future__ import annotations
from typing import Tuple


class CustomList(list):
    """
    Контейнер CustomList, наследующийся от list
    """

    def __init__(self, data=None):
        """
        Инициализация класса
        @param args:
        @type args:
        """
        super(CustomList, self).__init__()
        if data is not None:
            self.data = data
        else:
            self.data = []

    def __len__(self) -> int:
        """
        Количество элементов в контейнере
        @return: количество элементов
        @rtype: int
        """
        return len(self.data)

    def __str__(self):
        return f"CustomList: data={self.data}; sum={sum(self.data)}."

    def __add__(self, other) -> CustomList:
        """
        Метод для реализации сложения контейнеров типа CustomList и List
        @param other: Контейнер с которым будет происходить операция сложения
        @return: Новый контейнер типа CustomList
        @rtype: CustomList
        """
        if isinstance(other, CustomList):
            self_custom, other_custom = self.check_lens_and_add_zeros(other)
            result = CustomList(
                [self_custom.data[i] + other_custom.data[i]
                 for i, _ in enumerate(self_custom.data)])
        elif isinstance(other, list):
            other_custom_list = CustomList(other)
            self_custom, other_custom = self.check_lens_and_add_zeros(other_custom_list)
            result = CustomList(
                [self_custom.data[i] + other_custom.data[i]
                 for i, _ in enumerate(self_custom.data)])
        else:
            raise TypeError

        return result

    def check_lens_and_add_zeros(self, other: CustomList) -> Tuple[CustomList, CustomList]:
        """
        Метод проверяющий длину контейнеров и добавляющий необходимые нули
        @param other: Контейнер
        @type other: CustomList
        @return: Два контейнера, готовые к арифметическим операциям
        @rtype: Tuple[CustomList, CustomList]
        """
        delta: int = len(self.data) - len(other.data)
        if delta == 0:
            return self, other
        elif delta < 0:
            copy_self = CustomList(self.data.copy())
            copy_self = copy_self.add_zeros(abs(delta))
            return copy_self, other
        else:
            copy_other = CustomList(other.data.copy())
            copy_other = copy_other.add_zeros(delta)
            return self, copy_other

    def add_zeros(self, n: int) -> CustomList:
        """
        Добавление недостающих нулей для операций сложения и вычитания
        @param n: количество требуемых нулей
        @type n: int
        @return: экземпляр CustomList с добавленными n нулями
        @rtype: CustomList
        """
        copy_data = self.data.copy()
        for _ in range(n):
            copy_data.append(0)
        return CustomList(copy_data)

    def __sub__(self, other: CustomList) -> CustomList:
        """
        Метод для реализации вычитания контейнеров типа CustomList и List
        @param other: Контейнер с которым будет происходить операция вычитания
        @return: Новый контейнер типа CustomList
        @rtype: CustomList
        """
        if isinstance(other, CustomList):
            self_custom, other_custom = self.check_lens_and_add_zeros(other)
            result = CustomList(
                [self_custom.data[i] - other_custom.data[i]
                 for i, _ in enumerate(self_custom.data)])
        elif isinstance(other, list):
            other_custom_list = CustomList(other)
            self_custom, other_custom = self.check_lens_and_add_zeros(other_custom_list)
            result = CustomList(
                [self_custom.data[i] - other_custom.data[i]
                 for i, _ in enumerate(self_custom.data)])
        else:
            raise TypeError

        return result

    def __le__(self, other: CustomList) -> bool:
        return sum(self.data) <= sum(other.data)

    def __lt__(self, other: CustomList) -> bool:
        return sum(self.data) < sum(other.data)

    def __ge__(self, other: CustomList) -> bool:
        return sum(self.data) >= sum(other.data)

    def __gt__(self, other: CustomList) -> bool:
        return sum(self.data) > sum(other.data)

    def __eq__(self, other: CustomList) -> bool:
        return sum(self.data) == sum(other.data)


if __name__ == "__main__":
    A = CustomList([1, 2, 3])
    B = CustomList([1, 2])
    print(A + B)
