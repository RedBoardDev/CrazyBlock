from discord.ext import tasks
import requests
from send_notification import send_notif_payments
from funct_config import f_get_tx, f_set_tx, f_find_account

#========================== INITIALIZE VARIABLE ==========================#
crazyAPI_block = 'https://eth.crazypool.org/api/payments'

#========================== FUNCTION ==========================#

def request_json(url):
    return (requests.get(url).json())
def get_x_payment(x:int):
    req_json = request_json(crazyAPI_block)
    return (req_json['payments'][x])

async def check_all_tx(bot, req_json):
    address = req_json['address']
    i_account = f_find_account(address)
    if (i_account != None and i_account['wallet'] == address):
        if (i_account['settings']['payments'] == True):
            await send_notif_payments(req_json, i_account, bot)
        return (True)
    else:
        return (False)

@tasks.loop(seconds=120)
async def check_new_payment(bot):
    i:int = 0
    save_tx = f_get_tx()
    while (True):
        if (i >= 30):
            break
        req_json = get_x_payment(i)
        tx = req_json['tx']
        if (tx == save_tx):
            break
        if (await check_all_tx(bot, req_json) == True):
            save_tx = f_get_tx()
        i += 1
    f_set_tx(get_x_payment(0)['tx'])
