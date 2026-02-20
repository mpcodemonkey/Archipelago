from typing import List

from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld, World
from .Items import KHCOMItem, KHCOMItemData, event_item_table, get_items_by_category, item_table
from .Locations import KHCOMLocation, location_table, get_locations_by_category
from .Options import KHCOMOptions
from .Regions import create_regions
from .Rules import set_rules
from worlds.LauncherComponents import Component, components, Type, launch_subprocess
import random



def launch_client():
    from .Client import launch
    launch_subprocess(launch, name="KHCOM Client")


components.append(Component("KHCOM Client", "KHCOMClient", func=launch_client, component_type=Type.CLIENT))

class KHCOMWeb(WebWorld):
    theme = "ocean"
    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Kingdom Hearts Chain of Memories Randomizer software on your computer. This guide covers single-player, "
        "multiworld, and related software.",
        "English",
        "khcom_en.md",
        "khcom/en",
        ["Gicu"]
    )]

class KHCOMWorld(World):
    """
    Kingdom Hearts Chain of Memories is an action card RPG following
    Sora on his journey through Castle Oblivion to find Riku and Kairi.
    """
    game = "Kingdom Hearts Chain of Memories"
    options_dataclass = KHCOMOptions
    options: KHCOMOptions
    topology_present = True
    data_version = 4
    required_client_version = (0, 3, 5)
    web = KHCOMWeb()

    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = {name: data.code for name, data in location_table.items()}

    def create_items(self):
        item_pool: List[KHCOMItem] = []
        self.multiworld.get_location("Final Marluxia", self.player).place_locked_item(self.create_item("Victory"))
        # Handle starting packs
        if self.options.packs_or_sets == "packs" and self.options.starting_packs > 0:
            i = 0
            while i < self.options.starting_packs:
                self.multiworld.push_precollected(self.create_item("Bronze Card Pack"))
                i = i + 1
        # Handle starting worlds
        starting_worlds = []
        if self.options.starting_worlds > 0:
            possible_starting_worlds = [
                "World Card Wonderland",
                "World Card Olympus Coliseum",
                "World Card Agrabah",
                "World Card Monstro",
                "World Card Atlantica",
                "World Card Halloween Town",
                "World Card Neverland",
                "World Card Hollow Bastion",
                "World Card 100 Acre Wood",
                "World Card Twilight Town",
                "World Card Destiny Islands"]
            starting_worlds = self.random.sample(possible_starting_worlds, min(self.options.starting_worlds.value, len(possible_starting_worlds)))
            for starting_world in starting_worlds:
                self.multiworld.push_precollected(self.create_item(starting_world))
        if self.options.early_cure:
            self.multiworld.push_precollected(self.create_item("Card Set Cure 4-6"))
        total_locations = len(self.multiworld.get_unfilled_locations(self.player))
        for name, data in item_table.items():
            quantity = data.max_quantity
            
            # Ignore filler, it will be added in a later stage.
            if data.category not in ["World Unlocks", "Gold Map Cards", "Friend Cards"]:
                continue
            elif name not in starting_worlds:
                item_pool.append(self.create_item(name))

        # Fill any empty locations with filler items.
        item_names = []
        attempts = 0 #If we ever try to add items 200 times, and all the items are used up, lets clear the item_names array, we probably don't have enough items
        while len(item_pool) < total_locations:
            item_name = self.get_filler_item_name()
            if item_name not in item_names or "Pack" in item_name:
                item_names.append(item_name)
                item_pool.append(self.create_item(item_name))
                attempts = 0
            elif attempts >= 200:
                item_names = []
                attempts = 0
            else:
                attempts = attempts + 1

        self.multiworld.itempool += item_pool

    def get_filler_item_name(self) -> str:
        fillers = {}
        disclude = []
        if not self.options.zeroes:
            disclude.append("0")
        if not self.options.cure:
            disclude.append("Cure")
        if self.options.early_cure:
            disclude.append("Cure 4-6")
        if self.options.enemy_cards:
            fillers.update(get_items_by_category("Enemy Cards", disclude))
        if self.options.packs_or_sets == "packs":
            fillers.update(get_items_by_category("Packs", disclude))
        elif self.options.packs_or_sets == "sets":
            fillers.update(get_items_by_category("Sets", disclude))
        weights = [data.weight for data in fillers.values()]
        return self.multiworld.random.choices([filler for filler in fillers.keys()], weights, k=1)[0]
        
    def create_item(self, name: str) -> KHCOMItem:
        data = item_table[name]
        return KHCOMItem(name, data.classification, data.code, self.player)

    def create_event(self, name: str) -> KHCOMItem:
        data = event_item_table[name]
        return KHCOMItem(name, data.classification, data.code, self.player)

    def set_rules(self):
        set_rules(self.multiworld, self.player)

    def create_regions(self):
        create_regions(self.multiworld, self.player)