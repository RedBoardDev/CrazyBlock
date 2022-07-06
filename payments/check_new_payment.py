from discord.ext import tasks
from get_info import request_json
from send_notification import send_notif_payments
from funct_config import f_get_tx, f_set_tx, f_find_account

#========================== INITIALIZE VARIABLE ==========================#
crazyAPI_block = 'https://eth.crazypool.org/api/payments'

#========================== FUNCTION ==========================#

def get_payment():
    req_json = request_json(crazyAPI_block)
    if (req_json == None):
        return (None)
    return (req_json['payments'])

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
    req_json = get_payment()
    if (req_json == None):
        return
    while (True):
        if (i >= len(req_json)):
            break
        tx_code = req_json[i]['tx']
        if (tx_code == save_tx):
            break
        if (await check_all_tx(bot, req_json[i]) == True):
            save_tx = f_get_tx()
        i += 1
    f_set_tx(get_payment()[0]['tx'])
