import discord
import time
import datetime
from random import *

import variables

prefix = variables.prefix
admins = variables.admins

intents = discord.Intents.all()
client = discord.Client(intents = intents)
intents.members = True

def pdp(message):
    nomurl = []

    pdpTab = message.content.split()
    if message.content == "-pdp help":
        pdp_embed = discord.Embed(title = "Aide pour la commande \"pdp\"", color = discord.Colour.dark_green())
        pdp_embed.add_field(name= "Syntaxe : ",value = "-pdp ou alors -pdp @Jean Marie Le Bot" ,inline=False)
        pdp_embed.add_field(name= "Description : ",value = "Permet d'afficher votre photo de profil si aucune personne n'est mentionnée ou alors la photo de la ou des personnes qui sont mentionnées" ,inline=False)
        return pdp_embed  

    #Si le message contient une mention
    elif pdpTab[0] == "-pdp":
        if message.mentions != []:
            tab = message.content.split()
            tableauMentions = []
            del tab[0]
            i = 0
            for element in tab:
                if ("@" in element) and (element not in tableauMentions):
                    i = i+1
                    tableauMentions.append(element)
            print(message.mentions)
            for j in range(0,i):
                userMsg = message.mentions[j]
                if userMsg.name not in nomurl:
                    nomurl.append(str(userMsg.name))
                    nomurl.append(str(userMsg.avatar_url))
                
            print(userMsg)
            return nomurl
            
        else:
            nomUser = str(message.author.name)
            urlUser = str(message.author.avatar_url)
            response = nomUser + " : " + urlUser
            return response