from __future__ import annotations

from app.ammunition.armour import Armour
from app.ammunition.potion import Potion
from app.ammunition.weapon import Weapon


class Knight:
    __all_knights = []

    def __init__(
            self,
            name: str,
            power: int,
            hp: int,
            armour: [Armour],
            weapon: Weapon,
            potion: Potion,
    ) -> None:

        self.__name = name
        self.__hp = hp
        self.__power = power
        self.__protection = 0
        self.__weapon = weapon
        self.__armour = armour
        self.__potion = potion

        Knight.__all_knights.append(self)

    def get_name(self) -> str:
        return self.__name

    def get_power(self) -> int:
        return self.__power

    def get_hp(self) -> int:
        return self.__hp

    def get_protection(self) -> int:
        return self.__protection

    def get_armour(self) -> [Armour]:
        return self.__armour

    def get_weapon(self) -> Weapon:
        return self.__weapon

    def get_potion(self) -> [Potion]:
        return self.__potion

    def __apply_armour(self) -> None:
        self.__protection += sum([armour.get_protection()
                                  for armour in self.__armour])

    def __apply_potion(self) -> None:
        effects = self.__potion.get_effect()
        # print(effects)
        if "power" in effects:
            self.__power += effects["power"]
        if "hp" in effects:
            self.__hp += effects["hp"]
        if "protection" in effects:
            self.__protection += effects["protection"]

    def __appy_weapon(self) -> None:
        self.__power += self.__weapon.get_power()

    def prepare_for_battle(self) -> None:
        self.__apply_armour()
        self.__appy_weapon()
        try:
            self.__apply_potion()
        except AttributeError:
            pass

    def hit(self, other: Knight) -> None:
        if self.__power >= other.__protection + other.__hp:
            other.__protection = 0
            other.__hp = 0

        elif self.__power >= other.__protection:
            other.__hp -= self.__power - other.__protection
            other.__protection = 0

    @classmethod
    def get_hp_all_knights(cls) -> dict[str: int]:
        return {knight.__name: knight.__hp for knight in cls.__all_knights}
