class Armour:
    def __init__(self, part: str, protection: int) -> None:
        self.__part = part
        self.__protection = protection

    def get_name(self) -> str:
        return self.__part

    def get_protection(self) -> int:
        return self.__protection
