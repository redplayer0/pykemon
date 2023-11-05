from enum import Enum, auto


class Weather(Enum):
    sunny = 0
    rain = 1
    sandstorm = 2
    hail = 3


class Side(Enum):
    player = 0
    ally = 1
    enemy = 2
    npc = 3


class TrainerState(Enum):
    just_moved = 0
    standing = 1
    walking = 2


class Flag(Enum):
    allyanim = auto()  # The move plays its animation when used on an ally.
    bypasssub = auto()  # Ignores a target's substitute.
    # Power is multiplied by 1.5 when used by a Pokemon with the Ability Strong Jaw.
    bite = auto()
    bullet = auto()  # Has no effect on Pokemon with the Ability Bulletproof.
    charge = auto()  # The user is unable to make a move between turns.
    contact = auto()  # Makes contact.
    # When used by a Pokemon, other Pokemon with the Ability Dancer can attempt to execute the same move.
    dance = auto()
    # Thaws the user if executed successfully while the user is frozen.
    defrost = auto()
    # Can target a Pokemon positioned anywhere in a Triple Battle.
    distance = auto()
    failcopycat = auto()  # Cannot be selected by Copycat.
    failencore = auto()  # Encore fails if target used this move.
    failinstruct = auto()  # Cannot be repeated by Instruct.
    failmefirst = auto()  # Cannot be selected by Me First.
    failmimic = auto()  # Cannot be copied by Mimic.
    futuremove = auto()  # Targets a slot, and in 2 turns damages that slot.
    # Prevented from being executed or selected during Gravity's effect.
    gravity = auto()
    # Prevented from being executed or selected during Heal Block's effect.
    heal = auto()
    mirror = auto()  # Can be copied by Mirror Move.
    # Additional PP is deducted due to Pressure when it ordinarily would not .
    mustpressure = auto()
    noassist = auto()  # Cannot be selected by Assist.
    # Prevented from being executed or selected in a Sky Battle.
    nonsky = auto()
    noparentalbond = auto()  # Cannot be made to hit twice via Parental Bond.
    nosleeptalk = auto()  # Cannot be selected by Sleep Talk.
    # Gems will not activate. Cannot be redirected by Storm Drain / Lightning Rod.
    pledgecombo = auto()
    # Has no effect on Pokemon which are Grass-type, have the Ability Overcoat, or hold Safety Goggles.
    powder = auto()
    # Blocked by Detect, Protect, Spiky Shield, and if not a Status move, King's Shield.
    protect = auto()
    # Power is multiplied by 1.5 when used by a Pokemon with the Ability Mega Launcher.
    pulse = auto()
    # Power is multiplied by 1.2 when used by a Pokemon with the Ability Iron Fist.
    punch = auto()
    # If this move is successful, the user must recharge on the following turn and cannot make a move.
    recharge = auto()
    # Bounced back to the original user by Magic Coat or the Ability Magic Bounce.
    reflectable = auto()
    # Power is multiplied by 1.5 when used by a Pokemon with the Ability Sharpness.
    slicing = auto()
    # Can be stolen from the original user and instead used by another Pokemon using Snatch.
    snatch = auto()
    sound = auto()  # Has no effect on Pokemon with the Ability Soundproof.
    wind = auto()  # Activates the Wind Power and Wind Rider Abilities.


class Target(Enum):
    user = 0
    enemy = 1
    ally = 2
    all_allies = 3
    all_enemies = 4
    all = 5


class Stone(Enum):
    moon_stone = 0
    fire_stone = 1
    water_stone = 2
    leaf_stone = 3
    thunder_stone = 4
    ice_stone = 5
    sun_stone = 6


class Category(Enum):
    status = 0
    physical = 1
    special = 2


class GrowthRate(Enum):
    slightly_slow = 1
    medium_slow = 2
    slow = 3
    slightly_fast = 4
    medium_fast = 5
    fast = 6


class Priority(Enum):
    last = 0
    very_slow = 1
    slow = 2
    medium = 3
    fast = 4
    very_fast = 5
    first = 6


class Type(Enum):
    unknown = 0
    normal = 1
    fire = 2
    water = 3
    grass = 4
    electric = 5
    ice = 6
    fighting = 7
    poison = 8
    ground = 9
    flying = 10
    psychic = 11
    bug = 12
    rock = 13
    ghost = 14
    dark = 15
    dragon = 16
    steel = 17
    fairy = 18
