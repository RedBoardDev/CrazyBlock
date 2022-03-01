import asyncio
from discord.ext import tasks
from get_info import request_json
from send_notification import send_notif_payments
from funct_config import f_get_tx, f_set_tx, f_find_account

#========================== INITIALIZE VARIABLE ==========================#
crazyAPI_block = 'https://eth.crazypool.org/api/payments'

#========================== FUNCTION ==========================#

def get_last_payment():
    req_json = request_json(crazyAPI_block)
    return (req_json['payments'][0])

@tasks.loop(seconds=120)
async def check_new_payment(bot):
    last_payement = get_last_payment()
    last_tx = last_payement['tx']
    if (f_get_tx() != last_tx):
        f_set_tx(last_tx)
        last_address = last_payement['address']
        account = f_find_account(last_address)
        if (account != None and account['wallet'] == last_address):
            if (account['settings']['payments'] == True):
                await send_notif_payments(last_payement, account, bot)