from discord.ext import commands
from lib_discord import set_base_embed

class Help_command(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.group(invoke_without_command = True)
    async def help(self, ctx):
        em = set_base_embed("Help", "Use $help <command>\n Prefix: $", 0x95a5a6)
        cmd_list = "addwallet - add notification\n"
        cmd_list += "modifywallet - modify your notification\n"
        cmd_list += "findwallet - view account information\n"
        cmd_list += "testnotif - test notification\n"
        cmd_list += "setnotif - set settings notification"
        em.add_field(name = "Commands", value = cmd_list)
        await ctx.send(embed = em)

    @help.command()
    async def add_wallet(self, ctx):
        em = set_base_embed("Help - $addwallet", "$add_wallet <wallet> <channel> <role>", 0x95a5a6)
        args_list = "wallet - your wallet crazypool\n"
        args_list += "channel - tag the channel for notification\n"
        args_list += "role - tag the rôle who will be notified"
        em.add_field(name = "Arguments", value = args_list)
        await ctx.send(embed = em)

    @help.command()
    async def modify_wallet(self, ctx):
        em = set_base_embed("Help - $modifywallet", "$modify_wallet <wallet> <channel> <role>", 0x95a5a6)
        args_list = "wallet - your wallet crazypool\n"
        args_list += "channel - tag the channel for notification\n"
        args_list += "role - tag the rôle who will be notified"
        em.add_field(name = "Arguments", value = args_list)
        await ctx.send(embed = em)

    @help.command()
    async def find_wallet(self, ctx):
        em = set_base_embed("Help - $findwallet", "$find_wallet <wallet>", 0x95a5a6)
        args_list = "wallet - your wallet crazypool recorded\n"
        em.add_field(name = "Arguments", value = args_list)
        await ctx.send(embed = em)

    @help.command()
    async def test_notif(self, ctx):
        em = set_base_embed("Help - $testnotif", "$test_notif <wallet>", 0x95a5a6)
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
