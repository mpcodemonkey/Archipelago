from __future__ import annotations
import os
import sys
import asyncio
import shutil
import requests
import json
import time

import ModuleUpdate
ModuleUpdate.update()

import Utils

check_num = 0

###Set up game communication path###
input_path = os.getenv('APPDATA').replace("Roaming", "LocalLow")+"\\Project_Moon\\LobotomyAP\\Input.txt"
output_path  = os.getenv('APPDATA').replace("Roaming", "LocalLow")+"\\Project_Moon\\LobotomyAP\\Output.txt"





###Client###
if __name__ == "__main__":
    Utils.init_logging("LobotomyClient", exception_logger="Client")

from NetUtils import NetworkItem, ClientStatus
from CommonClient import gui_enabled, logger, get_base_parser, ClientCommandProcessor, \
    CommonContext, server_loop


def check_stdin() -> None:
    if Utils.is_windows and sys.stdin:
        print("WARNING: Console input is not routed reliably on Windows, use the GUI instead.")

class LobotomyClientCommandProcessor(ClientCommandProcessor):
    def __init__(self, ctx):
        super().__init__(ctx)

   
    def _cmd_deathlink(self):
        """Use this command to turn Death Link on and off."""
        
            
        if self.ctx.death_link:
            self.ctx.death_link = False
            self.output(f"Death Link turned off")
        else:
            self.ctx.death_link = True
            self.output(f"Death Link turned on")
            
        

class LobotomyContext(CommonContext):
    command_processor: int = LobotomyClientCommandProcessor
    game = "Lobotomy Corporation"
    items_handling = 0b111  # full remote
    

    def __init__(self, server_address, password):
        super(LobotomyContext, self).__init__(server_address, password)
        self.send_index: int = 0
        self.syncing = False
        self.awaiting_bridge = False
        self.slot_data = ""
        self.death_link = False
        self.queue = []
        self.last_write = time.time()
        
        # creates the path variables and makes sure they exsist
        #Linux/proton
        #May need change depending on where proton is installed
        if os.name == "posix":
          basePathProton = ".steam\\steam\\steamapps\\compatdata\\568220\\pfx\\drive_c\\users\\steamuser\\AppData\\LocalLow"
          self.input_path = basePathProton+"\\Project_Moon\\LobotomyAP\\Input.txt"
          self.output_path  = basePathProton+"\\Project_Moon\\LobotomyAP\\Output.txt"
          self.save_path = basePathProton+"\\Project_Moon\\LobotomyAP\\SaveFiles\\"
        #Windows
        else:
            self.input_path = os.getenv('APPDATA').replace("Roaming", "LocalLow")+"\\Project_Moon\\LobotomyAP\\Input.txt"
            self.output_path  = os.getenv('APPDATA').replace("Roaming", "LocalLow")+"\\Project_Moon\\LobotomyAP\\Output.txt"
            self.save_path = os.getenv('APPDATA').replace("Roaming", "LocalLow")+"\\Project_Moon\\LobotomyAP\\SaveFiles\\"
        

        if not os.path.exists(self.save_path):
            os.makedirs(self.save_path)
        if not os.path.exists(self.input_path):
            open(self.input_path,"w").close()
        if not os.path.exists(self.output_path):
            open(self.output_path,"w").close()

        self.victoryLocation1 = 99999999
        self.victoryLocation2 = 99999999
        self.hasSecondaryVictoryCondition = False

    

    def cleanup(self):
        file = open(self.input_path,"w")
        file.write('d{"text":"Client has disconnected"}\n')
        file.close()
            

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super(LobotomyContext, self).server_auth(password_requested)
        await self.get_username()
        await self.send_connect()

    async def connection_closed(self):
        await super(LobotomyContext, self).connection_closed()
        self.cleanup()

    @property
    def endpoints(self):
        if self.server:
            return [self.server]
        else:
            return []

    async def shutdown(self):
        await super(LobotomyContext, self).shutdown()
        self.cleanup()

    def write_queue(self):
        start = time.time()

        try:
            with open(self.input_path, 'a') as f:
                for i in range(len(self.queue)):
                        if(time.time()-start > 0.25):
                            logger.info("queue write timeout")
                            #TODO high traffic mode activate
                            break
                        if(len(self.queue) != 0):
                            f.write(str(self.queue.pop(0))) 
                        else:
                            break
                f.close()
        except Exception as e:
            logger.info(repr(e))
        self.last_write = time.time()


        

    def send_slot_data(self):
                
                    if (len(self.slot_data)==0):
                        self.queue.append("NO DATA\n") 
                    else:
                        self.queue.append(self.slot_data)              
                    

                

    def on_package(self, cmd: str, args: dict):
        try:
            if cmd in {"RoomInfo"}:
                self.seed_name = args['seed_name']

            if cmd in {"Connected"}:
                #for ss in self.checked_locations:
                    #filename = f"send{ss}"
                    #with open(os.path.join(self.game_communication_path, filename), 'w') as f:
                        #f.close()
                #Handle Slot Data
                
                    
                    optionsString  = "c{"
                    optionsString += '"seed":"'+self.seed_name+'",'
                    
                # optionsString += '"replace_leveling":' + str(args['slot_data']['replace_leveling']).lower() + ","
                    
                    optionsString += '"dissolutionGoal":' + str(args['slot_data']['dissolution_goal']) + ","
                    optionsString += '"baseEquipmentChecks":' + str(args['slot_data']['base_equipment_checks']) + ","   
                    optionsString += '"goalInfo":"' + str(args['slot_data']['goal_info']) + '",'
                    
                    optionsString += '"deathlink":' + str(args['slot_data']['deathlink']).lower() + ',' 
                    optionsString += '"deathlinkTrigger":"' + str(args['slot_data']['deathlinkTrigger']) + '",' 
                    optionsString += '"deathlinkEffect":"' + str(args['slot_data']['deathlinkEffect']) + '",' 
                    optionsString += '"deathlinkCount":' + str(args['slot_data']['deathlinkCount']) + "," 
                    
                    optionsString += '"deathlinkGraceTime":' + str(args['slot_data']['deathlinkGrace']) + "," 
                    
                    optionsString += '"upgradeEquipmentChecks":' + str(args['slot_data']['upgrade_equipment_checks'])  + "}\n"
                    

                    for abno in args['slot_data']['starting_abnos']:
                        optionsString += 's{"id":'+abno+'}\n'
                    
                    self.slot_data = optionsString
                    #logger.info("Wrote slotdata:"+self.slot_data)
                    self.victoryLocation1 = args['slot_data']['goal_location']
                    if(args['slot_data']['goal_second'] != 999999999):
                        self.hasSecondaryVictoryCondition = True
                        self.victoryLocation2 = args['slot_data']['goal_second']
                    
                    if(args['slot_data']['deathlink']):
                        
                        self.death_link = True
                        logger.info("Deathlink Activated")

                    self.send_slot_data()
                #End Handle Slot Data
            if cmd in {"PrintJSON"}:
                messageString = ""

                
                for message in args['data']:
                    
                    if 'type' in message.keys():
                        
                        if message['type'] == "player_id":
                            messageString += self.player_names[ int(message["text"])]
                        elif message['type'] == "item_id":
                            messageString += self.item_names.lookup_in_slot(int(message["text"]),args["receiving"])
                        elif message['type'] == "location_id":
                            messageString += self.location_names.lookup_in_slot(int(message["text"]),args["receiving"])
                    else:
                        messageString += str(message['text'])

                        
                messageString = messageString.replace('"',"'")
                lines = messageString.split("\n")
                
                for line in lines:
                    self.queue.append('m{"text":"'+line+'"}\n')
                
                    

            if cmd in {"ReceivedItems"}:
                start_index = args["index"]
                if start_index != len(self.items_received):
                    for item in args['items']:
                        netItem =  NetworkItem(*item)
                        
                        self.queue.append('i{"index":'+str(start_index)+',"id":'+str(netItem.item)+',"player":"'+self.player_names[netItem.player]+'","flags":'+str(netItem.flags)+'}\n')
                        start_index += 1
                    

            
        except Exception as e:
            logger.info(repr(e))
            
           # logger.info("Couldn't open input. Retrying in 1s.")



    def run_gui(self):
        """Import kivy UI system and start running it as self.ui_task."""
        from kvui import GameManager

        class LOLManager(GameManager):
            logging_pairs = [
                ("Client", "Archipelago")
            ]
            base_title = "Archipelago Lobotomy Client"

        self.ui = LOLManager(self)
        self.ui_task = asyncio.create_task(self.ui.async_run(), name="UI")

    def on_deathlink(self, data):
        try:

            self.queue.append('x{"text":"'+data["cause"] +'"}\n')
        except:
            self.queue.append('x{"text":}\n')
        



async def game_watcher(ctx: LobotomyContext):
    
    while not ctx.exit_event.is_set():
        if ctx.death_link and "DeathLink" not in ctx.tags:
            await ctx.update_death_link(ctx.death_link)
        if not ctx.death_link and "DeathLink" in ctx.tags:
            await ctx.update_death_link(ctx.death_link)

        if ctx.syncing == True:
            ctx.send_slot_data()
            sync_msg = [{'cmd': 'Sync'}]
            if ctx.locations_checked:
                sync_msg.append({"cmd": "LocationChecks", "locations": list(ctx.locations_checked)})
            await ctx.send_msgs(sync_msg)
            ctx.syncing = False
        sending = []
        try:
            with open(output_path,'r') as file:
                for line in file:
                    if line[0] == 's':
                        ctx.syncing = True
                        continue
                    if line[0] == 'x':
                        if(ctx.death_link):
                            #logger.info("Sent Death")
                            await ctx.send_death(ctx.player_names[ctx.slot]+" failed as a manager.")
                        
                    location = int(line.rstrip())
                    sending.append(location)
                    ctx.locations_checked.add(location)
                    
                file.close()
        except:
            print("Couldn't open output. Retrying in 1s.")
        try:
            with open(output_path,'w') as file:
                file.write("")
                file.close()
        except:
            print("Couldn't open output. Retrying in 1s.")
        print("Couldn't open output. Retrying in 1s.")
        message = [{"cmd": 'LocationChecks', "locations": sending}]
        await ctx.send_msgs(message)
        if not ctx.finished_game and ctx.victoryLocation1 in ctx.checked_locations:
            if ctx.hasSecondaryVictoryCondition:
                if ctx.victoryLocation2 in ctx.checked_locations:
                    await ctx.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])
                    ctx.finished_game = True 
            else:
                await ctx.send_msgs([{"cmd": "StatusUpdate", "status": ClientStatus.CLIENT_GOAL}])
                
                ctx.finished_game = True
        if(len(ctx.queue)>0 and time.time() - ctx.last_write > 0.25):
            
            ctx.write_queue()
            
        await asyncio.sleep(1)


def launch():
    async def main(args):
        ctx = LobotomyContext(args.connect, args.password)
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="server loop")
        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()

        progression_watcher = asyncio.create_task(
            game_watcher(ctx), name="LobotomyProgressionWatcher")

        await ctx.exit_event.wait()
        ctx.server_address = None

        await progression_watcher

        await ctx.shutdown()

    import colorama

    parser = get_base_parser(description="Lobotomy Client, for text interfacing.")

    args, rest = parser.parse_known_args()
    colorama.init()
    asyncio.run(main(args))
    colorama.deinit()
