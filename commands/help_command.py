from discord.ext import commands
from lib_discord import set_base_embed

class Help_command(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    # @commands.command(name = "help")
    @commands.group(invoke_without_command = True)
    async def help(self, ctx):
        em = set_base_embed("Help", "Use $help <command>\n Prefix: $", 0x95a5a6)
        cmd_list = "add_wallet - add notification\n"
        cmd_list += "modify_wallet - modify your notification\n"
        cmd_list += "find_wallet - view account information\n"
        cmd_list += "test_notif - test notification\n"
        cmd_list += "setnotif - set settings notification"
        em.add_field(name = "Commands", value = cmd_list)
        await ctx.send(embed = em)

    @help.command()
    async def add_wallet(self, ctx):
        em = set_base_embed("Help - $add_wallet", "$add_wallet <wallet> <round_share> <channel> <role>", 0x95a5a6)
        args_list = "wallet - your wallet crazypool\n"
        args_list += "round_share - your round share (ex: `0.05`)\n"
        args_list += "channel - tag the channel for notification\n"
        args_list += "role - tag the rôle who will be notified"
        em.add_field(name = "Arguments", value = args_list)
        await ctx.send(embed = em)
    
    @help.command()
    async def modify_wallet(self, ctx):
        em = set_base_embed("Help - $modify_wallet", "$modify_wallet <wallet> <round_share> <channel> <role>", 0x95a5a6)
        args_list = "wallet - your wallet crazypool\n"
        args_list += "round_share - your round share (ex: `0.05`)\n"
        args_list += "channel - tag the channel for notification\n"
        args_list += "role - tag the rôle who will be notified"
        em.add_field(name = "Arguments", value = args_list)
        await ctx.send(embed = em)

    @help.command()
    async def find_wallet(self, ctx):
        em = set_base_embed("Help - $find_wallet", "$find_wallet <wallet>", 0x95a5a6)
        args_list = "wallet - your wallet crazypool recorded\n"
        em.add_field(name = "Arguments", value = args_list)
        await ctx.send(embed = em)

    @help.command()
    async def test_notif(self, ctx):
        em = set_base_embed("Help - $test_notif", "$test_notif <wallet>", 0x95a5a6)
        args_list = "wallet - your wallet crazypool recorded\n"
        em.add_field(name = "Arguments", value = args_list)
        await ctx.send(embed = em)

    @help.command()
    async def setnotif(self, ctx):
        em = set_base_embed("Help - $setnotif", "$set_notif <wallet> <settings> <flags>", 0x95a5a6)
        args_list = "wallet - your wallet crazypool recorded\n"
        args_list += "settings - parameter to modify (ex: ""blocks"")\n"
        args_list += "flags - true or false"
        em.add_field(name = "Arguments", value = args_list)
        await ctx.send(embed = em)

def setup(bot):
    bot.add_cog(Help_command(bot))
