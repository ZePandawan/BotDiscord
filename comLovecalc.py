import discord
import time
import datetime
from random import *

import variables



intents = discord.Intents.all()
client = discord.Client(intents = intents)
intents.members = True


prefix = variables.prefix


def lovecalc(message):
    tab = message.content.split()
    if message.content == "-lovecalc help":
        love_embed = discord.Embed(title = "Aide pour la commande \"lovecalc\"", color = discord.Colour.dark_green())
        love_embed.add_field(name= "Syntaxe : ",value = "-lovecalc @personne1 @personne2" ,inline=False)
        love_embed.add_field(name= "Description : ",value = "Vous donne le pourcentage d'amour entre les deux ping" ,inline=False)
        return love_embed
    elif tab[0] == "-lovecalc" and len(tab) == 3 and message.mentions != []:
        print(message.mentions)
        pourcentage = str(randrange(0,101)) + "%"
        personne1 = str(message.mentions[0].name)
        personne2 = str(message.mentions[1].name)
        result = personne1 + " et " + personne2 + " s'aiment à " + pourcentage
        return result