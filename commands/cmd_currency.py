import discord
from discord.ext import commands
from funct_config import f_find_account, f_set_currency

class Change_currency(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name = "setcurrency")
    async def change_currency_cmd(self, ctx, wallet:str, currency:str):
        if (f_find_account(wallet) != None):
            if (f_set_currency(wallet, currency.upper()) == 0):
                await ctx.send("Please choose between USD and EUR !")
            else:
                await ctx.send("Currency modify successfully !")
        else:
            await ctx.send("This wallet not exists")

    @change_currency_cmd.error
    async def add_wallet_error(self, ctx, error: commands.CommandError):
        if isinstance(error, commands.ChannelNotReadable):
            await ctx.send('I don''t have permission to write in this room...')
        elif isinstance(error, commands.MissingRequiredArgument):
                await ctx.send('Error: $setcurrency wallet currency')
        elif isinstance(error, commands.CommandNotFound):
            await ctx.send('Command not found...')

def setup(bot):
    bot.add_cog(Change_currency(bot))
