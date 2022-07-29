import random
import discord
from discord.ext import commands

class basics (commands.Cog) :
    def __init__(self, bot, *args, **kwargs) :
        self.bot = bot


    #---------- Simple stuff ----------
        
    
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
    #Just to slap Yukibohras ass
    async def yuki (self, ctx) :
        await ctx.channel.send( "<@445647063137517570> mach mal endlich Rikou!", file = discord.File('files/img/DominaLuna.jpg'))

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
    #Randome Number by user input
    async def randnum(self, ctx) :
        value = ctx.message.content.split('!randnum ')[1]
        await ctx.channel.send(str(random.randint(0, int(value))))

    @commands.command()
    #Common PnP dices
    async def dice(self, ctx) :
        value = ctx.message.content.split('!dice ')[1]
        if value == '4' :
            dice = random.randint(1, 4)
        elif value == '6' :
            dice = random.randint(1, 6)
        elif value == '8' :
            dice = random.randint(1, 8)
        elif value == '10' :
            dice = random.randint(1, 10)
        elif value == '12' :
            dice = random.randint(1, 12)
        elif value == '20' :
            dice = random.randint(1, 20)
        elif value == '100' :
            bigdice = random.randint(1, 10)
            await ctx.channel.send(str(bigdice) + '0')
        else :
            await ctx.channel.send('Dies ist keiner der verfügbaren Würfel. Für eine zufällige Zahl verwende !randome.')
        await ctx.channel.send(dice)


#Setup cog
def setup(bot):
    bot.add_cog(basics(bot))
    print('Basics wurde geladen')