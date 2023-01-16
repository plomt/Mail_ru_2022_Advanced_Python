from unittest.mock import MagicMock

import pytest

from src.main.parser_json import parse_json
from src.main.utils import generate_json
from src.main.functions import upper


@pytest.mark.parametrize("json_str,keyword_callback,required_fields,keywords", [
    (1, MagicMock(return_value=3), ['key_field'], ['word_keyword']),
    ([], MagicMock(return_value=3), ['key_field'], ['word_keyword'])],
                         ids=['json_str_is_int=1', 'json_str_is_empty_list'])
def test_validate_input_json_str(json_str,
                                 keyword_callback,
                                 required_fields,
                                 keywords):
    with pytest.raises(TypeError):
        parse_json(json_str, keyword_callback, required_fields, keywords)


@pytest.mark.parametrize("json_str,keyword_callback,required_fields,keywords", [
    (str(generate_json(1)[0]), 1, ['key_field'], ['word_keyword']),
    (str(generate_json(1)[0]), [], ['key_field'], ['word_keyword'])],
                         ids=['keyword_callback_is_int', 'keyword_callback_is_empty_list'])
def test_validate_input_keyword_callback(json_str,
                                         keyword_callback,
                                         required_fields,
                                         keywords):
    with pytest.raises(TypeError):
        parse_json(json_str, keyword_callback, required_fields, keywords)


@pytest.mark.parametrize("json_str,keyword_callback,required_fields,keywords", [
    (str(generate_json(1)[0]), MagicMock(return_value=3), 1, ['word_keyword']),
    (str(generate_json(1)[0]), MagicMock(return_value=3), (), ['word_keyword'])],
                         ids=['required_fields_is_int', 'required_field_is_tuple'])
def test_validate_input_required_fields(json_str,
                                        keyword_callback,
                                        required_fields,
                                        keywords):
    with pytest.raises(TypeError):
        parse_json(json_str, keyword_callback, required_fields, keywords)


@pytest.mark.parametrize("json_str,keyword_callback,required_fields,keywords", [
    (str(generate_json(1)[0]), MagicMock(return_value=3), [[]], ['word_keyword']),
    (str(generate_json(1)[0]), MagicMock(return_value=3), [1], ['word_keyword'])],
                         ids=['required_fields_elements_is_list', 'required_fields_elements_is_int'])
def test_validate_input_required_fields_elements(json_str,
                                                 keyword_callback,
                                                 required_fields,
                                                 keywords):
    with pytest.raises(TypeError):
        parse_json(json_str, keyword_callback, required_fields, keywords)


@pytest.mark.parametrize("json_str,keyword_callback,required_fields,keywords", [
    (str(generate_json(1)[0]), MagicMock(return_value=3), ['key_field'], 1),
    (str(generate_json(1)[0]), MagicMock(return_value=3), ['key_field'], ())],
                         ids=['input_keywords_is_int', 'input_keywords_is_tuple'])
def test_validate_input_keywords(json_str,
                                 keyword_callback,
                                 required_fields,
                                 keywords):
    with pytest.raises(TypeError):
        parse_json(json_str, keyword_callback, required_fields, keywords)


@pytest.mark.parametrize("json_str,keyword_callback,required_fields,keywords", [
    (str(generate_json(1)[0]), MagicMock(return_value=3), ['key_field'], [1]),
    (str(generate_json(1)[0]), MagicMock(return_value=3), ['key_field'], [[]])],
                         ids=['input_keywords_elements_is_int', 'input_keywords_elements_is_list'])
def test_validate_input_keywords_elements(json_str,
                                          keyword_callback,
                                          required_fields,
                                          keywords):
    with pytest.raises(TypeError):
        parse_json(json_str, keyword_callback, required_fields, keywords)


def test_parse_json():
    json_str = '{"a": "b", "c": "d"}'
    expected_output = '{"a": "B", "c": "d"}'
    result = parse_json(json_str=json_str,
                        keyword_callback=upper,
                        required_fields=['a'],
                        keywords=['b'])
    assert expected_output == result, (
        f"expected: {expected_output}, result: {result}"
    )
