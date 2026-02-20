# world/mygame/__init__.py
import math
from typing import List
import typing
from Utils import visualize_regions
from worlds.AutoWorld import World, WebWorld
from BaseClasses import CollectionState, Region, Location, Item, ItemClassification, LocationProgressType, Tutorial
from worlds.generic.Rules import add_rule, set_rule, forbid_item, add_item_rule
from .Options import LobOptions
from worlds.LauncherComponents import Component, components, Type, launch_subprocess
from .Items import trap_table, item_table

def launch_client():
    from .Client import launch
    launch_subprocess(launch, name="Lobotomy Client")


components.append(Component("Lobotomy Client", "LobotomyClient", func=launch_client, component_type=Type.CLIENT))

class LobItem(Item):  
    game: str = "Lobotomy Corporation"  
    type: str

    def __init__(self,name:str,type:ItemClassification,id:int,player):
        if(name == "Victory"):
            super(LobItem,self).__init__(name,ItemClassification.progression,None,player)
        


        super(LobItem, self).__init__(name, type, id, player)

        self.type = type
        self.id = id
        self.name = name
#       Name                Type    count   id offset

class LobLocation(Location):  
    game = "Lobotomy Corporation"  

    def __init__(self,player,name,code:int,type,parent=None):
        super(LobLocation, self).__init__(player, name, code, parent)
        self.type = type

location_table = {
#Name/type         type count   id offset
    'TOOL OBSERVE':         [68,        9000] ,
    'ZAYIN ARMOR':          [70,       10000],
    'ZAYIN WEAPON':         [70,       11000],
    'ZAYIN OBSERVE':        [28,       12000],
    'ZAYIN UPGRADE ARMOR':  [70,       13000],
    'ZAYIN UPGRADE WEAPON': [70,       14000],
    'TETH ARMOR':           [160,      20000],
    'TETH WEAPON':          [160,      21000],
    'TETH OBSERVE':         [64,       22000],
    'TETH UPGRADE ARMOR':   [160,      23000],
    'TETH UPGRADE WEAPON':  [160,      24000],
    'HE ARMOR':             [150,       30000],
    'HE WEAPON':            [150,       31000],
    'HE OBSERVE':           [60,       32000],
    'HE UPGRADE ARMOR':     [160,      33000],
    'HE UPGRADE WEAPON':    [160,      34000],
    'WAW ARMOR':            [210,      40000],
    'WAW WEAPON':           [210,      41000],
    'WAW OBSERVE':          [84,       42000],
    'WAW UPGRADE ARMOR':     [200,      43000],
    'WAW UPGRADE WEAPON':    [200,      44000],
    'ALEPH ARMOR':           [100,       50000],
    'ALEPH WEAPON':          [100,       51000],
    'ALEPH OBSERVE':         [28,       52000], 
    'ALEPH UPGRADE ARMOR':     [160,      53000],
    'ALEPH UPGRADE WEAPON':    [160,      54000],         

                  

    'DAY COMPLETED':        [49,       60000],
    'FINAL DAY COMPLETED':  [1,        61000],

    'MALKUTH MISSION':       [4,         70000],
    'MALKUTH SUPPRESSION':  [5,         70100],
    'YESOD MISSION':         [4,         71000],
    'YESOD SUPPRESSION':    [5,         71100],
    'HOD MISSION':           [4,         72000],
    'HOD SUPPRESSION':      [5,         72100],
    'NETZACH MISSION':       [4,         73000],
    'NETZACH SUPPRESSION':  [5,         73100],
    'TIPHERETH MISSION':      [4,         74000],
    'TIPHERETH SUPPRESSION': [5,         74100],
    'GEBURA MISSION':        [4,         75000],
    'GEBURA SUPPRESSION':   [5,         75100],
    'CHESED MISSION':        [4,         76000],
    'CHESED SUPPRESSION':   [5,         76100],
    'BINAH MISSION':         [4,         77000],
    'BINAH SUPPRESSION':    [5,         77100],
    'HOKMA MISSION':         [4,         78000],
    'HOKMA SUPPRESSION':    [5,         78100],

    'APOCALYPSE BIRD SUPPRESSION':   [5,     80000],
    'WHITENIGHT SUPPRESSION':        [5,     81000],

    

    'DISSOLUTION GOAL':             [1,     90000],

}  

starting_item_table = {
'100009' : 0 ,
'100028' : 0 ,
'100034' : 0 ,
'100001' : 1 ,
'100018' : 1 ,
'100020' : 1 ,
'100021' : 1 ,
'100036' : 1,
'100012' : 1,
'100013' : 1,
'100022' : 1,
'100027' : 1,
'100037' : 1,
'100002' : 2,
'100003' : 2,
'100011' : 2,
'100016' : 2,
'100041' : 2,
'100017' : 2,
'100102' : 2,
'100023' : 3,
'100026' : 3,
'100029' : 3,
'100035' : 3,
'100039' : 3,
'100019' : 4,
'100005' : 4,
'100007' : 1,
'100043' : 2,
'100103' : 2,
'100047' : 3,
'100048' : 3,
'100049' : 2,
'100044' : 3,
'100045' : 3,
'100042' : 4,
'100046' : 3,
'100053' : 0,
'100054' : 1,
'100051' : 2,
'100056' : 4,
'100050' : 2,
'100055' : 3,
'100052' : 1,
'100057' : 2,
'100058' : 4,
'100031' : 2,
'100033' : 3,
'100032' : 3,
'100040' : 3,
'100006' : 2,
'100008' : 3,
'100004' : 3,
'100059' : 1,
'100060' : 1,
'100061' : 3,
'100014' : 0,
'100104' : 3,
'100064' : 0,
'100106' : 1,
'100105' : 3,
'100065' : 3,
'100063' : 4,
'100062' : 3,
}


end_day_table = {
    
    'Malkuth':  25,
    
    'Yesod':    27,
    
    'Hod':      27,
    
    'Netzach':  27,
    
    'Tiphereth': 38,
    
    'Gebura':   40,
    
    'Chesed':   40,
    
    'Binah':    45,
    
    'Hokma':    45,

    'Apocalypsebird':   25,
    'Whitenight':        25,


}

class LobWeb(WebWorld):
    theme = "ocean"
    tutorials = [Tutorial(
            "Multiworld Setup Guide",
            "A guide to setting up the Lobotomy Corporation software on your computer. This guide covers single-player, "
            "multiworld, and related software.",
            "English",
            "lob_en.md",
            "lob/en",
            ["Kli333"]
    )]     

class LobWorld(World):
    """An APWorld for Lobotomy Corporation"""
    game = "Lobotomy Corporation"  
    options_dataclass = LobOptions  
    options: LobOptions  
    topology_present = True  
    web = LobWeb()    
    goal_location = 999999999
    goal_second = 999999999

    total_abno_count = -1
    max_day= 50

    
    def create_location_table(self) -> dict[str,int]:
        locations: dict[str,int]

        return locations

    origin_region_name = "Menu"


    item_name_to_id = dict()
    location_name_to_id = dict()

    for item in item_table.items():
        for id in range(item[1][1]): 
            item_name_to_id[str(item[0])] = (int)(item[1][2])
    
    for location in location_table.items():
        for id in range(location[1][0]):
            if location[0] == "DISSOLUTION GOAL":
                location_name_to_id[location[0]] = (int)(location[1][1])
            elif location[0] == "FINAL DAY COMPLETED":
                location_name_to_id[location[0]] = (int)(location[1][1])
            else:
                location_name_to_id[str(location[0])+" "+str(id+1)] = (int)(id+location[1][1])

    item_name_groups = {}

    
    item_name_groups["ABNORMALTIES"] = { "PLAGUE DOCTOR", "BIG BIRD","SMALL BIRD", "LONG BIRD" , "ZAYIN ABNORMALITY", "TETH ABNORMALITY", "HE ABNORMALITY", "WAW ABNORMALITY", "ALEPH ABNORMALITY","TOOL ABNORMALITY"}
    item_name_groups["ZAYIN ABNORMALTIES"] = {"ZAYIN ABNORMALITY"}
    item_name_groups["TETH ABNORMALTIES"] = {"SMALL BIRD", "TETH ABNORMALITY"}
    item_name_groups["WAW ABNORMALTIES"] = {"BIG BIRD", "LONG BIRD" ,"WAW ABNORMALITY"}
    item_name_groups["ALEPH ABNORMALTIES"] = {"ALEPH ABNORMALITY"}

   

    
    def adjust_items(self):
        total_abno_weight = 0
        total_abno_weight += item_table['ZAYIN ABNORMALITY'][1]
        total_abno_weight += item_table['TETH ABNORMALITY'][1]
        total_abno_weight += item_table['HE ABNORMALITY'][1]
        total_abno_weight += item_table['WAW ABNORMALITY'][1]
        total_abno_weight += item_table['ALEPH ABNORMALITY'][1]
        total_abno_weight += item_table['TOOL ABNORMALITY'][1]

        item_table['ZAYIN ABNORMALITY'][1] = math.ceil(item_table['ZAYIN ABNORMALITY'][1]*(self.total_abno_count/total_abno_weight))
        item_table['TETH ABNORMALITY'][1] = math.ceil(item_table['TETH ABNORMALITY'][1]*(self.total_abno_count/total_abno_weight))
        item_table['HE ABNORMALITY'][1] = math.ceil(item_table['HE ABNORMALITY'][1]*(self.total_abno_count/total_abno_weight))
        item_table['WAW ABNORMALITY'][1] = math.ceil(item_table['WAW ABNORMALITY'][1]*(self.total_abno_count/total_abno_weight))
        item_table['ALEPH ABNORMALITY'][1] = math.ceil(item_table['ALEPH ABNORMALITY'][1]*(self.total_abno_count/total_abno_weight))
        item_table['TOOL ABNORMALITY'][1] = math.ceil(item_table['TOOL ABNORMALITY'][1]*(self.total_abno_count/total_abno_weight))

        item_table['ZAYIN WEAPON'][1] = math.ceil(item_table['ZAYIN WEAPON'][1]*(self.total_abno_count/total_abno_weight))
        item_table['TETH WEAPON'][1] = math.ceil(item_table['TETH WEAPON'][1]*(self.total_abno_count/total_abno_weight))
        item_table['HE WEAPON'][1] = math.ceil(item_table['HE WEAPON'][1]*(self.total_abno_count/total_abno_weight))
        item_table['WAW WEAPON'][1] = math.ceil(item_table['WAW WEAPON'][1]*(self.total_abno_count/total_abno_weight))
        item_table['ALEPH WEAPON'][1] = math.ceil(item_table['ALEPH WEAPON'][1]*(self.total_abno_count/total_abno_weight))

        item_table['ZAYIN ARMOR'][1] = math.ceil(item_table['ZAYIN ARMOR'][1]*(self.total_abno_count/total_abno_weight))
        item_table['TETH ARMOR'][1] = math.ceil(item_table['TETH ARMOR'][1]*(self.total_abno_count/total_abno_weight))
        item_table['HE ARMOR'][1] = math.ceil(item_table['HE ARMOR'][1]*(self.total_abno_count/total_abno_weight))
        item_table['WAW ARMOR'][1] = math.ceil(item_table['WAW ARMOR'][1]*(self.total_abno_count/total_abno_weight))
        item_table['ALEPH ARMOR'][1] = math.ceil(item_table['ALEPH ARMOR'][1]*(self.total_abno_count/total_abno_weight))

        item_table['DAILY LOB INCOME'][1] = math.ceil(item_table['DAILY LOB INCOME'][1]*(self.total_abno_count/total_abno_weight))
        item_table['DAILY AGENT TRAINING'][1] = math.ceil(item_table['DAILY AGENT TRAINING'][1]*(self.total_abno_count/total_abno_weight))
        item_table['STARTING LOB'][1] = math.ceil(item_table['STARTING LOB'][1]*(self.total_abno_count/total_abno_weight))

        if self.options.wn_mode == 'disabled':
            item_table['PLAGUE DOCTOR'][1] = 0

        if self.options.apoc_mode == 'disabled':
            item_table['SMALL BIRD'][1] = 0
            item_table['BIG BIRD'][1] = 0
            item_table['LONG BIRD'][1] = 0

        








        


    
    def fill_slot_data(self) -> dict:

        dissolution = -1
        if self.options.goal_type == 'dissolution' or self.options.goal_type == 'day_and_dissolution':
            dissolution = self.options.dissolution_goal.value

        goal_info = "!!! Manager! Your goal is "

        if self.options.goal_type == "suppression":
            goal_info += "to complete the core suppression of "
            goal_info += self.options.suppression_goal.current_key.title()+"!" 
        elif self.options.goal_type == 'dissolution':    
            goal_info += "to completely research "
            goal_info += str(self.options.dissolution_goal.value)+ " Abnormalities!"
        elif self.options.goal_type == 'day_and_dissolution':
            goal_info += "to completely research "
            goal_info += str(self.options.dissolution_goal.value)+ " Abnormalities and complete Day "
            goal_info += str(self.options.day_goal.value)+ "!"
        else: 
            goal_info += "to complete day 50!"
        goal_info += " !!!"
        
        
        slot_data = {                 
                    "starting_abnos":              list(self.options.starting_abnos.value)
                    ,"dissolution_goal":            int(dissolution)
                    ,"goal_location" :              int(self.goal_location)
                    ,"goal_second":                 int(self.goal_second)
                    ,"total_abno_count":            int(self.total_abno_count)
                    ,"base_equipment_checks":       int(self.options.base_equipment_checks.value)
                    ,"upgrade_equipment_checks":    int(self.options.upgrade_equipment_checks.value)
                    ,"goal_info":                   goal_info
                    ,"deathlink":                    bool(self.options.deathlink == True)
                    ,"deathlinkTrigger":            self.options.deathlink_trigger.current_key
                    ,"deathlinkEffect":             self.options.deathlink_effect.current_key
                    ,"deathlinkCount":              int(self.options.deathlink_count.value)
                    ,"deathlinkGrace":              int(self.options.deathlink_grace.value)
                    }
        
                
        return slot_data
    
    def get_abno_count_by_max_day(self, max_day:int) -> int:
        if(max_day<=20):
            return max_day
        elif(max_day<=25):
            return 20+((max_day-20)*2)
        elif(max_day<=45):
            return max_day+5
        else:
            return max_day+5+(max_day-45)
       
    def generate_early(self):

        if self.options.adaptive_locations == True:
            if self.options.goal_type == 'suppression':
                self.max_day = end_day_table[self.options.suppression_goal.get_option_name(self.options.suppression_goal.value)]
            if self.options.goal_type == 'vanilla':
                self.max_day = 50
            if self.options.goal_type == 'dissolution':
                    self.max_day = self.options.dissolution_goal.value
            if self.options.goal_type == 'day_and_dissolution':
                self.max_day = self.options.day_goal.value

            if self.max_day > 50:
                self.max_day = 50

            self.total_abno_count = self.get_abno_count_by_max_day(self.max_day)
            if self.options.goal_type == 'day_and_dissolution' or self.options.goal_type == 'day_and_dissolution':
                if self.total_abno_count < self.options.dissolution_goal.value:
                    self.total_abno_count = self.options.dissolution_goal.value
            self.total_abno_count += 3

            


            self.adjust_items()


    def create_abno_locations(self, region:Region) -> None:
        totalEquips = self.options.base_equipment_checks.value + self.options.upgrade_equipment_checks.value
        baseEquips = self.options.base_equipment_checks.value
        upgradeEquips = self.options.upgrade_equipment_checks.value

        for risk in ['ZAYIN','TETH','HE','WAW','ALEPH']:

            specialAbnos={'ZAYIN':0,'TETH':item_table['SMALL BIRD'][1],'HE':0,'WAW':item_table['BIG BIRD'][1]+item_table['LONG BIRD'][1],'ALEPH':0}    

            for id in range(baseEquips*(item_table[risk+' ABNORMALITY'][1]+specialAbnos[risk])):
                for equip_type in ['ARMOR','WEAPON']:
                    location = location_table[risk+' '+equip_type]
                    name = str(risk+' '+equip_type)+" "+str(id+1)
                    region.locations.append(LobLocation(self.player,name,(int)(id+location[1]),name,region))
            for id in range(upgradeEquips*(item_table[risk+' ABNORMALITY'][1]+specialAbnos[risk])):
                for equip_type in ['ARMOR','WEAPON']:
                    location = location_table[risk+' UPGRADE '+equip_type]
                    name = str(risk+' UPGRADE '+equip_type)+" "+str(id+1)
                    region.locations.append(LobLocation(self.player,name,(int)(id+location[1]),name,region))
            for id in range(4*(item_table[risk+' ABNORMALITY'][1]+specialAbnos[risk])):
                location = location_table[risk+' OBSERVE']
                name = str(risk+' OBSERVE')+" "+str(id+1)
                region.locations.append(LobLocation(self.player,name,(int)(id+location[1]),name,region))
        risk = "TOOL"
        for id in range(4*item_table[risk+' ABNORMALITY'][1]):
            location = location_table[risk+' OBSERVE']
            name = str(risk+' OBSERVE')+" "+str(id+1)
            region.locations.append(LobLocation(self.player,name,(int)(id+location[1]),name,region))

    def create_day_locations(self, region:Region) -> None:
     
        for id in range(1,self.max_day+1):
            if id == 50:
                location = location_table['FINAL DAY COMPLETED']
                name = 'FINAL DAY COMPLETED'
                region.locations.append(LobLocation(self.player,name,(int)(location[1]),name,region))
                continue

            location = location_table["DAY COMPLETED"]
            name = str("DAY COMPLETED")+" "+str(id)
            region.locations.append(LobLocation(self.player,name,(int)(id+location[1]),name,region))

    def create_sephira_locations(self, region:Region) -> None:

        for dayNumber in range(1,self.max_day):

            if dayNumber < 5 :
                id = dayNumber
                location = location_table["MALKUTH MISSION"]
                name = str("MALKUTH MISSION")+" "+str(id)
                region.locations.append(LobLocation(self.player,name,(int)(id+location[1]-1),name,region))

            elif dayNumber < 10 and dayNumber > 5:
                id = dayNumber-5
                location = location_table["YESOD MISSION"]
                name = str("YESOD MISSION")+" "+str(id)
                region.locations.append(LobLocation(self.player,name,(int)(id+location[1]-1),name,region))

            elif dayNumber < 20 and dayNumber >15:
                id = dayNumber-15

                location = location_table["HOD MISSION"]
                name = str("HOD MISSION")+" "+str(id)
                region.locations.append(LobLocation(self.player,name,(int)(id+location[1]-1),name,region))

                location = location_table["NETZACH MISSION"]
                name = str("NETZACH MISSION")+" "+str(id)
                region.locations.append(LobLocation(self.player,name,(int)(id+location[1]-1),name,region))

            elif dayNumber < 25 and dayNumber > 20:
                id = dayNumber-20

                location = location_table["TIPHERETH MISSION"]
                name = str("TIPHERETH MISSION")+" "+str(id)
                region.locations.append(LobLocation(self.player,name,(int)(id+location[1]-1),name,region))             
             
            elif dayNumber < 35 and dayNumber > 30:
                id = dayNumber-30

                location = location_table["GEBURA MISSION"]
                name = str("GEBURA MISSION")+" "+str(id)
                region.locations.append(LobLocation(self.player,name,(int)(id+location[1]-1),name,region))

                location = location_table["CHESED MISSION"]
                name = str("CHESED MISSION")+" "+str(id)
                region.locations.append(LobLocation(self.player,name,(int)(id+location[1]-1),name,region))

            elif dayNumber < 45 and dayNumber > 40:
                id = dayNumber-40

                location = location_table["BINAH MISSION"]
                name = str("BINAH MISSION")+" "+str(id)
                region.locations.append(LobLocation(self.player,name,(int)(id+location[1]-1),name,region))


                location = location_table["HOKMA MISSION"]
                name = str("HOKMA MISSION")+" "+str(id)
                region.locations.append(LobLocation(self.player,name,(int)(id+location[1]-1),name,region))
           

            

        if(self.max_day >= 25):
            for id in range(1,6):
                location = location_table["MALKUTH SUPPRESSION"]
                name = str("MALKUTH SUPPRESSION")+" "+str(id)
                region.locations.append(LobLocation(self.player,name,(int)(id+location[1]-1),name,region))

                location = location_table["YESOD SUPPRESSION"]
                name = str("YESOD SUPPRESSION")+" "+str(id)
                region.locations.append(LobLocation(self.player,name,(int)(id+location[1]-1),name,region))

                location = location_table["HOD SUPPRESSION"]
                name = str("HOD SUPPRESSION")+" "+str(id)
                region.locations.append(LobLocation(self.player,name,(int)(id+location[1]-1),name,region))

                location = location_table["NETZACH SUPPRESSION"]
                name = str("NETZACH SUPPRESSION")+" "+str(id)
                region.locations.append(LobLocation(self.player,name,(int)(id+location[1]-1),name,region))
        if(self.max_day >= 38):
            for id in range(1,6):
                location = location_table["TIPHERETH SUPPRESSION"]
                name = str("TIPHERETH SUPPRESSION")+" "+str(id)
                region.locations.append(LobLocation(self.player,name,(int)(id+location[1]-1),name,region))

                location = location_table["GEBURA SUPPRESSION"]
                name = str("GEBURA SUPPRESSION")+" "+str(id)
                region.locations.append(LobLocation(self.player,name,(int)(id+location[1]-1),name,region))

                location = location_table["CHESED SUPPRESSION"]
                name = str("CHESED SUPPRESSION")+" "+str(id)
                region.locations.append(LobLocation(self.player,name,(int)(id+location[1]-1),name,region))
        if(self.max_day >=45):
            for id in range(1,6):
                location = location_table["BINAH SUPPRESSION"]
                name = str("BINAH SUPPRESSION")+" "+str(id)
                region.locations.append(LobLocation(self.player,name,(int)(id+location[1]-1),name,region))

                location = location_table["HOKMA SUPPRESSION"]
                name = str("HOKMA SUPPRESSION")+" "+str(id)
                region.locations.append(LobLocation(self.player,name,(int)(id+location[1]-1),name,region))




    def create_regions(self) -> None:
        totalEquips = self.options.base_equipment_checks.value + self.options.upgrade_equipment_checks.value
        baseEquips = self.options.base_equipment_checks.value
        upgradeEquips = self.options.upgrade_equipment_checks.value
        
        
        menu_region = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu_region) 
        main_region = Region("Main Area", self.player, self.multiworld)
        self.multiworld.regions.append(main_region)

        menu_region.connect(main_region)


        #TODO adjust the weapon and equip count from options


        self.create_abno_locations(main_region)
        self.create_day_locations(main_region)
        self.create_sephira_locations(main_region)


        if self.options.wn_mode != 'disabled':
            location = location_table['WHITENIGHT SUPPRESSION']
            for id in range(location[0]):
                name = str('WHITENIGHT SUPPRESSION')+" "+str(id+1)
                l = LobLocation(self.player,name,(int)(id+location[1]),name,main_region)
                if self.options.wn_mode == 'excluded':
                    l.progress_type = LocationProgressType.EXCLUDED
                if self.options.wn_mode == 'darkdays':
                    l.progress_type = LocationProgressType.PRIORITY
                main_region.locations.append(l)
        
        if self.options.apoc_mode != 'disabled':
            location = location_table['APOCALYPSE BIRD SUPPRESSION']
            for id in range(location[0]):
                name = str('APOCALYPSE BIRD SUPPRESSION')+" "+str(id+1)
                l = LobLocation(self.player,name,(int)(id+location[1]),name,main_region)
                if self.options.apoc_mode == 'excluded':
                    l.progress_type = LocationProgressType.EXCLUDED
                if self.options.apoc_mode == 'apocalypse':
                    l.progress_type = LocationProgressType.PRIORITY
                main_region.locations.append(l)


        if self.options.goal_type == 'dissolution' or self.options.goal_type == 'day_and_dissolution':
            location = location_table["DISSOLUTION GOAL"]
            name = "DISSOLUTION GOAL"
            main_region.locations.append(LobLocation(self.player,name,(int)(location[1]),name,main_region))


    def create_item(self, name: str,type:ItemClassification=ItemClassification.filler,id:int=-1) -> LobItem:
        # Items will look like WEAPON ZAYIN 1 or PROGRESSIVE GEBURA 2
        if id == -1:
            id = item_table[name][2]
            type = item_table[name][0]
        
        return LobItem(name, type ,id,self.player)
    



    def set_rules(self) -> None:
        totalEquips = self.options.base_equipment_checks.value + self.options.upgrade_equipment_checks.value
        removedCounts = [0,0,0,0,0,0]
        for abno in self.options.starting_abnos.value:
            removedCounts[starting_item_table[abno]] += 1


        #Day Rules
        #Day 1-20
        abnoCount = 5

        for dayNumber in range(1,self.max_day+1):
            if dayNumber in range(1,21):
                set_rule(self.multiworld.get_location('DAY COMPLETED '+str(dayNumber), self.player), lambda state,c=abnoCount: 
                    (state.count('ZAYIN ABNORMALITY',self.player)+
                    state.count('TETH ABNORMALITY',self.player)+
                    state.count('HE ABNORMALITY',self.player)+
                    state.count('WAW ABNORMALITY',self.player)+
                    state.count('ALEPH ABNORMALITY',self.player)+
                    state.count('TOOL ABNORMALITY',self.player)+
                    state.count('SMALL BIRD',self.player)+
                    state.count('BIG BIRD',self.player)+
                    state.count('LONG BIRD',self.player)+
                    state.count('PLAGUE DOCTOR',self.player)
                    ) >= c+2)  
                abnoCount +=1  
            elif dayNumber in range(21,26):
                set_rule(self.multiworld.get_location('DAY COMPLETED '+str(dayNumber), self.player), lambda state,c=abnoCount: 
                    (state.count('ZAYIN ABNORMALITY',self.player)+
                    state.count('TETH ABNORMALITY',self.player)+
                    state.count('HE ABNORMALITY',self.player)+
                    state.count('WAW ABNORMALITY',self.player)+
                    state.count('ALEPH ABNORMALITY',self.player)+
                    state.count('TOOL ABNORMALITY',self.player)+
                    state.count('SMALL BIRD',self.player)+
                    state.count('BIG BIRD',self.player)+
                    state.count('LONG BIRD',self.player)+
                    state.count('PLAGUE DOCTOR',self.player)
                    ) >= c+3)  
                abnoCount +=2
            elif dayNumber in range(26,46):
                set_rule(self.multiworld.get_location('DAY COMPLETED '+str(dayNumber), self.player), lambda state,c=abnoCount: 
                    (state.count('ZAYIN ABNORMALITY',self.player)+
                    state.count('TETH ABNORMALITY',self.player)+
                    state.count('HE ABNORMALITY',self.player)+
                    state.count('WAW ABNORMALITY',self.player)+
                    state.count('ALEPH ABNORMALITY',self.player)+
                    state.count('TOOL ABNORMALITY',self.player)+
                    state.count('SMALL BIRD',self.player)+
                    state.count('BIG BIRD',self.player)+
                    state.count('LONG BIRD',self.player)+
                    state.count('PLAGUE DOCTOR',self.player)
                    ) >= c+2)  
                abnoCount +=1
            elif dayNumber == 46:
                set_rule(self.multiworld.get_location('DAY COMPLETED 46', self.player), lambda state: (state.has_group("ABNORMALTIES",self.player,abnoCount+2)))  
                abnoCount +=2
            elif dayNumber == 47:
                set_rule(self.multiworld.get_location('DAY COMPLETED 47', self.player), lambda state: (state.has_group("ABNORMALTIES",self.player,abnoCount+2)) and state.has('SEED OF LIGHT',self.player,4))  
                abnoCount +=2
            elif dayNumber == 48:
                set_rule(self.multiworld.get_location('DAY COMPLETED 48', self.player), lambda state: (state.has_group("ABNORMALTIES",self.player,abnoCount+2)) and state.has('SEED OF LIGHT',self.player,7))  
                abnoCount +=2
            elif dayNumber == 49:
                set_rule(self.multiworld.get_location('DAY COMPLETED 49', self.player), lambda state: (state.has_group("ABNORMALTIES",self.player,abnoCount+2)) and state.has('SEED OF LIGHT',self.player,9))  
                abnoCount +=2
            elif dayNumber == 50:
                set_rule(self.multiworld.get_location('FINAL DAY COMPLETED', self.player), lambda state: (state.has_group("ABNORMALTIES",self.player,abnoCount+2)) and state.has('SEED OF LIGHT',self.player,9))  


        """for dayNumber in range(1,21):
            set_rule(self.multiworld.get_location('DAY COMPLETED '+str(dayNumber), self.player), lambda state,c=abnoCount: 
                (state.count('ZAYIN ABNORMALITY',self.player)+
                state.count('TETH ABNORMALITY',self.player)+
                state.count('HE ABNORMALITY',self.player)+
                state.count('WAW ABNORMALITY',self.player)+
                state.count('ALEPH ABNORMALITY',self.player)+
                state.count('TOOL ABNORMALITY',self.player)+
                state.count('SMALL BIRD',self.player)+
                state.count('BIG BIRD',self.player)+
                state.count('LONG BIRD',self.player)+
                state.count('PLAGUE DOCTOR',self.player)
                ) >= c+2)  
            abnoCount +=1
        for dayNumber in range(21,26):
            set_rule(self.multiworld.get_location('DAY COMPLETED '+str(dayNumber), self.player), lambda state,c=abnoCount: 
                (state.count('ZAYIN ABNORMALITY',self.player)+
                state.count('TETH ABNORMALITY',self.player)+
                state.count('HE ABNORMALITY',self.player)+
                state.count('WAW ABNORMALITY',self.player)+
                state.count('ALEPH ABNORMALITY',self.player)+
                state.count('TOOL ABNORMALITY',self.player)+
                state.count('SMALL BIRD',self.player)+
                state.count('BIG BIRD',self.player)+
                state.count('LONG BIRD',self.player)+
                state.count('PLAGUE DOCTOR',self.player)
                ) >= c+3)  
            abnoCount +=2
        for dayNumber in range(26,46):
            set_rule(self.multiworld.get_location('DAY COMPLETED '+str(dayNumber), self.player), lambda state,c=abnoCount: 
                (state.count('ZAYIN ABNORMALITY',self.player)+
                state.count('TETH ABNORMALITY',self.player)+
                state.count('HE ABNORMALITY',self.player)+
                state.count('WAW ABNORMALITY',self.player)+
                state.count('ALEPH ABNORMALITY',self.player)+
                state.count('TOOL ABNORMALITY',self.player)+
                state.count('SMALL BIRD',self.player)+
                state.count('BIG BIRD',self.player)+
                state.count('LONG BIRD',self.player)+
                state.count('PLAGUE DOCTOR',self.player)
                ) >= c+2)  
            abnoCount +=1
        
        set_rule(self.multiworld.get_location('DAY COMPLETED 46', self.player), lambda state: (state.has_group("ABNORMALTIES",self.player,abnoCount+2)))  
        abnoCount +=2
        set_rule(self.multiworld.get_location('DAY COMPLETED 47', self.player), lambda state: (state.has_group("ABNORMALTIES",self.player,abnoCount+2)) and state.has('SEED OF LIGHT',self.player,4))  
        abnoCount +=2
        set_rule(self.multiworld.get_location('DAY COMPLETED 48', self.player), lambda state: (state.has_group("ABNORMALTIES",self.player,abnoCount+2)) and state.has('SEED OF LIGHT',self.player,7))  
        abnoCount +=2
        set_rule(self.multiworld.get_location('DAY COMPLETED 49', self.player), lambda state: (state.has_group("ABNORMALTIES",self.player,abnoCount+2)) and state.has('SEED OF LIGHT',self.player,9))  
        abnoCount +=2
        set_rule(self.multiworld.get_location('FINAL DAY COMPLETED', self.player), lambda state: (state.has_group("ABNORMALTIES",self.player,abnoCount+2)) and state.has('SEED OF LIGHT',self.player,9))  
        """
       
        #Mission Rules

        #Mission day limitations
        for dayNumber in range(1,self.max_day):
            if dayNumber < 5 :
                set_rule(self.multiworld.get_location('MALKUTH MISSION '+str(dayNumber), self.player),lambda state,day=str(dayNumber): state.can_reach(self.multiworld.get_location('DAY COMPLETED '+day, self.player)))
            elif dayNumber < 10 and dayNumber > 5:
                set_rule(self.multiworld.get_location('YESOD MISSION '+str(dayNumber-5), self.player),lambda state,day=str(dayNumber): state.can_reach(self.multiworld.get_location('DAY COMPLETED '+day, self.player)))
            elif dayNumber < 20 and dayNumber >15:
                set_rule(self.multiworld.get_location('HOD MISSION '+str(dayNumber-15), self.player),lambda state,day=str(dayNumber): state.can_reach(self.multiworld.get_location('DAY COMPLETED '+day, self.player)))
                set_rule(self.multiworld.get_location('NETZACH MISSION '+str(dayNumber-15), self.player),lambda state,day=str(dayNumber): state.can_reach(self.multiworld.get_location('DAY COMPLETED '+day, self.player)))
            elif dayNumber < 25 and dayNumber > 20:
                set_rule(self.multiworld.get_location('TIPHERETH MISSION '+str(dayNumber-20), self.player),lambda state,day=str(dayNumber): state.can_reach(self.multiworld.get_location('DAY COMPLETED '+day, self.player)))
            elif dayNumber < 35 and dayNumber > 30:
                set_rule(self.multiworld.get_location('GEBURA MISSION '+str(dayNumber-30), self.player),lambda state,day=str(dayNumber): state.can_reach(self.multiworld.get_location('DAY COMPLETED '+day, self.player)))
                set_rule(self.multiworld.get_location('CHESED MISSION '+str(dayNumber-30), self.player),lambda state,day=str(dayNumber): state.can_reach(self.multiworld.get_location('DAY COMPLETED '+day, self.player)))
            elif dayNumber < 45 and dayNumber > 40:
                set_rule(self.multiworld.get_location('BINAH MISSION '+str(dayNumber-40), self.player),lambda state,day=str(dayNumber): state.can_reach(self.multiworld.get_location('DAY COMPLETED '+day, self.player)))
                set_rule(self.multiworld.get_location('HOKMA MISSION '+str(dayNumber-40), self.player),lambda state,day=str(dayNumber): state.can_reach(self.multiworld.get_location('DAY COMPLETED '+day, self.player)))             






        #Mission other limitations
        if(self.max_day >= 21):
            add_rule(self.multiworld.get_location('MALKUTH MISSION 4', self.player),lambda state: state.can_reach(self.multiworld.get_location('DAY COMPLETED 21', self.player)))
        if(self.max_day >= 18):
            add_rule(self.multiworld.get_location('HOD MISSION 3', self.player), lambda state: 
                    (state.count('ZAYIN ABNORMALITY',self.player)+
                    state.count('TETH ABNORMALITY',self.player)+
                    state.count('HE ABNORMALITY',self.player)+
                    state.count('WAW ABNORMALITY',self.player)+
                    state.count('ALEPH ABNORMALITY',self.player)
                    ) >= 16)  
        if(self.max_day >= 19):
            add_rule(self.multiworld.get_location('HOD MISSION 4', self.player),lambda state: state.can_reach(self.multiworld.get_location('HOD MISSION 3', self.player)))

        if(self.max_day >= 31):
            add_rule(self.multiworld.get_location('GEBURA MISSION 1', self.player),lambda state:
                    (state.count('ZAYIN ABNORMALITY',self.player)+
                    state.count('TETH ABNORMALITY',self.player)+
                    state.count('HE ABNORMALITY',self.player)
                    ) >= 16)  
        if(self.max_day >= 32):
            add_rule(self.multiworld.get_location('GEBURA MISSION 2', self.player),lambda state: state.can_reach(self.multiworld.get_location('GEBURA MISSION 1', self.player)) and
                    state.count('WAW ABNORMALITY',self.player) >=5) 
        if(self.max_day >= 33):
            add_rule(self.multiworld.get_location('GEBURA MISSION 3', self.player),lambda state: state.can_reach(self.multiworld.get_location('GEBURA MISSION 2', self.player)) and
                    state.count('ALEPH ABNORMALITY',self.player) >=3) 
        if(self.max_day >= 34 ):
            add_rule(self.multiworld.get_location('GEBURA MISSION 4', self.player),lambda state: state.can_reach(self.multiworld.get_location('GEBURA MISSION 3', self.player)))
        if(self.max_day >=41):
            add_rule(self.multiworld.get_location('BINAH MISSION 1', self.player),lambda state: state.count('HE ABNORMALITY',self.player) >= 5)  
        if(self.max_day >=42):
            add_rule(self.multiworld.get_location('BINAH MISSION 2', self.player),lambda state: state.can_reach(self.multiworld.get_location('BINAH MISSION 1', self.player)))
        if(self.max_day >=43):
            add_rule(self.multiworld.get_location('BINAH MISSION 3', self.player),lambda state: state.can_reach(self.multiworld.get_location('BINAH MISSION 2', self.player)) and 
                 state.count('ALEPH WEAPON',self.player) + state.count('ALEPH ARMOR',self.player) >=8)
        if(self.max_day >=44):
            add_rule(self.multiworld.get_location('BINAH MISSION 4', self.player),lambda state: state.can_reach(self.multiworld.get_location('BINAH MISSION 3', self.player)))
                       
        #SUPPRESSION rules

        for missionNumber in range(1,6):
            if(self.max_day >= 25):
                set_rule(self.multiworld.get_location('MALKUTH SUPPRESSION '+str(missionNumber), self.player),lambda state: state.can_reach(self.multiworld.get_location('MALKUTH MISSION 4', self.player)) and state.can_reach(self.multiworld.get_location('TIPHERETH MISSION 3', self.player)))
                set_rule(self.multiworld.get_location('YESOD SUPPRESSION '+str(missionNumber), self.player),lambda state: state.can_reach(self.multiworld.get_location('YESOD MISSION 4', self.player)) and state.can_reach(self.multiworld.get_location('TIPHERETH MISSION 3', self.player)))
                set_rule(self.multiworld.get_location('HOD SUPPRESSION '+str(missionNumber), self.player),lambda state: state.can_reach(self.multiworld.get_location('HOD MISSION 4', self.player)) and state.can_reach(self.multiworld.get_location('TIPHERETH MISSION 3', self.player)))
                set_rule(self.multiworld.get_location('NETZACH SUPPRESSION '+str(missionNumber), self.player),lambda state: state.can_reach(self.multiworld.get_location('NETZACH MISSION 4', self.player)) and state.can_reach(self.multiworld.get_location('HOD SUPPRESSION 1', self.player)))
            if(self.max_day >= 38):
                set_rule(self.multiworld.get_location('TIPHERETH SUPPRESSION '+str(missionNumber), self.player),lambda state: state.can_reach(self.multiworld.get_location('TIPHERETH MISSION 4', self.player)) and state.can_reach(self.multiworld.get_location('NETZACH SUPPRESSION 1', self.player)))
                set_rule(self.multiworld.get_location('GEBURA SUPPRESSION '+str(missionNumber), self.player),lambda state: state.can_reach(self.multiworld.get_location('GEBURA MISSION 4', self.player)) and state.can_reach(self.multiworld.get_location('NETZACH SUPPRESSION 1', self.player)) and state.can_reach(self.multiworld.get_location('CHESED MISSION 4', self.player)))
                set_rule(self.multiworld.get_location('CHESED SUPPRESSION '+str(missionNumber), self.player),lambda state: state.can_reach(self.multiworld.get_location('GEBURA MISSION 4', self.player)) and state.can_reach(self.multiworld.get_location('NETZACH SUPPRESSION 1', self.player)) and state.can_reach(self.multiworld.get_location('CHESED MISSION 4', self.player)))
            if(self.max_day >=43):
                set_rule(self.multiworld.get_location('BINAH SUPPRESSION '+str(missionNumber), self.player),lambda state: 
                        state.can_reach(self.multiworld.get_location('BINAH MISSION 4', self.player)) and 
                        state.can_reach(self.multiworld.get_location('GEBURA SUPPRESSION 1', self.player)) and
                        state.can_reach(self.multiworld.get_location('CHESED SUPPRESSION 1', self.player)) and
                        state.can_reach(self.multiworld.get_location('TIPHERETH SUPPRESSION 1', self.player))
                        )
                set_rule(self.multiworld.get_location('HOKMA SUPPRESSION '+str(missionNumber), self.player),lambda state: 
                        state.can_reach(self.multiworld.get_location('HOKMA MISSION 4', self.player)) and 
                        state.can_reach(self.multiworld.get_location('GEBURA SUPPRESSION 1', self.player)) and
                        state.can_reach(self.multiworld.get_location('CHESED SUPPRESSION 1', self.player)) and
                        state.can_reach(self.multiworld.get_location('TIPHERETH SUPPRESSION 1', self.player))
                        )
       


        for count in range(item_table['TOOL ABNORMALITY'][1]):
                if removedCounts[5] <= count:
                    for obs in range(4):
                        set_rule(self.multiworld.get_location('TOOL OBSERVE '+str(obs+(count *4)+1), self.player), lambda state,amount=count+1: state.has('TOOL ABNORMALITY',self.player,amount)) 

                        
        for count in range(item_table['ZAYIN ABNORMALITY'][1]):
            if removedCounts[0] <= count:
                for obs in range(4):
                    set_rule(self.multiworld.get_location('ZAYIN OBSERVE '+str(obs+1+(count *4)), self.player), lambda state,amount=count+1: state.has_group('ZAYIN ABNORMALTIES',self.player,amount)) 
                for equip in range(self.options.base_equipment_checks.value):
                    set_rule(self.multiworld.get_location('ZAYIN ARMOR '+str(equip+(count * self.options.base_equipment_checks.value)+1), self.player), lambda state,amount=count+1: state.has_group('ZAYIN ABNORMALTIES',self.player,amount)) 
                    set_rule(self.multiworld.get_location('ZAYIN WEAPON '+str(equip+(count *self.options.base_equipment_checks.value)+1), self.player), lambda state,amount=count+1: state.has_group('ZAYIN ABNORMALTIES',self.player,amount)) 
            for upgrade in range(self.options.upgrade_equipment_checks.value):
                set_rule(self.multiworld.get_location('ZAYIN UPGRADE ARMOR '+str(upgrade+(count *self.options.upgrade_equipment_checks.value)+1), self.player), lambda state,amount=count+1: state.has_group('ZAYIN ABNORMALTIES',self.player,amount) and state.has('SEPHIRA MELTDOWN REWARD: GEBURA',self.player)) 
                set_rule(self.multiworld.get_location('ZAYIN UPGRADE WEAPON '+str(upgrade+(count *self.options.upgrade_equipment_checks.value)+1), self.player), lambda state,amount=count+1: state.has_group('ZAYIN ABNORMALTIES',self.player,amount) and state.has('SEPHIRA MELTDOWN REWARD: GEBURA',self.player)) 

        for count in range(item_table['TETH ABNORMALITY'][1]+item_table['SMALL BIRD'][1]):
            if removedCounts[1] <= count:
                for obs in range(4):
                    set_rule(self.multiworld.get_location('TETH OBSERVE '+str(obs+(count *4)+1), self.player), lambda state,amount=count+1: state.has_group('TETH ABNORMALTIES',self.player,amount)) 
                for equip in range(self.options.base_equipment_checks.value):
                    set_rule(self.multiworld.get_location('TETH ARMOR '+str(equip+(count *self.options.base_equipment_checks.value)+1), self.player), lambda state,amount=count+1: state.has_group('TETH ABNORMALTIES',self.player,amount)) 
                    set_rule(self.multiworld.get_location('TETH WEAPON '+str(equip+(count *self.options.base_equipment_checks.value)+1), self.player), lambda state,amount=count+1: state.has_group('TETH ABNORMALTIES',self.player,amount)) 
            for upgrade in range(self.options.upgrade_equipment_checks.value):
                set_rule(self.multiworld.get_location('TETH UPGRADE ARMOR '+str(upgrade+(count *self.options.upgrade_equipment_checks.value)+1), self.player), lambda state,amount=count+1: state.has_group('TETH ABNORMALTIES',self.player,amount) and state.has('SEPHIRA MELTDOWN REWARD: GEBURA',self.player)) 
                set_rule(self.multiworld.get_location('TETH UPGRADE WEAPON '+str(upgrade+(count *self.options.upgrade_equipment_checks.value)+1), self.player), lambda state,amount=count+1: state.has_group('TETH ABNORMALTIES',self.player,amount) and state.has('SEPHIRA MELTDOWN REWARD: GEBURA',self.player)) 

        for count in range(item_table['HE ABNORMALITY'][1]):
            if removedCounts[2] <= count:
                for obs in range(4):
                    set_rule(self.multiworld.get_location('HE OBSERVE '+str(obs+(count *4)+1), self.player), lambda state,amount=count+1: state.has('HE ABNORMALITY',self.player,amount)) 
                for equip in range(self.options.base_equipment_checks.value):
                    set_rule(self.multiworld.get_location('HE ARMOR '+str(equip+(count *self.options.base_equipment_checks.value)+1), self.player), lambda state,amount=count+1: state.has('HE ABNORMALITY',self.player,amount)) 
                    set_rule(self.multiworld.get_location('HE WEAPON '+str(equip+(count *self.options.base_equipment_checks.value)+1), self.player), lambda state,amount=count+1: state.has('HE ABNORMALITY',self.player,amount)) 
            for upgrade in range(self.options.upgrade_equipment_checks.value):
                set_rule(self.multiworld.get_location('HE UPGRADE ARMOR '+str(upgrade+(count *self.options.upgrade_equipment_checks.value)+1), self.player), lambda state,amount=count+1: state.has('HE ABNORMALITY',self.player,amount) and state.has('SEPHIRA MELTDOWN REWARD: GEBURA',self.player)) 
                set_rule(self.multiworld.get_location('HE UPGRADE WEAPON '+str(upgrade+(count *self.options.upgrade_equipment_checks.value)+1), self.player), lambda state,amount=count+1: state.has('HE ABNORMALITY',self.player,amount) and state.has('SEPHIRA MELTDOWN REWARD: GEBURA',self.player)) 

        for count in range(item_table['WAW ABNORMALITY'][1]+item_table['BIG BIRD'][1]+item_table['LONG BIRD'][1]):
            if removedCounts[3] <= count:
                for obs in range(4):
                    set_rule(self.multiworld.get_location('WAW OBSERVE '+str(obs+(count *4)+1), self.player), lambda state,amount=count+1: state.has_group('WAW ABNORMALTIES',self.player,amount)) 
                for equip in range(self.options.base_equipment_checks.value):
                    set_rule(self.multiworld.get_location('WAW ARMOR '+str(equip+(count *self.options.base_equipment_checks.value)+1), self.player), lambda state,amount=count+1: state.has_group('WAW ABNORMALTIES',self.player,amount)) 
                    set_rule(self.multiworld.get_location('WAW WEAPON '+str(equip+(count *self.options.base_equipment_checks.value)+1), self.player), lambda state,amount=count+1: state.has_group('WAW ABNORMALTIES',self.player,amount)) 
            for upgrade in range(self.options.upgrade_equipment_checks.value):
                set_rule(self.multiworld.get_location('WAW UPGRADE ARMOR '+str(upgrade+(count *self.options.upgrade_equipment_checks.value)+1), self.player), lambda state,amount=count+1: state.has_group('WAW ABNORMALTIES',self.player,amount) and state.has('SEPHIRA MELTDOWN REWARD: GEBURA',self.player)) 
                set_rule(self.multiworld.get_location('WAW UPGRADE WEAPON '+str(upgrade+(count *self.options.upgrade_equipment_checks.value)+1), self.player), lambda state,amount=count+1: state.has_group('WAW ABNORMALTIES',self.player,amount) and state.has('SEPHIRA MELTDOWN REWARD: GEBURA',self.player)) 

        for count in range(item_table['ALEPH ABNORMALITY'][1]):
            if removedCounts[4] <= count:
                for obs in range(4):
                    set_rule(self.multiworld.get_location('ALEPH OBSERVE '+str(obs+(count *4)+1), self.player), lambda state,amount=count+1: state.has_group('ALEPH ABNORMALTIES',self.player,amount)) 
                for equip in range(self.options.base_equipment_checks.value):
                    set_rule(self.multiworld.get_location('ALEPH ARMOR '+str(equip+(count *self.options.base_equipment_checks.value)+1), self.player), lambda state,amount=count+1: state.has_group('ALEPH ABNORMALTIES',self.player,amount)) 
                    set_rule(self.multiworld.get_location('ALEPH WEAPON '+str(equip+(count *self.options.base_equipment_checks.value)+1), self.player), lambda state,amount=count+1: state.has_group('ALEPH ABNORMALTIES',self.player,amount)) 
            for upgrade in range(self.options.upgrade_equipment_checks.value):
                set_rule(self.multiworld.get_location('ALEPH UPGRADE ARMOR '+str(upgrade+(count *self.options.upgrade_equipment_checks.value)+1), self.player), lambda state,amount=count+1: state.has_group('ALEPH ABNORMALTIES',self.player,amount) and state.has('SEPHIRA MELTDOWN REWARD: GEBURA',self.player)) 
                set_rule(self.multiworld.get_location('ALEPH UPGRADE WEAPON '+str(upgrade+(count *self.options.upgrade_equipment_checks.value)+1), self.player), lambda state,amount=count+1: state.has_group('ALEPH ABNORMALTIES',self.player,amount) and state.has('SEPHIRA MELTDOWN REWARD: GEBURA',self.player)) 

        if self.options.apoc_mode != 'disabled':
            for supr in range(location_table['APOCALYPSE BIRD SUPPRESSION'][0]):
                set_rule(self.multiworld.get_location('APOCALYPSE BIRD SUPPRESSION '+str(1+supr),self.player),lambda state: 
                        state.has('SMALL BIRD',self.player) and
                        state.has('LONG BIRD',self.player) and
                        state.has('BIG BIRD',self.player) and 
                        state.can_reach(self.multiworld.get_location('DAY COMPLETED 21', self.player)))


            
    


        if self.options.wn_mode != 'disabled':
            for supr in range(location_table['WHITENIGHT SUPPRESSION'][0]):
                set_rule(self.multiworld.get_location('WHITENIGHT SUPPRESSION '+str(1+supr),self.player),lambda state: state.has('PLAGUE DOCTOR',self.player) and state.can_reach(self.multiworld.get_location('DAY COMPLETED 21', self.player)))




        if self.options.goal_type == 'dissolution':
            set_rule(self.multiworld.get_location('DISSOLUTION GOAL', self.player),lambda state: 
                (state.count('ZAYIN ABNORMALITY',self.player)+
                state.count('TETH ABNORMALITY',self.player)+
                state.count('HE ABNORMALITY',self.player)+
                state.count('WAW ABNORMALITY',self.player)+
                state.count('ALEPH ABNORMALITY',self.player)+
                state.count('PLAGUE DOCTOR',self.player)*2+
                state.count('SMALL BIRD',self.player)+
                state.count('BIG BIRD',self.player)+
                state.count('LONG BIRD',self.player)+
                state.count('TOOL ABNORMALITY',self.player)
                )*4 >= self.options.dissolution_goal.value)

            self.multiworld.get_location('DISSOLUTION GOAL', self.player).place_locked_item(self.create_event("Victory"))
            self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)
            self.goal_location = self.multiworld.get_location('DISSOLUTION GOAL', self.player).address
        elif self.options.goal_type == 'day_and_dissolution':
            set_rule(self.multiworld.get_location('DISSOLUTION GOAL', self.player),lambda state: 
                (state.count('ZAYIN ABNORMALITY',self.player)+
                state.count('TETH ABNORMALITY',self.player)+
                state.count('HE ABNORMALITY',self.player)+
                state.count('WAW ABNORMALITY',self.player)+
                state.count('ALEPH ABNORMALITY',self.player)+
                state.count('PLAGUE DOCTOR',self.player)*2+
                state.count('SMALL BIRD',self.player)+
                state.count('BIG BIRD',self.player)+
                state.count('LONG BIRD',self.player)+
                state.count('TOOL ABNORMALITY',self.player)
                )*4 >= self.options.dissolution_goal.value)

            self.multiworld.get_location('DISSOLUTION GOAL', self.player).place_locked_item(self.create_event("Victory"))
            self.goal_location = self.multiworld.get_location('DISSOLUTION GOAL', self.player).address
            if self.options.day_goal.value != 50:
                self.multiworld.get_location('DAY COMPLETED ' + str(self.options.day_goal.value), self.player).place_locked_item(self.create_event("Victory"))
                self.goal_second = self.multiworld.get_location('DAY COMPLETED ' + str(self.options.day_goal.value), self.player).address
            else :
                self.multiworld.get_location("FINAL DAY COMPLETED", self.player).place_locked_item(self.create_event("Victory"))
                self.goal_second = self.multiworld.get_location("FINAL DAY COMPLETED", self.player).address
            self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player,2)

        elif self.options.goal_type == 'suppression':
            if self.options.suppression_goal == 'malkuth':
                self.multiworld.get_location("MALKUTH SUPPRESSION 1", self.player).place_locked_item(self.create_event("Victory"))
                self.goal_location = self.multiworld.get_location("MALKUTH SUPPRESSION 1", self.player).address
            elif self.options.suppression_goal == 'yesod':
                self.multiworld.get_location("YESOD SUPPRESSION 1", self.player).place_locked_item(self.create_event("Victory"))
                self.goal_location = self.multiworld.get_location("YESOD SUPPRESSION 1", self.player).address
            elif self.options.suppression_goal == 'hod':
                self.multiworld.get_location("HOD SUPPRESSION 1", self.player).place_locked_item(self.create_event("Victory"))
                self.goal_location = self.multiworld.get_location("HOD SUPPRESSION 1", self.player).address
            elif self.options.suppression_goal == 'netzach':
                self.multiworld.get_location("NETZACH SUPPRESSION 1", self.player).place_locked_item(self.create_event("Victory"))
                self.goal_location = self.multiworld.get_location("NETZACH SUPPRESSION 1", self.player).address
            elif self.options.suppression_goal == 'tiphereth':
                self.multiworld.get_location("TIPHERETH SUPPRESSION 1", self.player).place_locked_item(self.create_event("Victory"))
                self.goal_location = self.multiworld.get_location("TIPHERETH SUPPRESSION 1", self.player).address
            elif self.options.suppression_goal == 'gebura':
                self.multiworld.get_location("GEBURA SUPPRESSION 1", self.player).place_locked_item(self.create_event("Victory"))
                self.goal_location = self.multiworld.get_location("GEBURA SUPPRESSION 1", self.player).address
            elif self.options.suppression_goal == 'chesed':
                self.multiworld.get_location("CHESED SUPPRESSION 1", self.player).place_locked_item(self.create_event("Victory"))
                self.goal_location = self.multiworld.get_location("CHESED SUPPRESSION 1", self.player).address
            elif self.options.suppression_goal == 'binah':
                self.multiworld.get_location("BINAH SUPPRESSION 1", self.player).place_locked_item(self.create_event("Victory"))
                self.goal_location = self.multiworld.get_location("BINAH SUPPRESSION 1", self.player).address
            elif self.options.suppression_goal == 'hokma':
                self.multiworld.get_location("BINAH SUPPRESSION 1", self.player).place_locked_item(self.create_event("Victory"))
                self.goal_location = self.multiworld.get_location("HOKMA SUPPRESSION 1", self.player).address
            elif self.options.suppression_goal == 'whitenight':
                self.multiworld.get_location("WHITENIGHT SUPPRESSION 1", self.player).place_locked_item(self.create_event("Victory"))
                self.goal_location = self.multiworld.get_location("WHITENIGHT SUPPRESSION 1", self.player).address
            elif self.options.suppression_goal == 'apocalypsebird':
                self.multiworld.get_location("APOCALYPSE BIRD SUPPRESSION 1", self.player).place_locked_item(self.create_event("Victory"))
                self.goal_location = self.multiworld.get_location("APOCALYPSE BIRD SUPPRESSION 1", self.player).address
            self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)
        else:
        

            self.multiworld.get_location("FINAL DAY COMPLETED", self.player).place_locked_item(self.create_event("Victory"))
            self.goal_location = self.multiworld.get_location("FINAL DAY COMPLETED", self.player).address
            self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)
        
          

    



    def create_event(self, event: str) -> LobItem:
        
        return LobItem(event, ItemClassification.progression, 90000, self.player)
         
   


    def create_items(self)->None:
        removedCounts = [0,0,0,0,0]
        for abno in self.options.starting_abnos.value:
            removedCounts[starting_item_table[abno]] += 1


        local_item_pool: List[LobItem] = []
        for item in item_table.items():
            if item[1][0] == ItemClassification.trap:
                continue
            x = 0
            if item[0] == 'RESEARCH TT2 PROTOCOL':
                pre_item = self.create_item(str(item[0]),item[1][0],item[1][2])
                self.multiworld.push_precollected(pre_item)
                continue
            if item[1][2] >= 100000 and item[1][2] < 100005:
                x = removedCounts[item[1][2]%100000]
            for id in range(x):
                pre_item = self.create_item(str(item[0]),item[1][0],item[1][2])
                self.multiworld.push_precollected(pre_item)
            for id in range(item[1][1]-x): 
                local_item_pool.append(self.create_item(str(item[0]),item[1][0],item[1][2]))
        total_locations = len(self.multiworld.get_unfilled_locations(self.player))
        junk_locations = (total_locations-len(local_item_pool))
        trapped_locations = round(junk_locations * (self.options.trap_percent / 100))
        total_trap_weight = 0
        for trap in trap_table:
            
            total_trap_weight = self.options.trap_weights.value[trap]+total_trap_weight
            
        
        for trap in trap_table:
            trap_data = item_table[trap]
            trap_count = (int)((self.options.trap_weights.value[trap]/total_trap_weight) * trapped_locations)
            
            for i in range(trap_count):
                local_item_pool.append(self.create_item(str(trap),trap_data[0],trap_data[2]))

        event_item_count = 1
        if self.options.goal_type == 'day_and_dissolution':
            event_item_count = 2

        while len(local_item_pool) < total_locations - event_item_count:
            local_item_pool.append(self.create_item('LOB POINTS',ItemClassification.filler,80000))
        self.multiworld.itempool += local_item_pool


                

    

    