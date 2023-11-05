from __future__ import annotations
from typing import TYPE_CHECKING

import logging
import warnings
from dataclasses import dataclass

from constants import Side

warnings.simplefilter("ignore")

logging.basicConfig(
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y/%m/%d %I:%M:%S",
    handlers=[logging.FileHandler("debug.log"), logging.StreamHandler()],
    level=0,
)

if TYPE_CHECKING:
    from pokemon import Pokemon


@dataclass
class Trainer:
    name: str
    party: list[Pokemon]
    y: int | None = None
    x: int | None = None
    side: Side = Side.npc
    active_pokemon: Pokemon | None = None

    def __init__(self, name: str):
        logging.info(f"initialized trainer {name}")
        self.name = name
        self.party = []

    def set_position(self, y, x) -> Trainer:
        self.y = y
        self.x = x
        return self

    def set_side(self, side: Side) -> Trainer:
        self.side = side
        return self

    def set_party(self, party: list[Pokemon]) -> Trainer:
        self.party = party
        return self

    def add_to_party(self, pokemon: Pokemon):
        pokemon.trainer = self
        self.party.append(pokemon)

    def set_first_alive_as_active(self):
        if self.party:
            for pokemon in self.party:
                if pokemon.hp > 0:
                    self.active_pokemon = pokemon
