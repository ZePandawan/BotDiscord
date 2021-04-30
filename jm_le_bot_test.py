import discord
import time
import datetime
from random import *

import variables, comLovecalc, comHelp, comHelpadmin, comActivity, comPdp


intents = discord.Intents.all()
client = discord.Client(intents = intents)
intents.members = True

prefix = variables.prefix
admins = variables.admins



@client.event
#Quand le bot se connecte et est prêt
async def on_ready() :
    print(datetime.datetime.today(), "Connecté à {0.user}".format(client))
    #Changer l'activité de jeu du bot
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="LES DECIDEURS"))


@client.event
async def on_message(message) :
#Si le message n'est pas envoyé par un bot
    if message.author.bot == False :

        #Si le message commence par le préfixe
        if message.content.startswith(prefix):
            tabMess = message.content.split()



            #Si l'auteur est moi et que la commande est le close
            if tabMess[0] == prefix + "lovecalc":
                love_embed = comLovecalc.lovecalc(message)
                try:
                    await message.channel.send(embed = love_embed)
                except AttributeError:
                    await message.channel.send(love_embed)



            elif message.content == prefix +"help": 
                help_embed = comHelp.help()
                await message.channel.send(embed = help_embed)            
            


            elif message.content == prefix + "help admin":
                helpadmin_embed = comHelpadmin.helpadmin(message)
                try:
                    await message.channel.send(embed = helpadmin_embed)
                except AttributeError:
                    await message.channel.send(helpadmin_embed)



            elif message.author.id in admins and tabMess[0] == prefix+"activity" :
                activityBot = comActivity.activity(message)
                await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=activityBot))
                await message.channel.send("C'est fait ^^")



            elif message.author.id in admins and message.content == prefix+"close":
                await message.channel.send("Le bot va être éteint")
                await client.close()
                 
                

            elif tabMess[0] == prefix+"pdp" :
                result = comPdp.pdp(message)
                try:
                    await message.channel.send(embed = result)
                except AttributeError:
                    if type(result) == list :
                        for i in range (0, len(result)):
                            if i % 2 == 0 :
                                nom = result[i]
                            else:
                                url = result[i]
                                await message.channel.send(nom+" "+url)
                    else:
                        await message.channel.send(result)

            

            
                


#Lancer le bot
client.run("ODM2OTQzNDA4MzYyMjkxMjIw.YIlWSg.Q_pGCPkyJKDkmnsS185YcmFkA7w")