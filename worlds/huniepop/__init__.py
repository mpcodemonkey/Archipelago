import random

from BaseClasses import ItemClassification, Region
from worlds.AutoWorld import World
from worlds.huniepop.Items import HPItem, girl_unlock_table, item_table, panties_item_table, gift_item_table, \
    unique_item_table, token_item_table, girl_gift
from worlds.huniepop.Locations import HPLocation, location_table
from worlds.huniepop.Options import HPOptions
from worlds.huniepop.Rules import set_rules


class HuniePop(World):
    game = "Hunie Pop"
    worldversion = {
        "major":0,
        "minor":5,
        "build":0
    }

    item_name_to_id = item_table
    location_name_to_id = location_table

    options_dataclass = HPOptions
    options: HPOptions

    girllist = (
        "tiffany",
        "aiko",
        "kyanna",
        "audrey",
        "lola",
        "nikki",
        "jessie",
        "beli",
        "kyu",
        "momo",
        "celeste",
        "venus"
    )

    giftsets = {
        "academy":0,
        "toys":0,
        "fitness":0,
        "rave":0,
        "sports":0,
        "artist":0,
        "baking":0,
        "yoga":0,
        "dancer":0,
        "aquarium":0,
        "scuba":0,
        "garden":0,
    }

    startgirls = []
    startgirl = -1
    enabledgirls = []

    trashitems = 0
    shopslots = 0

    def generate_early(self):
        self.startgirls = []
        self.startgirl = -1
        for key in self.giftsets:
            self.giftsets[key] = 0

        self.options.enabled_girls.value.add("kyu")
        tmpgirls = list(self.options.enabled_girls.value.copy())
        #tmpgirls.add("kyu")
        self.enabledgirls = tmpgirls.copy()
        self.startgirls = random.sample(tmpgirls, self.options.number_of_staring_girls.value)
        self.startgirl = self.girllist.index(random.sample(self.startgirls, 1)[0])+1

        print(f"girls unlocked: {self.startgirls}")
        print(f"starting girl: {self.girllist[(self.startgirl-1)]}")

        for g in self.enabledgirls:
            for gift in girl_gift[g]:
                self.giftsets[gift] += 1

        if self.options.number_extra_gifts.value >0:
            for x in self.giftsets:
                if self.giftsets[x] >0:
                    self.giftsets[x] += self.options.number_extra_gifts.value

        totallocations = 0
        totalitems = 0

        #total locations
        if True: #date locations
            totallocations += (4*len(self.enabledgirls))
        if True: #pantie locations
            totallocations += len(self.enabledgirls)
        if True: #gift locations
            totallocations += (24*len(self.enabledgirls))
        if True: #question locations
            totallocations += (12*len(self.enabledgirls))
        if True: #shop locations
            totallocations += self.options.number_shop_items.value


        #total items
        if True: #girl unlock items
            totalitems += len(self.enabledgirls) - len(self.startgirls)
        if True: #pantie items
            totalitems += len(self.enabledgirls)
        if True: #gift items
            for gift in self.giftsets:
                totalitems += (self.giftsets[gift] * 6)
        if True: #unique gift items
            totalitems += (len(self.enabledgirls) * 6)
        if True: #token items
            totalitems += (8*6)

        print(f"totalitems: {totalitems}")
        print(self.giftsets)
        print(f"totallocations: {totallocations}")

        if totallocations != totalitems:
            if totallocations > totalitems:
                self.trashitems = totallocations-totalitems
                self.shopslots = self.options.number_shop_items.value
            else:
                self.shopslots = totalitems - (totallocations - self.options.number_shop_items.value)


    def create_regions(self):
        hub_region = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(hub_region)


        for girl in self.enabledgirls:
            girlregion = Region(f"{girl} Region", self.player, self.multiworld)

            girlregion.add_locations({
                f"{girl} date 1": self.location_name_to_id[f"{girl} date 1"],
                f"{girl} date 2": self.location_name_to_id[f"{girl} date 2"],
                f"{girl} date 3": self.location_name_to_id[f"{girl} date 3"],
                f"{girl} date 4": self.location_name_to_id[f"{girl} date 4"],
                f"received {girl}'s panties": self.location_name_to_id[f"received {girl}'s panties"],
                f"{girl}'s Last Name": self.location_name_to_id[f"{girl}'s Last Name"],
                f"{girl}'s Age": self.location_name_to_id[f"{girl}'s Age"],
                f"{girl}'s Education": self.location_name_to_id[f"{girl}'s Education"],
                f"{girl}'s Height": self.location_name_to_id[f"{girl}'s Height"],
                f"{girl}'s Weight": self.location_name_to_id[f"{girl}'s Weight"],
                f"{girl}'s Occupation": self.location_name_to_id[f"{girl}'s Occupation"],
                f"{girl}'s Cup Size": self.location_name_to_id[f"{girl}'s Cup Size"],
                f"{girl}'s Birthday": self.location_name_to_id[f"{girl}'s Birthday"],
                f"{girl}'s Hobby": self.location_name_to_id[f"{girl}'s Hobby"],
                f"{girl}'s Favourite Color": self.location_name_to_id[f"{girl}'s Favourite Color"],
                f"{girl}'s Favourite Season": self.location_name_to_id[f"{girl}'s Favourite Season"],
                f"{girl}'s Favourite Hangout": self.location_name_to_id[f"{girl}'s Favourite Hangout"],
                f"{girl} gift location 1": self.location_name_to_id[f"{girl} gift location 1"],
                f"{girl} gift location 2": self.location_name_to_id[f"{girl} gift location 2"],
                f"{girl} gift location 3": self.location_name_to_id[f"{girl} gift location 3"],
                f"{girl} gift location 4": self.location_name_to_id[f"{girl} gift location 4"],
                f"{girl} gift location 5": self.location_name_to_id[f"{girl} gift location 5"],
                f"{girl} gift location 6": self.location_name_to_id[f"{girl} gift location 6"],
                f"{girl} gift location 7": self.location_name_to_id[f"{girl} gift location 7"],
                f"{girl} gift location 8": self.location_name_to_id[f"{girl} gift location 8"],
                f"{girl} gift location 9": self.location_name_to_id[f"{girl} gift location 9"],
                f"{girl} gift location 10": self.location_name_to_id[f"{girl} gift location 10"],
                f"{girl} gift location 11": self.location_name_to_id[f"{girl} gift location 11"],
                f"{girl} gift location 12": self.location_name_to_id[f"{girl} gift location 12"],
                f"{girl} gift location 13": self.location_name_to_id[f"{girl} gift location 13"],
                f"{girl} gift location 14": self.location_name_to_id[f"{girl} gift location 14"],
                f"{girl} gift location 15": self.location_name_to_id[f"{girl} gift location 15"],
                f"{girl} gift location 16": self.location_name_to_id[f"{girl} gift location 16"],
                f"{girl} gift location 17": self.location_name_to_id[f"{girl} gift location 17"],
                f"{girl} gift location 18": self.location_name_to_id[f"{girl} gift location 18"],
                f"{girl} gift location 19": self.location_name_to_id[f"{girl} gift location 19"],
                f"{girl} gift location 20": self.location_name_to_id[f"{girl} gift location 20"],
                f"{girl} gift location 21": self.location_name_to_id[f"{girl} gift location 21"],
                f"{girl} gift location 22": self.location_name_to_id[f"{girl} gift location 22"],
                f"{girl} gift location 23": self.location_name_to_id[f"{girl} gift location 23"],
                f"{girl} gift location 24": self.location_name_to_id[f"{girl} gift location 24"]
            }, HPLocation)

            if girl == "kyu":
                girlregion.add_locations({"boss" : self.location_name_to_id["boss"]}, HPLocation)

            hub_region.connect(girlregion, f"hub-{girl}")

        if self.shopslots > 0:
            shop_region = Region("shop", self.player, self.multiworld)
            for i in range(self.shopslots):
                #self.location_name_to_id[f"shop_location: {i+1}"] = 69420506+i
                shop_region.add_locations({f"shop_location: {i+1}" : 42069501+i}, HPLocation)
            hub_region.connect(shop_region, "hub-shop")




    def create_item(self, name: str) -> HPItem:
        if (name ==  "victory"):
            return HPItem(name, ItemClassification.progression, 42069999, self.player)
        if name in girl_unlock_table or name in panties_item_table or name in girl_unlock_table or name in gift_item_table or name in unique_item_table:
            return HPItem(name, ItemClassification.progression, self.item_name_to_id[name], self.player)
        if name in token_item_table:
            return HPItem(name, ItemClassification.useful, self.item_name_to_id[name], self.player)

        return HPItem(name, ItemClassification.filler, self.item_name_to_id[name], self.player)



    def create_items(self):
        for girl in self.enabledgirls:
            if girl in self.startgirls:
                self.multiworld.push_precollected(self.create_item(f"Unlock Girl({girl})"))
            else:
                self.multiworld.itempool.append(self.create_item(f"Unlock Girl({girl})"))
            self.multiworld.itempool.append((self.create_item(f"{girl}'s panties")))

            self.multiworld.itempool.append((self.create_item(f"{girl} unique item 1")))
            self.multiworld.itempool.append((self.create_item(f"{girl} unique item 2")))
            self.multiworld.itempool.append((self.create_item(f"{girl} unique item 3")))
            self.multiworld.itempool.append((self.create_item(f"{girl} unique item 4")))
            self.multiworld.itempool.append((self.create_item(f"{girl} unique item 5")))
            self.multiworld.itempool.append((self.create_item(f"{girl} unique item 6")))

            for gift in girl_gift[girl]:
                self.multiworld.itempool.append((self.create_item(f"{gift} gift item 1")))
                self.multiworld.itempool.append((self.create_item(f"{gift} gift item 2")))
                self.multiworld.itempool.append((self.create_item(f"{gift} gift item 3")))
                self.multiworld.itempool.append((self.create_item(f"{gift} gift item 4")))
                self.multiworld.itempool.append((self.create_item(f"{gift} gift item 5")))
                self.multiworld.itempool.append((self.create_item(f"{gift} gift item 6")))

        for x in range(self.options.number_extra_gifts.value):
            if "tiffany" in self.enabledgirls or "nikki" in self.enabledgirls or "celeste" in self.enabledgirls:
                self.multiworld.itempool.append((self.create_item("academy gift item 1")))
                self.multiworld.itempool.append((self.create_item("academy gift item 2")))
                self.multiworld.itempool.append((self.create_item("academy gift item 3")))
                self.multiworld.itempool.append((self.create_item("academy gift item 4")))
                self.multiworld.itempool.append((self.create_item("academy gift item 5")))
                self.multiworld.itempool.append((self.create_item("academy gift item 6")))
            if "aiko" in self.enabledgirls or "audrey" in self.enabledgirls or "momo" in self.enabledgirls:
                self.multiworld.itempool.append((self.create_item("toys gift item 1")))
                self.multiworld.itempool.append((self.create_item("toys gift item 2")))
                self.multiworld.itempool.append((self.create_item("toys gift item 3")))
                self.multiworld.itempool.append((self.create_item("toys gift item 4")))
                self.multiworld.itempool.append((self.create_item("toys gift item 5")))
                self.multiworld.itempool.append((self.create_item("toys gift item 6")))
            if "kyanna" in self.enabledgirls or "jessie" in self.enabledgirls or "celeste" in self.enabledgirls:
                self.multiworld.itempool.append((self.create_item("fitness gift item 1")))
                self.multiworld.itempool.append((self.create_item("fitness gift item 2")))
                self.multiworld.itempool.append((self.create_item("fitness gift item 3")))
                self.multiworld.itempool.append((self.create_item("fitness gift item 4")))
                self.multiworld.itempool.append((self.create_item("fitness gift item 5")))
                self.multiworld.itempool.append((self.create_item("fitness gift item 6")))
            if "tiffany" in self.enabledgirls or "audrey" in self.enabledgirls or "kyu" in self.enabledgirls:
                self.multiworld.itempool.append((self.create_item("rave gift item 1")))
                self.multiworld.itempool.append((self.create_item("rave gift item 2")))
                self.multiworld.itempool.append((self.create_item("rave gift item 3")))
                self.multiworld.itempool.append((self.create_item("rave gift item 4")))
                self.multiworld.itempool.append((self.create_item("rave gift item 5")))
                self.multiworld.itempool.append((self.create_item("rave gift item 6")))
            if "lola" in self.enabledgirls or "beli" in self.enabledgirls or "momo" in self.enabledgirls:
                self.multiworld.itempool.append((self.create_item("sports gift item 1")))
                self.multiworld.itempool.append((self.create_item("sports gift item 2")))
                self.multiworld.itempool.append((self.create_item("sports gift item 3")))
                self.multiworld.itempool.append((self.create_item("sports gift item 4")))
                self.multiworld.itempool.append((self.create_item("sports gift item 5")))
                self.multiworld.itempool.append((self.create_item("sports gift item 6")))
            if "aiko" in self.enabledgirls or "nikki" in self.enabledgirls or "kyu" in self.enabledgirls:
                self.multiworld.itempool.append((self.create_item("artist gift item 1")))
                self.multiworld.itempool.append((self.create_item("artist gift item 2")))
                self.multiworld.itempool.append((self.create_item("artist gift item 3")))
                self.multiworld.itempool.append((self.create_item("artist gift item 4")))
                self.multiworld.itempool.append((self.create_item("artist gift item 5")))
                self.multiworld.itempool.append((self.create_item("artist gift item 6")))
            if "lola" in self.enabledgirls or "jessie" in self.enabledgirls or "venus" in self.enabledgirls:
                self.multiworld.itempool.append((self.create_item("baking gift item 1")))
                self.multiworld.itempool.append((self.create_item("baking gift item 2")))
                self.multiworld.itempool.append((self.create_item("baking gift item 3")))
                self.multiworld.itempool.append((self.create_item("baking gift item 4")))
                self.multiworld.itempool.append((self.create_item("baking gift item 5")))
                self.multiworld.itempool.append((self.create_item("baking gift item 6")))
            if "kyanna" in self.enabledgirls or "beli" in self.enabledgirls or "venus" in self.enabledgirls:
                self.multiworld.itempool.append((self.create_item("yoga gift item 1")))
                self.multiworld.itempool.append((self.create_item("yoga gift item 2")))
                self.multiworld.itempool.append((self.create_item("yoga gift item 3")))
                self.multiworld.itempool.append((self.create_item("yoga gift item 4")))
                self.multiworld.itempool.append((self.create_item("yoga gift item 5")))
                self.multiworld.itempool.append((self.create_item("yoga gift item 6")))
            if "kyanna" in self.enabledgirls or "jessie" in self.enabledgirls or "kyu" in self.enabledgirls:
                self.multiworld.itempool.append((self.create_item("dancer gift item 1")))
                self.multiworld.itempool.append((self.create_item("dancer gift item 2")))
                self.multiworld.itempool.append((self.create_item("dancer gift item 3")))
                self.multiworld.itempool.append((self.create_item("dancer gift item 4")))
                self.multiworld.itempool.append((self.create_item("dancer gift item 5")))
                self.multiworld.itempool.append((self.create_item("dancer gift item 6")))
            if "audrey" in self.enabledgirls or "nikki" in self.enabledgirls or "momo" in self.enabledgirls:
                self.multiworld.itempool.append((self.create_item("aquarium gift item 1")))
                self.multiworld.itempool.append((self.create_item("aquarium gift item 2")))
                self.multiworld.itempool.append((self.create_item("aquarium gift item 3")))
                self.multiworld.itempool.append((self.create_item("aquarium gift item 4")))
                self.multiworld.itempool.append((self.create_item("aquarium gift item 5")))
                self.multiworld.itempool.append((self.create_item("aquarium gift item 6")))
            if "tiffany" in self.enabledgirls or "lola" in self.enabledgirls or "celeste" in self.enabledgirls:
                self.multiworld.itempool.append((self.create_item("scuba gift item 1")))
                self.multiworld.itempool.append((self.create_item("scuba gift item 2")))
                self.multiworld.itempool.append((self.create_item("scuba gift item 3")))
                self.multiworld.itempool.append((self.create_item("scuba gift item 4")))
                self.multiworld.itempool.append((self.create_item("scuba gift item 5")))
                self.multiworld.itempool.append((self.create_item("scuba gift item 6")))
            if "aiko" in self.enabledgirls or "beli" in self.enabledgirls or "venus" in self.enabledgirls:
                self.multiworld.itempool.append((self.create_item("garden gift item 1")))
                self.multiworld.itempool.append((self.create_item("garden gift item 2")))
                self.multiworld.itempool.append((self.create_item("garden gift item 3")))
                self.multiworld.itempool.append((self.create_item("garden gift item 4")))
                self.multiworld.itempool.append((self.create_item("garden gift item 5")))
                self.multiworld.itempool.append((self.create_item("garden gift item 6")))

        for t in token_item_table:
            self.multiworld.itempool.append(self.create_item(t))


        if self.trashitems > 0:
            for i in range(self.trashitems):
                self.multiworld.itempool.append(self.create_item("nothing"))


    def set_rules(self):
        self.multiworld.get_location("boss", self.player).place_locked_item(self.create_item("victory"))
        self.multiworld.completion_condition[self.player] = lambda state: state.has("victory", self.player)

        set_rules(self.multiworld, self.player, self.enabledgirls, self.startgirls)



    def fill_slot_data(self) -> dict:
        returndict = {
            "start_girl": self.startgirl,
            "number_of_shop_items": self.shopslots,
            "shop_item_cost": self.options.shop_item_cost.value,
            "puzzle_moves": self.options.puzzle_moves.value,
            "puzzle_affection_base": self.options.puzzle_affection_base.value,
            "puzzle_affection_add": self.options.puzzle_affection_add.value,
            "world_version": self.worldversion
        }

        if "tiffany" in self.options.enabled_girls:
            returndict["tiffany_enabled"] = 1
        else:
            returndict["tiffany_enabled"] = 0

        if "aiko" in self.options.enabled_girls:
            returndict["aiko_enabled"] = 1
        else:
            returndict["aiko_enabled"] = 0

        if "kyanna" in self.options.enabled_girls:
            returndict["kyanna_enabled"] = 1
        else:
            returndict["kyanna_enabled"] = 0

        if "audrey" in self.options.enabled_girls:
            returndict["audrey_enabled"] = 1
        else:
            returndict["audrey_enabled"] = 0

        if "lola" in self.options.enabled_girls:
            returndict["lola_enabled"] = 1
        else:
            returndict["lola_enabled"] = 0

        if "nikki" in self.options.enabled_girls:
            returndict["nikki_enabled"] = 1
        else:
            returndict["nikki_enabled"] = 0

        if "jessie" in self.options.enabled_girls:
            returndict["jessie_enabled"] = 1
        else:
            returndict["jessie_enabled"] = 0

        if "beli" in self.options.enabled_girls:
            returndict["beli_enabled"] = 1
        else:
            returndict["beli_enabled"] = 0

        #if "kyu" in self.options.enabled_girls:
        returndict["kyu_enabled"] = 1
        #else:
        #    returndict["kyu_enabled"] = 0

        if "momo" in self.options.enabled_girls:
            returndict["momo_enabled"] = 1
        else:
            returndict["momo_enabled"] = 0

        if "celeste" in self.options.enabled_girls:
            returndict["celeste_enabled"] = 1
        else:
            returndict["celeste_enabled"] = 0

        if "venus" in self.options.enabled_girls:
            returndict["venus_enabled"] = 1
        else:
            returndict["venus_enabled"] = 0

        return returndict