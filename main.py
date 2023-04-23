#Rikou is a young, multi-purpose discord bot with very specific features.
#This bot is not meant to be invited to other servers.
#Code is free to use as a template for your own bot. There is no reason to use this trash code aniway.

#Developed by Maevisss (The main Developer) and LeTak (The better Developer)



#---------- Dependencies main ----------



import os
import discord
import asyncio
from discord.ext import commands
from discord.ext.commands import CommandNotFound
#imports may vary from file to file

#Python 3.10
#discord.py 2.1



#---------- Config ----------



#0 = Main Bot
#1 = Developement Bot
Mode = 1

if Mode == 0 : #Change here to switch versions
    #Live
    with open('files/TokenLive.txt', 'r') as TokenFile :
        Token = TokenFile.read()
    with open('files/ID-Live.txt', 'r') as IDFile :
        BotID = IDFile.read()
    prefix = '!'
else :
    #Developement
    with open('files/TokenDev.txt', 'r') as TokenFile :
        Token = TokenFile.read()
    with open('files/ID-Dev.txt', 'r') as IDFile :
        BotID = IDFile.read()
    prefix = '<'

bot = commands.Bot(command_prefix = prefix, intents = discord.Intents.all(), application_id = BotID)



#---------- The core ----------



async def load_cogs() :
    for filename in os.listdir('./cogs') :
        if filename.endswith('.py') :
            await bot.load_extension(f'cogs.{filename[:-3]}')


async def main() :
    await load_cogs()
    await bot.start(Token)


@bot.event #On bot login
async def on_ready() :
    await bot.change_presence(activity=discord.Game(name='!info'))
    if Mode == 0 :
        print('Rikou ist online!')
    else :
        print('RikouDev ist online!')
        

@bot.event #Send error if command is unknown
async def on_command_error(ctx, error) :
    if isinstance(error, CommandNotFound) :
        await ctx.channel.send('Dieser Befehl ist nicht bekannt. Überprüfe ob du ihn richtig geschrieben hast oder schaue bei !info nach.')
        return


@bot.event #Bot shouldn't react on own messages
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