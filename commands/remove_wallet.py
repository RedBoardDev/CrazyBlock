import discord
from discord.ext import commands
from funct_config import f_find_account, f_remove_account

class Remove_wallet(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name = "removewallet")
    async def remove_wallet_cmd(self, ctx, wallet: str):
        if (f_find_account(wallet) != None):
            f_remove_account(wallet)
            await ctx.send("User remove successfully !")
        else:
            await ctx.send("This wallet not exists, please check $findwallet")

    @remove_wallet_cmd.error
    async def add_wallet_error(self, ctx, error: commands.CommandError):
        if isinstance(error, commands.ChannelNotReadable):
            await ctx.send('I don''t have permission to write in this room...')
        elif isinstance(error, commands.MissingRequiredArgument):
                await ctx.send('Error: $removewallet wallet')
        elif isinstance(error, commands.CommandNotFound):
            await ctx.send('Command not found...')

def setup(bot):
    bot.add_cog(Remove_wallet(bot))
