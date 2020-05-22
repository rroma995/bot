import discord
from discord.ext import commands


colour = discord.Colour.blue()

class 도움말(commands.Cog):
    """도움말을 보여줍니다"""

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title='도움말', color=colour)
        embed.add_field(name="!한영번역", value="한국어를 영어로 번역합니다.", inline=False)
        embed.add_field(name="!영한번역", value="영어를 한국어로 번역합니다.", inline=False)
        embed.add_field(name="!봇초대", value="봇초대 주소를 보여줍니다", inline=False)
        embed.add_field(name="!코로나", value="한국의 코로나 바이러스 현황을 알려줍니다.", inline=False)
        embed.add_field(name="!채팅청소", value="메시지를 청소합니다(관리자)", inline=False)
        embed.add_field(name="!채팅청소", value="메시지를 청소합니다(관리자)", inline=False)
        embed.add_field(name="!킥", value="맨션한 사람을 추방시킵니다. (관리자)", inline=False)
        embed.add_field(name="!밴", value="맨션한 사람을 밴시킵니다. (관리자)", inline=False)
        embed.add_field(name="!언밴", value="이름#아이디를 하시면 언밴 시킵니다. (관리자)", inline=False)
        embed.add_field(name="!뮤트", value="유저를 뮤트시킵니다.\nMuted라는 역할이 있서야 작동합니다.\nMuted역할은 뮤트의 기능을 추가해주세요 (관리자)", inline=False)
        embed.add_field(name="!언뮤트", value="유저를 언뮤트 시킵니다. (관리자)", inline=False)
        embed.add_field(name="!피드백", value="피드백을 보낼수있는 링크가 나옵니다.", inline=False)
        await ctx.send(embed=embed)
        embed = discord.Embed(title='도움말(노래)', color=colour)
        embed.add_field(name="!플레이", value="노래를 재생합니다.", inline=False)
        embed.add_field(name="!입장", value="봇이 음악 채널에 들어갑니다.", inline=False)
        embed.add_field(name="!멈추기", value="음악을 멈춥니다", inline=False)
        embed.add_field(name="!재생", value="멈춘음악을 다시 재생합니다.", inline=False)
        embed.add_field(name="!종료", value="플레이어를 중지하고 재생 목록을 지우고 음성 채널을 떠납니다.", inline=False)
        embed.add_field(name="!볼륨", value="볼륨을 설정합니다. 0부터 100까지", inline=False)
        embed.add_field(name="!기록삭제", value="재생목록을 지웁니다.", inline=False)
        embed.add_field(name="!스킵", value="음악을 스킵합니다.", inline=False)
        embed.add_field(name="!리스트", value="음악 리스트를 보여줍니다.", inline=False)
        embed.add_field(name="!음악정보", value="음악 정보를 보여줍니다.", inline=False)
        await ctx.send(embed=embed)



def setup(client):
    client.add_cog(도움말(client))