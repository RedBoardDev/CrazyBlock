import time
import discord
from funct_config import *
from discord.ext import tasks
from lib_discord import set_embed_block
from crazypool import block_info, get_candidates

#========================== INITIALIZE VARIABLE ==========================#
client = discord.Client()

#========================== FUNCTION ==========================#

def get_localtime():
    t = time.localtime()
    current_time = time.strftime("%H:%M", t)
    return (current_time)

#========================== MAIN ==========================#
async def send_allMessage(message_l):
    account_l = f_get_account()
    for i in range(len(account_l)):
        channel = client.get_channel(account_l[i]['channel'])
        role_id = "<@&" + account_l[i]['role_id'] + ">"
        await channel.send(role_id, embed = set_embed_block(message_l[0], message_l[1]))

@tasks.loop(seconds = 1)
async def check_new_block():
    rsp = get_candidates()
    if (str(rsp) != "None"):
        height = str(rsp[0]['height'])
        if (height != f_get_height()):
            f_set_height(height)
            message_l = block_info(rsp[0], height)
            await send_allMessage(message_l)
@client.event
async def on_ready():
    print("Le bot est prêt !")
    check_new_block.start()
client.run("OTQwNzQ4MjM5OTk1NTY4MTgw.YgL6Eg.v-_L5aIm5N8szEBxtKkBpQYrfm8")
