from __future__ import annotations
from typing import Type


class Currency:
    """
    1 EUR = 2 USD = 100 GBP
    1 EUR = 2 USD    ;  1 EUR = 100 GBP
    1 USD = 0.5 EUR  ;  1 USD = 50 GBP
    1 GBP = 0.02 USD ;  1 GBP = 0.01 EUR
    """

    conversion_rates = {
        "Euro": {"Euro": 1, "Dollar": 2, "Pound": 100},
        "Dollar": {"Euro": 0.5, "Dollar": 1, "Pound": 50},
        "Pound": {"Euro": 0.01, "Dollar": 0.02, "Pound": 1},
    }

    short_names = {
        "Euro": "EUR",
        "Dollar": "USD",
        "Pound": "GBP",
    }

    def __init__(self, value: float):
        self.value = value

    @classmethod
    def course(cls, other_cls: Type[Currency]) -> str:
        rate = cls.conversion_rates[cls.__name__][other_cls.__name__]
        formatted_rate = f"{rate:.2f}" if rate % 1 != 0 else f"{rate:.1f}"
        return f"{formatted_rate} {other_cls.short_names[other_cls.__name__]} for 1 {cls.short_names[cls.__name__]}"

    def to_currency(self, other_cls: Type[Currency]) -> Currency:
        rate = self.conversion_rates[self.__class__.__name__][other_cls.__name__]
        return other_cls(self.value * rate)

    def __add__(self, other: Currency) -> Currency:
        rate = self.conversion_rates[other.__class__.__name__][self.__class__.__name__]
        return self.__class__(self.value + other.value * rate)

    def __eq__(self, other: Currency) -> bool:
        self_in_euro = self.value * self.conversion_rates[self.__class__.__name__]["Euro"]
        other_in_euro = other.value * self.conversion_rates[other.__class__.__name__]["Euro"]
        return self_in_euro == other_in_euro

    def __lt__(self, other: Currency) -> bool:
        self_in_euro = self.value * self.conversion_rates[self.__class__.__name__]["Euro"]
        other_in_euro = other.value * self.conversion_rates[other.__class__.__name__]["Euro"]
        return self_in_euro < other_in_euro

    def __gt__(self, other: Currency) -> bool:
        return not (self < other or self == other)

    def __str__(self):
        formatted_value = f"{self.value:.2f}" if self.value % 1 != 0 else f"{self.value:.1f}"
        return f"{formatted_value} {self.short_names[self.__class__.__name__]}"


class Euro(Currency):
    pass


class Dollar(Currency):
    pass


class Pound(Currency):
    pass