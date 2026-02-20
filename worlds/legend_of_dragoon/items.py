from __future__ import annotations

from typing import Dict, Set, TYPE_CHECKING, List

from BaseClasses import ItemClassification
from worlds.legend_of_dragoon.item.additions import additions_table, all_additions, progressive_additions_table
from worlds.legend_of_dragoon.item.consumables import  consumables_table
from worlds.legend_of_dragoon.item.equipment import  equipment_table
from worlds.legend_of_dragoon.item.goods import goods_table
from .item.item_data import LegendOfDragoonItemData, LegendOfDragoonItem

if TYPE_CHECKING:
    from .world import LegendOfDragoonWorld

def get_items_by_category(item_category: str) -> Dict[str, LegendOfDragoonItemData]:
    return {name: data for name, data in lookup_table.items() if data.category == item_category}

lookup_table: Dict[str, LegendOfDragoonItemData] = {
    **all_additions,
    **consumables_table,
    **equipment_table,
    **goods_table,
}

ITEM_NAME_TO_ID = {name: data.code for name, data in lookup_table.items()}

def get_random_filler_item_name(world: LegendOfDragoonWorld):
    filtered_dict = {key: value for key, value in lookup_table.items() if value.classification == ItemClassification.filler}
    return world.random.choices([filler for filler in filtered_dict.keys()])[0]

def create_item(world: LegendOfDragoonWorld, name: str):
    data = lookup_table[name]
    return LegendOfDragoonItem(name, data.classification, data.code, world.player)

def create_all_items(world: LegendOfDragoonWorld):
    itempool: List[LegendOfDragoonItem] = []

    # set up goods
    for lod_item in map(world.create_item, goods_table):
        if not lod_item.classification.filler:
            itempool.append(lod_item)

    # set up equipment
    if world.options.enable_shopsanity:
        for lod_item in map(world.create_item, equipment_table):
            if not lod_item.classification.filler:
                itempool.append(lod_item)

    # set up additions
    if world.options.enable_addition_randomizer == world.options.enable_addition_randomizer.option_progressive_character:
        for key, value in progressive_additions_table.items():
            for i in range(0, value.quantity - 1):
                itempool.append(create_item(world, key))
    else:
        for lod_item in map(world.create_item, additions_table):
            itempool.append(lod_item)

    if world.options.lod_completion_condition.option_faust:
        itempool.append(create_item(world, "Legend Casque"))
        itempool.append(create_item(world, "Legend Casque"))

    if world.options.enable_addition_randomizer == world.options.enable_addition_randomizer.option_progressive_character:
        for addition in progressive_additions_table.keys():
           progressive_addition = world.create_item(addition)
           world.push_precollected(progressive_addition)
    elif not world.options.random_starting_addition:
        double_slash = world.create_item("Dart Double Slash")
        lavitz_harpoon = world.create_item("Lavitz Harpoon")
        whip_smack = world.create_item("Rose Whip Smack")
        double_punch = world.create_item("Haschel Double Punch")
        albert_harpoon = world.create_item("Albert Harpoon")
        double_smack = world.create_item("Meru Double Smack")
        pursuit = world.create_item("Kongol Pursuit")

        itempool.remove(double_slash)
        itempool.remove(lavitz_harpoon)
        itempool.remove(whip_smack)
        itempool.remove(double_punch)
        itempool.remove(albert_harpoon)
        itempool.remove(double_smack)
        itempool.remove(pursuit)

        world.push_precollected(double_slash)
        world.push_precollected(lavitz_harpoon)
        world.push_precollected(whip_smack)
        world.push_precollected(double_punch)
        world.push_precollected(albert_harpoon)
        world.push_precollected(double_smack)
        world.push_precollected(pursuit)
    else:
        dart_additions = [key for key in additions_table.keys() if "Dart" in key]
        lavitz_additions = [key for key in additions_table.keys() if "Lavitz" in key]
        rose_additions = [key for key in additions_table.keys() if "Rose" in key]
        haschel_additions = [key for key in additions_table.keys() if "Haschel" in key]
        albert_additions = [key for key in additions_table.keys() if "Albert" in key]
        meru_additions = [key for key in additions_table.keys() if "Meru" in key]
        kongol_additions = [key for key in additions_table.keys() if "Kongol" in key]

        dart_addition = create_item(world, world.random.choices(dart_additions)[0])
        lavitz_addition = create_item(world, world.random.choices(lavitz_additions)[0])
        rose_addition = create_item(world, world.random.choices(rose_additions)[0])
        haschel_addition = create_item(world, world.random.choices(haschel_additions)[0])
        albert_addition = create_item(world, world.random.choices(albert_additions)[0])
        meru_addition = create_item(world, world.random.choices(meru_additions)[0])
        kongol_addition = create_item(world, world.random.choices(kongol_additions)[0])

        itempool.remove(dart_addition)
        itempool.remove(lavitz_addition)
        itempool.remove(rose_addition)
        itempool.remove(haschel_addition)
        itempool.remove(albert_addition)
        itempool.remove(meru_addition)
        itempool.remove(kongol_addition)

        world.push_precollected(dart_addition)
        world.push_precollected(lavitz_addition)
        world.push_precollected(rose_addition)
        world.push_precollected(haschel_addition)
        world.push_precollected(albert_addition)
        world.push_precollected(meru_addition)
        world.push_precollected(kongol_addition)

    number_of_items = len(itempool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))

    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    world.multiworld.itempool += itempool


# Make item categories
item_name_groups: Dict[str, Set[str]] = {}
for item in lookup_table.keys():
    category = lookup_table[item].category
    if category not in item_name_groups.keys():
        item_name_groups[category] = set()
    item_name_groups[category].add(item)
