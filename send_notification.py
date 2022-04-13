from matplotlib.pyplot import get
import get_luck
from blocks.get_info_block import block_info
from get_info import get_price_eth
from get_info import request_json
from funct_config import f_get_account
from lib_discord import set_base_embed, set_embed_block, set_embed_payments

def set_message(message:str, round_share, reward, price_eth):
    reward_for_me = (round_share * reward) / 100
    message = message.replace("reward_for_me", str(round(reward_for_me, 9)))
    reward_in_usd:float = reward_for_me * price_eth
    message = message.replace("reward_in_usd", str(round(reward_in_usd, 2)))
    return (message)

def get_round_share(wallet:str):
    url = "https://api.crazypool.org/api/v1/eth/miners/" + wallet + "/round-shares"
    req:int = request_json(url)
    return ((float)(req / 30001))

async def send_notif_block(height, bot):
    account_l = f_get_account()
    price_eth = get_price_eth()
    message_l = block_info(height, price_eth, get_luck.luck_CP)
    for i in range(len(account_l)):
        i_account = account_l[i]
        if (i_account['settings']['blocks'] == True):
            round_share:float = get_round_share(i_account['wallet'])
            message = set_message(message_l[1], round_share, message_l[2], price_eth)
            channel = bot.get_channel(i_account['channel'])
            role_id = "<@&" + str(i_account['role_id']) + ">"
            # await asyncio.create_task(permission_send_message(ctx.me, channel)) # A FAIRE
            embed = set_embed_block(set_base_embed("ETH | New block found !", "", 0x1ABC9C), message_l[0], message)
            await channel.send(role_id + " | " + str(round(message_l[2], 2)) + " ETH", embed = embed)

async def send_notif_payments(last_payement, account, bot):
    price_eth = get_price_eth()
    amountPay = last_payement['amountPay'] / 1000000000
    amount_dollars = round(amountPay * price_eth, 2)
    amount = str(round(amountPay, 9)) + " ETH | " + str(amount_dollars) + '$'
    price_eth = "Price ETH: " + str(price_eth) + '$'
    role_id = "<@&" + str(account['role_id']) + '>'
    channel = bot.get_channel(account['channel'])
    embed = set_embed_payments(set_base_embed("ETH | New payments", "", 0x1ABC9C), amount, price_eth)
    await channel.send(role_id + " | New payments", embed = embed)
