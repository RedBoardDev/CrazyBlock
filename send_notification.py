from get_info import block_info
from get_info import get_price_eth
from funct_config import f_get_account
from lib_discord import set_base_embed, set_embed_block

def set_message(message:str, round_share, reward, price_eth):
    reward_for_me = (round_share * reward) / 100
    message = message.replace("reward_for_me", str(round(reward_for_me, 9)))
    reward_in_usd:float = reward_for_me * price_eth
    message = message.replace("reward_in_usd", str(round(reward_in_usd, 2)))
    return (message)

async def send_allMessage(rsp, height, bot):
    account_l = f_get_account()
    price_eth = get_price_eth()
    message_l = block_info(rsp, height, price_eth, "- %")
    for i in range(len(account_l)):
        i_account = account_l[i]
        round_share:float = i_account['round_share']
        message = set_message(message_l[1], round_share, message_l[2], price_eth)
        channel = bot.get_channel(i_account['channel'])
        role_id = "<@&" + str(i_account['role_id']) + ">"
        # await asyncio.create_task(permission_send_message(ctx.me, channel)) # A FAIRE
        await channel.send(role_id, embed = set_embed_block(set_base_embed("ETH | New block found !", "", 0x1ABC9C), message_l[0], message))