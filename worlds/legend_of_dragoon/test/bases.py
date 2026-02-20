from test.bases import WorldTestBase
from worlds.legend_of_dragoon.game_id import lod_name
from ..world import LegendOfDragoonWorld

class LegendOfDragoonTestBase(WorldTestBase):
    game = lod_name
    world = LegendOfDragoonWorld
