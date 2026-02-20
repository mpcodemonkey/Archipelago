from typing import Dict

from .item_data import LegendOfDragoonItemData, ItemCategory, ItemClassification as IC

additions_table:  Dict[str, LegendOfDragoonItemData] = {
    "Dart Double Slash": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30002, IC.progression),
    "Dart Volcano": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30003, IC.progression),
    "Dart Burning Rush": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30004, IC.progression),
    "Dart Crush Dance": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30005, IC.progression),
    "Dart Madness Hero": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30006, IC.progression),
    "Dart Moon Strike": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30007, IC.progression),
    "Dart Blazing Dynamo": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30008, IC.progression),

    "Lavitz Harpoon": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30010, IC.progression),
    "Lavitz Spinning Cane": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30011, IC.progression),
    "Lavitz Rod Typhoon": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30012, IC.progression),
    "Lavitz Gust Of Wind Dance": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30013, IC.progression),
    "Lavitz Flower Storm": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30014, IC.progression),

    "Rose Whip Smack": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30016, IC.progression),
    "Rose More More": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30017, IC.progression),
    "Rose Hard Blade": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30018, IC.progression),
    "Rose Demons Dance": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30019, IC.progression),

    "Haschel Double Punch": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30021, IC.progression),
    "Haschel Ferry Of Styx": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30022, IC.progression),
    "Haschel Summon 4 Gods": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30023, IC.progression),
    "Haschel Five Ring Shattering": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30024, IC.progression),
    "Haschel Hex Hammer": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30025, IC.progression),
    "Haschel Omni Sweep": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30026, IC.progression),

    "Albert Harpoon": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30028, IC.progression),
    "Albert Spinning Cane": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30029, IC.progression),
    "Albert Rod Typhoon": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30030, IC.progression),
    "Albert Gust Of Wind Dance": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30031, IC.progression),
    "Albert Flower Storm": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30032, IC.progression),

    "Meru Double Smack": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30034, IC.progression),
    "Meru Hammer Spin": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30035, IC.progression),
    "Meru Cool Boogie": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30036, IC.progression),
    "Meru Cats Cradle": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30037, IC.progression),
    "Meru Perky Step": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30038, IC.progression),

    "Kongol Pursuit": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30040, IC.progression),
    "Kongol Inferno": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30041, IC.progression),
    "Kongol Bone Crush": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30042, IC.progression),
}

progressive_additions_table: Dict[str, LegendOfDragoonItemData] = {
    "Dart Progressive Addition": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30001, IC.progression, 7),
    "Lavitz Progressive Addition": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30009, IC.progression, 5),
    "Rose Progressive Addition": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30015, IC.progression, 4),
    "Haschel Progressive Addition": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30020, IC.progression, 6),
    "Albert Progressive Addition": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30027, IC.progression, 5),
    "Meru Progressive Addition": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30033, IC.progression, 5),
    "Kongol Progressive Addition": LegendOfDragoonItemData(ItemCategory.ADDITION, 108_30039, IC.progression, 3),
}

all_additions: Dict[str, LegendOfDragoonItemData] = {
    **additions_table,
    **progressive_additions_table,
}