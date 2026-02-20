from typing import Optional, NamedTuple

from BaseClasses import Location
from worlds.legend_of_dragoon.game_id import lod_name


class LegendOfDragoonLocation(Location):
    game: str = lod_name


class LegendOfDragoonLocationData(NamedTuple):
    category: str
    code: Optional[int] = None
    type: Optional[str] = None
