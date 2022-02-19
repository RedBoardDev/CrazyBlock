import requests
from datetime import datetime, timedelta

#========================== INITIALIZE VARIABLE ==========================#
crazyAPI_block = 'https://eth.crazypool.org/api/blocks'
etherscan_priceETH = 'https://api.etherscan.io/api?module=stats&action=ethprice&apikey=VFKV6IWHAFQ3X8P948TCQEFVASCT7YF9QU'
etherscanAPI_blockInfo = 'https://api.etherscan.io/api?module=block&action=getblockreward&blockno=BLOCK_ID&apikey=VFKV6IWHAFQ3X8P948TCQEFVASCT7YF9QU'

#========================== FUNCTION ==========================#

def request_json(url):
    return (requests.get(url).json())

def check_if_uncle(blockMiner):
    return (blockMiner != "0x4f9bebe3adc3c7f647c0023c60f91ac9dffa52d5")

def block_info(height, price_eth, luck):
    rsp_request = request_json(etherscanAPI_blockInfo.replace("BLOCK_ID", str(height)))['result']

    if (check_if_uncle(rsp_request['blockMiner'])):
        height = height + 1
        reward = 1.75
        uncle = "True"
    else:
        reward = int(rsp_request['blockReward']) / 1000000000000000000
        uncle = "False"

    link = "https://etherscan.io/block/" + str(height)
    message = "\nReward perso : " + "reward_for_me" + " | " + "reward_in_usd" + "$\n" + "Luck : " + luck + '\n'
    message = message + "Uncle : " + uncle + "\nPrice ETH : " + str(price_eth) + "$\n" + link
    message_l = ["Reward : " + str(round(reward, 9)) + " ETH", message, reward]
    return (message_l)

def get_candidates():
    return (request_json(crazyAPI_block)['candidates'])

def get_yesterday_date():
    yesterday = datetime.now() - timedelta(1)
    return datetime.strftime(yesterday, '%Y-%m-%d')

def get_price_eth():
    rsp = float(request_json(etherscan_priceETH)['result']['ethusd'])
    return (rsp)

def get_localtime():
    current_time = datetime.now()
    return (current_time)
