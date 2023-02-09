class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self.__name = name
        self.__power = power

    def get_name(self) -> str:
        return self.__name

    def get_power(self) -> int:
        return self.__power
