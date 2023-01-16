"""
utils.py - модуль с вспомогательными функциями
"""
from typing import Dict, List

from faker import Faker


def generate_json(num: int) -> List[Dict]:
    """
    Генерация данных в формате json
    :param num: int - количество данных
    :return: List[Dict]
    """
    jsons = []
    fake = Faker(locale="Ru_ru")
    for i in range(num):
        doc = {
            'name': fake.name(),
            'address': fake.address(),
            'company': fake.company(),
            'country': fake.country(),
            'text': fake.sentence()
        }
        jsons.append(doc)
    return jsons
