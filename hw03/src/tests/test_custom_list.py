import io
from unittest.mock import patch

import pytest

from src.main.custom_list import CustomList


@pytest.mark.parametrize("input,expected", [
    ([1, 2, 3], 3),
    ([], 0),
    (None, 0)],
                         ids=['len=3', 'len=0', 'len=0'])
def test_len(input, expected):
    custom_list = CustomList(input)
    output = len(custom_list)
    assert expected == output


@patch('sys.stdout', new_callable=io.StringIO)
def assert_stdout_str_magic_method(expected_output, mock_stdout):
    test = CustomList([1, 2, 3])
    print(test, end='')
    assert expected_output == mock_stdout.getvalue(), (
        f"\nexpected: {expected_output},\nresult:{mock_stdout.getvalue()}"
    )


def test_stdout_str_magic_method():
    value = "CustomList: data=[1, 2, 3]; sum=6."
    assert_stdout_str_magic_method(value)


@pytest.mark.parametrize("data", [
    (1), '1', (())], ids=["input_int", "input_str", "input_tuple"])
def test_add_magic_method_instance_custom_list_and_list(data):
    with pytest.raises(TypeError):
         CustomList([1, 2, 3]) + data


@pytest.mark.parametrize("data_self,data_other,expected", [
    ([1, 2, 3], [1, 2, 3],[2, 4, 6]),
    ([1, 2, 3], [1, 2], [2, 4, 3]),
    ([1, 2], [1, 2, 3], [2, 4, 3]),
    ([], [], [])],
                         ids=['self=[1, 2, 3]; other=[1, 2, 3]',
                              'self=[1, 2, 3]; other=[1, 2]',
                              'self=[1, 2]; other=[1, 2, 3]',
                              'self=[]; other=[]'])
def test_add_magic_method_custom_list_plus_custom_list(data_self, data_other, expected):
    result = CustomList(data_self) + CustomList(data_other)
    assert expected == result.data, (
        f"expected: {expected}, result: {result.data}"
    )


@pytest.mark.parametrize("data_self,data_other,expected", [
    ([1, 2, 3], [1, 2, 3],[2, 4, 6]),
    ([1, 2, 3], [1, 2], [2, 4, 3]),
    ([1, 2], [1, 2, 3], [2, 4, 3]),
    ([], [], [])],
                         ids=['self=[1, 2, 3]; other=[1, 2, 3]',
                              'self=[1, 2, 3]; other=[1, 2]',
                              'self=[1, 2]; other=[1, 2, 3]',
                              'self=[]; other=[]']
                         )
def test_add_magic_method_custom_list_plus_list(data_self, data_other, expected):
    result = CustomList(data_self) + data_other
    assert expected == result.data, (
        f"expected: {expected}, result: {result.data}"
    )


@pytest.mark.parametrize("data_self,data_other,expected", [
    ([1, 2, 3], [1, 2, 3],[0, 0, 0]),
    ([1, 2, 3], [1, 2], [0, 0, 3]),
    ([1, 2], [1, 2, 3], [0, 0, -3]),
    ([], [], [])],
                         ids=['self=[1, 2, 3]; other=[1, 2, 3]',
                              'self=[1, 2, 3]; other=[1, 2]',
                              'self=[1, 2]; other=[1, 2, 3]',
                              'self=[]; other=[]'])
def test_add_magic_method_custom_list_minus_custom_list(data_self, data_other, expected):
    result = CustomList(data_self) - CustomList(data_other)
    assert expected == result.data, (
        f"expected: {expected}, result: {result.data}"
    )


@pytest.mark.parametrize("data_self,data_other,expected", [
    ([1, 2, 3], [1, 2, 3],[0, 0, 0]),
    ([1, 2, 3], [1, 2], [0, 0, 3]),
    ([1, 2], [1, 2, 3], [0, 0, -3]),
    ([], [], [])],
                         ids=['self=[1, 2, 3]; other=[1, 2, 3]',
                              'self=[1, 2, 3]; other=[1, 2]',
                              'self=[1, 2]; other=[1, 2, 3]',
                              'self=[]; other=[]']
                         )
def test_add_magic_method_custom_list_minus_list(data_self, data_other, expected):
    result = CustomList(data_self) - data_other
    assert expected == result.data, (
        f"expected: {expected}, result: {result.data}"
    )


@pytest.mark.parametrize("data_self,data_other,expected", [
    ([1, 2, 3], [1, 2, 3], True),
    ([1, 2], [1, 2, 3], True),
    ([], [], True),
    ([1, 2, 3], [1, 2], False)],
                         ids=['self=[1, 2, 3]; other=[1, 2, 3]',
                              'self=[1, 2]; other=[1, 2, 3]',
                              'self=[]; other=[]',
                              'self=[1, 2, 3]; other=[1, 2]'])
def test_le_magic_method(data_self, data_other, expected):
    result = CustomList(data_self) <= CustomList(data_other)
    assert expected == result, (
        f"expected: {expected}, result: {result}"
    )


@pytest.mark.parametrize("data_self,data_other,expected", [
    ([1, 2, 3], [1, 2, 3], False),
    ([1, 2], [1, 2, 3], True),
    ([], [], False),
    ([1, 2, 3], [1, 2], False)],
                         ids=['self=[1, 2, 3]; other=[1, 2, 3]',
                              'self=[1, 2]; other=[1, 2, 3]',
                              'self=[]; other=[]',
                              'self=[1, 2, 3]; other=[1, 2]'])
def test_lt_magic_method(data_self, data_other, expected):
    result = CustomList(data_self) < CustomList(data_other)
    assert expected == result, (
        f"expected: {expected}, result: {result}"
    )


@pytest.mark.parametrize("data_self,data_other,expected", [
    ([1, 2, 3], [1, 2, 3], True),
    ([1, 2], [1, 2, 3], False),
    ([], [], True),
    ([1, 2, 3], [1, 2], True)],
                         ids=['self=[1, 2, 3]; other=[1, 2, 3]',
                              'self=[1, 2]; other=[1, 2, 3]',
                              'self=[]; other=[]',
                              'self=[1, 2, 3]; other=[1, 2]'])
def test_ge_magic_method(data_self, data_other, expected):
    result = CustomList(data_self) >= CustomList(data_other)
    assert expected == result, (
        f"expected: {expected}, result: {result}"
    )


@pytest.mark.parametrize("data_self,data_other,expected", [
    ([1, 2, 3], [1, 2, 3], False),
    ([1, 2], [1, 2, 3], False),
    ([], [], False),
    ([1, 2, 3], [1, 2], True)],
                         ids=['self=[1, 2, 3]; other=[1, 2, 3]',
                              'self=[1, 2]; other=[1, 2, 3]',
                              'self=[]; other=[]',
                              'self=[1, 2, 3]; other=[1, 2]'])
def test_gt_magic_method(data_self, data_other, expected):
    result = CustomList(data_self) > CustomList(data_other)
    assert expected == result, (
        f"expected: {expected}, result: {result}"
    )


@pytest.mark.parametrize("data_self,data_other,expected", [
    ([1, 2, 3], [1, 2, 3], True),
    ([1, 2], [1, 2, 3], False),
    ([], [], True),
    ([1, 2, 3], [1, 2], False)],
                         ids=['self=[1, 2, 3]; other=[1, 2, 3]',
                              'self=[1, 2]; other=[1, 2, 3]',
                              'self=[]; other=[]',
                              'self=[1, 2, 3]; other=[1, 2]'])
def test_gt_magic_method(data_self, data_other, expected):
    result = CustomList(data_self) == CustomList(data_other)
    assert expected == result, (
        f"expected: {expected}, result: {result}"
    )
