import asyncio
import discord
from funct_config import *
from datetime import datetime
from get_info import get_price_eth
from discord.ext import tasks, commands
from lib_discord import set_base_embed, set_embed_block
from crazypool import block_info, get_candidates

#========================== INITIALIZE VARIABLE ==========================#
# client = discord.Client()
discord_cmd = commands.Bot(command_prefix='$')

#========================== MAIN ==========================#

def set_message(message, round_share, reward, price_eth):
    reward_for_me = (round_share * reward) / 100
    message = message.replace("reward_for_me", str(round(reward_for_me, 9)))
    reward_in_usd:float = reward_for_me * price_eth
    message = message.replace("reward_in_usd", str(round(reward_in_usd, 2)))
    speed_test = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
    print(speed_test)
    return (message)

async def send_allMessage(rsp, height, embed_base):
    account_l = f_get_account()
    price_eth = get_price_eth()
    message_l = block_info(rsp, height, price_eth)
    for i in range(len(account_l)):
        round_share:float = account_l[i]['round_share']
        message_l[1] = set_message(message_l[1], round_share, message_l[2], price_eth)
        channel = discord_cmd.get_channel(account_l[i]['channel'])
        role_id = "<@&" + str(account_l[i]['role_id']) + ">"
        await channel.send(role_id, embed = set_embed_block(set_base_embed(), message_l[0], message_l[1])) # await obligatoire ? Je perd 1ms..
    print('------------------------------')
    

@tasks.loop()
async def check_new_block(embed_base):
    rsp = get_candidates()
    if (str(rsp) != "None"):
        height = str(rsp[0]['height'])
        if (height != f_get_height()):
            f_set_height(height)
            asyncio.create_task(send_allMessage(rsp[0], height, embed_base))

# check if wallet exist into wallet.yml and in crazypool

@discord_cmd.command()
async def add_wallet(ctx, wallet: str, round_share:float, channel: discord.TextChannel, role: discord.Role):
    f_add_account(wallet, round_share, channel.id, role.id)
    await ctx.send("User added successfully !")

@add_wallet.error
async def add_wallet_error(ctx, error: commands.CommandError):
    if isinstance(error, commands.RoleNotFound):
        await ctx.send('I couldn''t find this role...')
    elif isinstance(error, commands.ChannelNotFound):
        await ctx.send('I couldn''t find this room...')
    elif isinstance(error, commands.ChannelNotReadable):
        await ctx.send('I don''t have permission to write in this room...')
    elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Error: $add_wallet wallet channel_id role_id')
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send('Command not found...')
    else:
        raise error

embed_base = set_base_embed()
@discord_cmd.event
async def on_ready():
    print("Le bot est prêt !")
    check_new_block.start(embed_base)
discord_cmd.run("OTQwNzQ4MjM5OTk1NTY4MTgw.YgL6Eg.v-_L5aIm5N8szEBxtKkBpQYrfm8")
