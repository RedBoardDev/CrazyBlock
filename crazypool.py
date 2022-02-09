import requests
from get_info import get_price_eth, request_json

#========================== INITIALIZE VARIABLE ==========================#
crazyAPI_block = 'https://eth.crazypool.org/api/blocks'
etherscanAPI_blockInfo = 'https://api.etherscan.io/api?module=block&action=getblockreward&blockno=BLOCK_ID&apikey=VFKV6IWHAFQ3X8P948TCQEFVASCT7YF9QU'

#========================== FUNCTION ==========================#

def get_candidates():
    return (request_json(crazyAPI_block)['candidates'])

def block_info(rsp, height, round_share):
    rsp_request = request_json(etherscanAPI_blockInfo.replace("BLOCK_ID", height))['result']
    reward = int(rsp_request['blockReward']) / 1000000000000000000
    reward_for_me = (round_share * reward) / 100
    price_eth = get_price_eth()
    reward_in_usd = reward_for_me * price_eth
    uncle = str(rsp['uncle'])
    orphan = str(rsp['orphan'])
    link = "https://etherscan.io/block/" + str(height)
    message = "\nReward perso : " + str(round(reward_for_me, 9)) + " | " + str(round(reward_in_usd, 2)) + "$\n"
    message = message + "Uncle : " + uncle + "\nOrphan : " + orphan + "\nPrice ETH : " + str(price_eth) + "$\n" + link
    message_l = ["Reward : " + str(round(reward, 9)) + " ETH", message]
    return (message_l)
