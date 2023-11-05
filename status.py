from dataclasses import dataclass
from pokemon import Pokemon
from pokemon import PokemonBoosts as Boost
from random import randint


@dataclass
class Status:
    name: str
    turns: tuple[int, int] | int | bool
    chance: int | bool
    effects: list[str]

    def __init__(self):
        if type(self.turns) == tuple:
            self.turns = randint(*self.turns)
        else:
            self.turns = self.turns
        self.name = self.__class__.__name__
        self.effects = [
            method
            for method in dir(self)
            if callable(getattr(self, method)) and not method.startswith("__")
        ]


class Paralyze(Status):
    turns = True
    chance = 30

    def onApply(self, pokemon: Pokemon):
        pokemon.applyboost(Boost(speed=-1))

    def onRemove(self, pokemon: Pokemon):
        pokemon.applyboost(Boost(speed=1))

    def onTryAttack(self, pokemon: Pokemon) -> bool:
        return randint(0, 100) > self.chance


def test():
    con = Paralyze()


if __name__ == "__main__":
    test()
