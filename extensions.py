import requests as rq
import json
from config import keys


class APIException(Exception):
    pass


class Converter:
    @staticmethod
    def get_price(qoute: str, base: str, amount: str):

        try:
            qoute_ticker = keys[qoute]
        except KeyError:
            raise APIException(f'Неправильно введены данные. Вы ввели {qoute} {base} в качестве валют')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Неправильно введены данные. Вы ввели {qoute} {base} в качестве валют')

        if qoute == base:
            raise APIException(f'Введены две одинаковые валюты {qoute}')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Нечисловые данные в количестве валют. Вы ввели {amount}')

        r = rq.get(f'https://min-api.cryptocompare.com/data/price?fsym={qoute_ticker}&tsyms={base_ticker}')
        r = json.loads(r.content)[keys[base]] * amount
        return r
