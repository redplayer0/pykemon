from __future__ import annotations

from dataclasses import dataclass
from random import randint
from typing import TYPE_CHECKING

from constants import GrowthRate, Stone, Type

if TYPE_CHECKING:
    from move import Move


@dataclass
class PokemonBases:
    hp: int
    attack: int
    defence: int
    speed: int
    sp_attack: int
    sp_defence: int


@dataclass
class PokemonIVs:
    hp: int
    attack: int
    defence: int
    speed: int
    sp_attack: int
    sp_defence: int

    def __init__(self):
        self.hp = randint(0, 31)
        self.attack = randint(0, 31)
        self.defence = randint(0, 31)
        self.speed = randint(0, 31)
        self.sp_attack = randint(0, 31)
        self.sp_defence = randint(0, 31)


@dataclass
class PokemonBoosts:
    hp: int = 0
    attack: int = 0
    defence: int = 0
    speed: int = 0
    sp_attack: int = 0
    sp_defence: int = 0


@dataclass
class PokemonStats:
    hp: int = 0
    attack: int = 0
    defence: int = 0
    speed: int = 0
    sp_attack: int = 0
    sp_defence: int = 0


@dataclass
class Pokemon:
    name: str
    bases: PokemonBases
    ivs: PokemonIVs
    boosts: PokemonBoosts
    stats: PokemonStats
    hp: int
    level: int
    catch_rate: int
    base_exp: int
    growth_rate: GrowthRate
    types: list[Type]
    lv_moves: dict[int, Move | list[Move]]
    learnset: list[Move]
    moves: list[Move]
    evolutions: dict[int | str, Pokemon] | dict[Stone, Pokemon] | None = None
    is_egg: bool = False
    step_cycles: None | int = None
    exp: int = 0
    gender_ratio: int = 0
    gender: str = "genderless"
    is_active: bool = False

    def __init__(self, level: int, *moves):
        # set pokemon name
        self.name = self.__class__.__name__
        # set level
        self.level = level
        # generate ivs
        self.ivs = PokemonIVs()
        # generate stats
        self.generate_stats()
        # set hp
        self.hp = self.stats.hp
        # add boosts
        self.boosts = PokemonBoosts()
        # set gender
        if self.gender_ratio > 0:
            if randint(1, 100) > self.gender_ratio:
                self.gender = "female"
            else:
                self.gender = "male"
        # set moves
        self.moves = []
        self.set_moves(*moves)

    def generate_stats(self):
        self.stats = PokemonStats(
            hp=(
                ((self.bases.hp * 2 + self.ivs.hp) * self.level) / 100 + self.level + 10
            ),
            attack=(self.bases.attack * 2 + self.ivs.attack) * self.level / 100 + 5,
            defence=(self.bases.defence * 2 + self.ivs.defence) * self.level / 100 + 5,
            speed=(self.bases.speed * 2 + self.ivs.speed) * self.level / 100 + 5,
            sp_attack=(self.bases.sp_attack * 2 + self.ivs.sp_attack) * self.level / 100
            + 5,
            sp_defence=(self.bases.sp_defence * 2 + self.ivs.sp_defence)
            * self.level
            / 100
            + 5,
        )

    def set_moves(self, *moves):
        if moves:
            for move in moves:
                self.moves.append(move())
        else:
            for lv in range(1, self.level + 1):
                if lv in self.lv_moves:
                    if type(self.lv_moves[lv]) == list:
                        for m in self.lv_moves[lv]:
                            self.moves.append(m())
                    else:
                        self.moves.append(self.lv_moves[lv]())
            if len(self.moves) > 4:
                self.moves = self.moves[-4::]

    def applyboost(self, boost: PokemonBoosts) -> Pokemon:
        # do stuff with boosts
        return self

    def deal_damage(self, damage: int):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
