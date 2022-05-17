import discord
from discord.ext import commands
from funct_config import f_add_account, f_find_account

class Add_wallet(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name = "addwallet")
    async def add_wallet_cmd(self, ctx, wallet: str, channel: discord.TextChannel, role: discord.Role):
        if (f_find_account(wallet) == None):
            f_add_account(wallet, channel.id, role.id)
            await ctx.send("User added successfully !")
        else:
            await ctx.send("This wallet already exists, please use $modify_wallet")

    @add_wallet_cmd.error
    async def add_wallet_error(self, ctx, error: commands.CommandError):
        if isinstance(error, commands.ChannelNotFound):
            await ctx.send('I couldn''t find this room...')
        elif isinstance(error, commands.ChannelNotReadable):
            await ctx.send('I don''t have permission to write in this room...')
        elif isinstance(error, commands.MissingRequiredArgument):
                await ctx.send('Error: $add_wallet wallet channel_id role_id')
        elif isinstance(error, commands.CommandNotFound):
            await ctx.send('Command not found...')

def setup(bot):
    bot.add_cog(Add_wallet(bot))
