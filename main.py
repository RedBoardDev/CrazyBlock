import os
from dotenv import load_dotenv
from discord.ext import commands
from check_new_block import check_new_block
from commands import help_command

#========================== INITIALIZE VARIABLE ==========================#
bot = commands.Bot(command_prefix='.', help_command = help_command.Help_command())

#========================== MAIN ==========================#

load_dotenv()
TOKEN  = os.getenv("TOKEN_CrazyBlock")
@bot.event
async def on_ready():
    print("Le bot est prêt !")
    check_new_block.start(bot)
bot.load_extension("commands.add_wallet")
bot.load_extension("commands.test_notif")
bot.load_extension("commands.find_wallet")
bot.load_extension("commands.modify_wallet")
# bot.load_extension("commands.help_command")
bot.run(TOKEN)
