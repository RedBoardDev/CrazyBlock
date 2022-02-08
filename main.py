from ast import Global
from discord.ext import tasks
import requests
import time
import discord
from discord.ext import tasks
from crazypool import crazy_block, get_candidates
from lib_discord_epitech import set_embed_block
from set_file import *

#========================== INITIALIZE VARIABLE ==========================#
client = discord.Client()

#========================== FUNCTION ==========================#

def get_localtime():
    t = time.localtime()
    current_time = time.strftime("%H:%M", t)
    return (current_time)

#========================== MAIN ==========================#

@tasks.loop(seconds = 1)
async def check_new_block():
    rsp = get_candidates()
    if (str(rsp) != "None"):
        height = str(rsp[0]['height'])
        if (height != f_get_height()):
            f_set_height(height)
            message_l = crazy_block(rsp, height)
            channel = client.get_channel(933874035966754946)
            await channel.send("<@&924801318151925830>", embed = set_embed_block(message_l[0], message_l[1]))

@client.event
async def on_ready():
    print("Le bot est prêt !")
    check_new_block.start()
client.run("OTIzNzM3NjgzMzMzOTA2NDUy.YcUXwQ.iDdyjXIHSMws9jv5v_iEIAqQPQM")
