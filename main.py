import os
from dotenv import load_dotenv
from discord.ext import commands
from blocks.check_new_block import check_new_block
from check_new_payment import check_new_payment

#========================== INITIALIZE VARIABLE ==========================#
bot = commands.Bot(command_prefix = '$', help_command = None)

#========================== MAIN ==========================#

load_dotenv()
TOKEN = os.getenv("TOKEN_CrazyBlock")
@bot.event
async def on_ready():
    print("Le bot est prêt !")
    check_new_block.start(bot)
    check_new_payment.start(bot)
bot.load_extension("commands.add_wallet")
bot.load_extension("commands.test_notif")
bot.load_extension("commands.find_wallet")
bot.load_extension("commands.modify_wallet")
bot.load_extension("commands.help_command")
bot.load_extension("commands.cmd_notification")
bot.run(TOKEN)
