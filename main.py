import os
import asyncio
import discord
from funct_config import *
from datetime import datetime
from dotenv import load_dotenv
from get_info import get_price_eth
from discord.ext import tasks, commands
from lib_discord import set_base_embed, set_embed_block, permission_send_message
from crazypool import block_info, get_candidates

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

#========================== INITIALIZE VARIABLE ==========================#
bot = commands.Bot(command_prefix='$')
options = webdriver.ChromeOptions() 
chrome_options = Options()
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=chrome_options)
luck = "0%"

#========================== MAIN ==========================#

def set_message(message, round_share, reward, price_eth):
    reward_for_me = (round_share * reward) / 100
    message = message.replace("reward_for_me", str(round(reward_for_me, 9)))
    reward_in_usd:float = reward_for_me * price_eth
    message = message.replace("reward_in_usd", str(round(reward_in_usd, 2)))
    return (message)

async def send_allMessage(rsp, height, luck):
    account_l = f_get_account()
    price_eth = get_price_eth()
    message_l = block_info(rsp, height, price_eth, luck)
    for i in range(len(account_l)):
        round_share:float = account_l[i]['round_share']
        message = set_message(message_l[1], round_share, message_l[2], price_eth)
        channel = bot.get_channel(account_l[i]['channel'])
        role_id = "<@&" + str(account_l[i]['role_id']) + ">"
        # await asyncio.create_task(permission_send_message(ctx.me, channel)) # A FAIRE
        await channel.send(role_id, embed = set_embed_block(set_base_embed("ETH | New block found !", 0x1ABC9C), message_l[0], message)) # await obligatoire ? Je perd 1s..

@tasks.loop(seconds = 30)
async def find_luck():
    global luck
    driver.refresh()
    luck = None
    luck = driver.find_element(by = By.XPATH, value= '//*[@id="ember349"]/div/div/div/div/div/div/div[3]/div/div[3]/div/div[4]/div/h3/b').text
    await bot.change_presence(activity = discord.Game(name = luck))

@tasks.loop()
async def check_new_block():
    global luck
    rsp = get_candidates()
    if (str(rsp) != "None"):
        height = str(rsp[0]['height'])
        if (height != f_get_height()):
            f_set_height(height)
            asyncio.create_task(send_allMessage(rsp[0], height, luck))
# check if wallet exist into wallet.yml and in crazypool

load_dotenv()
TOKEN  = os.getenv("TOKEN_CrazyBlock")
driver.implicitly_wait(10)
driver.get("https://eth.crazypool.org/#/account/0xd02073950ce250cb9ead35498b9def88385d6e2c/shift")
@bot.event
async def on_ready():
    print("Le bot est prêt !")
    find_luck.start()
    check_new_block.start()
bot.load_extension("commands.add_wallet")
bot.load_extension("commands.test_notif")
bot.load_extension("commands.find_wallet")
bot.load_extension("commands.modify_wallet")
bot.run(TOKEN)
