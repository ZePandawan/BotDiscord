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




def helpadmin(message):
    if message.author.id in admins:
        helpadmin_embed = discord.Embed(title = "Liste des commandes administrateurs", description = "Pour avoir plus d'info sur une commande veuillez taper le nom de la commande suivie de help exemple : -pdp help", color = discord.Colour.green())
        helpadmin_embed.add_field(name= "Afficher cette aide",value = "-help admin", inline=False) 
        helpadmin_embed.add_field(name= "Eteindre le bot",value = "-close", inline=False) 
        helpadmin_embed.add_field(name= "Changer l'activité du bot",value = "-activity ActivitéDonnée", inline=False)
        return helpadmin_embed
    else:
        return "Vous n'êtes pas administrateur du bot ! Vous ne pouvez pas accéder à ce menu !"