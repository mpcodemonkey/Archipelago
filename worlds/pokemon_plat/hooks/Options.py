# Object classes from AP that represent different types of options that you can create
from Options import FreeText, NumericOption, Toggle, DefaultOnToggle, Choice, TextChoice, Range, NamedRange

# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value



####################################################################
# NOTE: At the time that options are created, Manual has no concept of the multiworld or its own world.
#       Options are defined before the world is even created.
#
# Example of creating your own option:
#
#   class MakeThePlayerOP(Toggle):
#       """Should the player be overpowered? Probably not, but you can choose for this to do... something!"""
#       display_name = "Make me OP"
#
#   options["make_op"] = MakeThePlayerOP
#
#
# Then, to see if the option is set, you can call is_option_enabled or get_option_value.
#####################################################################


# To add an option, use the before_options_defined hook below and something like this:
#   options["total_characters_to_win_with"] = TotalCharactersToWinWith
#
    
class HiddenItems(DefaultOnToggle):
    """Shuffles hidden items into the pool
    """
    display_name = "Hidden Items"
    
class DowsingMachine(Toggle):
    """Hidden items require the Dowsing Machine in logic.
    Note that this does NOT impact the Hidden Items on Route 217.
    """
    display_name = "Dowsing Machine Logic"
    
class DowsingMachine217(DefaultOnToggle):
    """Hidden items on Route 217 require the Dowsing Machine in logic.
    This is separate from all other hidden items. Given the size of the route and its poor visibility,
    it is suggested you leave this on, even if other Hidden Items will not require Dowsing Machine.
    """
    display_name = "Dowsing Machine Route 217 Logic"
    
class DefogTraversal(DefaultOnToggle):
    """Should entering a foggy area logically require Defog?
    """
    display_name = "Defog Traversal"
    
class DefogPickup(DefaultOnToggle):
    """Do items in foggy areas logically require Defog to pick up?
    If Defog Traversal is on, this option does nothing.
    """
    display_name = "Defog Pickup"
    
class NorthSinnohFly(Toggle):
    """The game logically expects you to have access to Fly
    before entering Northern Sinnoh.
    Northern Sinnoh starts at Mt. Coronet B1F.
    
    If Early Fly is on, this option will have no impact.
    """
    display_name = "Northern Sinnoh Fly"
    
class StorageKey(Toggle):
    """Adds the Storage Key from Diamond & Pearl into the multiworld.
    This allows access to the Galactic Warehouse without the need to clear the three lakes.
    
    Note that clearing the lakes still opens the Warehouse, and logic accounts for both of these.
    """
    display_name = "Storage Key"
    
class VeilstoneFlash(Toggle):
    """Buying Flash from Veilstone Dept. Store will be considered in logic with this option.
    """
    display_name = "Veilstone Flash"
    
class BattleZone(DefaultOnToggle):
    """Adds the Battle Zone (the Fight Area, Survival Area, Resort Area, Stark Mountain, and all Routes in between) to the list of locations.
    Namely, this includes all checks that require defeating Flint and Volkner at the Fight Area to access.
    """
    display_name = "Battle Zone"
    
class EarlyFly(Toggle):
    """Guarantees that Fly and the Cobble Badge will be acquired within an early sphere.
    Twinleaf, Sandgem, Pal Park, Jubilife, Oreburgh, and Floaroma will be the only regions logic will expect you to travel without
    the ability to Fly.
    
    In a multiworld, 'HM02 Fly' and 'Cobble Badge' can be added to the local_items option for added insurance.
    """
    display_name = "Early Fly"
    
class OpenSunyshore(Toggle):
    """Removes the roadblock at Hotel Grand Lake preventing access to Route 222.
    This removes the requirement of defeating Cyrus in the Distortion World to access this area.
    """
    display_name = "Open Sunyshore"
    
class ExtraRoadblocks(Toggle):
    """Adds roadblocks to Routes 214 (directly south of Veilstone) and 212 (directly south of Hearthome).
    These routes cannot be traversed without Surf, which prevents access to Pastoria and the surrounding area.
    
    This aims to take away some of the Bike's power as an access tool.
    """
    display_name = "Extra Roadblocks"


# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict) -> dict:
    return options

# This is called after any manual options are defined, in case you want to see what options are defined or want to modify the defined options
def after_options_defined(options: dict) -> dict:
    options.update({
        'randomize_hidden_items': HiddenItems,
        'require_dowsing_machine': DowsingMachine,
        'require_dowsing_machine_on_route_217': DowsingMachine217,
        'defog_traversal': DefogTraversal,
        'defog_pickup': DefogPickup,
        'early_fly': EarlyFly,
        'northern_sinnoh_fly': NorthSinnohFly,
        'storage_key': StorageKey,
        'veilstone_flash': VeilstoneFlash,
        'battle_zone': BattleZone,
        'open_sunyshore': OpenSunyshore,
        'extra_roadblocks': ExtraRoadblocks
    })
    return options