from __future__ import annotations

import logging
import warnings
from dataclasses import dataclass
from pokemon import PokemonBoosts as Boost
from volatile import Volatile
from status import Status

from random import randint
from constants import Category, Priority, Target, Type, Flag

warnings.simplefilter("ignore")

logging.basicConfig(
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y/%m/%d %I:%M:%S",
    handlers=[logging.FileHandler("debug.log"), logging.StreamHandler()],
    level=0,
)


@dataclass
class Secondary:
    chance: int
    effect: Boost | Volatile | Status


@dataclass
class Move:
    name: str
    basepower: int
    acurracy: int
    pp: int
    type: Type
    category: Category
    priority: Priority
    target: Target = Target.enemy
    flags: list[Flag] | None = None
    secondaries: list[Secondary] | None = None

    def __init__(self):
        self.pp = self.pp
        self.name = self.__class__.__name__

    def activate_secodaries(self) -> list[Status | Volatile]:
        effects = []
        if self.secondaries:
            for sec in self.secondaries:
                if randint(0, 100) > sec.chance:
                    effects.append(sec.effect)
        return effects
