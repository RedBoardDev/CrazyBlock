import discord
from discord.ext import commands
from funct_config import f_find_account
from lib_discord import set_base_embed, set_embed_info

class Help_command(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    # @commands.command(name = "help")
    @commands.group(invoke_without_command = True)
    async def help(self, ctx):
        em = set_base_embed("Help", "Use $help <command>\n Prefix: $", 0x95a5a6)
        # em = discord.Embed(title = "Help", description = "Use $help <command>\n Prefix: $")
        cmd_list = "add_account - add notification\n"
        cmd_list += "modify_account - modify your notification\n"
        cmd_list += "find_account - view account information\n"
        cmd_list += "test_notif - test notification"
        em.add_field(name = "Commands", value = cmd_list)
        await ctx.send(embed = em)

    @help.command()
    async def add(self, ctx):
        em = set_base_embed("Help - $add_account", "$add_account <wallet> <round_share> <channel> <role>", 0x95a5a6)
        args_list = "wallet - your wallet crazypool\n"
        args_list += "round_share - your round share (ex: `0.05`)\n"
        args_list += "channel - tag the channel for notification\n"
        args_list += "role - tag the rôle who will be notified"
        em.add_field(name = "Arguments", value = args_list)
        await ctx.send(embed = em)
    
    @help.command()
    async def add(self, ctx):
        em = set_base_embed("Help - $modify_account", "$modify_account <wallet> <round_share> <channel> <role>", 0x95a5a6)
        args_list = "wallet - your wallet crazypool\n"
        args_list += "round_share - your round share (ex: `0.05`)\n"
        args_list += "channel - tag the channel for notification\n"
        args_list += "role - tag the rôle who will be notified"
        em.add_field(name = "Arguments", value = args_list)
        await ctx.send(embed = em)

    @help.command()
    async def add(self, ctx):
        em = set_base_embed("Help - $find_account", "$find_account <wallet>", 0x95a5a6)
        args_list = "wallet - your wallet crazypool recorded\n"
        em.add_field(name = "Arguments", value = args_list)
        await ctx.send(embed = em)

    @help.command()
    async def add(self, ctx):
        em = set_base_embed("Help - $test_notif", "$test_notif <wallet>", 0x95a5a6)
        args_list = "wallet - your wallet crazypool recorded\n"
        em.add_field(name = "Arguments", value = args_list)
        await ctx.send(embed = em)

def setup(bot):
    bot.add_cog(Help_command(bot))
