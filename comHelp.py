import discord
import time
import datetime
from random import *

import variables

intents = discord.Intents.all()
client = discord.Client(intents = intents)
intents.members = True

prefix = variables.prefix

def help():
    help_embed = discord.Embed(title = "Liste des commandes utilisateurs", description = "Pour avoir plus d'info sur une commande veuillez taper le nom de la commande suivie de help exemple : -pdp help", color = discord.Colour.green())
    help_embed.add_field(name= "Afficher cette aide",value = "-help", inline=False) 
    help_embed.add_field(name= "Photo de profil",value = "-pdp (avec ou sans mention)   ✅" ,inline=False)
    help_embed.add_field(name= "Pierre-Feuille-Ciseaux",value = "-pfc pierre/feuille/ciseaux   ✅", inline=False)
    help_embed.add_field(name= "Afficher le twitch de mon créateur ✅",value = "-twitch", inline=False)  
    help_embed.add_field(name= "Afficher le site préféré de mon créateur ✅",value = "-je veux m'amuser", inline=False)
    help_embed.add_field(name= "Pose une question au bot ✅",value = "-question TaQuestion", inline=False)
    help_embed.add_field(name= "Pourcentage d'amour entre deux personnes ✅",value = "-lovecalc @personne1 @personne2", inline=False)
    help_embed.add_field(name= "Jeu du Nombre ❌",value = "-jeuDuNombre", inline=False)
    return help_embed