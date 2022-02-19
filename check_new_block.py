import asyncio
from discord.ext import tasks
from funct_config import f_get_height, f_set_height
from get_info import get_candidates
from send_notification import send_allMessage

# @tasks.loop()
# async def check_new_block(bot):
#     rsp = get_candidates()
#     if (str(rsp) != "None"):
#         height = str(rsp[0]['height'])
#         if (height != f_get_height()):
#             f_set_height(height)
#             asyncio.create_task(send_allMessage(rsp[0], height, bot))

@tasks.loop()
async def check_new_block(bot):
    rsp = get_candidates()
    if (str(rsp) != "None"):
        for block_l in reversed(rsp):
            height = int(block_l['height'])
            if (height > f_get_height()):
                print(height)
                f_set_height(height)
                asyncio.create_task(send_allMessage(height, bot))
