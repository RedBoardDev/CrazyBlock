import requests
from datetime import datetime
from get_info import request_json

#========================== INITIALIZE VARIABLE ==========================#
crazyAPI_block = 'https://eth.crazypool.org/api/blocks'
etherscanAPI_blockInfo = 'https://api.etherscan.io/api?module=block&action=getblockreward&blockno=BLOCK_ID&apikey=VFKV6IWHAFQ3X8P948TCQEFVASCT7YF9QU'

#========================== FUNCTION ==========================#

def get_candidates():
    return (request_json(crazyAPI_block)['candidates'])

def block_info(rsp, height, price_eth):
    rsp_request = request_json(etherscanAPI_blockInfo.replace("BLOCK_ID", height))['result']
    reward = int(rsp_request['blockReward']) / 1000000000000000000
    uncle = str(rsp['uncle'])
    orphan = str(rsp['orphan'])
    link = "https://etherscan.io/block/" + str(height)
    message = "\nReward perso : " + "reward_for_me" + " | " + "reward_in_usd" + "$\n"
    speed_test = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
    message = message + "Uncle : " + uncle + "\nOrphan : " + orphan + "\nPrice ETH : " + str(price_eth) + "$\n" + link + "\nSpeed test bot 2: " + speed_test
    message_l = ["Reward : " + str(round(reward, 9)) + " ETH", message, reward]
    return (message_l)
