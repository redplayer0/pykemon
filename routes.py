from route import Route, Grass, Wall, Sign
from prototypes import Trainer
from pokemon import Pikachu


class Pallet(Route):
    name = "pallet"
    trainers = [
        Trainer("Green").set_position(0, 2).set_enemy().set_party([Pikachu(10)]),
        Trainer("Green").set_position(0, 2).set_enemy().set_party([Pikachu(10)]),
    ]


def test():
    m = Pallet()
    print(m)


if __name__ == "__main__":
    test()
