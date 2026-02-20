from typing import NamedTuple, Optional
from BaseClasses import ItemClassification, Item
from worlds.legend_of_dragoon.game_id import lod_name

class LegendOfDragoonItem(Item):
    game: str = lod_name

class LegendOfDragoonItemData(NamedTuple):
    category: str
    code: Optional[int]
    classification: ItemClassification
    quantity: int = 1

class ItemCategory:
    CONSUMABLE  = "Consumable"
    EQUIPMENT   = "Equipment"
    GOOD        = "Good"
    ADDITION    = "Addition"
    EVENT       = "Event"
