import os
import discord
from discord.ext import commands

class gear (commands.Cog) :
    def __init__(self, bot, *args, **kwargs) :
        self.bot = bot


    #---------- Manage AirSoft Gear ----------


    @commands.command()
    #List user gear files
    async def showgear (self, ctx) :
        Ordner = os.scandir('files/txt/AirSoft/')
        await ctx.channel.send('Nutzer die ihr Gear angebeben haben :')
        for entry in Ordner :
            await ctx.channel.send(str(entry.name[:-4]))

    @commands.command()
    #Create gear file
    async def creategear (self, ctx) :
        Name = str(ctx.author)
        if os.path.isfile('files/txt/AirSoft/' + Name + '.txt') == True :
            await ctx.channel.send('Du hast bereits dein Gear erstellt.')
        else :
            with open('files/txt/AirSoft/' + Name + '.txt', 'w') as f :
                f.write('')
            await ctx.channel.send('Das Gear von ' + Name + ' wurde erstellt.')

    @commands.command()
    #Add gear to file
    async def addgear (self, ctx, *, arg) :
        Name = str(ctx.message.author)
        if os.path.isfile('files/txt/AirSoft/' + Name + '.txt') == True :
            with open('files/txt/AirSoft/' + Name + '.txt', 'a') as file :
                file.write(arg + '\n')
            await ctx.channel.send('Die Waffe ' + arg + ' wurde zu dem Gear von ' + Name + ' hinzugefügt.')
        else :
            await ctx.channel.send('Du musst erst mit !creategear deine Gear erstellen.')

    @commands.command()
    #Show own gear
    async def mygear (self, ctx) :
        Name = str(ctx.message.author)
        if os.path.isfile('files/txt/AirSoft/' + Name + '.txt') == True :
            with open('files/txt/AirSoft/' + Name + '.txt', 'r') as file :
                gear = file.read()
            if gear != '' :
                await ctx.channel.send(gear)
            else :
                await ctx.channel.send('Dein Gear ist leer.')
        else :
            await ctx.channel.send('Du musst erst mit !creategear deine Gear erstellen.')

    @commands.command()
    #Show gear from other user
    async def seegear (self, ctx, *, arg) :
        if os.path.isfile('files/txt/AirSoft/' + arg + '.txt') == True :
            with open('files/txt/AirSoft/' + arg + '.txt', 'r') as file :
                gear = file.read()
            if gear != '' :
                await ctx.channel.send(gear)
            else :
                await ctx.channel.send('Das Gear von ' + arg + ' ist leer.')
        else :
            await ctx.channel.send('Das angegebene Gear wurde nicht gefunden.')

    @commands.command()
    #Remove item from gear
    async def removegear (self, ctx, *, arg) :
        Name = str(ctx.message.author)
        if os.path.isfile('files/txt/AirSoft/' + Name + '.txt') == True :
            with open('files/txt/AirSoft/' + Name + '.txt', 'r') as file :
                gear = file.read()
            if gear != '' :
                gearlist = gear.split('\n')
                if arg in gearlist :
                    gearlist.remove(str(arg))
                    with open('files/txt/AirSoft/' + Name + '.txt', 'w') as file :
                        for item in gearlist :
                            file.write('%s\n' % item )
                    await ctx.channel.send(arg + ' wurde aus dem Gear von ' + Name + ' entfernt.')
                else :
                    await ctx.channel.send(arg + ' ist nicht Teil deiner Ausrüstung.')
            else :
                await ctx.channel.send('Dein Gear ist leer.')
        else :
            await ctx.channel.send('Du hast noch kein Gear erstellt.')

    @commands.command()
    #Delete own gear
    async def deletegear (self, ctx) :
        Name = str(ctx.message.author)
        if os.path.isfile('files/txt/AirSoft/' + Name + '.txt') == True :
            os.remove('files/txt/AirSoft/' + Name + '.txt')
            await ctx.channel.send('Das Gear von ' + Name + ' wurde gelöscht.')
        else :
            await ctx.channel.send('Du hast kein Gear das gelöscht werden kann.')


#Setup cog
def setup(bot):
    bot.add_cog(gear(bot))
    print('Gear wurde geladen')