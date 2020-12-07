class Product():
    def __init__(self, name, price, quantity, description) -> None:
        self.__name = name
        self.__price = price
        self.__quantity = quantity
        self.__description = description

    def get_name(self) -> str:
        return self.__name
    def get_price(self) -> str:
        return self.__price
    def get_quantity(self) -> str:
        return self.__quantity
    def get_description(self) -> str:
        return self.__description

    def set_name(self, value) -> None:
        self.__name = value
    def set_price(self, value) -> None:
        self.__price = value
    def set_quantity(self, value) -> None:
        self.__quantity = value
    def set_description(self, value) -> None:
        self.__description = value