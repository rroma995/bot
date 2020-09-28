import discord
import datetime
import json
import urllib.request
import aiohttp
from discord.ext import commands
from urllib.parse import quote
from urllib.request import urlopen, Request, HTTPError

#Naver Open API application ID
client_id = "YeOVJk0bK59ryYiRDIiY"
#Naver Open API application token
client_secret = "ZBHDeMCaMe"
colour = discord.Colour.blue()

class 기타(commands.Cog):
    """기타등등의 기능들을 보여줍니다"""

    def __init__(self, client):
        self.client = client
        self.CBSList = "http://m.safekorea.go.kr/idsiSFK/neo/ext/json/disasterDataList/disasterDataList.json"

    @commands.command(name="한영번역", pass_context=True)
    async def translation(self, ctx, *, trsText):
        """한국어를 영어로 번역합니다."""
        baseurl = "https://openapi.naver.com/v1/papago/n2mt"
        try:
            if len(trsText) == 1:
                await ctx.send("단어 혹은 문장이 입력되지 않았어요. 다시한번 확인해주세요.")
            else:
                combineword = ""
                for word in trsText:
                    combineword += "" + word
                # if entered value is sentence, assemble again and strip blank at both side
                savedCombineword = combineword.strip()
                combineword = quote(savedCombineword)
                print(combineword)
                # Make Query String.
                dataParmas = "source=ko&target=en&text=" + combineword
                # Make a Request Instance
                request = Request(baseurl)
                # add header to packet
                request.add_header("X-Naver-Client-Id", client_id)
                request.add_header("X-Naver-Client-Secret", client_secret)
                response = urlopen(request, data=dataParmas.encode("utf-8"))

                responsedCode = response.getcode()
                if (responsedCode == 200):
                    response_body = response.read()
                    # response_body -> byte string : decode to utf-8
                    api_callResult = response_body.decode('utf-8')
                    # JSON data will be printed as string type. So need to make it back to type JSON(like dictionary)
                    api_callResult = json.loads(api_callResult)
                    # Final Result
                    translatedText = api_callResult['message']['result']["translatedText"]
                    embed = discord.Embed(title="한국어 -> 영어", description="", color=colour)
                    embed.add_field(name="한국어", value=savedCombineword, inline=False)
                    embed.add_field(name="영어", value=translatedText, inline=False)
                    embed.set_thumbnail(url="https://papago.naver.com/static/img/papago_og.png")
                    embed.timestamp = datetime.datetime.utcnow()
                    await ctx.send("번역 완료", embed=embed)
                else:
                    await ctx.send("Error Code : " + responsedCode)
        except HTTPError as e:
            await ctx.send("Translate Failed. HTTPError Occured.")

    @commands.command(name="영한번역", pass_context=True)
    async def displayembed(self, ctx, *, trsText):
        """영어를 한국어로 번역합니다."""
        baseurl = "https://openapi.naver.com/v1/papago/n2mt"
        try:
            if len(trsText) == 1:
                await ctx.send("단어 혹은 문장이 입력되지 않았어요. 다시한번 확인해주세요.")
            else:
                combineword = ""
                for word in trsText:
                    combineword += "" + word
                # if entered value is sentence, assemble again and strip blank at both side
                savedCombineword = combineword.strip()
                combineword = quote(savedCombineword)
                # Make Query String.
                dataParmas = "source=en&target=ko&text=" + combineword
                # Make a Request Instance
                request = Request(baseurl)
                # add header to packet
                request.add_header("X-Naver-Client-Id", client_id)
                request.add_header("X-Naver-Client-Secret", client_secret)
                response = urlopen(request, data=dataParmas.encode("utf-8"))

                responsedCode = response.getcode()
                if (responsedCode == 200):
                    response_body = response.read()
                    # response_body -> byte string : decode to utf-8
                    api_callResult = response_body.decode('utf-8')

                    # JSON data will be printed as string type. So need to make it back to type JSON(like dictionary)
                    api_callResult = json.loads(api_callResult)
                    # Final Result
                    translatedText = api_callResult['message']['result']["translatedText"]
                    embed = discord.Embed(title="영어 -> 한국어", description="", color=colour)
                    embed.add_field(name="영어", value=savedCombineword, inline=False)
                    embed.add_field(name="한국어", value=translatedText, inline=False)
                    embed.set_thumbnail(url="https://papago.naver.com/static/img/papago_og.png")
                    embed.timestamp = datetime.datetime.utcnow()
                    await ctx.send("번역 완료", embed=embed)
                else:
                    await ctx.send("Error Code : " + responsedCode)
        except HTTPError as e:
            await ctx.send("Translate Failed. HTTPError Occured.")

    
        
    @commands.command(name="봇초대", pass_context=True)
    async def invite(self, ctx):
        """봇초대 주소를 보여줍니다"""
        await ctx.send("https://discord.com/api/oauth2/authorize?client_id=754694147214016572&permissions=8&scope=bot")
    
    @commands.command(name="사이트", pass_context=True)
    async def fidbak(self, ctx):
        """아론봇 사이트 주소를 보여줍니다"""
        await ctx.send("https://aaronbot.netlify.app/")

    @commands.command(name="온라인")
    async def servernumber(self, ctx):
        """현재 들어가있는 서버수를 보여줍니다"""
        embed = discord.Embed(color=colour)
        embed.add_field(name="들어가있는 서버수", value=f"{len(self.client.guilds)}개")
        await ctx.send(embed=embed)
    
    @commands.command(name="재난문자")
    async def get_cbs(self, ctx):
        """최근에 발생한 재난문자를 보여줍니다"""
        async with aiohttp.ClientSession() as session:
            async with session.get(self.CBSList) as r:
                data = await r.json()

        embed = discord.Embed(
            title="📢 재난문자",
            description="최근 발송된 3개의 재난문자를 보여줘요.",
            color=0xE71212
        )

        for i in data[:3]:
            embed.add_field(name=i["SJ"], value=i["CONT"], inline=False)
        await ctx.send(embed=embed)
    




def setup(client):
    client.add_cog(기타(client))
