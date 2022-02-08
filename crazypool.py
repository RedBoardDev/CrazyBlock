import requests
from get_info import get_price_eth

crazyAPI_block = 'https://eth.crazypool.org/api/blocks'
etherscanAPI_blockInfo = 'https://api.etherscan.io/api?module=block&action=getblockreward&blockno=BLOCK_ID&apikey=VFKV6IWHAFQ3X8P948TCQEFVASCT7YF9QU'
etherscan_priceETH = 'https://api.etherscan.io/api?module=stats&action=ethprice&apikey=VFKV6IWHAFQ3X8P948TCQEFVASCT7YF9QU'

def get_candidates():
    return (requests.get(crazyAPI_block).json()['candidates'])

def crazy_block(rsp, height):
    rsp2 = requests.get(etherscanAPI_blockInfo.replace("BLOCK_ID", height)).json()['result']
    reward = int(rsp2['blockReward']) / 1000000000000000000
    reward_for_me = (0.014 * reward) / 100
    reward_in_usd = reward_for_me * get_price_eth(etherscan_priceETH)
    uncle = str(rsp[0]['uncle'])
    orphan = str(rsp[0]['orphan'])
    link = "https://etherscan.io/block/" + str(height)
    message:str = "\nReward perso : " + str(round(reward_for_me, 9)) + " | " + str(round(reward_in_usd, 2)) + "$\n"
    message = message + "Uncle : " + uncle + "\nOrphan : " + orphan + "\nPrice ETH : " + str(get_price_eth(etherscan_priceETH)) + "$\n" + link
    message_l = ["Reward : " + str(round(reward, 9)) + " ETH", message]
    return (message_l)
