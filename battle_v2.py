from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

from constants import Side, Target, Weather
from pokemon import Pokemon
from trainer import Trainer

from random import choices

if TYPE_CHECKING:
    from move import Move


class Action:
    pass


@dataclass
class MoveAction(Action):
    battle: Battle
    move: Move
    pokemon: Pokemon
    priority: int | None = None
    og_targets: list[Pokemon] | None = None
    new_targets: list[Pokemon] | None = None

    def is_target_user(self) -> bool:
        if self.move.target == Target.user:
            self.og_target == self.pokemon
            return True
        else:
            return False

    def execute(self):
        target = self.og_targets[0]
        if target.is_active:
            self.move.execute()


@dataclass
class SwitchAction:
    battle: Battle
    priority: int
    pokemon: Pokemon
    target: Pokemon


@dataclass
class Turn:
    actions: list[Action] = field(default_factory=list)

    def add_action(self, action: Action):
        self.actions.append(action)

    def sort_actions(self):
        self.actions = sorted(self.actions, key=lambda a: a.priority)

    def get_next(self):
        return self.actions.pop()


@dataclass
class Battle:
    trainers: list[Trainer]
    player: Trainer
    allies: list[Trainer]
    enemies: list[Trainer]
    turns: list[Turn]
    weather: Weather | None = None

    def __init__(self, trainers: list[Trainer]):
        self.trainers = trainers
        self.player = [t for t in trainers if t.side == Side.player][0]
        self.allies = [t for t in trainers if t.side == Side.ally]
        self.enemies = [t for t in trainers if t.side == Side.enemy]
        self.turns = []
        for trainer in self.trainers:
            trainer.set_first_alive_as_active()

    @property
    def is_active(self):
        all_have_alive_pokemon = True
        for trainer in self.trainers:
            has_alive_pokemon = False
            for pokemon in trainer.party:
                has_alive_pokemon = has_alive_pokemon or pokemon.hp > 0
                if has_alive_pokemon:
                    break
            all_have_alive_pokemon = all_have_alive_pokemon and has_alive_pokemon
        return all_have_alive_pokemon

    def new_turn(self):
        turn = Turn()
        player_action = self.select_player_action()
        turn.add_action(player_action)
        ai_actions = self.ai_select_action()
        map(turn.add_action, ai_actions)
        turn.sort_actions()

    def select_player_action(self) -> Action:
        while True:
            choice = input("Select [a/s/i]: ")
            match choice:
                case "a":
                    action = self.select_player_move()
                case "s":
                    action = self.select_switch_target()
                case _:
                    continue
            return action

    def select_player_move(self) -> Action:
        pokemon = self.player.active_pokemon
        while True:
            for i, move in enumerate(pokemon.moves):
                print(i, move.name)
            choice = int(input(f"Select move for {pokemon.name}: "))
            action = MoveAction(self, pokemon.moves[choice], pokemon)
            if not action.is_target_user():
                targets = self.select_player_action_targets(action)
                action.og_targets = targets
                return action

    def select_player_action_targets(self, action: MoveAction) -> list[Pokemon]:
        targets = []
        match action.move.target:
            case Target.enemy:
                possible_targets = self.get_all_enemy_pokemon()
                while True:
                    for i, pokemon in enumerate(possible_targets):
                        print(i, pokemon.name)
                    choice = int(input(f"Select targets for {action.move.name}: "))
                    if choice in range(len(possible_targets)):
                        targets.append(possible_targets[choice])
                        break
                    else:
                        continue
            case Target.all_enemies:
                targets = self.get_all_enemy_pokemon()
        return targets

    def ai_select_action(self) -> list[Action]:
        # TODO split this to select_move and select_action
        ai_actions = []
        for trainer in self.enemies:
            move = choices(trainer.active_pokemon.moves)
            targets = [self.player.active_pokemon]
            ai_actions.append(MoveAction(self, move, trainer.active_pokemon, targets))
        return ai_actions

    def get_all_enemy_pokemon(self) -> list[Pokemon]:
        return [e.active_pokemon for e in self.enemies]

    def run(self):
        while self.is_active:
            turn = self.new_turn()
            self.turns.append(turn)
        print("battle end")


def test():
    from pokemons import Pikachu

    red = Trainer("red").set_side(Side.player).set_party([Pikachu(10)])
    green = Trainer("green").set_side(Side.enemy).set_party([Pikachu(10)])

    battle = Battle([red, green])

    battle.run()

    print(battle)


if __name__ == "__main__":
    test()
