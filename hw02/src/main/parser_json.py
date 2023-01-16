"""
parser_json.py - модуль, отвечающий за обработку файла в формате json
"""
import json
from typing import List, Callable, Dict

from functions import upper


def validate_input(json_str: str,
                   keyword_callback: Callable,
                   required_fields: List[str] = None,
                   keywords: List[str] = None) -> None:
    """
    Валидация входных параметров функции
    :param json_str: str
    :param keyword_callback: Callable
    :param required_fields: List[str]
    :param keywords: List[str]
    :return: None
    """
    if not isinstance(json_str, str):
        raise TypeError

    if not isinstance(keyword_callback, Callable):
        raise TypeError

    if not isinstance(required_fields, list):
        raise TypeError
    if not all(isinstance(elem, str) for elem in required_fields):
        raise TypeError

    if not isinstance(keywords, list):
        raise TypeError
    if not all(isinstance(elem, str) for elem in keywords):
        raise TypeError


def parse_json(json_str: str,
               keyword_callback: Callable,
               required_fields: List[str] = None,
               keywords: List[str] = None) -> str:
    """
    Функция обработчик json-строк
    :param json_str: str - строка json, которую нужно обработать
    :param keyword_callback: Callable - функция обработчик слов, которые встретились в
     списке ключевых слов
    :param required_fields: List[str] - список необходимых полей
    :param keywords: List[str] - список ключевых слов, которые будут искаться в необходимых полях
    :return: None
    """
    validate_input(json_str, keyword_callback, required_fields, keywords)

    json_doc: Dict[str, str] = json.loads(json_str)

    for req_field in required_fields:
        for keyword in keywords:
            words = json_doc[req_field].split()
            for i, _ in enumerate(words):
                if words[i] == keyword:
                    words[i] = keyword_callback(words[i])
            json_doc[req_field] = ' '.join(words)

    return json.dumps(json_doc)


if __name__ == "__main__":
    jsons = []
    jsons.append(parse_json(json_str='{"a": "b", "c": "d"}',
                            keyword_callback=upper,
                            required_fields=["a"],
                            keywords=["b"]))
