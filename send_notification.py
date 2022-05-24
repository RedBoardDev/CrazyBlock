from decimal import Decimal
from blocks.get_info_block import block_info
from get_info import get_price_eth
from get_info import request_json
from funct_config import f_get_account, f_get_currency
from lib_discord import set_base_embed, set_embed_block, set_embed_payments
from currency_converter import CurrencyConverter

def convert_usd_to_eur(to_usd:float) -> float:
    c = CurrencyConverter(decimal = True)
    to_eur = c.convert(to_usd, 'USD', 'EUR')
    return (to_eur)

def set_reward_message(message:str, round_share:float, currency:str, reward, price_eth:float) -> str:
    reward_for_me = (round_share * reward) / 100
    if (currency == "EUR"):
        message = message.replace("$", "€")
        price_eth = convert_usd_to_eur(price_eth)
    message = message.replace("PRICE_ETH", str(price_eth))
    message = message.replace("reward_for_me", str(round(reward_for_me, 9)))
    reward_in_currency:float = reward_for_me * price_eth
    message = message.replace("reward_in_currency", str(round(reward_in_currency, 2)))
    return (message)

def get_round_share(wallet:str) -> float:
    url = "https://api.crazypool.org/api/v1/eth/miners/" + wallet + "/round-shares"
    req = request_json(url)['data']
    return ((float)(req / 3001))

async def send_notif_block(height, bot):
    account_l = f_get_account()
    price_eth = get_price_eth()
    message_l = block_info(height)
    for i in range(len(account_l)):
        i_account = account_l[i]
        if (i_account['settings']['blocks'] == True):
            round_share:float = get_round_share(i_account['wallet'])
            currency:str = f_get_currency(i_account['wallet'])
            message = set_reward_message(message_l[1], round_share, currency, message_l[2], price_eth)
            channel = bot.get_channel(i_account['channel'])
            role_id = "<@&" + str(i_account['role_id']) + ">"
            embed = set_embed_block(set_base_embed("ETH | New block found !", "", 0x1ABC9C), message_l[0], message)
            if (channel != None):
                await channel.send(role_id + " | " + str(round(message_l[2], 2)) + " ETH", embed = embed)

async def send_notif_payments(last_payement, i_account, bot):
    price_eth = get_price_eth()
    currency:str = f_get_currency(i_account['wallet'])
    if (currency == "EUR"):
        price_eth = convert_usd_to_eur(price_eth)
    amountPay = last_payement['amountPay'] / 1000000000
    amount_currency = round(amountPay * price_eth, 2)
    amount = str(round(amountPay, 9)) + " ETH | " + str(amount_currency) + '$'
    price_eth_str = "Price ETH: " + str(price_eth) + '$'
    if (currency == "EUR"):
        amount = amount.replace('$', '€')
        price_eth_str = price_eth_str.replace('$', '€')
    role_id = "<@&" + str(i_account['role_id']) + '>'
    channel = bot.get_channel(i_account['channel'])
    embed = set_embed_payments(set_base_embed("ETH | New payments", "", 0x1ABC9C), amount, price_eth_str)
    await channel.send(role_id + " | New payments", embed = embed)
