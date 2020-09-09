import discord
import asyncio
import datetime

client = discord.Client()

#/dm {할말}로 전체DM 전송
@client.event
async def on_message(message):
    if message.content.startswith('!dm'):
        for i in message.guild.members:
            if i.bot == True:
                pass
            else:
                try:
                    msg = message.content[4:]
                    if message.author.id == 726445175869538374:
                        embed = discord.Embed(colour=0x1DDB16, timestamp=message.created_at, title="DM공지")
                        embed.add_field(name="공지사항 입니다 필독 바랍니다.", value=msg, inline=True)
                        embed.set_footer(text=f"감사합니다.")
                        await i.send(embed=embed)
                except:
                    pass
