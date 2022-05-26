from xmlrpc.client import Boolean, boolean
from discord.ext import tasks
from get_info import request_json
from send_notification import send_notif_payments
from funct_config import f_get_tx, f_set_tx, f_find_account

#========================== INITIALIZE VARIABLE ==========================#
crazyAPI_block = 'https://eth.crazypool.org/api/payments'

#========================== FUNCTION ==========================#

def get_x_payment(x):
    req_json = request_json(crazyAPI_block)
    if (req_json == None):
        return (None)
    return (req_json['payments'][x])

async def check_all_tx(bot, req_json) -> bool:
    address = req_json['address']
    account = f_find_account(address)
    if (account != None and account['wallet'] == address):
        if (account['settings']['payments'] == True):
            await send_notif_payments(req_json, account, bot)
        return (True)
    else:
        return (False)

@tasks.loop(seconds = 120)
async def check_new_payment(bot):
    i:int = 0
    save_tx = f_get_tx()
    while (True):
        req_json = get_x_payment(i)
        if (req_json == None):
            continue
        tx = req_json['tx']
        if (tx == save_tx):
            break
        if (await check_all_tx(bot, req_json) == True):
            save_tx = f_get_tx()
        i += 1
    f_set_tx(get_x_payment(0)['tx'])
