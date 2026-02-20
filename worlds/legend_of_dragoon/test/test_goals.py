from .bases import LegendOfDragoonTestBase

class TestDefault(LegendOfDragoonTestBase):
    options = {}


class TestFruegel2(LegendOfDragoonTestBase):
    options = {
        "lod_completion_condition": 2,
    }

    def test_fruegel2_accessible(self) -> None:
        with self.subTest("Test Commander is Accessible without any good"):
            commander = self.world.get_location("Commander")
            self.assertTrue(commander.can_reach(self.multiworld.state))

        with self.subTest("Test Fruegel 1 is Accessible with Prison Key"):
            self.assertAccessDependency(
        [
                    "Fruegel 1",
                ],
                [["Prison Key"]],
                only_check_listed=True,
            )

        with self.subTest("Test Urobolus is accessible with Axe from the Shack"):
            self.assertAccessDependency(
                [
                    "Urobolus",
                ],
                [["Prison Key", "Axe from the Shack"]],
                only_check_listed=True,
            )

        with self.subTest("Test Kongol 1 is accessible with lavitzs picture"):
            self.assertAccessDependency(
                [
                    "Sandora Elite",
                    "Kongol 1",
                ],
                [["Prison key, Axe from the Shack", "Lavitzs Picture"]],
                only_check_listed=True,
            )


        with self.subTest("Test Lloyd 1 is required for hellena 02 access"):
            # Manually checking the dependency in the previous function was a bit of a hassle, wasn't it?
            # Now we are checking four locations. It would be even longer as a result.
            # Well, there is another option. It's the assertAccessDependency function of WorldTestBase.
            self.assertAccessDependency(
                [
                    "Fruegel 2",
                ],
                [["Prison key, Axe from the Shack", "Lavitzs Picture", "Lloyd 1"]],
                only_check_listed=True,
            )

class TestDoel(LegendOfDragoonTestBase):
    options = {
        "lod_completion_condition": 3,
    }

class TestLenus2(LegendOfDragoonTestBase):
    options = {
        "lod_completion_condition": 4,
    }

class TestFaust(LegendOfDragoonTestBase):
    options = {
        "lod_completion_condition": 5,
    }

class TestMelbu(LegendOfDragoonTestBase):
    options = {
        "lod_completion_condition": 6,
    }

