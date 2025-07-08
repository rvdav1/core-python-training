class PriceControl:
    """
    Descriptor which doesn't allow to set price less than 0 and more than 100 included.
    """
    def __init__(self):
        self._value = {}

    def __get__(self, instance, owner):
        return self._value.get(instance)

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError("Price must be between 0 and 100.")
        self._value[instance] = value


class NameControl:
    """
    Descriptor which doesn't allow to change field value after initialization.
    """
    def __init__(self):
        self._value = {}

    def __get__(self, instance, owner):
        return self._value.get(instance)

    def __set__(self, instance, value):
        if instance in self._value:
            raise ValueError(f"{self.__class__.__name__.replace('Control', '')} can not be changed.")
        self._value[instance] = value


class Book:
    author = NameControl()
    name = NameControl()
    price = PriceControl()

    def __init__(self, author, name, price):
        self.author = author
        self.name = name
        self.price = price