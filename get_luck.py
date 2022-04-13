from get_info import request_json
from discord import Game
from discord.ext import tasks


#========================== INITIALIZE VARIABLE ==========================#
crazyAPI_stats = 'https://eth.crazypool.org/api/stats'
luck_CP:float

#========================== FUNCTION ==========================#

@tasks.loop(seconds=30)
async def get_luck(bot):
    global luck_CP
    req = request_json(crazyAPI_stats)
    difficulty = req['nodes'][0]['difficulty']
    roundshares = req['stats']['roundShares']
    buff_luck:float = (roundshares / (float)(difficulty)) * 100
    luck_CP = (str)(round(buff_luck, 2))
    luck_str = "Luck: " + luck_CP + "%"
    await bot.change_presence(activity = Game(name = luck_str))
