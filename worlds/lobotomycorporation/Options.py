import typing
import random
from dataclasses import dataclass
from Options import Option, DefaultOnToggle, Toggle, Range, OptionSet, DeathLink, PlandoConnections, ItemDict, \
    PerGameCommonOptions, OptionGroup, Choice
from .Items import trap_table




class ItemWeights(ItemDict):
    def __init__(self, value: typing.Dict[str, int]):
        if any(item_count < 0 for item_count in value.values()):
            raise Exception("Cannot have negative item counts.")
        if all(item_count == 0 for item_count in value.values()):
            raise Exception("At least one item count must be positive.")
        super(ItemDict, self).__init__(value)

class AdaptiveLocations(DefaultOnToggle):
    """
    Reduces the number of Abnos availiable to be in line with your goal.
    For example: MALKUTH SUPRESSION = 28 Abnos items total (25 days + 3)
    This massively reduces the amount of locations this game has.
    """
    display_name = "Adaptive Locations"

class BaseEquipmentChecks(Range):
    """
    This sets the amount of Equipment Checks each abnormality has.
    """
    display_name = "Base Equipment Checks"
    default = 4
    range_start = 0
    range_end = 9

class UpgradeEquipmentChecks(Range):
    """
    This sets the amount of Equipment Checks the Gebura supression upgrade adds to each abnormality.
    """
    display_name = "Upgrade Equipment Checks"
    default = 1
    range_start = 0
    range_end = 9

class StartingAbnos(OptionSet):
    """
    Which abnos would you like to start with. Written as ID from the table below:
    ID: 100009 ZAYIN | One Sin and Hundreds of Good Deeds: 
    ID: 100028 ZAYIN | WellCheers: 
    ID: 100024 ZAYIN | Don’t Touch Me: 
    ID: 100034 ZAYIN | You’re Bald…: 
    ID: 100001 TETH | Scorched Girl: 
    ID: 100018 TETH | Forsaken Murderer: 
    ID: 100020 TETH | Small Bird: 
    ID: 100021 TETH | Old Lady: 
    ID: 100036 TETH | Fragment of the Universe: 
    ID: 100012 TETH | Spider Bud: 
    ID: 100013 TETH | Beauty and the Beast: 
    ID: 100022 TETH | Wall Gazer: 
    ID: 100027 TETH | Bloodbath: 
    ID: 100037 TETH | Crumbling Armor: 
    ID: 100002 HE | A Teddy Bear: 
    ID: 100003 HE | The Red Shoes: 
    ID: 100011 HE | Little Helper: 
    ID: 100016 HE | Rudolta of the Sleigh: 
    ID: 100041 HE | A Wee Witch: 
    ID: 100017 HE | Nameless Fetus: 
    ID: 100102 HE | The Snow Queen: 
    ID: 100023 WAW | Snow White's Apple: 
    ID: 100026 WAW | Queen Bee: 
    ID: 100029 WAW | Alriune: 
    ID: 100035 WAW | Long Bird: 
    ID: 100039 WAW | Magical Girl: 
    ID: 100019 ALEPH | The Silent Orchestra: 
    ID: 100005 ALEPH | Nothing There: 
    ID: 100007 TETH | 1.76 MHz: 
    ID: 100043 HE | The Funeral of the Dead Butterflies: 
    ID: 100103 HE | Der Freischütz: 
    ID: 100047 WAW | The Dreaming Current: 
    ID: 100048 WAW | Magical Girl: 
    ID: 100049 HE | Schadenfreude: 
    ID: 100044 WAW | The Burrowing Heaven: 
    ID: 100045 WAW | Dream of a Black Swan: 
    ID: 100042 ALEPH | Mountain of Smiling Bodies: 
    ID: 100046 WAW | The Naked Nest: 
    ID: 100053 ZAYIN | Fairy Festival: 
    ID: 100054 TETH | Meat Lantern: 
    ID: 100051 HE | Warm-hearted Woodsman: 
    ID: 100056 ALEPH | CENSORED: 
    ID: 100050 HE | Scarecrow Searching for Wisdom: 
    ID: 100055 WAW | Dimensional Refraction Variant: 
    ID: 100052 TETH | Today’s Shy Look: 
    ID: 100057 HE | Porccubus: 
    ID: 100058 ALEPH | Blue Star: 
    ID: 100031 HE | Child of the Galaxy: 
    ID: 100033 WAW | Big and Might be Bad Wolf: 
    ID: 100032 WAW | Little Red Riding Hooded Mercenary: 
    ID: 100040 WAW | Giant Mushroom Chunk: 
    ID: 100006 HE | Singing Machine: 
    ID: 100008 WAW | Big Bird: 
    ID: 100004 WAW | Magical Girl: 
    ID: 100059 TETH | Grave of Cherry Blossoms: 
    ID: 100060 TETH | Void Dream: 
    ID: 100061 WAW | The Firebird: 
    ID: 100014 ZAYIN | Plague Doctor: 
    ID: 100104 WAW | Yin: 
    ID: 100064 ZAYIN | Army in Pink: 
    ID: 100106 TETH | Ppodae: 
    ID: 100105 WAW | Honored Monk: 
    ID: 100065 WAW | Il Pianto della Luna: 
    ID: 100063 ALEPH | Melting Love: 
    ID: 100062 WAW | World Tree: 
    """
    display_name = "Starting Abnos"
    valid_keys = [str(id+100000) for id in range(107)]
    default = ['100009','100106']

class GoalType(Choice):
    """
    What goal are you trying to reach in this game:
    Vanilla: Collect 9 Seeds of Light and Beat Day 50
    Dissolution: Reach a certain Dissolutuion percentage
    Day and Dissolution: Reach a certain Dissolutuion percentage and complete a certain day
    Supression: Clear a certain Core Supression / supress WhiteKnight or apocalypse bird
    """
    display_name = "Goal Type"
    option_vanilla = 0
    option_dissolution = 1
    option_day_and_dissolution = 2
    option_suppression = 3
    default = option_vanilla

class DissolutionGoal(Range):
    """
    This sets the amount of Dissolution required to complete your goal.
    !Only Observation Checks on non-tool Abnos are counted towards this!
    The percentage how close you are to your goal will be dsiplayed at the start of every day.
    This option is only applied if Goal Type is 'Dissolution' or 'Day and Dissolution'.
    Min : 0
    Max : 100
    """
    display_name = "Dissolution Goal"
    default = 100
    range_start = 0
    range_end = 250

class DayGoal(Range):
    """
    This sets the amount of days required to beat to complete your goal.
    This option is only applied if Goal Type is 'Day and Dissolution'.
    """
    display_name = "Day Goal"
    default = 25
    range_start = 0
    range_end = 50

class SupressionGoal(Choice):
    """
    This sets the supression required to complete your goal.
    This option is only applied if Goal Type is 'Supression'.
    """
    display_name = "Supression Goal"
    option_malkuth = 0
    option_yesod = 1
    option_hod = 2
    option_netzach = 3
    option_tiphereth = 4
    option_gebura = 5
    option_chesed = 6
    option_binah = 7
    option_hokma = 8
    option_whitenight = 9
    option_apocalypsebird = 10
    
    default = option_gebura 


class TrapPercent(Range):
    """
    Choose the percentage of trap items that will appear when filling the item pool with junk.
    """
    display_name = "Trap Item Percentage"
    range_start = 0
    range_end = 100
    default = 25    
        
class TrapWeights(ItemWeights):
    """Choose the odds of each trap item being created when filling the item pool with traps."""
    display_name = "Trap Item Weights"
    valid_keys = trap_table
    default = {item: 50 for item in trap_table}
    

class WhitenightMode(Choice):
    """
    Determines if and how Whitenight is in your run.
    Disabled: Plague Doctor will not appear in the Item Pool
    Excluded: Whitenight Suppression Locations will not have progression items
    Enabled: Whitennight Suppression Locations might have progression items
    DarkDay: Whitennight Suppression Locations will have progression items
    """
    display_name = "Whitenight Mode"
    option_disabled = 0
    option_excluded = 1
    option_enabled = 2
    option_darkDays = 3
    default = option_excluded

class ApocalypseBirdMode(Choice):
    """
    Determines if and how Apocalypse Bird is in your run.
    Disabled: The three Birds will not appear in the Item Pool
    Excluded: Apocalypse Bird Suppression Locations will not have progression items
    Enabled: Apocalypse Bird Suppression Locations might have progression items
    Apocalypse: Apocalypse Bird Suppression Locations will have progression items
    """
    display_name = "Apocalypse Bird Mode"
    option_disabled = 0
    option_excluded = 1
    option_enabled = 2
    option_apocalypse = 3
    default = option_excluded

class Deathlink(Toggle):
    """
    Determines if Deathlink is enabled or not.
    """
    display_name = "Deathlink"
    

class DeathlinkGrace(Range):
    """
    After a Deathlink is recieved a timer starts, a grace period.
    While this timer is running there are no consequences for triggering a deathlink.
    This is to prevent chain deaths. (A deathlink leading to the lobcorp player sending a deathlink at a later date)
    Determines how long the grace period is in seconds.
    """
    display_name = "Deathlink Grace Period Length"
    range_start = 0
    range_end = 1000
    default = 60  

class DeathlinkTrigger(Choice):
    """ 
    Determines which event counts as a death for Deathlink.
    EmployeeDeath: A Deathlink is sent after X clerks and agents die. Counter resets on day end/reset. (X is determined by the DeathlinkCount option)
    AgentDeath: A Deathlink is sent after X agent. Counter resets on day end/reset. (X is determined by the DeathlinkCount option)
    DepartmentDeath: A Deathlink is sent after a whole department is dead.
    Retry: A Deatlink is sent on Retry of a day.
    """
    display_name = "Deathlink Trigger"
    option_employeeDeath = 0
    option_agentDeath = 1
    option_departmentDeath = 2
    option_retry = 3
    default = option_departmentDeath

class DeathlinkCount(Range):
    """
    Only takes effect if DeathlinkTrigger is 'EmployeeDeath' or 'AgentDeath'
    Choose amount of times an Employee can die before a Deathlink is sent.
    """
    display_name = "Deathlink Count"
    range_start = 1
    range_end = 100
    default = 10   

class DeathlinkEffect(Choice):
    """
    Determines what consequences recieving a deathlink brings:
    Button: DontTouchMe will be pressed.
    Breakout: Sets all abnos Qlipoth-Counters in a department to 0.
    Ordeal: Start the next ordeal after 30 seconds. Should Midnight already be completed, you will have to do it again.
    Graze: Calls the Rabbit team to a random Department.
    Trap: Triggers a random trap.
    Train: Summons the Express Train to Hell.
    Random: Randomly picks one from the above options everytime a deathlink is recieved.
    """
    display_name = "Deathlink Effect"
    option_button = 0
    option_breakout = 1
    option_ordeal = 2
    option_graze = 3
    option_trap = 4
    option_train = 5
    option_randomEffect = 6
    default = option_graze


@dataclass
class LobOptions(PerGameCommonOptions):
    adaptive_locations: AdaptiveLocations

    base_equipment_checks: BaseEquipmentChecks
    upgrade_equipment_checks: UpgradeEquipmentChecks

    starting_abnos: StartingAbnos

    goal_type: GoalType
    dissolution_goal: DissolutionGoal
    day_goal: DayGoal
    suppression_goal: SupressionGoal

    trap_percent: TrapPercent
    trap_weights: TrapWeights

    apoc_mode: ApocalypseBirdMode
    wn_mode: WhitenightMode

    deathlink:Deathlink
    deathlink_count: DeathlinkCount
    deathlink_grace: DeathlinkGrace
    deathlink_effect: DeathlinkEffect
    deathlink_trigger: DeathlinkTrigger