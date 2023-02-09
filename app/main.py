from app.data.source_data import KNIGHTS

from app.knight import Knight
from app.ammunition.armour import Armour
from app.ammunition.potion import Potion
from app.ammunition.weapon import Weapon


def create_knights(knights: dict) -> {Knight}:
    knights_dict = {}

    for params in knights.values():
        name = params["name"]
        power = params["power"]
        hp = params["hp"]

        armour = [Armour(arm["part"], arm["protection"])
                  for arm in params["armour"]]

        weapon = Weapon(params["weapon"]["name"],
                        params["weapon"]["power"])
        try:
            potion = Potion(params["potion"]["name"],
                            params["potion"]["effect"])
        except TypeError:
            potion = None

        knights_dict[name] = Knight(name, power, hp, armour, weapon, potion)

    return knights_dict


def battle(knights_config: dict) -> {}:
    knights = create_knights(knights_config)
    [knight.prepare_for_battle() for knight in knights.values()]
    lancelot = knights["Lancelot"]
    mordred = knights["Mordred"]
    arthur = knights["Artur"]
    red_knight = knights["Red Knight"]

    lancelot.hit(mordred)
    mordred.hit(lancelot)

    arthur.hit(red_knight)
    red_knight.hit(arthur)

    return Knight.get_hp_all_knights()


if __name__ == "__main__":
    battle(KNIGHTS)
