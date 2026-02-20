from __future__ import annotations
from typing import  List, NamedTuple, Optional, TYPE_CHECKING

import Utils
from BaseClasses import Region, MultiWorld, CollectionState

if TYPE_CHECKING:
    from .world import LegendOfDragoonWorld

class LegendOfDragoonRegionData(NamedTuple):
    locations: List[str]
    region_exits: Optional[List[str]]


def create_and_connect_regions(world: LegendOfDragoonWorld) -> None:
    create_all_regions(world)
    connect_regions(world)

def create_all_regions(world: LegendOfDragoonWorld) -> None:
    regions = [
        Region("Menu", world.player, world.multiworld),
        Region("Dart Additions", world.player, world.multiworld),
        Region("Lavitz Additions", world.player, world.multiworld),
        Region("Rose Additions", world.player, world.multiworld),
        Region("Haschel Additions", world.player, world.multiworld),
        Region("Albert Additions", world.player, world.multiworld),
        Region("Meru Additions", world.player, world.multiworld),
        Region("Kongol Additions", world.player, world.multiworld),
        Region("Seles", world.player, world.multiworld),
        Region("Forest", world.player, world.multiworld),
        Region("Hellena Prison 01", world.player, world.multiworld),
        Region("Hellena Prison 02", world.player, world.multiworld),
        Region("Prairie", world.player, world.multiworld),
        Region("Limestone Cave", world.player, world.multiworld),
        Region("Bale", world.player, world.multiworld),
        Region("Hoax", world.player, world.multiworld),
        Region("Marshland", world.player, world.multiworld),
        Region("Volcano Villude", world.player, world.multiworld),
        Region("Dragon's Nest", world.player, world.multiworld),
        Region("Lohan", world.player, world.multiworld),
        Region("Shrine of Shirley", world.player, world.multiworld),
        Region("Kazas", world.player, world.multiworld),
        Region("Black Castle", world.player, world.multiworld),
        Region("Black Castle Throne Room", world.player, world.multiworld),

        Region("Queen Fury", world.player, world.multiworld),
        Region("Phantom Ship", world.player, world.multiworld),
        Region("Fletz", world.player, world.multiworld),
        Region("Fletz Castle", world.player, world.multiworld),
        Region("Barrens", world.player, world.multiworld),
        Region("Donau", world.player, world.multiworld),
        Region("Valley of Corrupted Gravity", world.player, world.multiworld),
        Region("Home of Giganto", world.player, world.multiworld),

        Region("Lidiera", world.player, world.multiworld),
        Region("Underwater Cavern", world.player, world.multiworld),
        Region("Fueno", world.player, world.multiworld),
        Region("Furni", world.player, world.multiworld),
        Region("Evergreen Forest", world.player, world.multiworld),
        Region("Deningrad", world.player, world.multiworld),
        Region("Neet", world.player, world.multiworld),
        Region("Wingly Forest", world.player, world.multiworld),
        Region("Forbidden Land", world.player, world.multiworld),
        Region("Mortal Dragon Mountain", world.player, world.multiworld),
        Region("Kashua Glacier", world.player, world.multiworld),
        Region("Tower of Flanvel", world.player, world.multiworld),
        Region("Snowfield", world.player, world.multiworld),
        Region("Fort Magrad", world.player, world.multiworld),
        Region("Vellweb", world.player, world.multiworld),
        Region("Death Frontier", world.player, world.multiworld),
        Region("Ulara", world.player, world.multiworld),
        Region("Rouge", world.player, world.multiworld),
        Region("Aglis", world.player, world.multiworld),
        Region("Zenebatos", world.player, world.multiworld),
        Region("Mayfil", world.player, world.multiworld),
        Region("Divine Tree", world.player, world.multiworld),
        Region("Moon That Never Sets", world.player, world.multiworld),
    ]

    world.multiworld.regions += regions

def connect_regions(world: LegendOfDragoonWorld) -> None:
    menu = world.get_region("Menu")
    dart_additions = world.get_region("Dart Additions")
    lavitz_additions = world.get_region("Lavitz Additions")
    rose_additions = world.get_region("Rose Additions")
    haschel_additions = world.get_region("Haschel Additions")
    albert_additions = world.get_region("Albert Additions")
    meru_additions = world.get_region("Meru Additions")
    kongol_additions = world.get_region("Kongol Additions")
    seles = world.get_region("Seles")
    forest = world.get_region("Forest")
    hellena_prison_01 = world.get_region("Hellena Prison 01")
    hellena_prison_02 = world.get_region("Hellena Prison 02")
    prairie = world.get_region("Prairie")
    limestone_cave = world.get_region("Limestone Cave")
    bale = world.get_region("Bale")
    hoax = world.get_region("Hoax")
    marshland = world.get_region("Marshland")
    volcano_villude = world.get_region("Volcano Villude")
    dragons_nest = world.get_region("Dragon's Nest")
    lohan = world.get_region("Lohan")
    shrine_of_shirley = world.get_region("Shrine of Shirley")
    kazas = world.get_region("Kazas")
    black_castle = world.get_region("Black Castle")
    black_castle_throne_room = world.get_region("Black Castle Throne Room")

    fletz = world.get_region("Fletz")
    barrens = world.get_region("Barrens")
    donau = world.get_region("Donau")
    fletz_castle = world.get_region("Fletz Castle")
    valley_of_corrupted_gravity = world.get_region("Valley of Corrupted Gravity")
    home_of_giganto = world.get_region("Home of Giganto")
    queen_fury = world.get_region("Queen Fury")
    phantom_ship = world.get_region("Phantom Ship")
    lidiera = world.get_region("Lidiera")
    underwater_cavern = world.get_region("Underwater Cavern")
    fueno = world.get_region("Fueno")

    furni = world.get_region("Furni")
    evergreen_forest = world.get_region("Evergreen Forest")
    deningrad = world.get_region("Deningrad")
    neet = world.get_region("Neet")
    wingly_forest = world.get_region("Wingly Forest")
    forbidden_land = world.get_region("Forbidden Land")
    mortal_dragon_mountain = world.get_region("Mortal Dragon Mountain")
    kashua_glacier = world.get_region("Kashua Glacier")
    tower_of_flanvel = world.get_region("Tower of Flanvel")
    snowfield = world.get_region("Snowfield")
    fort_magrad = world.get_region("Fort Magrad")
    vellweb = world.get_region("Vellweb")

    death_frontier = world.get_region("Death Frontier")
    ulara = world.get_region("Ulara")
    rouge = world.get_region("Rouge")
    aglis = world.get_region("Aglis")
    zenebatos = world.get_region("Zenebatos")
    mayfil = world.get_region("Mayfil")
    divine_tree = world.get_region("Divine Tree")
    moon_that_never_sets = world.get_region("Moon That Never Sets")

    menu.connect(dart_additions, "Menu to Dart Additions")
    menu.connect(lavitz_additions, "Menu to Lavitz Additions")
    menu.connect(rose_additions, "Menu to Rose Additions")
    menu.connect(haschel_additions, "Menu to Haschel Additions")
    menu.connect(albert_additions, "Menu to Albert Additions")
    menu.connect(meru_additions, "Menu to Meru Additions")
    menu.connect(kongol_additions, "Menu to Kongol Additions")

    # path out disc one
    menu.connect(seles, "Intro to Seles")
    seles.connect(forest, "Seles to Forest")
    forest.connect(seles, "Forest to Seles")
    forest.connect(hellena_prison_01, "Forest to Hellena Prison 01")
    forest.connect(prairie, "Forest to Prairie")
    hellena_prison_01.connect(forest, "Hellena Prison 01 to Forest", lambda state: state.has("Fruegel 1", world.player))
    hellena_prison_01.connect(hellena_prison_02, "Hellena Prison 01 to 02", lambda state: state.has("Lloyd 1", world.player))
    hellena_prison_02.connect(hellena_prison_01, "Hellena Prison 02 to 01", lambda state: state.has("Lloyd 1", world.player))
    prairie.connect(forest, "Prairie to Forest")
    prairie.connect(limestone_cave, "Prairie to Limestone Cave")
    limestone_cave.connect(prairie, "Limestone Cave to Prairie")
    limestone_cave.connect(bale, "Limestone Cave to Bale", lambda state: state.has("Urobolus", world.player))
    bale.connect(limestone_cave, "Bale to Limestone Cave")
    bale.connect(hoax, "Bale to Hoax")
    hoax.connect(bale, "Hoax to Bale")
    hoax.connect(marshland, "Hoax to Marshland", lambda state: state.has("Kongol 1", world.player))
    marshland.connect(hoax, "Marshland to Hoax")
    marshland.connect(volcano_villude, "Marshland to Volcano Villude")
    volcano_villude.connect(marshland, "Volcano Villude to Marshland")
    volcano_villude.connect(dragons_nest, "Volcano Villude to Dragon's Nest", lambda state: state.has("Firebird", world.player))
    dragons_nest.connect(volcano_villude, "Dragon's Nest to Volcano Villude")
    dragons_nest.connect(lohan, "Dragon's Nest to Lohan")
    lohan.connect(dragons_nest, "Lohan to Dragon's Nest")
    dragons_nest.connect(shrine_of_shirley, "Dragon's Nest to Shrine of Shirley")
    shrine_of_shirley.connect(dragons_nest, "Shrine of Shirley to Dragon's Nest")
    forest.connect(kazas, "Forest to Kazas")
    kazas.connect(forest, "Kazas to Forest")
    kazas.connect(black_castle, "Kazas to Black Castle")
    black_castle.connect(kazas, "Black Castle to Kazas")
    black_castle.connect(black_castle_throne_room, "Black Castle to Black Castle Throne Room", lambda state: state.has_all(["Magic Oil", "Blue Stone", "Yellow Stone", "Red Stone"], world.player))
    black_castle_throne_room.connect(fletz, "Black Castle Throne Room to Fletz")

    # path out disc 2
    fletz.connect(barrens, "Fletz to Barrens")
    fletz.connect(fletz_castle, "Fletz to Fletz Castle")
    fletz_castle.connect(fletz, "Fletz Castle to Fletz")
    barrens.connect(fletz, "Barrens to Fletz")
    barrens.connect(donau, "Barrens to Donau")
    barrens.connect(valley_of_corrupted_gravity, "Barrens to Valley of Corrupted Gravity")
    valley_of_corrupted_gravity.connect(barrens, "Valley of Corrupted Gravity to Barrens")
    valley_of_corrupted_gravity.connect(home_of_giganto, "Valley of Corrupted Gravity to Home of Giganto", lambda state: state.has("Valley Virage", world.player))
    home_of_giganto.connect(valley_of_corrupted_gravity, "Home of Giganto to Valley of Corrupted Gravity")
    donau.connect(queen_fury, "Donau to Queen Fury")
    queen_fury.connect(donau, "Queen Fury to Donau")
    queen_fury.connect(phantom_ship, "Queen Fury to Phantom Ship")
    phantom_ship.connect(lidiera, "Phantom Ship to Lidiera")
    lidiera.connect(underwater_cavern, "Lidiera to Underwater Cavern")
    underwater_cavern.connect(lidiera, "Underwater Cavern to Lidiera")
    underwater_cavern.connect(fueno, "Underwater Cavern to Fueno")
    fueno.connect(underwater_cavern, "Fueno to Underwater Cavern")
    fueno.connect(queen_fury, "Fueno to Queen Fury", lambda state: state.has("Lenus 2", world.player))
    donau.connect(furni, "Donau to Furni", lambda state: state.has("Lenus 2", world.player))

    # path out disc 3
    furni.connect(evergreen_forest, "Furni to Evergreen Forest")
    evergreen_forest.connect(furni, "Evergreen Forest to Furni")
    evergreen_forest.connect(deningrad, "Evergreen Forest to Deningrad")
    evergreen_forest.connect(neet, "Evergreen Forest to Neet")
    deningrad.connect(evergreen_forest, "Deningrad to Evergreen Forest")
    neet.connect(evergreen_forest, "Neet to Evergreen Forest")
    evergreen_forest.connect(wingly_forest, "Evergreen Forest to Wingly Forest")
    wingly_forest.connect(forbidden_land, "Wingly Forest to Forbidden Land")
    forbidden_land.connect(wingly_forest, "Forbidden Land to Wingly Forest")
    wingly_forest.connect(deningrad, "Wingly Forest to Deningrad")
    evergreen_forest.connect(mortal_dragon_mountain, "Evergreen Forest to Mortal Dragon Mountain")
    mortal_dragon_mountain.connect(evergreen_forest, "Mortal Dragon Mountain to Evergreen Forest")
    deningrad.connect(kashua_glacier, "Deningrad to Kashua Glacier")
    kashua_glacier.connect(deningrad, "Kashua Glacier to Deningrad")
    kashua_glacier.connect(tower_of_flanvel, "Kashua Glacier to Tower of Flanvel")
    tower_of_flanvel.connect(kashua_glacier, "Tower of Flanvel to Kashua Glacier")
    kashua_glacier.connect(snowfield, "Kashua Glacier to Snowfield")
    snowfield.connect(kashua_glacier, "Snowfield to Kashua Glacier")
    snowfield.connect(fort_magrad, "Snowfield to Fort Magrad")
    fort_magrad.connect(snowfield, "Fort Magrad to Snowfield")
    snowfield.connect(vellweb, "Snowfield to Vellweb")
    vellweb.connect(snowfield, "Vellweb to Snowfield")
    vellweb.connect(death_frontier, "Vellweb to Death Frontier")

    # path out disc 4
    death_frontier.connect(ulara, "Death Frontier to Ulara")
    ulara.connect(death_frontier, "Ulara to Death Frontier")
    ulara.connect(home_of_giganto, "Ulara to Home of Giganto")
    home_of_giganto.connect(ulara, "Home of Giganto to Ulara")
    queen_fury.connect(rouge, "Queen Fury to Rouge")
    rouge.connect(queen_fury, "Rouge to Queen Fury")
    rouge.connect(aglis, "Rouge to Aglis")
    aglis.connect(rouge, "Aglis to Rouge")
    aglis.connect(zenebatos, "Aglis to Zenebatos")
    # coolon is now able to fly us anywhere, minus phantom ship.
    zenebatos.connect(aglis, "Zenebatos to Aglis")
    zenebatos.connect(mayfil, "Zenebatos to Mayfil")
    mayfil.connect(zenebatos, "Mayfil to Zenebatos")
    mayfil.connect(divine_tree, "Mayfil to Divine Tree")
    divine_tree.connect(moon_that_never_sets, "Divine Tree to Moon That Never Sets")

def visualize_world(multiworld: "MultiWorld", state: "CollectionState" = None):
    if not state:
        state = CollectionState(multiworld, True)
        for item in multiworld.itempool:
            state.collect(item, True)
        state.sweep_for_advancements()
    Utils.visualize_regions(multiworld.get_region(multiworld.worlds[1].origin_region_name, 1), f"{multiworld.player_name[1]}.puml",
                            linetype_ortho=False,
                            regions_to_highlight=state.reachable_regions[1])