from .bases import LegendOfDragoonTestBase

class TestDefault(LegendOfDragoonTestBase):
    options = {
        "enable_addition_randomizer": 4
    }

class TestProgressive(LegendOfDragoonTestBase):
    options = {
        "enable_addition_randomizer": 3,
    }

class TestAdditionSanity(LegendOfDragoonTestBase):
    options = {
        "enable_addition_randomizer": 4,
    }

class TestRandomizedProgression(LegendOfDragoonTestBase):
    options = {
        "enable_addition_randomizer": 3,
        "random_starting_addition": True,
    }