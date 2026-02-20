from typing import Callable, TYPE_CHECKING

from BaseClasses import CollectionState

if TYPE_CHECKING:
    from . import PokePinballWorld


def getdexcount(state, player):
    from .Locations import location_table
    dex_count = 0
    for name, data in location_table.items():
        if data.address < 0x1C20A0:
            if state.has(name, player):
                dex_count +=1
    return dex_count

def get_region_rules(player, options):
    return {
        "Red Table -> Viridian Forest":
            lambda state: state.has("Viridian Forest", player),
        "Blue Table -> Viridian Forest":
            lambda state: state.has("Viridian Forest", player),
        "Red Table -> Pewter City":
            lambda state: state.has("Pewter City", player),
        "Blue Table -> Mt Moon":
            lambda state: state.has("Mt Moon", player),
        "Red Table -> Cerulean City":
            lambda state: state.has("Cerulean City", player),
        "Blue Table -> Cerulean City":
            lambda state: state.has("Cerulean City", player),
        "Red Table -> Vermilion City Seaside":
            lambda state: state.has("Vermilion City Seaside", player),
        "Blue Table -> Vermilion City Streets":
            lambda state: state.has("Vermilion City Streets", player),
        "Red Table -> Rock Mountain":
            lambda state: state.has("Rock Mountain", player),
        "Blue Table -> Rock Mountain":
            lambda state: state.has("Rock Mountain", player),
        "Red Table -> Lavender Town":
            lambda state: state.has("Lavender Town", player),
        "Blue Table -> Celadon City":
            lambda state: state.has("Celadon City", player),
        "Red Table -> Cycling Road":
            lambda state: state.has("Cycling Road", player),
        "Red Table -> Safari Zone":
            lambda state: state.has("Safari Zone", player),
        "Blue Table -> Safari Zone":
            lambda state: state.has("Safari Zone", player),
        "Blue Table -> Fuchsia City":
            lambda state: state.has("Fuchsia City", player),
        "Blue Table -> Saffron City":
            lambda state: state.has("Saffron City", player),
        "Red Table -> Seafoam Islands":
            lambda state: state.has("Seafoam Islands", player),
        "Red Table -> Cinnabar Island":
            lambda state: state.has("Cinnabar Island", player),
        "Blue Table -> Cinnabar Island":
            lambda state: state.has("Cinnabar Island", player),
        "Red Table -> Indigo Plateau":
            lambda state: state.has("Indigo Plateau", player),
        "Blue Table -> Indigo Plateau":
            lambda state: state.has("Indigo Plateau", player),
            

        "Caterpie -> Viridian Forest":
            lambda state: state.has("Viridian Forest", player),
        "Weedle -> Viridian Forest":
            lambda state: state.has("Viridian Forest", player),
        "Pidgey -> Viridian Forest":
            lambda state: state.has("Viridian Forest", player),
        "Rattata -> Viridian Forest":
            lambda state: state.has("Viridian Forest", player),
        "Pikachu -> Viridian Forest":
            lambda state: state.has("Viridian Forest", player),
        
        "Pidgey -> Pewter City":
            lambda state: state.has("Pewter City", player),
        "Spearow -> Pewter City":
            lambda state: state.has("Pewter City", player),
        "Ekans -> Pewter City":
            lambda state: state.has("Pewter City", player),
        "Jigglypuff -> Pewter City":
            lambda state: state.has("Pewter City", player),
        "Magikarp -> Pewter City":
            lambda state: state.has("Pewter City", player),
        
        "Rattata -> Mt Moon":
            lambda state: state.has("Mt Moon", player),
        "Spearow -> Mt Moon":
            lambda state: state.has("Mt Moon", player),
        "Ekans -> Mt Moon":
            lambda state: state.has("Mt Moon", player),
        "Sandshrew -> Mt Moon":
            lambda state: state.has("Mt Moon", player),
        "Clefairy -> Mt Moon":
            lambda state: state.has("Mt Moon", player),
        "Zubat -> Mt Moon":
            lambda state: state.has("Mt Moon", player),
        "Paras -> Mt Moon":
            lambda state: state.has("Mt Moon", player),
        "Psyduck -> Mt Moon":
            lambda state: state.has("Mt Moon", player),
        "Geodude -> Mt Moon":
            lambda state: state.has("Mt Moon", player), 
        "Krabby -> Mt Moon":
            lambda state: state.has("Mt Moon", player),
        "Goldeen -> Mt Moon":
            lambda state: state.has("Mt Moon", player),
        
        "Caterpie -> Cerulean City":
            lambda state: state.has("Cerulean City", player),
        "Weedle -> Cerulean City":
            lambda state: state.has("Cerulean City", player),
        "Nidoran Male -> Cerulean City":
            lambda state: state.has("Cerulean City", player),
        "Oddish -> Cerulean City":
            lambda state: state.has("Cerulean City", player),
        "Psyduck -> Cerulean City":
            lambda state: state.has("Cerulean City", player),
        "Mankey -> Cerulean City":
            lambda state: state.has("Cerulean City", player),
        "Abra -> Cerulean City":
            lambda state: state.has("Cerulean City", player),
        "Krabby -> Cerulean City":
            lambda state: state.has("Cerulean City", player),
        "Goldeen -> Cerulean City":
            lambda state: state.has("Cerulean City", player),
        "Jynx -> Cerulean City":
            lambda state: state.has("Cerulean City", player),
        "Meowth -> Cerulean City":
            lambda state: state.has("Cerulean City", player),
        "Bellsprout -> Cerulean City":
            lambda state: state.has("Cerulean City", player),
       
        "Pidgey -> Vermilion City Seaside":
            lambda state: state.has("Vermilion City Seaside", player),
        "Spearow -> Vermilion City Seaside":
            lambda state: state.has("Vermilion City Seaside", player),
        "Ekans -> Vermilion City Seaside":
            lambda state: state.has("Vermilion City Seaside", player),
        "Oddish -> Vermilion City Seaside":
            lambda state: state.has("Vermilion City Seaside", player),
        "Mankey -> Vermilion City Seaside":
            lambda state: state.has("Vermilion City Seaside", player),
        "Farfetchd -> Vermilion City Seaside":
            lambda state: state.has("Vermilion City Seaside", player),
        "Shellder -> Vermilion City Seaside":
            lambda state: state.has("Vermilion City Seaside", player),
        "Drowzee -> Vermilion City Seaside":
            lambda state: state.has("Vermilion City Seaside", player),
        "Krabby -> Vermilion City Seaside":
            lambda state: state.has("Vermilion City Seaside", player),
        
        "Pidgey -> Vermilion City Streets":
            lambda state: state.has("Vermilion City Streets", player),
        "Spearow -> Vermilion City Streets":
            lambda state: state.has("Vermilion City Streets", player),
        "Sandshrew -> Vermilion City Streets":
            lambda state: state.has("Vermilion City Streets", player),
        "Meowth -> Vermilion City Streets":
            lambda state: state.has("Vermilion City Streets", player),
        "Bellsprout -> Vermilion City Streets":
            lambda state: state.has("Vermilion City Streets", player),
        "Farfetchd -> Vermilion City Streets":
            lambda state: state.has("Vermilion City Streets", player),
        "Shellder -> Vermilion City Streets":
            lambda state: state.has("Vermilion City Streets", player),
        "Drowzee -> Vermilion City Streets":
            lambda state: state.has("Vermilion City Streets", player),
        "Krabby -> Vermilion City Streets":
            lambda state: state.has("Vermilion City Streets", player),
        
        "Rattata -> Rock Mountain":
            lambda state: state.has("Rock Mountain", player),
        "Spearow -> Rock Mountain":
            lambda state: state.has("Rock Mountain", player),
        "Ekans -> Rock Mountain":
            lambda state: state.has("Rock Mountain", player),
        "Zubat -> Rock Mountain":
            lambda state: state.has("Rock Mountain", player),
        "Diglett -> Rock Mountain":
            lambda state: state.has("Rock Mountain", player),  
        "Machop -> Rock Mountain":
            lambda state: state.has("Rock Mountain", player),
        "Geodude -> Rock Mountain":
            lambda state: state.has("Rock Mountain", player),
        "Slowpoke -> Rock Mountain":
            lambda state: state.has("Rock Mountain", player),
        "Onix -> Rock Mountain":
            lambda state: state.has("Rock Mountain", player),
        "Voltorb -> Rock Mountain":
            lambda state: state.has("Rock Mountain", player),
        "Mr Mime -> Rock Mountain":
            lambda state: state.has("Rock Mountain", player),
        
        "Ekans -> Lavender Town":
            lambda state: state.has("Lavender Town", player),
        "Mankey -> Lavender Town":
            lambda state: state.has("Lavender Town", player),
        "Growlithe -> Lavender Town":
            lambda state: state.has("Lavender Town", player),
        "Magnemite -> Lavender Town":
            lambda state: state.has("Lavender Town", player),
        "Gastly -> Lavender Town":
            lambda state: state.has("Lavender Town", player),
        "Cubone -> Lavender Town":
            lambda state: state.has("Lavender Town", player),
        "Electabuzz -> Lavender Town":
            lambda state: state.has("Lavender Town", player),
        "Zapdos -> Lavender Town":
            lambda state: state.has("Lavender Town", player),
        
        "Pidgey -> Celadon City":
	        lambda state: state.has("Celadon City", player),
        "Vulpix -> Celadon City":
            lambda state: state.has("Celadon City", player),
        "Oddish -> Celadon City":
            lambda state: state.has("Celadon City", player),
        "Meowth -> Celadon City":
            lambda state: state.has("Celadon City", player),
        "Mankey -> Celadon City":
            lambda state: state.has("Celadon City", player),
        "Growlithe -> Celadon City":
            lambda state: state.has("Celadon City", player),
        "Bellsprout -> Celadon City":
            lambda state: state.has("Celadon City", player),
        "Abra -> Celadon City":
            lambda state: state.has("Celadon City", player),
        "Scyther -> Celadon City":
            lambda state: state.has("Celadon City", player),
        "Pinsir -> Celadon City":
            lambda state: state.has("Celadon City", player),
        "Eevee -> Celadon City":
            lambda state: state.has("Celadon City", player),
        "Porygon -> Celadon City":
            lambda state: state.has("Celadon City", player),
        "Dratini -> Celadon City":
            lambda state: state.has("Celadon City", player),
    
        "Rattata -> Cycling Road":
            lambda state: state.has("Cycling Road", player),
        "Spearow -> Cycling Road":
            lambda state: state.has("Cycling Road", player),
        "Tentacool -> Cycling Road":
            lambda state: state.has("Cycling Road", player),
        "Doduo -> Cycling Road":
            lambda state: state.has("Cycling Road", player),
        "Krabby -> Cycling Road":
            lambda state: state.has("Cycling Road", player),
        "Lickitung -> Cycling Road":
            lambda state: state.has("Cycling Road", player),
        "Goldeen -> Cycling Road":
            lambda state: state.has("Cycling Road", player),
        "Magikarp -> Cycling Road":
            lambda state: state.has("Cycling Road", player),
        "Snorlax -> Cycling Road":
            lambda state: state.has("Cycling Road", player),
    
        "Venonat -> Fuchsia City":
            lambda state: state.has("Fuchsia City", player),
        "Krabby -> Fuchsia City":
            lambda state: state.has("Fuchsia City", player),
        "Exeggcute -> Fuchsia City":
            lambda state: state.has("Fuchsia City", player),
        "Kangaskhan -> Fuchsia City":
            lambda state: state.has("Fuchsia City", player),
        "Goldeen -> Fuchsia City":
            lambda state: state.has("Fuchsia City", player),
        "Magikarp -> Fuchsia City":
            lambda state: state.has("Fuchsia City", player),
    
        "Nidoran Male -> Safari Zone":
            lambda state: state.has("Safari Zone", player),
        "Paras -> Safari Zone":
            lambda state: state.has("Safari Zone", player),
        "Doduo -> Safari Zone":
            lambda state: state.has("Safari Zone", player),
        "Rhyhorn -> Safari Zone":
            lambda state: state.has("Safari Zone", player),
        "Chansey -> Safari Zone":
            lambda state: state.has("Safari Zone", player),
        "Scyther -> Safari Zone":
            lambda state: state.has("Safari Zone", player),
        "Tauros -> Safari Zone":
            lambda state: state.has("Safari Zone", player),
        "Dratini -> Safari Zone":
            lambda state: state.has("Safari Zone", player), 
        "Nidoran Female -> Safari Zone":
            lambda state: state.has("Safari Zone", player),
        "Pinsir -> Safari Zone":
            lambda state: state.has("Safari Zone", player),
    
        "Pidgey -> Saffron City":
	        lambda state: state.has("Saffron City", player),
        "Ekans -> Saffron City":
            lambda state: state.has("Saffron City", player),
        "Sandshrew -> Saffron City":
            lambda state: state.has("Saffron City", player),
        "Vulpix -> Saffron City":
            lambda state: state.has("Saffron City", player),
        "Oddish -> Saffron City":
            lambda state: state.has("Saffron City", player),
        "Meowth -> Saffron City":
            lambda state: state.has("Saffron City", player),
        "Mankey -> Saffron City":
            lambda state: state.has("Saffron City", player),
        "Growlithe -> Saffron City":
            lambda state: state.has("Saffron City", player),
        "Hitmonlee -> Saffron City":
            lambda state: state.has("Saffron City", player),
        "Hitmonchan -> Saffron City":
            lambda state: state.has("Saffron City", player),
        "Lapras -> Saffron City":
            lambda state: state.has("Saffron City", player),
    
        "Zubat -> Seafoam Islands":
            lambda state: state.has("Seafoam Islands", player),
        "Psyduck -> Seafoam Islands":
            lambda state: state.has("Seafoam Islands", player),
        "Tentacool -> Seafoam Islands":
            lambda state: state.has("Seafoam Islands", player),
        "Slowpoke -> Seafoam Islands":
            lambda state: state.has("Seafoam Islands", player),
        "Seel -> Seafoam Islands":
            lambda state: state.has("Seafoam Islands", player),
        "Shellder -> Seafoam Islands":
            lambda state: state.has("Seafoam Islands", player),
        "Krabby -> Seafoam Islands":
            lambda state: state.has("Seafoam Islands", player),
        "Horsea -> Seafoam Islands":
            lambda state: state.has("Seafoam Islands", player),
        "Goldeen -> Seafoam Islands":
            lambda state: state.has("Seafoam Islands", player),
        "Staryu -> Seafoam Islands":
            lambda state: state.has("Seafoam Islands", player),
        "Articuno -> Seafoam Islands":
            lambda state: state.has("Seafoam Islands", player),
    
        "Vulpix -> Cinnabar Island":
            lambda state: state.has("Cinnabar Island", player),
        "Growlithe -> Cinnabar Island":
            lambda state: state.has("Cinnabar Island", player),
        "Ponyta -> Cinnabar Island":
            lambda state: state.has("Cinnabar Island", player),
        "Omanyte -> Cinnabar Island":
            lambda state: state.has("Cinnabar Island", player),
        "Kabuto -> Cinnabar Island":
            lambda state: state.has("Cinnabar Island", player), 
        "Koffing -> Cinnabar Island":
            lambda state: state.has("Cinnabar Island", player),
        "Grimer -> Cinnabar Island":
            lambda state: state.has("Cinnabar Island", player),
        "Tangela -> Cinnabar Island":
            lambda state: state.has("Cinnabar Island", player),
        "Magmar -> Cinnabar Island":
            lambda state: state.has("Cinnabar Island", player),
        "Aerodactyl -> Cinnabar Island":
            lambda state: state.has("Cinnabar Island", player),
        
        "Spearow -> Indigo Plateau":
            lambda state: state.has("Indigo Plateau", player),
        "Ekans -> Indigo Plateau":
            lambda state: state.has("Indigo Plateau", player),
        "Zubat -> Indigo Plateau":
            lambda state: state.has("Indigo Plateau", player),
        "Sandshrew -> Indigo Plateau":
            lambda state: state.has("Indigo Plateau", player),
        "Machop -> Indigo Plateau":
            lambda state: state.has("Indigo Plateau", player),
        "Geodude -> Indigo Plateau":
            lambda state: state.has("Indigo Plateau", player),
        "Onix -> Indigo Plateau":
            lambda state: state.has("Indigo Plateau", player),
        "Ditto -> Indigo Plateau":
            lambda state: state.has("Indigo Plateau", player),
        "Moltres -> Indigo Plateau":
            lambda state: state.has("Indigo Plateau", player),
        "Mewtwo -> Indigo Plateau":
            lambda state: state.has("Indigo Plateau", player),
        "Mew -> Indigo Plateau":
            lambda state: state.has("Indigo Plateau", player),
    }

def get_location_rules(player, dex_needed):
    from .Regions import stage_names
    return {
        "Gastly Bonus":
            lambda state: state.has_from_list(stage_names, player, 0x04),
        "Seel Bonus":
            lambda state: state.has_from_list(stage_names, player, 0x04),
        "Mewtwo Bonus":
            lambda state: state.has_from_list(stage_names, player, 0x0A),
        "50,000,000 Points":
            lambda state: state.has_from_list(stage_names, player, 0x01),
        "100,000,000 Points":
            lambda state: state.has_from_list(stage_names, player, 0x03),
        "250,000,000 Points":
            lambda state: state.has_from_list(stage_names, player, 0x06),
        "500,000,000 Points":
            lambda state: state.has_from_list(stage_names, player, 0x0A),
        "Pokedex Completed":
            lambda state: state.has_from_list(stage_names, player, 0x0F)
    }