from typing import Callable, Dict, NamedTuple, Optional, TYPE_CHECKING

from BaseClasses import Location

if TYPE_CHECKING:
    from . import PokePinballWorld


pokemon_names = [
    #"None",
    "Bulbasaur",
    "Ivysaur",
    "Venusaur",
    "Charmander",
    "Charmeleon",
    "Charizard",
    "Squirtle",
    "Wartortle",
    "Blastoise",
    "Caterpie",
    "Metapod",
    "Butterfree",
    "Weedle",
    "Kakuna",
    "Beedrill",
    "Pidgey",
    "Pidgeotto",
    "Pidgeot",
    "Rattata",
    "Raticate",
    "Spearow",
    "Fearow",
    "Ekans",
    "Arbok",
    "Pikachu",
    "Raichu",
    "Sandshrew",
    "Sandslash",
    "Nidoran Female",
    "Nidorina",
    "Nidoqueen",
    "Nidoran Male",
    "Nidorino",
    "Nidoking",
    "Clefairy",
    "Clefable",
    "Vulpix",
    "Ninetales",
    "Jigglypuff",
    "Wigglytuff",
    "Zubat",
    "Golbat",
    "Oddish",
    "Gloom",
    "Vileplume",
    "Paras",
    "Parasect",
    "Venonat",
    "Venomoth",
    "Diglett",
    "Dugtrio",
    "Meowth",
    "Persian",
    "Psyduck",
    "Golduck",
    "Mankey",
    "Primeape",
    "Growlithe",
    "Arcanine",
    "Poliwag",
    "Poliwhirl",
    "Poliwrath",
    "Abra",
    "Kadabra",
    "Alakazam",
    "Machop",
    "Machoke",
    "Machamp",
    "Bellsprout",
    "Weepinbell",
    "Victreebel",
    "Tentacool",
    "Tentacruel",
    "Geodude",
    "Graveler",
    "Golem",
    "Ponyta",
    "Rapidash",
    "Slowpoke",
    "Slowbro",
    "Magnemite",
    "Magneton",
    "Farfetchd",
    "Doduo",
    "Dodrio",
    "Seel",
    "Dewgong",
    "Grimer",
    "Muk",
    "Shellder",
    "Cloyster",
    "Gastly",
    "Haunter",
    "Gengar",
    "Onix",
    "Drowzee",
    "Hypno",
    "Krabby",
    "Kingler",
    "Voltorb",
    "Electrode",
    "Exeggcute",
    "Exeggutor",
    "Cubone",
    "Marowak",
    "Hitmonlee",
    "Hitmonchan",
    "Lickitung",
    "Koffing",
    "Weezing",
    "Rhyhorn",
    "Rhydon",
    "Chansey",
    "Tangela",
    "Kangaskhan",
    "Horsea",
    "Seadra",
    "Goldeen",
    "Seaking",
    "Staryu",
    "Starmie",
    "Mr Mime",
    "Scyther",
    "Jynx",
    "Electabuzz",
    "Magmar",
    "Pinsir",
    "Tauros",
    "Magikarp",
    "Gyarados",
    "Lapras",
    "Ditto",
    "Eevee",
    "Vaporeon",
    "Jolteon",
    "Flareon",
    "Porygon",
    "Omanyte",
    "Omastar",
    "Kabuto",
    "Kabutops",
    "Aerodactyl",
    "Snorlax",
    "Articuno",
    "Zapdos",
    "Moltres",
    "Dratini",
    "Dragonair",
    "Dragonite",
    "Mewtwo",
    "Mew",
]

class PokePinballLocation(Location):
    game = "Pokemon Pinball"

class PokePinballLocationData(NamedTuple):
    region: str
    address: Optional[int] = None
    can_create: Callable[["PokePinballWorld"], bool] = lambda world: True
    locked_item: Optional[str] = None

location_data_table: Dict[str, PokePinballLocation] = {
    "Bulbasaur": PokePinballLocationData(
    region="Bulbasaur",
    address=0x1C2001,
    ),
    "Ivysaur": PokePinballLocationData(
    region="Bulbasaur",
    address=0x1C2002,
    ),
    "Venusaur": PokePinballLocationData(
    region="Bulbasaur",
    address=0x1C2003,
    ),

    "Charmander": PokePinballLocationData(
    region="Charmander",
    address=0x1C2004,
    ),
    "Charmeleon": PokePinballLocationData(
    region="Charmander",
    address=0x1C2005,
    ),
    "Charizard": PokePinballLocationData(
    region="Charmander",
    address=0x1C2006,
    ),

    "Squirtle": PokePinballLocationData(
    region="Squirtle",
    address=0x1C2007,
    ),
    "Wartortle": PokePinballLocationData(
    region="Squirtle",
    address=0x1C2008,
    ),
    "Blastoise": PokePinballLocationData(
    region="Squirtle",
    address=0x1C2009,
    ),

    "Caterpie": PokePinballLocationData(
    region="Caterpie",
    address=0x1C200a,
    ),
    "Metapod": PokePinballLocationData(
    region="Caterpie",
    address=0x1C200b,
    ),
    "Butterfree": PokePinballLocationData(
    region="Caterpie",
    address=0x1C200c,
    ),

    "Weedle": PokePinballLocationData(
    region="Weedle",
    address=0x1C200d,
    ),
    "Kakuna": PokePinballLocationData(
    region="Weedle",
    address=0x1C200e,
    ),
    "Beedrill": PokePinballLocationData(
    region="Weedle",
    address=0x1C200f,
    ),

    "Pidgey": PokePinballLocationData(
    region="Pidgey",
    address=0x1C2010,
    ),
    "Pidgeotto": PokePinballLocationData(
    region="Pidgey",
    address=0x1C2011,
    ),
    "Pidgeot": PokePinballLocationData(
    region="Pidgey",
    address=0x1C2012,
    ),

    "Rattata": PokePinballLocationData(
    region="Rattata",
    address=0x1C2013,
    ),
    "Raticate": PokePinballLocationData(
    region="Rattata",
    address=0x1C2014,
    ),

    "Spearow": PokePinballLocationData(
    region="Spearow",
    address=0x1C2015,
    ),
    "Fearow": PokePinballLocationData(
    region="Spearow",
    address=0x1C2016,
    ),

    "Ekans": PokePinballLocationData(
    region="Ekans",
    address=0x1C2017,
    ),
    "Arbok": PokePinballLocationData(
    region="Ekans",
    address=0x1C2018,
    ),

    "Pikachu": PokePinballLocationData(
    region="Pikachu",
    address=0x1C2019,
    ),
    "Raichu": PokePinballLocationData(
    region="Pikachu",
    address=0x1C201a,
    ),

    "Sandshrew": PokePinballLocationData(
    region="Sandshrew",
    address=0x1C201b,
    ),
    "Sandslash": PokePinballLocationData(
    region="Sandshrew",
    address=0x1C201c,
    ),

    "Nidoran Female": PokePinballLocationData(
    region="Nidoran Female",
    address=0x1C201d,
    ),
    "Nidorina": PokePinballLocationData(
    region="Nidoran Female",
    address=0x1C201e,
    ),
    "Nidoqueen": PokePinballLocationData(
    region="Nidoran Female",
    address=0x1C201f,
    ),

    "Nidoran Male": PokePinballLocationData(
    region="Nidoran Male",
    address=0x1C2020,
    ),
    "Nidorino": PokePinballLocationData(
    region="Nidoran Male",
    address=0x1C2021,
    ),
    "Nidoking": PokePinballLocationData(
    region="Nidoran Male",
    address=0x1C2022,
    ),

    "Clefairy": PokePinballLocationData(
    region="Clefairy",
    address=0x1C2023,
    ),
    "Clefable": PokePinballLocationData(
    region="Clefairy",
    address=0x1C2024,
    ),

    "Vulpix": PokePinballLocationData(
    region="Vulpix",
    address=0x1C2025,
    ),
    "Ninetales": PokePinballLocationData(
    region="Vulpix",
    address=0x1C2026,
    ),

    "Jigglypuff": PokePinballLocationData(
    region="Jigglypuff",
    address=0x1C2027,
    ),
    "Wigglytuff": PokePinballLocationData(
    region="Jigglypuff",
    address=0x1C2028,
    ),

    "Zubat": PokePinballLocationData(
    region="Zubat",
    address=0x1C2029,
    ),
    "Golbat": PokePinballLocationData(
    region="Zubat",
    address=0x1C202a,
    ),

    "Oddish": PokePinballLocationData(
    region="Oddish",
    address=0x1C202b,
    ),
    "Gloom": PokePinballLocationData(
    region="Oddish",
    address=0x1C202c,
    ),
    "Vileplume": PokePinballLocationData(
    region="Oddish",
    address=0x1C202d,
    ),

    "Paras": PokePinballLocationData(
    region="Paras",
    address=0x1C202e,
    ),
    "Parasect": PokePinballLocationData(
    region="Paras",
    address=0x1C202f,
    ),

    "Venonat": PokePinballLocationData(
    region="Venonat",
    address=0x1C2030,
    ),
    "Venomoth": PokePinballLocationData(
    region="Venonat",
    address=0x1C2031,
    ),

    "Diglett": PokePinballLocationData(
    region="Diglett",
    address=0x1C2032,
    ),
    "Dugtrio": PokePinballLocationData(
    region="Diglett",
    address=0x1C2033,
    ),

    "Meowth": PokePinballLocationData(
    region="Meowth",
    address=0x1C2034,
    ),
    "Persian": PokePinballLocationData(
    region="Meowth",
    address=0x1C2035,
    ),

    "Psyduck": PokePinballLocationData(
    region="Psyduck",
    address=0x1C2036,
    ),
    "Golduck": PokePinballLocationData(
    region="Psyduck",
    address=0x1C2037,
    ),

    "Mankey": PokePinballLocationData(
    region="Mankey",
    address=0x1C2038,
    ),
    "Primeape": PokePinballLocationData(
    region="Mankey",
    address=0x1C2039,
    ),

    "Growlithe": PokePinballLocationData(
    region="Growlithe",
    address=0x1C203a,
    ),
    "Arcanine": PokePinballLocationData(
    region="Growlithe",
    address=0x1C203b,
    ),
    
    "Poliwag": PokePinballLocationData(
    region="Poliwag",
    address=0x1C203c,
    ),
    "Poliwhirl": PokePinballLocationData(
    region="Poliwag",
    address=0x1C203d,
    ),
    "Poliwrath": PokePinballLocationData(
    region="Poliwag",
    address=0x1C203e,
    ),

    "Abra": PokePinballLocationData(
    region="Abra",
    address=0x1C203f,
    ),
    "Kadabra": PokePinballLocationData(
    region="Abra",
    address=0x1C2040,
    ),
    "Alakazam": PokePinballLocationData(
    region="Abra",
    address=0x1C2041,
    ),

    "Machop": PokePinballLocationData(
    region="Machop",
    address=0x1C2042,
    ),
    "Machoke": PokePinballLocationData(
    region="Machop",
    address=0x1C2043,
    ),
    "Machamp": PokePinballLocationData(
    region="Machop",
    address=0x1C2044,
    ),

    "Bellsprout": PokePinballLocationData(
    region="Bellsprout",
    address=0x1C2045,
    ),
    "Weepinbell": PokePinballLocationData(
    region="Bellsprout",
    address=0x1C2046,
    ),
    "Victreebel": PokePinballLocationData(
    region="Bellsprout",
    address=0x1C2047,
    ),

    "Tentacool": PokePinballLocationData(
    region="Tentacool",
    address=0x1C2048,
    ),
    "Tentacruel": PokePinballLocationData(
    region="Tentacool",
    address=0x1C2049,
    ),

    "Geodude": PokePinballLocationData(
    region="Geodude",
    address=0x1C204a,
    ),
    "Graveler": PokePinballLocationData(
    region="Geodude",
    address=0x1C204b,
    ),
    "Golem": PokePinballLocationData(
    region="Geodude",
    address=0x1C204c,
    ),

    "Ponyta": PokePinballLocationData(
    region="Ponyta",
    address=0x1C204d,
    ),
    "Rapidash": PokePinballLocationData(
    region="Ponyta",
    address=0x1C204e,
    ),

    "Slowpoke": PokePinballLocationData(
    region="Slowpoke",
    address=0x1C204f,
    ),
    "Slowbro": PokePinballLocationData(
    region="Slowpoke",
    address=0x1C2050,
    ),

    "Magnemite": PokePinballLocationData(
    region="Magnemite",
    address=0x1C2051,
    ),
    "Magneton": PokePinballLocationData(
    region="Magnemite",
    address=0x1C2052,
    ),

    "Farfetchd": PokePinballLocationData(
    region="Farfetchd",
    address=0x1C2053,
    ),

    "Doduo": PokePinballLocationData(
    region="Doduo",
    address=0x1C2054,
    ),
    "Dodrio": PokePinballLocationData(
    region="Doduo",
    address=0x1C2055,
    ),

    "Seel": PokePinballLocationData(
    region="Seel",
    address=0x1C2056,
    ),
    "Dewgong": PokePinballLocationData(
    region="Seel",
    address=0x1C2057,
    ),

    "Grimer": PokePinballLocationData(
    region="Grimer",
    address=0x1C2058,
    ),
    "Muk": PokePinballLocationData(
    region="Grimer",
    address=0x1C2059,
    ),

    "Shellder": PokePinballLocationData(
    region="Shellder",
    address=0x1C205a,
    ),
    "Cloyster": PokePinballLocationData(
    region="Shellder",
    address=0x1C205b,
    ),

    "Gastly": PokePinballLocationData(
    region="Gastly",
    address=0x1C205c,
    ),
    "Haunter": PokePinballLocationData(
    region="Gastly",
    address=0x1C205d,
    ),
    "Gengar": PokePinballLocationData(
    region="Gastly",
    address=0x1C205e,
    ),

    "Onix": PokePinballLocationData(
    region="Onix",
    address=0x1C205f,
    ),

    "Drowzee": PokePinballLocationData(
    region="Drowzee",
    address=0x1C2060,
    ),
    "Hypno": PokePinballLocationData(
    region="Drowzee",
    address=0x1C2061,
    ),

    "Krabby": PokePinballLocationData(
    region="Krabby",
    address=0x1C2062,
    ),
    "Kingler": PokePinballLocationData(
    region="Krabby",
    address=0x1C2063,
    ),

    "Voltorb": PokePinballLocationData(
    region="Voltorb",
    address=0x1C2064,
    ),
    "Electrode": PokePinballLocationData(
    region="Voltorb",
    address=0x1C2065,
    ),

    "Exeggcute": PokePinballLocationData(
    region="Exeggcute",
    address=0x1C2066,
    ),
    "Exeggutor": PokePinballLocationData(
    region="Exeggcute",
    address=0x1C2067,
    ),

    "Cubone": PokePinballLocationData(
    region="Cubone",
    address=0x1C2068,
    ),
    "Marowak": PokePinballLocationData(
    region="Cubone",
    address=0x1C2069,
    ),

    "Hitmonlee": PokePinballLocationData(
    region="Hitmonlee",
    address=0x1C206a,
    ),

    "Hitmonchan": PokePinballLocationData(
    region="Hitmonchan",
    address=0x1C206b,
    ),

    "Lickitung": PokePinballLocationData(
    region="Lickitung",
    address=0x1C206c,
    ),

    "Koffing": PokePinballLocationData(
    region="Koffing",
    address=0x1C206d,
    ),
    "Weezing": PokePinballLocationData(
    region="Koffing",
    address=0x1C206e,
    ),

    "Rhyhorn": PokePinballLocationData(
    region="Rhyhorn",
    address=0x1C206f,
    ),
    "Rhydon": PokePinballLocationData(
    region="Rhyhorn",
    address=0x1C2070,
    ),

    "Chansey": PokePinballLocationData(
    region="Chansey",
    address=0x1C2071,
    ),

    "Tangela": PokePinballLocationData(
    region="Tangela",
    address=0x1C2072,
    ),

    "Kangaskhan": PokePinballLocationData(
    region="Kangaskhan",
    address=0x1C2073,
    ),

    "Horsea": PokePinballLocationData(
    region="Horsea",
    address=0x1C2074,
    ),
    "Seadra": PokePinballLocationData(
    region="Horsea",
    address=0x1C2075,
    ),

    "Goldeen": PokePinballLocationData(
    region="Goldeen",
    address=0x1C2076,
    ),
    "Seaking": PokePinballLocationData(
    region="Goldeen",
    address=0x1C2077,
    ),

    "Staryu": PokePinballLocationData(
    region="Staryu",
    address=0x1C2078,
    ),
    "Starmie": PokePinballLocationData(
    region="Staryu",
    address=0x1C2079,
    ),

    "Mr Mime": PokePinballLocationData(
    region="Mr Mime",
    address=0x1C207a,
    ),

    "Scyther": PokePinballLocationData(
    region="Scyther",
    address=0x1C207b,
    ),

    "Jynx": PokePinballLocationData(
    region="Jynx",
    address=0x1C207c,
    ),

    "Electabuzz": PokePinballLocationData(
    region="Electabuzz",
    address=0x1C207d,
    ),
    
    "Magmar": PokePinballLocationData(
    region="Magmar",
    address=0x1C207e,
    ),

    "Pinsir": PokePinballLocationData(
    region="Pinsir",
    address=0x1C207f,
    ),

    "Tauros": PokePinballLocationData(
    region="Tauros",
    address=0x1C2080,
    ),

    "Magikarp": PokePinballLocationData(
    region="Magikarp",
    address=0x1C2081,
    ),
    "Gyarados": PokePinballLocationData(
    region="Magikarp",
    address=0x1C2082,
    ),

    "Lapras": PokePinballLocationData(
    region="Lapras",
    address=0x1C2083,
    ),

    "Ditto": PokePinballLocationData(
    region="Ditto",
    address=0x1C2084,
    ),

    "Eevee": PokePinballLocationData(
    region="Eevee",
    address=0x1C2085,
    ),
    "Vaporeon": PokePinballLocationData(
    region="Eevee",
    address=0x1C2086,
    ),
    "Jolteon": PokePinballLocationData(
    region="Eevee",
    address=0x1C2087,
    ),
    "Flareon": PokePinballLocationData(
    region="Eevee",
    address=0x1C2088,
    ),

    "Porygon": PokePinballLocationData(
    region="Porygon",
    address=0x1C2089,
    ),

    "Omanyte": PokePinballLocationData(
    region="Omanyte",
    address=0x1C208a,
    ),
    "Omastar": PokePinballLocationData(
    region="Omanyte",
    address=0x1C208b,
    ),

    "Kabuto": PokePinballLocationData(
    region="Kabuto",
    address=0x1C208c,
    ),
    "Kabutops": PokePinballLocationData(
    region="Kabuto",
    address=0x1C208d,
    ),

    "Aerodactyl": PokePinballLocationData(
    region="Aerodactyl",
    address=0x1C208e,
    ),

    "Snorlax": PokePinballLocationData(
    region="Snorlax",
    address=0x1C208f,
    ),

    "Articuno": PokePinballLocationData(
    region="Articuno",
    address=0x1C2090,
    ),

    "Zapdos": PokePinballLocationData(
    region="Zapdos",
    address=0x1C2091,
    ),

    "Moltres": PokePinballLocationData(
    region="Moltres",
    address=0x1C2092,
    ),

    "Dratini": PokePinballLocationData(
    region="Dratini",
    address=0x1C2093,
    ),
    "Dragonair": PokePinballLocationData(
    region="Dratini",
    address=0x1C2094,
    ),
    "Dragonite": PokePinballLocationData(
    region="Dratini",
    address=0x1C2095,
    ),

    "Mewtwo": PokePinballLocationData(
    region="Mewtwo",
    address=0x1C2096,
    ),

    "Mew": PokePinballLocationData(
    region="Mew",
    address=0x1C2097,
    ),

    "Red Table Movement": PokePinballLocationData(
    region="Red Table",
    address=0x1C2098,
    ),
    "Blue Table Movement": PokePinballLocationData(
    region="Blue Table",
    address=0x1C2099,
    ),

    "Diglett Bonus": PokePinballLocationData(
    region="Blue Table",
    address=0x1C209A,
    ),
    "Meowth Bonus": PokePinballLocationData(
    region="Blue Table",
    address=0x1C209B,
    ),
    "Gastly Bonus": PokePinballLocationData(
    region="Red Table",
    address=0x1C209C,
    ),
    "Seel Bonus": PokePinballLocationData(
    region="Blue Table",
    address=0x1C209D,
    ),
    "Mewtwo Bonus": PokePinballLocationData(
    region="Menu",
    address=0x1C209E,
    ),

    "20,000,000 Points": PokePinballLocationData(
    region= "Menu",
    address=0x1C20A0,
    ),
    "50,000,000 Points": PokePinballLocationData(
    region= "Menu",
    address=0x1C20A1,
    ),
    "100,000,000 Points": PokePinballLocationData(
    region= "Menu",
    address=0x1C20A2,
    ),
    "250,000,000 Points": PokePinballLocationData(
    region= "Menu",
    address=0x1C20A3,
    ),
    "500,000,000 Points": PokePinballLocationData(
    region= "Menu",
    address=0x1C20A4,
    ),

    #"Pokedex Completed": PokePinballLocationData(
    #region="Menu",
    #address=0x1C209F,
    #locked_item="Victory"
    #),

}

location_table = {name: data.address for name, data in location_data_table.items() if data.address is not None}
locked_locations = {name: data for name, data in location_data_table.items() if data.locked_item}