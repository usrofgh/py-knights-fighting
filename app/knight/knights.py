from __future__ import annotations

from app.knight.armours import Armour
from app.knight.potions import Potion
from app.knight.weapons import Weapon


class Knight:
    _knights_list = []

    def __init__(self, knight: dict) -> None:
        self._name = knight["name"]
        self._power = knight["power"]
        self._hp = knight["hp"]
        self._armour = knight["armour"]
        self._weapon = knight["weapon"]
        self._potion = knight["potion"]
        self._protection = 0
        Knight._knights_list.append(self)

    @staticmethod
    def get_name_hp_all_knights() -> dict:
        res = {}
        for knight_i in Knight._knights_list:
            res.update(res | {knight_i.get_name(): knight_i.get_hp()})
        return res

    def get_name(self) -> str:
        return self._name

    def get_power(self) -> int:
        return self._power

    def get_hp(self) -> int:
        return self._hp

    def get_armour(self) -> dict[Armour]:
        return self._armour

    def get_weapon(self) -> Weapon:
        return self._weapon

    def get_potion(self) -> Potion:
        return self._potion

    def get_protection(self) -> int:
        return self._protection


    def set_power(self, power: int) -> None:
        self._power = power

    def set_hp(self, hp: int) -> None:
        self._hp = hp

    def set_protection(self, protection: int) -> None:
        self._protection = protection

    def set_armour(self, armours: dict) -> None:
        self._armour = [Armour(armour_i["part"],
                               armour_i["protection"]) for armour_i in armours]

    def set_potion(self, potions: dict) -> None:
        if potions is not None:
            self._potion = Potion(potions["name"], potions["effect"])
        else:
            self._potion = []

    def set_weapon(self, weapons: dict) -> None:
        self._weapon = Weapon(weapons["name"], weapons["power"])

    def preparing_for_battle(self) -> None:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()

    def apply_armour(self) -> None:
        self.set_armour(self.get_armour())
        for armour in self.get_armour():
            self.set_protection(self.get_protection() + armour.get_protection())

    def apply_weapon(self) -> None:
        self.set_weapon(self.get_weapon())
        self.set_power(self.get_power() + self.get_weapon().get_power())

    def apply_potion(self) -> None:
        self.set_potion(self.get_potion())
        if self.get_potion():
            potion_effects = self.get_potion().get_effect()
            if "power" in potion_effects:
                self.set_power(self.get_power() + potion_effects["power"])

            if "protection" in potion_effects:
                self.set_protection(self.get_protection() + potion_effects["protection"])

            if "hp" in potion_effects:
                self.set_hp(self.get_hp() + potion_effects["hp"])

    def battle(self, opponent: Knight) -> None:
        self.hit(opponent)
        opponent.hit(self)

        self.is_dead()
        opponent.is_dead()

    def hit(self, opponent: Knight) -> None:
        remnants_power = self.get_power() - opponent.get_protection()
        if remnants_power >= 0:
            opponent.set_protection(0)
            opponent.set_hp(opponent.get_hp() - remnants_power)

    def is_dead(self) -> None:
        if self.get_hp() <= 0:
            self.set_hp(0)
