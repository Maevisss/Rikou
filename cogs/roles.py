#---------- Dependencies ----------


import discord
from discord.ext import commands


#---------- Array with all roles and the matching emote ----------


rolelist = [["XBOX", "XBOX"], ["PlayStation", "PlayStation"], ["Nintendo", "Nintendo"], ["PC", "Computer"],
                       ["GamePass", "GamePass"], ["AirSoft", "CatGun"], ["YouTube", "YouTube"], ["Twitch", "Twitch"],
                       ["Anime", "RemPout"], ["IT", "Server"], ["Developer", "Terminal"], ["VR", "VR"],
                       ["Schwarzfuchs", "SFD"], ["GameCentral", "GC"]]


#---------- Cog setup 1/2 ----------


class roles (commands.Cog) :
    def __init__(self, bot, *args, **kwargs) :
        self.bot = bot


    #---------- Generate message for roles ----------


    @commands.command()
    async def rolemsg(self, ctx) :
        role = "1063530524259405875" #For developer use only
        user = ctx.author
        
        if discord.utils.get(user.roles, name = 'Developer') is None :
            await ctx.channel.send('Du hast keine Berechtigung diesen Befehl zu nutzen.')
        else :
            with open('files/txt/role_message.txt', 'r', encoding = 'utf-8') as RoleFile :
                RoleMessage = await ctx.channel.send(RoleFile.read())

            #Message.add_Emoji(Name:ID)
            await RoleMessage.add_reaction('<:XBOX:1061629245559935017>')
            await RoleMessage.add_reaction('<:PlayStation:1061629107202437151>')
            await RoleMessage.add_reaction('<:Nintendo:1061629069764075601>')
            await RoleMessage.add_reaction('<:Computer:1061629050281541712>')
            await RoleMessage.add_reaction('<:GamePass:1061629205516927027>')
            await RoleMessage.add_reaction('<:CatGun:1061633180328787988>>')
            await RoleMessage.add_reaction('<:YouTube:1063541188071796777>')
            await RoleMessage.add_reaction('<:Twitch:1063541229138223164>')
            await RoleMessage.add_reaction('<:RemPout:1063551455899951145>')
            await RoleMessage.add_reaction('<:Server:1063554322891284570>')
            await RoleMessage.add_reaction('<:Terminal:1063541718370242572>')
            await RoleMessage.add_reaction('<:VR:1166353764563816489>')
            #Old server roles
            await RoleMessage.add_reaction('<:SFD:1063542308169064528>')
            await RoleMessage.add_reaction('<:GC:1063542584749871225>')


    #---------- Add role on reaction ----------


    @commands.Cog.listener()
    #Add roles when reaction is set
    async def on_raw_reaction_add(self, payload) :

        #Reaction on role message
        with open('files/txt/msg_id_int.txt', 'r') as int_id :
            iid = int_id.read()

        message_id = payload.message_id

        if str(message_id) == str(iid) : #Needs to be static on live bot
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, self.bot.guilds)

            for element in rolelist:
                if payload.emoji.name == element[1]:
                    role = discord.utils.get(guild.roles, name = element[0])
                    await payload.member.add_roles(role)


    @commands.Cog.listener()
    #Remove roles when reaction is removed
    async def on_raw_reaction_remove(self, payload):

        #Reaction on role message
        with open('files/txt/msg_id_int.txt', 'r') as int_id:
            iid = int_id.read()
        message_id = payload.message_id


        if str(message_id) == str(iid):  #Needs to be static on live bot
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g: g.id == guild_id, self.bot.guilds)
            member = await guild.fetch_member(payload.user_id) #Fetch member id, needed for removal

            for element in rolelist:
                if payload.emoji.name == element[1]:
                    role = discord.utils.get(guild.roles, name=element[0])
                    await member.remove_roles(role)


#---------- Cog setup 2/2 ----------


async def setup(bot):
    await bot.add_cog(roles(bot))
    print('Roles wurde geladen')