from typing import Mapping, Any

import Utils
from BaseClasses import CollectionState, MultiWorld
from worlds.AutoWorld import World
from . import items, locations, regions, rules, web_world, options as lod_options
from .game_id import lod_name
from .item.item_data import LegendOfDragoonItem


class LegendOfDragoonWorld(World):
    """
    The Legend of Dragoon is a role-playing game developed and published by Sony Computer Entertainment for the video game console PlayStation.
    It was first released in Japan on December 2, 1999, in North America on June 11, 2000, and on January 19, 2001 in Europe.
    It was re-released in PlayStation Network December 22, 2010 in Japan and May 1, 2012 in North America.
    The game follows a young man, Dart Feld, on his journey through a world of magic, where ancient dragon warriors
    called Dragoons exist, to fight against evil forces who are threatening to destroy the world.
    """

    game = lod_name
    web = web_world.LegendOfDragoonWebWorld()

    # Options
    options_dataclass = lod_options.LegendOfDragoonOptions
    options: lod_options.LegendOfDragoonOptions

    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID

    origin_region_name = "Menu"

    def create_regions(self):
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self):
        rules.set_all_rules(self)

    def create_item(self, name: str) -> LegendOfDragoonItem:
        return items.create_item(self, name)

    def create_items(self):
        items.create_all_items(self)

    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

    def fill_slot_data(self) -> Mapping[str, Any]:
        # If you need access to the player's chosen options on the client side, there is a helper for that.
        return {
            "enable_addition_randomizer": self.options.enable_addition_randomizer.value,
            "random_starting_addition": self.options.random_starting_addition.value,
            "lod_completion_condition": self.options.lod_completion_condition.value,
            "enable_shop_sanity": self.options.enable_shopsanity.value,
            "world_version": self.world_version,
        }
