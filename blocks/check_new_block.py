import time
import asyncio
from get_luck import set_luck_status
from discord.ext import tasks
from funct_config import f_get_height, f_set_height
from blocks.get_info_block import get_candidates
from send_notification import send_notif_block

@tasks.loop(seconds = 10)
async def check_new_block(bot):
    rsp = get_candidates()
    if (str(rsp) != "None"):
        for block_l in reversed(rsp):
            height = int(block_l['height'])
            if (height > f_get_height()):
                f_set_height(height)
                asyncio.create_task(send_notif_block(height, block_l['hash'], bot))
                time.sleep(1)
                await set_luck_status(bot)
