from __future__ import annotations

from moves import Thunderbolt, Thundershock, Tackle
from pokemon import Pokemon, PokemonBases
from constants import Type, GrowthRate, Stone


class Raichu(Pokemon):
    # base stats
    bases = PokemonBases(
        hp=35,
        attack=55,
        defence=30,
        speed=90,
        sp_attack=50,
        sp_defence=40,
    )
    catch_rate = 190
    base_exp = 82
    growth_rate = GrowthRate.medium_fast
    types = [Type.electric]
    # moves
    lv_moves = {1: [Tackle, Thundershock]}
    learnset = [Tackle, Thunderbolt, Thundershock]
    # physical traits
    gender_ratio = 50


class Pikachu(Pokemon):
    # base stats
    bases = PokemonBases(
        hp=35,
        attack=55,
        defence=30,
        speed=90,
        sp_attack=50,
        sp_defence=40,
    )
    catch_rate = 190
    base_exp = 82
    growth_rate = GrowthRate.medium_fast
    types = [Type.electric]
    # moves
    lv_moves = {1: [Tackle, Thundershock]}
    learnset = [Tackle, Thunderbolt, Thundershock]
    # evolutions
    evolutions = {Stone.thunder_stone: Raichu}
    # physical traits
    gender_ratio = 50


def test():
    pika = Pikachu(level=10)
    print(pika)


if __name__ == "__main__":
    test()
