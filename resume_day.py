from get_info import request_json

#========================== INITIALIZE VARIABLE ==========================#
whattomine_API = 'https://whattomine.com/coins.json'
crazyAPI_stats = 'https://eth.crazypool.org/api/stats'

#========================== FUNCTION ==========================#

hashrate_CrazyPool = request_json(crazyAPI_stats)['hashrate'] / 1000000
print(hashrate_CrazyPool)

req = request_json(whattomine_API)
estimated_rewards24 = float(req['coins']['Ethereum']['estimated_rewards24'])
target_CrazyPool_ETH = estimated_rewards24 * hashrate_CrazyPool / 100
target_miner_ETH = estimated_rewards24 * 406 / 100
print(target_CrazyPool_ETH)

def resume_day():
    hashrate_CrazyPool = request_json(crazyAPI_stats)['hashrate'] / 1000000
    req = request_json(whattomine_API)
    target_CrazyPool_ETH = estimated_rewards24 * hashrate_CrazyPool / 100