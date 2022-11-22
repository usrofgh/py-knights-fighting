from app.data.knight_parameters import KNIGHTS
from app.knight.knights import Knight


def battle(knights: dict) -> dict:
    lancelot = Knight(knights["lancelot"])
    arthur = Knight(knights["arthur"])
    mordred = Knight(knights["mordred"])
    red_knight = Knight(knights["red_knight"])

    lancelot.preparing_for_battle()
    arthur.preparing_for_battle()
    mordred.preparing_for_battle()
    red_knight.preparing_for_battle()

    lancelot.battle(mordred)
    arthur.battle(red_knight)

    return Knight.get_name_hp_all_knights()


print(battle(KNIGHTS))
