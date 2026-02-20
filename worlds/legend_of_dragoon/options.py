from dataclasses import dataclass
from Options import PerGameCommonOptions, Choice, OptionGroup, Toggle


class AdditionRandomization(Choice):
    """
    Controls how character Additions are unlocked.

    Progressive (Character):
        Progressive addition items are added to the item pool
        and unlock additions for their respective character.

    Addition Sanity:
        Each addition unlock is its own item in the item pool
        and can be placed in any world.
    """
    display_name = "Addition Randomization"

    # these will be added later.
    # option_off = 0
    # option_shuffled_character = 1
    # option_shuffled_party = 2
    option_progressive_character = 3
    option_addition_sanity = 4

    default = 4

class Shopsanity(Toggle):
    """
    Toggles all shop items to be locations. This disables vanilla behavior.
    """
    display_name = "Shopsanity"
    default = True

class RandomStartingAddition(Toggle):
    """Start each character with a random addition unlocked."""
    display_name = "Random Starting Addition"
    rich_text_doc = True


class CompletionCondition(Choice):
    """
    Set the goal for completing the game.
    """
    display_name = "Completion Condition"
    # option_stardust_count_25 = 0
    # option_stardust_count_50 = 1 # collect all stardust in the game
    option_fruegel2 =  2# goal after fruegel 2
    option_doel = 3 # goal after defeating dragoon doel
    option_lenus2 = 4# goal after defeating lenus w/ regole
    option_faust =  5 # goal after defeating Magician Faust
    option_melbu =  6 # goal after defeating Melbu Frahma
    default = 3


@dataclass
class LegendOfDragoonOptions(PerGameCommonOptions):
    enable_addition_randomizer: AdditionRandomization
    random_starting_addition: RandomStartingAddition
    lod_completion_condition: CompletionCondition
    enable_shopsanity: Shopsanity

option_groups = [
    OptionGroup("General", [
        AdditionRandomization,
        RandomStartingAddition,
        CompletionCondition,
        Shopsanity
    ], False)
]

option_presets = {

}