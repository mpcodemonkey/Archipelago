from __future__ import annotations

from typing import Dict, TYPE_CHECKING

from worlds.legend_of_dragoon.loc.additions import addition_table
from worlds.legend_of_dragoon.loc.chests import chests_table
from worlds.legend_of_dragoon.loc.enemies import enemy_table
from worlds.legend_of_dragoon.loc.events import events_table
from worlds.legend_of_dragoon.loc.location_data import LegendOfDragoonLocationData, LegendOfDragoonLocation
from worlds.legend_of_dragoon.loc.shops import shop_table
from .item.item_data import LegendOfDragoonItem
from .loc.goods import goods_location_table

if TYPE_CHECKING:
    from .world import LegendOfDragoonWorld

location_table: Dict[str, LegendOfDragoonLocationData] = {
    **addition_table,
    # **chests_table,
    **events_table,
    **enemy_table,
    # **goods_location_table,
}

all_location_table: Dict[str, LegendOfDragoonLocationData] = {
    **addition_table,
    **chests_table,
    **events_table,
    **enemy_table,
    **goods_location_table,
    **shop_table,
}

LOCATION_NAME_TO_ID = {name: data.code for name, data in all_location_table.items()}

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}

def get_locations_by_category(location_category: str) -> Dict[str, LegendOfDragoonLocationData]:
    return {name: data for name, data in location_table.items() if data.category == location_category}

def get_locations_by_category_with_ids(location_category: str) -> Dict[str, int | None]:
    locs: Dict[str,LegendOfDragoonLocationData] = get_locations_by_category(location_category)
    return {location_name: locs[location_name].code for location_name in locs}


def create_all_locations(world: LegendOfDragoonWorld) -> None:
    create_regular_locations(world)
    create_events(world)

def create_regular_locations(world: LegendOfDragoonWorld) -> None:
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

    if world.options.enable_shopsanity:
        location_table.update(**shop_table)

    seles.add_locations(get_locations_by_category_with_ids("Seles"), LegendOfDragoonLocation)
    forest.add_locations(get_locations_by_category_with_ids("Forest"), LegendOfDragoonLocation)
    limestone_cave.add_locations(get_locations_by_category_with_ids("Limestone Cave"), LegendOfDragoonLocation)
    bale.add_locations(get_locations_by_category_with_ids("Bale"), LegendOfDragoonLocation)
    hoax.add_locations(get_locations_by_category_with_ids("Hoax"), LegendOfDragoonLocation)
    lohan.add_locations(get_locations_by_category_with_ids("Lohan"), LegendOfDragoonLocation)
    shrine_of_shirley.add_locations(get_locations_by_category_with_ids("Shrine of Shirley"), LegendOfDragoonLocation)
    dragons_nest.add_locations(get_locations_by_category_with_ids("Dragon's Nest"), LegendOfDragoonLocation)
    kazas.add_locations(get_locations_by_category_with_ids("Kazas"), LegendOfDragoonLocation)
    black_castle.add_locations(get_locations_by_category_with_ids("Black Castle"), LegendOfDragoonLocation)
    black_castle_throne_room.add_locations(get_locations_by_category_with_ids("Black Castle Throne Room"), LegendOfDragoonLocation)
    fletz.add_locations(get_locations_by_category_with_ids("Fletz"), LegendOfDragoonLocation)
    fletz_castle.add_locations(get_locations_by_category_with_ids("Fletz Castle"), LegendOfDragoonLocation)
    barrens.add_locations(get_locations_by_category_with_ids("Barrens"), LegendOfDragoonLocation)
    donau.add_locations(get_locations_by_category_with_ids("Donau"), LegendOfDragoonLocation)
    valley_of_corrupted_gravity.add_locations(get_locations_by_category_with_ids("Valley of Corrupted Gravity"), LegendOfDragoonLocation)
    home_of_giganto.add_locations(get_locations_by_category_with_ids("Home of Giganto"), LegendOfDragoonLocation)
    queen_fury.add_locations(get_locations_by_category_with_ids("Queen Fury"), LegendOfDragoonLocation)
    phantom_ship.add_locations(get_locations_by_category_with_ids("Phantom Ship"), LegendOfDragoonLocation)
    underwater_cavern.add_locations(get_locations_by_category_with_ids("Underwater Cavern"), LegendOfDragoonLocation)
    fueno.add_locations(get_locations_by_category_with_ids("Fueno"), LegendOfDragoonLocation)
    furni.add_locations(get_locations_by_category_with_ids("Furni"), LegendOfDragoonLocation)
    evergreen_forest.add_locations(get_locations_by_category_with_ids("Evergreen Forest"), LegendOfDragoonLocation)
    deningrad.add_locations(get_locations_by_category_with_ids("Deningrad"), LegendOfDragoonLocation)
    wingly_forest.add_locations(get_locations_by_category_with_ids("Wingly Forest"), LegendOfDragoonLocation)
    forbidden_land.add_locations(get_locations_by_category_with_ids("Forbidden Land"), LegendOfDragoonLocation)
    vellweb.add_locations(get_locations_by_category_with_ids("Vellweb"), LegendOfDragoonLocation)
    mortal_dragon_mountain.add_locations(get_locations_by_category_with_ids("Mortal Dragon Mountain"), LegendOfDragoonLocation)
    kashua_glacier.add_locations(get_locations_by_category_with_ids("Kashua Glacier"), LegendOfDragoonLocation)
    tower_of_flanvel.add_locations(get_locations_by_category_with_ids("Tower of Flanvel"), LegendOfDragoonLocation)
    snowfield.add_locations(get_locations_by_category_with_ids("Snowfield"), LegendOfDragoonLocation)
    ulara.add_locations(get_locations_by_category_with_ids("Ulara"), LegendOfDragoonLocation)
    rouge.add_locations(get_locations_by_category_with_ids("Rouge"), LegendOfDragoonLocation)
    aglis.add_locations(get_locations_by_category_with_ids("Aglis"), LegendOfDragoonLocation)
    moon_that_never_sets.add_locations(get_locations_by_category_with_ids("Moon"), LegendOfDragoonLocation)
    # we want hellena prison to have the same items, in case they are needed later, but thats for the mod. not here.
    hellena_prison_01.add_locations(get_locations_by_category_with_ids("Hellena 01"), LegendOfDragoonLocation)
    hellena_prison_02.add_locations(get_locations_by_category_with_ids("Hellena 02"), LegendOfDragoonLocation)
    kashua_glacier.add_locations(get_locations_by_category_with_ids("Kashua"), LegendOfDragoonLocation)
    volcano_villude.add_locations(get_locations_by_category_with_ids("Volcano"), LegendOfDragoonLocation)
    volcano_villude.add_locations(get_locations_by_category_with_ids("Volcano Villude"), LegendOfDragoonLocation)
    zenebatos.add_locations(get_locations_by_category_with_ids("Zenebatos"), LegendOfDragoonLocation)
    divine_tree.add_locations(get_locations_by_category_with_ids("Divine Tree"), LegendOfDragoonLocation)

    # additions
    dart_additions.add_locations(get_locations_by_category_with_ids("Dart"), LegendOfDragoonLocation)
    lavitz_additions.add_locations(get_locations_by_category_with_ids("Lavitz"), LegendOfDragoonLocation)
    rose_additions.add_locations(get_locations_by_category_with_ids("Rose"), LegendOfDragoonLocation)
    haschel_additions.add_locations(get_locations_by_category_with_ids("Haschel"), LegendOfDragoonLocation)
    albert_additions.add_locations(get_locations_by_category_with_ids("Albert"), LegendOfDragoonLocation)
    meru_additions.add_locations(get_locations_by_category_with_ids("Meru"), LegendOfDragoonLocation)
    kongol_additions.add_locations(get_locations_by_category_with_ids("Kongol"), LegendOfDragoonLocation)


def create_events(world: LegendOfDragoonWorld) -> None:
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

    # set boss events
    seles.add_event("Defeat Commander", "Commander", location_type=LegendOfDragoonLocation, item_type=LegendOfDragoonItem)
    hellena_prison_01.add_event("Defeat Fruegel 1", "Fruegel 1", location_type=LegendOfDragoonLocation, item_type=LegendOfDragoonItem)
    limestone_cave.add_event("Defeat Urobolus", "Urobolus", location_type=LegendOfDragoonLocation, item_type=LegendOfDragoonItem)
    hoax.add_event("Defeat Kongol 1", "Kongol 1", location_type=LegendOfDragoonLocation, item_type=LegendOfDragoonItem)
    volcano_villude.add_event("Defeat Volcano Virage", "Volcano Virage", location_type=LegendOfDragoonLocation, item_type=LegendOfDragoonItem)
    volcano_villude.add_event("Defeat Firebird", "Firebird", location_type=LegendOfDragoonLocation, item_type=LegendOfDragoonItem)
    dragons_nest.add_event("Defeat Greham", "Greham", location_type=LegendOfDragoonLocation, item_type=LegendOfDragoonItem)
    shrine_of_shirley.add_event("Defeat Shirley", "Shirley", location_type=LegendOfDragoonLocation, item_type=LegendOfDragoonItem)
    lohan.add_event("Lose to Lloyd", "Lloyd 1", location_type=LegendOfDragoonLocation, item_type=LegendOfDragoonItem)
    hellena_prison_02.add_event("Defeat Fruegel 2", "Fruegel 2", location_type=LegendOfDragoonLocation, item_type=LegendOfDragoonItem)
    black_castle.add_event("Defeat Kongol 2", "Kongol 2", location_type=LegendOfDragoonLocation, item_type=LegendOfDragoonItem)
    black_castle_throne_room.add_event("Defeat Dragoon Doel", "Dragoon Doel", location_type=LegendOfDragoonLocation, item_type=LegendOfDragoonItem)
    barrens.add_event("Mappi Steals Orb", "Mappi Steals Orb", location_type=LegendOfDragoonLocation, item_type=LegendOfDragoonItem)
    valley_of_corrupted_gravity.add_event("Defeat Valley Virage", "Valley Virage", location_type=LegendOfDragoonLocation, item_type=LegendOfDragoonItem)
    home_of_giganto.add_event("Defeat Gehrich", "Gehrich", location_type=LegendOfDragoonLocation, item_type=LegendOfDragoonItem)
    fletz_castle.add_event("Defeat Lenus 1", "Lenus 1", location_type=LegendOfDragoonLocation, item_type=LegendOfDragoonItem)
    phantom_ship.add_event("Defeat Ghost Commander", "Ghost Commander", location_type=LegendOfDragoonLocation, item_type=LegendOfDragoonItem)
    underwater_cavern.add_event("Defeat Lenus & Regole", "Lenus 2", location_type=LegendOfDragoonLocation, item_type=LegendOfDragoonItem)
    evergreen_forest.add_event("Defeat Kamuy", "Kamuy", location_type=LegendOfDragoonLocation, item_type=LegendOfDragoonItem)
    deningrad.add_event("Talk to Ute", "Talk to Ute", location_type=LegendOfDragoonLocation, item_type=LegendOfDragoonItem)
    forbidden_land.add_event("Defeat Kadessa Virage", "Kadessa Virage", location_type=LegendOfDragoonLocation, item_type=LegendOfDragoonItem)
    forbidden_land.add_event("Defeat Grand Jewel", "Grand Jewel", location_type=LegendOfDragoonLocation, item_type=LegendOfDragoonItem)
    mortal_dragon_mountain.add_event("Defeat Divine Dragon", "Divine Dragon", location_type=LegendOfDragoonLocation, item_type=LegendOfDragoonItem)
    kashua_glacier.add_event("Defeat Windigo", "Windigo", location_type=LegendOfDragoonLocation, item_type=LegendOfDragoonItem)
    tower_of_flanvel.add_event("Defeat Lloyd", "Lloyd 2", location_type=LegendOfDragoonLocation, item_type=LegendOfDragoonItem)
    tower_of_flanvel.add_event("Defeat Magician Faust", "Faust", location_type=LegendOfDragoonLocation, item_type=LegendOfDragoonItem)
    snowfield.add_event("Defeat Polter", "Polter", location_type=LegendOfDragoonLocation, item_type=LegendOfDragoonItem)
    ulara.add_event("Unlock Ulara Teleporter", "Ulara Teleporter", location_type=LegendOfDragoonLocation, item_type=LegendOfDragoonItem)
    aglis.add_event("Defeat Kraken", "Kraken", location_type=LegendOfDragoonLocation, item_type=LegendOfDragoonItem)

    zenebatos.add_event("Defeat Vector", "Vector", location_type=LegendOfDragoonLocation, item_type=LegendOfDragoonItem)
    zenebatos.add_event("Defeat Kubila", "Kubila", location_type=LegendOfDragoonLocation, item_type=LegendOfDragoonItem)
    zenebatos.add_event("Defeat Selebus", "Selebus", location_type=LegendOfDragoonLocation, item_type=LegendOfDragoonItem)
    mayfil.add_event("Defeat Feyrbrand", "Feyrbrand", location_type=LegendOfDragoonLocation, item_type=LegendOfDragoonItem)
    mayfil.add_event("Defeat Regole", "Regole", location_type=LegendOfDragoonLocation, item_type=LegendOfDragoonItem)
    mayfil.add_event("Defeat Divine Dragon Ghost", "Divine Dragon Ghost", location_type=LegendOfDragoonLocation, item_type=LegendOfDragoonItem)
    mayfil.add_event("Defeat Zackwell", "Zackwell", location_type=LegendOfDragoonLocation, item_type=LegendOfDragoonItem)
    divine_tree.add_event("Defeat Imago", "Imago", location_type=LegendOfDragoonLocation, item_type=LegendOfDragoonItem)
    moon_that_never_sets.add_event("Defeat Moon Virage", "Moon Virage", location_type=LegendOfDragoonLocation, item_type=LegendOfDragoonItem)
    moon_that_never_sets.add_event("Defeat Zieg", "Zieg", location_type=LegendOfDragoonLocation, item_type=LegendOfDragoonItem)
    moon_that_never_sets.add_event("Defeat Melbu Frahma", "Melbu Frahma", location_type=LegendOfDragoonLocation, item_type=LegendOfDragoonItem)
