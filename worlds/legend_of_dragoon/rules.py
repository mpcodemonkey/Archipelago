from __future__ import annotations

from typing import TYPE_CHECKING

from worlds.generic.Rules import set_rule
from .regions import visualize_world

if TYPE_CHECKING:
    from .world import LegendOfDragoonWorld

def set_all_rules(world: LegendOfDragoonWorld) -> None:
    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)

    # for debugging purposes:
    visualize_world(world.multiworld)


def set_all_entrance_rules(world: LegendOfDragoonWorld) -> None:
    dart_additions = world.get_entrance("Menu to Dart Additions")
    lavitz_additions = world.get_entrance("Menu to Lavitz Additions")
    rose_additions = world.get_entrance("Menu to Rose Additions")
    haschel_additions = world.get_entrance("Menu to Haschel Additions")
    albert_additions = world.get_entrance("Menu to Albert Additions")
    meru_additions = world.get_entrance("Menu to Meru Additions")
    kongol_additions = world.get_entrance("Menu to Kongol Additions")

    # set_rule(dart_additions, lambda state: state.has("Commander", world.player))
    set_rule(lavitz_additions, lambda state: state.has("Prison Key", world.player))
    set_rule(rose_additions, lambda state: state.has("Kongol 1", world.player))
    set_rule(haschel_additions, lambda state: state.has("Lloyd 1", world.player))
    set_rule(albert_additions, lambda state: state.has("Fruegel 2", world.player))
    set_rule(meru_additions, lambda state: state.has_all(["Mappi Steals Orb","Letter from Lynn"], world.player))
    set_rule(kongol_additions, lambda state: state.has("Gehrich", world.player))

    forest_to_prairie = world.get_entrance("Forest to Prairie")
    set_rule(forest_to_prairie, lambda state: state.has_all(["Prison Key", "Fruegel 1"], world.player))

    hellena_prison_01_to_forest = world.get_entrance("Hellena Prison 01 to Forest")
    set_rule(hellena_prison_01_to_forest, lambda state: state.has_all(["Prison Key", "Fruegel 1"], world.player))

    hellena_prison_01_to_02 = world.get_entrance("Hellena Prison 01 to 02")
    set_rule(hellena_prison_01_to_02, lambda state: state.has("Lloyd 1", world.player))

    prairie_to_limestone_cave = world.get_entrance("Prairie to Limestone Cave")
    set_rule(prairie_to_limestone_cave, lambda state: state.has("Axe from the Shack", world.player))

    limestone_cave_to_bale = world.get_entrance("Limestone Cave to Bale")
    set_rule(limestone_cave_to_bale, lambda state: state.has("Urobolus", world.player))

    bale_to_hoax = world.get_entrance("Bale to Hoax")
    set_rule(bale_to_hoax, lambda state: state.has_all(["Lavitzs Picture", "Fathers Stone"], world.player))

    dragons_nest_to_shrine_of_shirley = world.get_entrance("Dragon's Nest to Shrine of Shirley")
    set_rule(dragons_nest_to_shrine_of_shirley, lambda state: state.has_all(["Life Water", "Water Bottle"], world.player))

    forest_to_kazas = world.get_entrance("Forest to Kazas")
    set_rule(forest_to_kazas, lambda state: state.has("Fruegel 2", world.player))

    black_castle_throne_room_to_fletz = world.get_entrance("Black Castle Throne Room to Fletz")
    set_rule(black_castle_throne_room_to_fletz, lambda state: state.has("Dragoon Doel", world.player))

    barrens_to_valley = world.get_entrance("Barrens to Valley of Corrupted Gravity")
    set_rule(barrens_to_valley, lambda state: state.has("Pass for Valley", world.player))

    valley_to_home_of_giganto = world.get_entrance("Valley of Corrupted Gravity to Home of Giganto")
    set_rule(valley_to_home_of_giganto, lambda state: state.has("Valley Virage", world.player))

    donau_to_queen_fury = world.get_entrance("Donau to Queen Fury")
    set_rule(donau_to_queen_fury, lambda state: state.has("Gehrich", world.player))

    phantom_ship_to_lidiera = world.get_entrance("Phantom Ship to Lidiera")
    set_rule(phantom_ship_to_lidiera, lambda state: state.has("Key to Ship", world.player))

    donau_to_furni = world.get_entrance("Donau to Furni")
    set_rule(donau_to_furni, lambda state: state.has_all(["Boat License", "Lenus 2"], world.player))

    evergreen_forest_to_wingly_forest = world.get_entrance("Evergreen Forest to Wingly Forest")
    set_rule(evergreen_forest_to_wingly_forest, lambda state: state.has("Talk to Ute", world.player))

    wingly_forest_to_deningrad = world.get_entrance("Wingly Forest to Deningrad")
    set_rule(wingly_forest_to_deningrad, lambda state: state.has("Dragon Blocker", world.player))

    evergreen_forest_to_mortal_dragon_mountain = world.get_entrance("Evergreen Forest to Mortal Dragon Mountain")
    set_rule(evergreen_forest_to_mortal_dragon_mountain, lambda state: state.has("Grand Jewel", world.player))

    deningrad_to_kashua_glacier = world.get_entrance("Deningrad to Kashua Glacier")
    set_rule(deningrad_to_kashua_glacier, lambda state: state.has("Divine Dragon", world.player))

    kashua_glacier_to_flanvel_tower = world.get_entrance("Kashua Glacier to Tower of Flanvel")
    set_rule(kashua_glacier_to_flanvel_tower, lambda state: state.has("Windigo", world.player))

    kashua_glacier_to_snowfield = world.get_entrance("Kashua Glacier to Snowfield")
    set_rule(kashua_glacier_to_snowfield, lambda state: state.has("Lloyd 2", world.player))

    snowfield_to_vellweb = world.get_entrance("Snowfield to Vellweb")
    set_rule(snowfield_to_vellweb, lambda state: state.has_all(["Moon Mirror", "Moon Dagger", "Moon Gem"], world.player))

    vellweb_to_death_frontier = world.get_entrance("Vellweb to Death Frontier")
    set_rule(vellweb_to_death_frontier, lambda state: state.has_all(["Moon Mirror", "Moon Dagger", "Moon Gem"], world.player))

    ulara_to_home_of_giganto = world.get_entrance("Ulara to Home of Giganto")
    home_of_giganto_to_ulara = world.get_entrance("Home of Giganto to Ulara")
    set_rule(ulara_to_home_of_giganto, lambda state: state.has("Ulara Teleporter", world.player))
    set_rule(home_of_giganto_to_ulara, lambda state: state.has("Ulara Teleporter", world.player))

    queen_fury_to_rouge = world.get_entrance("Queen Fury to Rouge")
    set_rule(queen_fury_to_rouge, lambda state: state.has("Ulara Teleporter", world.player))

    aglis_to_zenebatos = world.get_entrance("Aglis to Zenebatos")
    set_rule(aglis_to_zenebatos, lambda state: state.has("Kraken", world.player))

    zenebatos_to_mayfil = world.get_entrance("Zenebatos to Mayfil")
    set_rule(zenebatos_to_mayfil, lambda state: state.has_all(["Law Maker", "Law Output"], world.player))

    mayfil_to_divine_tree = world.get_entrance("Mayfil to Divine Tree")
    set_rule(mayfil_to_divine_tree, lambda state: state.has("Zackwell", world.player))

    divine_tree_to_moon_that_never_sets = world.get_entrance("Divine Tree to Moon That Never Sets")
    set_rule(divine_tree_to_moon_that_never_sets, lambda state: state.has("Imago", world.player))

def set_all_location_rules(world: LegendOfDragoonWorld) -> None:
    set_addition_starting_rules(world)
    set_addition_progression_rules(world)

    fruegel_1 = world.get_location("Fruegel 1")
    set_rule(fruegel_1, lambda state: state.has("Prison Key", world.player))

    # life_water = world.get_location("Life Water")
    # set_rule(life_water, lambda state: state.has("Water Bottle", world.player))

    kongol_2 = world.get_location("Kongol 2")
    set_rule(kongol_2, lambda state: state.has("Magic Oil", world.player))

    doel = world.get_location("Dragoon Doel")
    set_rule(doel, lambda state: state.has_all(["Red Stone", "Blue Stone", "Yellow Stone"], world.player))

    ghost_commander = world.get_location("Ghost Commander")
    set_rule(ghost_commander, lambda state: state.has("Key to Ship", world.player))

    kubila = world.get_location("Defeat Kubila")
    selebus = world.get_location("Defeat Selebus")
    vector = world.get_location("Defeat Vector")

    set_rule(kubila, lambda state: state.has_all(["Law Maker", "Law Output"], world.player))
    set_rule(selebus, lambda state: state.has_all(["Law Maker", "Law Output"], world.player))
    set_rule(vector, lambda state: state.has_all(["Law Maker", "Law Output"], world.player))

    # vanishing_stone = world.get_location("Vanishing Stone")
    # set_rule(vanishing_stone, lambda state: state.has("Stardust", world.player, 50))

def set_addition_starting_rules(world: LegendOfDragoonWorld) -> None:
    blazing_dynamo = world.get_location("Dart - Blazing Dynamo Unlock")
    lavitz_blossom_storm = world.get_location("Lavitz - Blossom Storm Unlock")
    demons_dance = world.get_location("Rose - Demon's Dance Unlock")
    omni_sweep = world.get_location("Haschel - Omni-Sweep Unlock")
    albert_blossom_storm = world.get_location("Albert - Blossom Storm Unlock")
    perky_step = world.get_location("Meru - Perky Step Unlock")
    bone_crush = world.get_location("Kongol - Bone Crush Unlock")

    if world.options.enable_addition_randomizer == world.options.enable_addition_randomizer.option_progressive_character:
        set_rule(blazing_dynamo, lambda state: state.has("Dart Progressive Addition", world.player, 6))
        set_rule(lavitz_blossom_storm, lambda state: state.has("Lavitz Progressive Addition", world.player, 4))
        set_rule(demons_dance, lambda state: state.has("Rose Progressive Addition", world.player, 3))
        set_rule(omni_sweep, lambda state: state.has("Haschel Progressive Addition", world.player, 5))
        set_rule(albert_blossom_storm, lambda state: state.has("Albert Progressive Addition", world.player, 4))
        set_rule(perky_step, lambda state: state.has("Meru Progressive Addition", world.player, 4))
        set_rule(bone_crush, lambda state: state.has("Kongol Progressive Addition", world.player, 2))
    else:
        set_rule(
            blazing_dynamo,
            lambda state: (
                state.has_all((
                    "Dart Double Slash",
                    "Dart Volcano",
                    "Dart Burning Rush",
                    "Dart Crush Dance",
                    "Dart Madness Hero",
                    "Dart Moon Strike",
                ), world.player)
            ),
        )

        set_rule(
            lavitz_blossom_storm,
            lambda state: (
                state.has_all((
                    "Lavitz Harpoon",
                    "Lavitz Spinning Cane",
                    "Lavitz Rod Typhoon",
                    "Lavitz Gust Of Wind Dance",
                ), world.player)
            ),
        )

        set_rule(
            demons_dance,
            lambda state: (
                state.has_all((
                    "Rose Whip Smack",
                    "Rose More More",
                    "Rose Hard Blade",
                ), world.player)
            ),
        )

        set_rule(
            omni_sweep,
            lambda state: (
                state.has_all((
                    "Haschel Double Punch",
                    "Haschel Ferry Of Styx",
                    "Haschel Summon 4 Gods",
                    "Haschel Five Ring Shattering",
                    "Haschel Hex Hammer",
                ), world.player)
            ),
        )

        set_rule(
            albert_blossom_storm,
            lambda state: (
                state.has_all((
                    "Albert Harpoon",
                    "Albert Spinning Cane",
                    "Albert Rod Typhoon",
                    "Albert Gust Of Wind Dance",
                ), world.player)
            ),
        )

        set_rule(
            perky_step,
            lambda state: (
                state.has_all((
                    "Meru Double Smack",
                    "Meru Hammer Spin",
                    "Meru Cool Boogie",
                    "Meru Cats Cradle",
                ), world.player)
            ),
        )

        set_rule(
            bone_crush,
            lambda state: (
                state.has_all((
                    "Kongol Pursuit",
                    "Kongol Inferno",
                ), world.player)
            ),
        )

def set_completion_condition(world: LegendOfDragoonWorld) -> None:
    # set completion conditions
    conditions = world.options.lod_completion_condition

    item = ""
    if conditions.option_fruegel2 == world.options.lod_completion_condition:
        item = "Fruegel 2"

    if conditions.option_doel == world.options.lod_completion_condition:
        item = "Dragoon Doel"

    if conditions.option_lenus2 == world.options.lod_completion_condition:
        item = "Lenus 2"

    if conditions.option_faust == world.options.lod_completion_condition:
        item = "Faust"

    if conditions.option_melbu == world.options.lod_completion_condition:
        item = "Melbu Frahma"

    world.multiworld.completion_condition[world.player] = lambda state: state.has(item, world.player)

def set_addition_progression_rules(world: LegendOfDragoonWorld) -> None:
    # dart additions
    dart_burning_rush = world.get_location("Dart - Burning Rush Unlock")
    dart_crush_dance = world.get_location("Dart - Crush Dance Unlock")
    dart_madness_hero = world.get_location("Dart - Madness Hero Unlock")
    dart_moon_strike = world.get_location("Dart - Moon Strike Unlock")

    set_rule(dart_burning_rush, lambda state: state.has("Kongol 1", world.player))
    set_rule(dart_crush_dance, lambda state: state.has("Dragoon Doel", world.player))
    set_rule(dart_madness_hero, lambda state: state.has("Kamuy", world.player))
    set_rule(dart_moon_strike, lambda state: state.has_all(["Moon Mirror", "Moon Dagger", "Moon Gem"], world.player))

    # rose additions
    rose_more_more = world.get_location("Rose - More and More Unlock")
    rose_hard_blade = world.get_location("Rose - Hard Blade Unlock")

    set_rule(rose_more_more, lambda state: state.has("Dragoon Doel", world.player))
    set_rule(rose_hard_blade, lambda state: state.has("Key to Ship", world.player))

    lavitz_spinning_cane = world.get_location("Lavitz - Spinning Cane Unlock")
    lavitz_rod_typhoon = world.get_location("Lavitz - Rod Typhoon Unlock")
    lavitz_gust_of_wind_dance = world.get_location("Lavitz - Gust of Wind Dance Unlock")

    set_rule(lavitz_spinning_cane, lambda state: state.has("Axe from the Shack", world.player))
    set_rule(lavitz_rod_typhoon, lambda state: state.has("Kongol 1", world.player))
    set_rule(lavitz_gust_of_wind_dance, lambda state: state.has("Shirley", world.player))

    albert_spinning_cane = world.get_location("Albert - Spinning Cane Unlock")
    albert_rod_typhoon = world.get_location("Albert - Rod Typhoon Unlock")
    albert_gust_of_wind_dance = world.get_location("Albert - Gust of Wind Dance Unlock")

    set_rule(albert_spinning_cane, lambda state: state.has("Axe from the Shack", world.player))
    set_rule(albert_rod_typhoon, lambda state: state.has("Kongol 1", world.player))
    set_rule(albert_gust_of_wind_dance, lambda state: state.has("Shirley", world.player))

    haschel_flurry_of_styx = world.get_location("Haschel - Flurry of Styx Unlock")
    haschel_summon_4_gods = world.get_location("Haschel - Summon 4 Gods Unlock")
    haschel_5_ring_shattering = world.get_location("Haschel - 5-Ring Shattering Unlock")
    haschel_hex_hammer = world.get_location("Haschel - Hex Hammer Unlock")

    set_rule(haschel_flurry_of_styx, lambda state: state.has("Dragoon Doel", world.player))
    set_rule(haschel_summon_4_gods, lambda state: state.has("Gehrich", world.player))
    set_rule(haschel_5_ring_shattering, lambda state: state.has("Kamuy", world.player))
    set_rule(haschel_hex_hammer, lambda state: state.has("Polter", world.player))

    meru_hammer_spin = world.get_location("Meru - Hammer Spin Unlock")
    meru_cool_boogie = world.get_location("Meru - Cool Boogie Unlock")
    meru_cats_cradle = world.get_location("Meru - Cat's Cradle Unlock")

    set_rule(meru_hammer_spin, lambda state: state.has("Lenus 2", world.player))
    set_rule(meru_cool_boogie, lambda state: state.has("Polter", world.player))
    set_rule(meru_cats_cradle, lambda state: state.has("Kraken", world.player))

    kongol_inferno = world.get_location("Kongol - Inferno Unlock")
    set_rule(kongol_inferno, lambda state: state.has("Divine Dragon", world.player))