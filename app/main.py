from app.data.source_data import KNIGHTS

from app.knight import Knight
from app.ammunition.armour import Armour
from app.ammunition.weapon import Weapon
from app.ammunition.potion import Potion


def battle(knights: {Knight}) -> {}:
    [knight.prepare_for_battle() for knight in knights.values()]

    lancelot = knights["Lancelot"]
    mordred = knights["Mordred"]
    arthur = knights["Artur"]
    red_knight = knights["Red Knight"]

    lancelot.hit(mordred)
    mordred.hit(lancelot)

    arthur.hit(red_knight)
    red_knight.hit(arthur)

    return {
        lancelot.get_name(): lancelot.get_hp(),
        arthur.get_name(): arthur.get_hp(),
        mordred.get_name(): mordred.get_hp(),
        red_knight.get_name(): red_knight.get_hp(),
    }


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


def main() -> None:
    knights = create_knights(KNIGHTS)
    print(battle(knights))


if __name__ == "__main__":
    main()


# def battle1(knightsConfig):
#     # 1 Lancelot vs Mordred:
#     lancelot["hp"] -= mordred["power"] - lancelot["protection"]
#     mordred["hp"] -= lancelot["power"] - mordred["protection"]
#
#     # check if someone fell in battle
#     if lancelot["hp"] <= 0:
#         lancelot["hp"] = 0
#
#     if mordred["hp"] <= 0:
#         mordred["hp"] = 0
#
#     # 2 Arthur vs Red Knight:
#     arthur["hp"] -= red_knight["power"] - arthur["protection"]
#     red_knight["hp"] -= arthur["power"] - red_knight["protection"]
#
#     # check if someone fell in battle
#     if arthur["hp"] <= 0:
#         arthur["hp"] = 0
#
#     if red_knight["hp"] <= 0:
#         red_knight["hp"] = 0
#
#     # Return battle results:
#     return {
#         lancelot["name"]: lancelot["hp"],
#         arthur["name"]: arthur["hp"],
#         mordred["name"]: mordred["hp"],
#         red_knight["name"]: red_knight["hp"],
#     }


# print(battle(KNIGHTS))
