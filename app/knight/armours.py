class Armour:
    def __init__(self, name: str, protection: int) -> None:
        self._name = name
        self._protection = protection

    def get_name(self) -> str:
        return self._name

    def get_protection(self) -> int:
        return self._protection
