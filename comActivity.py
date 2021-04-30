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

def activity(message):
    tableauCommande = message.content.split()
    valeur = ""
    for element in tableauCommande:
        if element != "-" and element != "-activity" and element != "activity":
            #Faire de la concaténation de chaine avec element
            valeur = valeur + " " + element
    return valeur