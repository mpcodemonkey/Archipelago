from dataclasses import dataclass

from Options import Choice, Range, Option, Toggle, DeathLink, DefaultOnToggle, OptionSet, PerGameCommonOptions, StartInventoryPool

class PacksOrSets(Choice):
    """
    Packs contain cards that are randomized upon receipt at the lua script level
    Sets are static card sets (i.e. You received Card Set Lady Luck 4-6)
    """
    display_name = "Packs or Sets"
    option_sets   = 1
    option_packs  = 2
    default       = 1

class StartingPacks(Range):
    """
    If Packs are enabled, sets how many you start with
    """
    display_name = "Starting Packs"
    default = 4
    range_start = 0
    range_end = 10

class Zeroes(DefaultOnToggle):
    """
    Toggle whether 0 value card's should be included in the item pool.  Innefective if you are using card packs
    """
    display_name = "Zeroes"

class Cure(DefaultOnToggle):
    """
    Toggle whether Cure cards should be included in the item pool.  Innefective if you are using card packs
    """
    display_name = "Cure"

class EarlyCure(DefaultOnToggle):
    """
    Toggles whether one of the starting locations should contain Cure 4-6?
    """
    display_name = "Early Cure"

class EnemyCards(DefaultOnToggle):
    """
    Toggles whether enemy cards should be shuffled into the item pool.
    """
    display_name = "Enemy Cards"

class StartingWorlds(Range):
    """
    Number of random world cards to start with in addition to Traverse Town, which is always available.
    """
    display_name = "Starting Worlds"
    default = 3
    range_start = 0
    range_end = 11


@dataclass
class KHCOMOptions(PerGameCommonOptions):
    packs_or_sets: PacksOrSets
    starting_packs: StartingPacks
    zeroes: Zeroes
    cure: Cure
    early_cure: EarlyCure
    enemy_cards: EnemyCards
    starting_worlds: StartingWorlds
    start_inventory_from_pool: StartInventoryPool
