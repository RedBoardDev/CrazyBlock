import requests
from datetime import datetime, timedelta

#========================== INITIALIZE VARIABLE ==========================#
crazyAPI_block = 'https://eth.crazypool.org/api/blocks'
etherscan_priceETH = 'https://api.etherscan.io/api?module=stats&action=ethprice&apikey=VFKV6IWHAFQ3X8P948TCQEFVASCT7YF9QU'
etherscanAPI_blockInfo = 'https://api.etherscan.io/api?module=block&action=getblockreward&blockno=BLOCK_ID&apikey=VFKV6IWHAFQ3X8P948TCQEFVASCT7YF9QU'

#========================== FUNCTION ==========================#

def request_json(url):
    return (requests.get(url).json())

def get_candidates():
    return (request_json(crazyAPI_block)['candidates'])

def block_info(rsp, height, price_eth, luck):
    rsp_request = request_json(etherscanAPI_blockInfo.replace("BLOCK_ID", height))['result']
    reward = int(rsp_request['blockReward']) / 1000000000000000000
    uncle = str(rsp['uncle'])
    orphan = str(rsp['orphan'])
    link = "https://etherscan.io/block/" + str(height)
    message = "\nReward perso : " + "reward_for_me" + " | " + "reward_in_usd" + "$\n" + "Luck : " + luck + '\n'
    message = message + "Uncle : " + uncle + "\nOrphan : " + orphan + "\nPrice ETH : " + str(price_eth) + "$\n" + link
    message_l = ["Reward : " + str(round(reward, 9)) + " ETH", message, reward]
    return (message_l)

def get_yesterday_date():
    yesterday = datetime.now() - timedelta(1)
    return datetime.strftime(yesterday, '%Y-%m-%d')

def get_price_eth():
    rsp = float(request_json(etherscan_priceETH)['result']['ethusd'])
    return (rsp)

def get_localtime():
    current_time = datetime.now()
    return (current_time)
