from discord.ext import commands
from funct_config import f_find_account
from lib_discord import set_base_embed, set_embed_info

class Find_wallet(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name = "find_wallet")
    async def find_wallet_cmd(self, ctx, wallet:str):
        data = f_find_account(wallet)
        if (data == None):
            await ctx.send('I couldn''t find this wallet into database...')
        else:
            field_name = str(data['wallet'])
            message = "Role_id: " + str(data['channel']) + "\nRole_id: " + str(data['role_id']) + "\nRound share: " + str(data['round_share'])
            await ctx.send(embed = set_embed_info(set_base_embed("About this wallet...", 0x1ABC9C), field_name, message))

    @find_wallet_cmd.error
    async def add_wallet_error(self, ctx, error: commands.CommandError):
        if isinstance(error, commands.BadArgument):
                await ctx.send('Error: $test wallet')
        elif isinstance(error, commands.CommandNotFound):
            await ctx.send('Command not found...')

def setup(bot):
    bot.add_cog(Find_wallet(bot))
