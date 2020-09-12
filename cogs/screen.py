#기본 import 
import discord

#추가 import
import os
import pyautogui

client = discord.Client()

@client.event
#봇이 준비가 되면 콘솔 창에 "ready" 가 출력 됨.
async def on_ready():
    print("ready")

@client.event

async def on_message(message):
    #!screen 을 입력 하면 
    if message.content.startswith('!screen'):
        #캡쳐를 해서 0.png 로 저장하고
        img = pyautogui.screenshot("0.png")
        #!screen 을 친 채널에 0.png 를 보낸다.
        await message.channel.send(file=discord.File("0.png"))
        #그 후 0.png 를 삭제 한다.
        os.remove("0.png")