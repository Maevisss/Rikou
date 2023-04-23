#---------- Dependencies tarkov ----------



import csv
import discord
from discord.ext import commands



#---------- Setup cog 1/2 ----------



class tarkov (commands.Cog) :
    def __init__(self, bot, *args, **kwargs) :
        self.bot = bot



    #---------- Commands ----------



    @commands.command()
    #Show list of useless eft keys
    async def keys(self, ctx) :
        KeyList = []
        with open('files/TarkovKeys.csv', 'r') as file :
            TarkovKeys = csv.reader(file, delimiter = ';')

        for row in TarkovKeys:
            print(row)
            KeyList.append('{:<15}  {:<15}  {:<20} {:<25}'.format(*row))

        await ctx.channel.send(str(KeyList))


    @commands.command()
    #Add key to file
    async def keyadd(self, ctx,) :
        user = ctx.author
        keyquestions = ['Schlüssel name :', 'Map des Schlüssels :', 'Hinter dem Schloss :', 'Qurestrelevant Ja/Nein :']
        keyinfo = []
        counter = 0

        while counter <= 3 :
            await ctx.channel.send(keyquestions[counter])
            value = await self.bot.wait_for('message', check = lambda message : message.author == user)
            keyinfo.append(value.content)
            counter += 1

        with open('files/TarkovKeys.csv', 'w', encoding = 'UTF8', newline = '') as file :
            writer = csv.writer(file, delimiter = ';')
            writer.writerow(keyinfo)


    @commands.command()
    #Remove key from file
    async def removekey(self, ctx, *, arg) :
        with open('files/txt/eft_keys.txt', 'r') as file :
            keyfile = file.read()
            keylist = keyfile.split('\n')
            if arg in keylist :
                keylist.remove(str(arg))
                with open('files/txt/eft_keys.txt', 'w') as file :
                    for line in keylist :
                        file.write('%s\n' % line )
                    await ctx.channel.send(arg + ' wurde aus der Liste entfernt.')
            else :
                await ctx.channel.send(arg + ' ist nicht in der Liste.')



#---------- Setup cog 2/2 ----------



async def setup(bot) :
    await bot.add_cog(tarkov(bot))
    print('Tarkov wurde geladen')