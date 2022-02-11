import discord
from get_info import get_localtime

def set_base_embed():
    embed = discord.Embed(
        title = "ETH | New block found !",
        color = 0x1ABC9C
    )
    embed.set_thumbnail(url = "https://c.tenor.com/WpekNE8saNQAAAAi/crazypool-logo-spin.gif")
    embed.set_footer(text = "RedMining |", icon_url="https://cdn.discordapp.com/attachments/933874035966754946/940006924143968326/crazypool-logo-spin.png")
    embed.timestamp = get_localtime()
    return (embed)

def set_embed_block(embed, field_name, message):
    embed.add_field(name = field_name, value = message, inline = False)
    return (embed)
