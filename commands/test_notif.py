import asyncio
from discord.ext import commands
from funct_config import f_find_account
from lib_discord import set_embed_block, set_base_embed, permission_send_message
from send_notification import set_message

class Test_notif(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name = "test_notif")
    async def test_notif_cmd(self, ctx, wallet:str):
        data = f_find_account(wallet)
        if (data == None):
            await ctx.send('I couldn''t find this wallet into database...')
        else:
            message = "\nReward perso : " + "reward_for_me" + " | " + "reward_in_usd" + "$\n"
            message = message + "Uncle : False\nOrphan : False\nPrice ETH : 666$\nhttps://etherscan.io/block/666"
            message_l = ["Reward : 6.666 ETH", message, 6.666]
            message = set_message(message_l[1], 1, message_l[2], 6.666)
            channel = self.bot.get_channel(data['channel'])
            role_id = "<@&" + str(data['role_id']) + "> Notification test"
            await asyncio.create_task(permission_send_message(ctx.me, channel))
            await channel.send(role_id, embed = set_embed_block(set_base_embed("ETH | New block found !", "", 0x1ABC9C), message_l[0], message))

    @test_notif_cmd.error
    async def add_wallet_error(self, ctx, error: commands.CommandError):
        if isinstance(error, commands.BadArgument):
                await ctx.send('Error: $test wallet')
        elif isinstance(error, commands.CommandNotFound):
            await ctx.send('Command not found...')

def setup(bot):
    bot.add_cog(Test_notif(bot))
