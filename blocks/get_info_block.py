from get_info import request_json

#========================== INITIALIZE VARIABLE ==========================#
crazyAPI_block = 'https://eth.crazypool.org/api/blocks'
MPP_API_block = 'https://www.miningpoolsprofits.com/api/blocks?pool=CrazyPool&size=5&currentPage=0&coin=ETH'
etherscanAPI_blockInfo = 'https://api.etherscan.io/api?module=block&action=getblockreward&blockno=BLOCK_ID&apikey=VFKV6IWHAFQ3X8P948TCQEFVASCT7YF9QU'
crazyAPI_blockbyhash = 'https://api.crazypool.org/api/v1/eth/pools/blocks/BLOCK_HASH/hashs'

#========================== FUNCTION ==========================#

def get_candidates():
    req = request_json('https://eth.crazypool.org/api/blocks')
    if (req == None):
        return (None)
    return ((req)['candidates'])

def check_if_uncle(blockMiner):
    if (blockMiner != "0x4f9bebe3adc3c7f647c0023c60f91ac9dffa52d5"):
        return (1)
    return (0)

def get_luck_block(rsp_request_MPP, height:int) -> str:
    luck_block:float = -1
    if (rsp_request_MPP != None):
        for block_info in rsp_request_MPP['data']:
            if (height == block_info['block_number']):
                luck_block:float = block_info['current_luck_calculated']
                break
            if (height > block_info['block_number']):
                break
    if (luck_block == -1):
        return ("-")
    return ((str)(round(luck_block, 2)))

def block_info(height:int):
    luck_block:str = '-'
    rsp_request = request_json(etherscanAPI_blockInfo.replace("BLOCK_ID", str(height)))
    rsp_request_MPP = request_json(MPP_API_block)
    if (rsp_request == None):
        return
    res_request = rsp_request['result']
    try:
        reward:float = float(res_request['blockReward']) / 1000000000000000000
    except:
        reward:float = 0
    uncle = (str)(check_if_uncle(res_request['blockMiner']))
    if (check_if_uncle(res_request['blockMiner']) == 1):
        height = height + 1
        uncle = "True"
        reward:float = (float)(rsp_request_MPP['data'][0]['block_reward']) / 1000000000000000000
    else:
        uncle = "False"
    luck_block:str = get_luck_block(rsp_request_MPP, height)
    link = "https://etherscan.io/block/" + (str)(height)
    reward_block:str = "Reward : " + (str)(round(reward, 9)) + " ETH"
    message_me:str = "\nReward perso : " + "reward_for_me" + " | " + "reward_in_currency" + "$\n" + "Luck : " + luck_block + '%\n'
    message_me:str = message_me + "Uncle : " + uncle + "\nPrice ETH : PRICE_ETH $\n" + link
    message_l:list(str) = [reward_block, message_me, reward]
    return (message_l)


