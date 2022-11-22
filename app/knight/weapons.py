class Weapon:
    def __init__(self, name: str, power: int) -> None:
        self._name = name
        self._power = power

    def get_name(self) -> str:
        return self._name

    def get_power(self) -> int:
        return self._power
