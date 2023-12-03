#---------- Dependencies ----------


import random
import discord
from discord.ext import commands


#---------- Cog setup 1/2 ----------


class basics (commands.Cog) :
    def __init__(self, bot, *args, **kwargs) :
        self.bot = bot
        
        
    #---------- Basic commands ----------
        
    
    @commands.command()
    #Sends link to GDrive Folder with Schwarzfuchs related profile pictures
    async def pb (self, ctx) :
        with open('files/txt/gdrive_link.txt', 'r', encoding = 'utf-8') as GDFile :
            await ctx.channel.send(GDFile.read())

    @commands.command()
    #Meme about my outstanding coding skills
    async def code (self, ctx) :
        await ctx.channel.send(file=discord.File('files/img/maevisss-meme.jpg'))

    @commands.command()
    #Happy Sakamata Chloe gif
    async def happy (self, ctx) :
        authorid = str(ctx.author.id)
        await ctx.channel.send('<@' + authorid + '> ist happy!' ,file=discord.File('files/img/sakamata-chloe.gif'))

    @commands.command()
    #Post info message
    async def info(self, ctx) :
        with open('files/txt/info.txt', 'r',encoding='utf-8') as InfoFile :
            await ctx.channel.send(InfoFile.read())

    @commands.command()
    #Send a list of commands via dm
    async def com(self, ctx) :
        member = ctx.message.author
        with open('files/txt/commands.txt', 'r',encoding='utf-8') as CommandFile :
            await member.send(CommandFile.read())
        await ctx.channel.send('Du hast eine DM mit der Liste erhalte.')


    #---------- Commands with random ----------


    @commands.command()
    #Toss a coin to your witcher~
    async def coin(self, ctx) :
        Ergebnis = random.randint(1, 2)
        if (Ergebnis == 1) :
            await ctx.channel.send('Kopf')
        else :
            await ctx.channel.send('Zahl')

    @commands.command()
    #Random number by user input
    async def randnum(self, ctx) :
        value = ctx.message.content.split('!randnum ')[1]
        await ctx.channel.send(str(random.randint(0, int(value))))


#---------- Cog setup 2/2 ----------


async def setup(bot):
    await bot.add_cog(basics(bot))
    print('Basics wurde geladen')