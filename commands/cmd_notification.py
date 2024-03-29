from discord.ext import commands
from funct_config import f_find_account, f_set_flags_settings

class Notification(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name = "setnotif")
    async def cmd_setnotification(self, ctx, wallet:str, param:str, flags:bool):
        data = f_find_account(wallet)
        if (data == None):
            await ctx.send('I couldn''t find this wallet into database...')
        if (param == "blocks" or param == "payments"):
            f_set_flags_settings(wallet, param, flags)
            await ctx.send("Settings modify successfully !")
        else:
            await ctx.send('We can''t find this notification settings: ', param)

def setup(bot):
    bot.add_cog(Notification(bot))
