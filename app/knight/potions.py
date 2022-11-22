class Potion:
    def __init__(self, name: str, effect: dict) -> None:
        self._name = name
        self._effect = effect

    def get_name(self) -> str:
        return self._name

    def get_effect(self) -> dict:
        return self._effect
