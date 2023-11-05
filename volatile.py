from __future__ import annotations

from dataclasses import dataclass
from random import randint

from battle_v2 import Battle
from pokemon import Pokemon


@dataclass
class Volatile:
    name: str
    turns: tuple[int, int] | int
    effects: list[str]

    def __init__(self):
        if type(self.turns) != int:
            self.turns = randint(*self.turns)
        else:
            self.turns = self.turns
        self.name = self.__class__.__name__
        self.effects = [
            method
            for method in dir(self)
            if callable(getattr(self, method)) and not method.startswith("__")
        ]

    def has_method(self, method):
        return method in self.effects


class Confusion(Volatile):
    turns = (1, 4)

    def on_try_attack(self, pokemon: Pokemon):
        pass


class Flinch(Volatile):
    turns = 1

    def on_try_attack(self, pokemon: Pokemon):
        pass


def test():
    con = Confusion()
    if con.has_method("on_try_attack"):
        con.on_try_attack("pokemon")
    print(con)


if __name__ == "__main__":
    test()
