import discord
import os
from discord.ext import commands




colour = discord.Colour.blue()


client = commands.Bot(command_prefix='!')
client.remove_command('help')




for filename in os.listdir("cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")

 
@client.event
async def on_ready():
    print("다음으로 로그인합니다")
    print(client.user.name)
    print(client.user.id)
    print('Discord.py 버전 : ' + discord.__version__)
    print("bot starting..")#봇 시작이라고 뜨게하기
    print("==========")
    await client.change_presence(activity=discord.Game('〔🔹포코봇🔹〕 !도움'))







access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
