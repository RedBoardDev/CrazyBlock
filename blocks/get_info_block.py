import get_luck
from get_info import request_json

#========================== INITIALIZE VARIABLE ==========================#
crazyAPI_block = 'https://eth.crazypool.org/api/blocks'
MPP_API_block = 'https://www.miningpoolsprofits.com/api/blocks?pool=CrazyPool&size=5&currentPage=0&coin=ETH'
etherscanAPI_blockInfo = 'https://api.etherscan.io/api?module=block&action=getblockreward&blockno=BLOCK_ID&apikey=VFKV6IWHAFQ3X8P948TCQEFVASCT7YF9QU'

#========================== FUNCTION ==========================#

def get_candidates():
    return (request_json('https://eth.crazypool.org/api/blocks')['candidates'])

def check_if_uncle(blockMiner):
    return (blockMiner != "0x4f9bebe3adc3c7f647c0023c60f91ac9dffa52d5")

def block_info(height):
    rsp_request = request_json(etherscanAPI_blockInfo.replace("BLOCK_ID", str(height)))['result']
    rsp_request_MPP = request_json(MPP_API_block)['data']

    reward = float(rsp_request['blockReward']) / 1000000000000000000
    for block_info in rsp_request_MPP:
        if (block_info['block_number']) == height:
            luck_block:float = block_info['current_luck_calculated']
            if (block_info['uncle'] == False):
                uncle = "False"
            else:
                height = height + 1
                reward = 1.75
                uncle = "True"
            break

    link = "https://etherscan.io/block/" + (str)(height)
    message_all = "Reward : " + (str)(round(reward, 9)) + " ETH"
    message_me = "\nReward perso : " + "reward_for_me" + " | " + "reward_in_currency" + "$\n" + "Luck : " + (str)(round(luck_block, 2)) + '%\n'
    message_me = message_me + "Uncle : " + uncle + "\nPrice ETH : PRICE_ETH $\n" + link
    message_l = [message_all, message_me, reward]
    return (message_l)
