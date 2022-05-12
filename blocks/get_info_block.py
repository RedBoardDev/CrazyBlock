from get_info import request_json

#========================== INITIALIZE VARIABLE ==========================#
crazyAPI_block = 'https://eth.crazypool.org/api/blocks'
etherscanAPI_blockInfo = 'https://api.etherscan.io/api?module=block&action=getblockreward&blockno=BLOCK_ID&apikey=VFKV6IWHAFQ3X8P948TCQEFVASCT7YF9QU'

#========================== FUNCTION ==========================#

def get_status_uncle(status):
    if (status == 'True'):
        return (True)
    return (False)

def get_candidates():
    return (request_json('https://www.miningpoolsprofits.com/api/blocks?pool=CrazyPool&size=4&currentPage=0&coin=ETH')['data'])

def block_info(block_l, height, price_eth):
    luck = round(float(block_l["current_luck_calculated"]), 2)
    status_uncle = get_status_uncle(block_l['uncle'])
    reward_mev = int(block_l['block_mev']) / 1000000000000000000
    if (status_uncle):
        height = height + 1 # a revoir
        reward = 1.75 # a revoir
    else:
        reward = int(block_l['block_reward']) / 1000000000000000000
    link = "https://etherscan.io/block/" + str(height)
    message = "\nReward perso : " + "reward_for_me" + " | " + "reward_in_usd" + "$\n" + "Luck : " + (str)(luck) + '%\n'
    message = message + "Uncle : " + str(status_uncle) + "\nPrice ETH : " + str(price_eth) + "$\n" + link
    message_l = ["Reward : " + str(round(reward, 9)) + " ETH" + "\nMEV : " + str(round(reward_mev, 4)) + " ETH", message, reward, reward_mev]
    return (message_l)
