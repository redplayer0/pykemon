from __future__ import annotations
from dataclasses import dataclass
from trainer import Trainer
from pokemon import Pokemon


@dataclass
class Tile:
    spr: str = "."
    is_obstacle: bool = False
    text: str | None = None
    is_warp: bool = False
    target_map: Route | None = None
    x: int | None = None
    y: int | None = None


class Wall(Tile):
    spr = "#"
    is_obstacle = True


class Grass(Tile):
    spr = "."
    is_obstacle = False


class Water(Tile):
    spr = "~"
    is_obstacle = False


class Sign(Tile):
    spr = "$"
    is_obstacle = True

    def read_sign(self):
        return self.text


@dataclass
class Route:
    name: str
    tiles: dict[tuple[int, int], Tile]
    player: Trainer | None = None
    trainers: list[Trainer] | None = None
    items: list[Item] | None = None
    grass_rates: dict[int, Pokemon] | None = None
    water_rates: dict[int, Pokemon] | None = None

    def __init__(self):
        mapfile = "maps/" + self.name + ".txt"
        self.tiles = {}
        with open(mapfile, "r") as f:
            for x, line in enumerate(f.readlines()):
                for y, tile in enumerate(line.split()):
                    self.tiles[y, x] = tile

    def move_player(self, direction):
        # something with trainer x, y
        pass

    def move_trainers(self):
        for trainer in self.trainers:
            # something with trainer x, y
            pass

    def try_encounter(self):
        pass

    def check_trainer_battle(self):
        pass

    def try_warp(self):
        pass

    def try_read_sign(self):
        pass
