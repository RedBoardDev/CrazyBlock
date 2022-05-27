import get_luck
from get_info import request_json

#========================== INITIALIZE VARIABLE ==========================#
crazyAPI_block = 'https://eth.crazypool.org/api/blocks'
MPP_API_block = 'https://www.miningpoolsprofits.com/api/blocks?pool=CrazyPool&size=5&currentPage=0&coin=ETH'
etherscanAPI_blockInfo = 'https://api.etherscan.io/api?module=block&action=getblockreward&blockno=BLOCK_ID&apikey=VFKV6IWHAFQ3X8P948TCQEFVASCT7YF9QU'

#========================== FUNCTION ==========================#

def get_candidates():
    req = request_json('https://eth.crazypool.org/api/blocks')
    if (req == None):
        return (None)
    return ((req)['candidates'])

def check_if_uncle(blockMiner):
    return (blockMiner != "0x4f9bebe3adc3c7f647c0023c60f91ac9dffa52d5")

def block_info(height):
    rsp_request = request_json(etherscanAPI_blockInfo.replace("BLOCK_ID", str(height)))
    rsp_request_MPP = request_json(MPP_API_block)

    if (rsp_request == None):
        return
    res_request = rsp_request['result']
    luck_block:float = float(get_luck.luck_CP)
    uncle = (str)(check_if_uncle(res_request['blockMiner']))
    reward = float(res_request['blockReward']) / 1000000000000000000
    if (rsp_request_MPP != None):
        for block_info in rsp_request_MPP['data']:
            if (block_info['block_number']) == height:
                luck_block:float = block_info['current_luck_calculated']
                uncle = (str)(block_info['uncle'])
                break
    if (uncle == "True"):
        height = height + 1
        reward = 1.75
    link = "https://etherscan.io/block/" + (str)(height)
    rewar_block:str = "Reward : " + (str)(round(reward, 9)) + " ETH"
    message_me:str = "\nReward perso : " + "reward_for_me" + " | " + "reward_in_currency" + "$\n" + "Luck : " + (str)(round(luck_block, 2)) + '%\n'
    message_me:str = message_me + "Uncle : " + uncle + "\nPrice ETH : PRICE_ETH $\n" + link
    message_l:list(str) = [rewar_block, message_me, reward]
    return (message_l)
