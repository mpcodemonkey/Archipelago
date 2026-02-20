from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld
from .game_id import lod_name

from .options import option_groups, option_presets


class LegendOfDragoonWebWorld(WebWorld):
    game = lod_name
    theme = "jungle"
    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up ArchiDragoon (Archipelago on Severed Chains)",
        "English",
        "en_setup.md",
        "setup/en",
        ["pkolb-dev"]
    )

    tutorials = [setup_en]
    bug_report_page = "https://github.com/pkolb-dev/Archipelago/issues"
    option_groups = option_groups
    options_presets = option_presets
