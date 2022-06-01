import os
from dotenv import load_dotenv
import update
from discord.ext import commands
from blocks.check_new_block import check_new_block
from payments.check_new_payment import check_new_payment
from get_luck import get_luck

#========================== INITIALIZE VARIABLE ==========================#
bot = commands.Bot(command_prefix = '$', help_command = None)

#========================== MAIN ==========================#

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Unknown command, please refer to $help")

load_dotenv()
TOKEN = os.getenv("TOKEN_CrazyBlock")
@bot.event
async def on_ready():
    print("The bot is launched !")
    if not check_new_block.is_running():
        check_new_block.start(bot)
    if not check_new_payment.is_running():
        check_new_payment.start(bot)
    if not get_luck.is_running():
        get_luck.start(bot)
bot.load_extension("commands.add_wallet")
bot.load_extension("commands.remove_wallet")
bot.load_extension("commands.test_notif")
bot.load_extension("commands.find_wallet")
bot.load_extension("commands.modify_wallet")
bot.load_extension("commands.help_command")
bot.load_extension("commands.cmd_notification")
bot.load_extension("commands.cmd_currency")
bot.run(TOKEN)
