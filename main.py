import requests
import time
import discord
from discord.ext import tasks
from crazypool import crazy_block
from get_info import *
from lib_discord_epitech import set_embed_block
from set_file import *

#========================== INITIALIZE VARIABLE ==========================#
crazyAPI_block = 'https://eth.crazypool.org/api/blocks'

url0 = 'https://eth.crazypool.org/api/accounts/0xb35ff0343da28525fCE4BD49308920f2B8f7bEd4'
url1 = 'https://api2.hiveos.farm/api/v2/farms/776169/workers/1669282/metrics'
url2 = 'https://api2.hiveos.farm/api/v2/farms/776169/workers'
hiveToken = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC9hcGkiLCJpYXQiOjE2Mjg3OTQ3NjksImV4cCI6MTk0NDE1NDc2OSwibmJmIjoxNjI4Nzk0NzY5LCJqdGkiOjM5Njc1MDc0LCJzdWIiOjM5Njc1MDc0fQ.QwcvWJdodnvt9ZD9NkwPpFTiF7Yo_WFd2BUyZA-4R0Y"
tempLimit = 48
client = discord.Client()

#========================== FUNCTION ==========================#

# balance = get_balance(url0)
# gain_yesterday = get_last_gain_crazy(get_yesterday_date(), url0)
#calcul moyenne total
# status_rig = get_status_rig(url2, hiveToken)
# status_temp = get_status_temp(url1, hiveToken, tempLimit)

def get_localtime():
    t = time.localtime()
    current_time = time.strftime("%H:%M", t)
    return (current_time)

def send_info():
    crazy_request = requests.get(url0).json()
    balance = get_balance(crazy_request)
    gain_yesterday = get_last_gain_crazy(get_yesterday_date(), crazy_request)
    # add to the list in data.py -> rewards
    # calcul moyenne total with data.py -> rewards

#========================== MAIN ==========================#

@tasks.loop(seconds = 1)
async def check_new_block():
    rsp = requests.get(crazyAPI_block).json()['candidates']
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
