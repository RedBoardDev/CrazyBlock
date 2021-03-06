import discord
from get_info import get_localtime

def set_base_embed(title, description, color):
    embed = discord.Embed(
        title = title,
        color = color,
        description = description
    )
    embed.set_footer(text = "RedMining |", icon_url = "https://cdn.discordapp.com/attachments/897885530895839313/943181488877359184/20210609_213217.jpg")
    embed.timestamp = get_localtime()
    return (embed)

def set_embed_block(embed, field_name, message):
    embed.set_thumbnail(url = "https://c.tenor.com/WpekNE8saNQAAAAi/crazypool-logo-spin.gif")
    embed.add_field(name = field_name, value = message, inline = False)
    return (embed)

def set_embed_payments(embed, field_name, message):
    embed.set_thumbnail(url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSyY7a3pBk35ROogrvsfHvJ4sNx_fzCNJFsyA&usqp=CAU")
    embed.add_field(name = field_name, value = message, inline = False)
    return (embed)

async def permission_send_message(bot_member, channel):
    bot_permissions = channel.permissions_for(bot_member)
    if bot_permissions.send_messages:
        print("The bot has permissions to send messages within the channel!")
    if not bot_permissions.send_messages:
        await channel.set_permissions(bot_member, send_messages = True)

def set_embed_info(embed, field_name, message, field_name_1, message_1):
    embed.add_field(name = field_name, value = message, inline = False)
    embed.add_field(name = field_name_1, value = message_1, inline = False)
    return (embed)
