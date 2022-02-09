import discord
from funct_config import *
from discord.ext import tasks, commands
from lib_discord import set_embed_block
from crazypool import block_info, get_candidates

#========================== INITIALIZE VARIABLE ==========================#
# client = discord.Client()
discord_cmd = commands.Bot(command_prefix='$')

#========================== MAIN ==========================#
async def send_allMessage(rsp, height):
    account_l = f_get_account()
    for i in range(len(account_l)):
        round_share:float = account_l[i]['round_share']
        message_l = block_info(rsp, height, round_share)
        channel = discord_cmd.get_channel(account_l[i]['channel'])
        role_id = "<@&" + str(account_l[i]['role_id']) + ">"
        await channel.send(role_id, embed = set_embed_block(message_l[0], message_l[1]))

@tasks.loop(seconds = 1)
async def check_new_block():
    rsp = get_candidates()
    if (str(rsp) != "None"):
        height = str(rsp[0]['height'])
        if (height != f_get_height()):
            f_set_height(height)
            await send_allMessage(rsp[0], height)

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

@discord_cmd.event
async def on_ready():
    print("Le bot est prêt !")
    check_new_block.start()
discord_cmd.run("OTQwNzQ4MjM5OTk1NTY4MTgw.YgL6Eg.v-_L5aIm5N8szEBxtKkBpQYrfm8")
