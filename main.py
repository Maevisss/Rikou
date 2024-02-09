#Rikou is a simple, multi-purpose discord bot with server specific features.
#Its pointless to invite this bot to your server, but you can use this as template for your own bot.

#Developed by Maevisss (main developer), LeTak (better eveloper), and Panzerband1337 (I just want the badge inactive developer)


#---------- Dependencies ----------


import os
import json
import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import CommandNotFound
#Python 3.11
#discord.py 2.3


#---------- Config ----------


with open("files/config.json") as config_file:
    config = json.load(config_file)

Mode = config["Mode"]
if Mode == 1 :
    Token = config["TokenLive"]
    prefix = "!"
else :
    Token = config["TokenDev"]
    prefix = "^"

bot = commands.Bot(command_prefix = prefix, intents = discord.Intents.all())


#---------- Core ----------


async def load_cogs() :
    for filename in os.listdir('./cogs') :
        if filename.endswith('.py') :
            await bot.load_extension(f'cogs.{filename[:-3]}')


async def main () :
    await load_cogs()
    await bot.start(Token)


@bot.event
#On Bot login
async def on_ready() :
    if Mode == 0 :
        await bot.change_presence(activity=discord.Game(name='!info'))
        print('Rikou ist online!')
    else :
        await bot.change_presence(activity=discord.Game(name='world.execute(me);'))
        print('RikouDev ist online!')
        

@bot.event
#Send error if command is unknown
async def on_command_error(ctx, error) :
    if isinstance(error, CommandNotFound) :
        await ctx.channel.send('Dieser Befehl ist nicht bekannt. Überprüfe ob du ihn richtig geschrieben hast oder schaue bei !info nach.')
        return


@bot.event
#Bot shouldn't react on own messages
async def on_message(message) :
    if message.author == bot.user :
        return
    else :
        #Just dont ask...
        if 'loli' in message.content.lower() :
            await message.channel.send('<:MatsuLewd:1061639068645068842>')
        elif 'lolis' in message.content.lower() :
            await message.channel.send('<:MatsuLewd:1061639068645068842>')

        #Prevents that on_message kills all commands
        await bot.process_commands(message)


asyncio.run(main())