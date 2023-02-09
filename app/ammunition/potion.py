class Potion:
    def __init__(self, name: str, effect: dict) -> None:
        self.__name = name
        self.__effect = effect

    def get_name(self) -> str:
        return self.__name

    def get_effect(self) -> dict:
        return self.__effect
