from __future__ import annotations
from typing import TYPE_CHECKING

from constants import Category, Priority, Target, Type
from move import Move, Secondary
from pokemon import PokemonBoosts as Boost
from status import Paralyze

if TYPE_CHECKING:
    from pokemon import Pokemon
    from battle_v2 import Battle


class Tackle(Move):
    basepower = 40
    acurracy = 100
    pp = 40
    type = Type.normal
    category = Category.physical
    flags = []
    priority = Priority.medium
    target = Target.enemy


class Thundershock(Move):
    basepower = 40
    acurracy = 100
    pp = 40
    type = Type.electric
    category = Category.special
    priority = Priority.medium
    target = Target.enemy
    secondaries = [Secondary(100, Paralyze)]

    def execute(self, battle: Battle, pokemon: Pokemon, target: Pokemon):
        damage = self.basepower + pokemon.level - target.level
        effects = self.activate_secodaries()
        if effects:
            for effect in effects:
                target.inflict(effect())
        target.deal_damage(damage)


class Thunderbolt(Move):
    basepower = 80
    acurracy = 100
    pp = 20
    type = Type.electric
    category = Category.special
    priority = Priority.medium
    target = Target.enemy
    secondaries = [Secondary(100, Paralyze())]


class SolarBeam(Move):
    basepower = 120
    acurracy = 100
    pp = 20
    type = Type.grass
    category = Category.special
    priority = Priority.medium
    target = Target.enemy

    def do(self, user: Pokemon, target: None | Pokemon):
        if not user.is_charging:
            user.is_charging == self
        else:
            damage = self.power * user.level
            target.deal_damage(self, damage)
            self.decrease_pp()


def test():
    mov = Thundershock()
    print(mov)


if __name__ == "__main__":
    test()
