from __future__ import annotations


class Knight:

    def __init__(self, knight: dict) -> None:
        self.name = knight["name"]
        self.power = knight["power"]
        self.hp = knight["hp"]
        self.armour = knight["armour"]
        self.weapon = knight["weapon"]
        self.potion = knight["potion"]
        self.protection = 0

    def preparing_for_battle(self) -> None:
        self.apply_armour()
        self.apply_weapon()
        self.apply_potion()

    def apply_armour(self) -> None:
        for armour in self.armour:
            self.protection += armour["protection"]

    def apply_weapon(self) -> None:
        self.power += self.weapon["power"]

    def apply_potion(self) -> None:
        if self.potion is not None:
            potion_effects = self.potion["effect"]

            if "power" in potion_effects:
                self.power += potion_effects["power"]

            if "protection" in potion_effects:
                self.protection += potion_effects["protection"]

            if "hp" in potion_effects:
                self.hp += potion_effects["hp"]

    def battle(self, opponent: Knight) -> None:
        self.hit(opponent)
        opponent.hit(self)

        self.is_dead()
        opponent.is_dead()

    def hit(self, opponent: Knight) -> None:
        remnants_power = self.power - opponent.protection
        if remnants_power >= 0:
            opponent.protection = 0
            opponent.hp -= remnants_power

    def is_dead(self) -> None:
        if self.hp <= 0:
            self.hp = 0
