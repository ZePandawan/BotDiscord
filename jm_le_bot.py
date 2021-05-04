import discord
import time
import datetime
from random import *

intents = discord.Intents.all()
client = discord.Client(intents = intents)
intents.members = True


prefix = "-"
admins = [421999801685508107,181887983979462656,450305095645528074]
tab8ball = ["Oui","Non","Je sais pas","Bien Sur !","Tu as vraiment cru xDD","La mer noire ?","Est-ce que tu veux vraiment savoir la réponse ?","Fuck ..."]


@client.event
#Quand le bot se connecte et est prêt
async def on_ready() :
    print(datetime.datetime.today(), "Connecté à {0.user}".format(client))
    #Changer l'activité de jeu du bot
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="son maitre chéri"))


@client.event
#Quand un message est reçu
async def on_message(message):

    #Si le message n'est pas envoyé par un bot
    if message.author.bot == False :

        #Si le message commence par le préfixe
        if message.content.startswith(prefix):
            tabMess = message.content.split()

            #Si l'auteur est moi et que la commande est le close
            if message.author.id in admins and message.content == prefix+"close":
                await message.channel.send("Le bot va être éteint")
                await client.close()

            elif message.author.id in admins and tabMess[0] == "-activity" :
                tableauCommande = message.content.split()
                valeur = ""
                for element in tableauCommande:
                    if element != "-" and element != "-activity" and element != "activity":
                        #Faire de la concaténation de chaine avec element
                        valeur = valeur + " " + element
                await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=valeur))
                await message.channel.send("C'est fait ^^")


            #Commande help
            elif message.content == prefix +"help":
                help_embed = discord.Embed(title = "Liste des commandes utilisateurs", description = "Pour avoir plus d'info sur une commande veuillez taper le nom de la commande suivie de help exemple : -pdp help", color = discord.Colour.green())
                help_embed.add_field(name= "Afficher cette aide",value = "-help", inline=False) 
                help_embed.add_field(name= "Photo de profil",value = "-pdp (avec ou sans mention)   ✅" ,inline=False)
                help_embed.add_field(name= "Pierre-Feuille-Ciseaux",value = "-pfc pierre/feuille/ciseaux   ✅", inline=False)
                help_embed.add_field(name= "Afficher le twitch de mon créateur ✅",value = "-twitch", inline=False)  
                help_embed.add_field(name= "Afficher le site préféré de mon créateur ✅",value = "-je veux m'amuser", inline=False)
                help_embed.add_field(name= "Pose une question au bot ✅",value = "-question TaQuestion", inline=False)
                help_embed.add_field(name= "Pourcentage d'amour entre deux personnes ✅",value = "-lovecalc @personne1 @personne2", inline=False) 

                help_embed.add_field(name= "Jeu du Nombre ❌",value = "-jeuDuNombre", inline=False) 
                await message.channel.send(embed = help_embed)            
                #await message.channel.send("Liste des commandes : ``` -help \r -pdp (avec ou sans mentions) \r -pcf (Pierre Feuille Ciseaux) ```")
            
            elif message.content == prefix + "help admin":
                if message.author.id in admins:
                    helpadmin_embed = discord.Embed(title = "Liste des commandes administrateurs", description = "Pour avoir plus d'info sur une commande veuillez taper le nom de la commande suivie de help exemple : -pdp help", color = discord.Colour.green())
                    helpadmin_embed.add_field(name= "Afficher cette aide",value = "-help admin", inline=False) 
                    helpadmin_embed.add_field(name= "Eteindre le bot",value = "-close", inline=False) 
                    helpadmin_embed.add_field(name= "Changer l'activité du bot",value = "-activity ActivitéDonnée", inline=False)
                    await message.channel.send(embed = helpadmin_embed) 
                else:
                    await message.channel.send("Vous n'êtes pas administrateur du bot ! Vous ne pouvez pas accéder à ce menu !")

            #Commande pour afficher pdp
            elif tabMess[0] == "-pdp" :
                pdpTab = message.content.split()
                if message.content == "-pdp help":
                    pdp_embed = discord.Embed(title = "Aide pour la commande \"pdp\"", color = discord.Colour.dark_green())
                    pdp_embed.add_field(name= "Syntaxe : ",value = "-pdp ou alors -pdp @Jean Marie Le Bot" ,inline=False)
                    pdp_embed.add_field(name= "Description : ",value = "Permet d'afficher votre photo de profil si aucune personne n'est mentionnée ou alors la photo de la ou des personnes qui sont mentionnées" ,inline=False)
                    await message.channel.send(embed = pdp_embed) 
                #Si le message contient une mention

                elif pdpTab[0] == "-pdp":
                    if message.mentions != []:
                        tab = message.content.split()
                        if tab[0] == "-pdp":
                            del tab[0]
                            i = 0
                            for element in tab:
                                if "@" in element:
                                    i = i+1
                        print(message.mentions)
                        for j in range(0,i):
                            userMsg = message.mentions[j]
                            nom = str(userMsg.name)
                            url = str(userMsg.avatar_url)
                            await message.channel.send(nom + " : " + url)
                        print(userMsg)
                        
                    else:
                        await message.channel.send(message.author.avatar_url)

            #Commande pour afficher mon Twitch
            elif tabMess[0] == "-twitch":
                tabTwitch = message.content.split()
                if message.content == "-twitch help":
                    twitch_embed = discord.Embed(title = "Aide pour la commande \"twitch\"", color = discord.Colour.dark_green())
                    twitch_embed.add_field(name= "Syntaxe : ",value = "-twitch" ,inline=False)
                    twitch_embed.add_field(name= "Description : ",value = "Permet d'afficher le lien vers le profil Twitch de mon créateur adoré" ,inline=False)
                    await message.channel.send(embed = twitch_embed)
                elif tabTwitch[0] == "-twitch":
                    await message.channel.send("https://www.twitch.tv/zepandawan")

            #Commande secrète
            elif tabMess[0] == "-je" and tabMess[1] == "veux" and tabMess[2] == "m'amuser":
                funTab = message.content.split()
                if message.content == "-je veux m'amuser help":
                    fun_embed = discord.Embed(title = "Aide pour la commande \"je veux m'amuser\"", color = discord.Colour.dark_green())
                    fun_embed.add_field(name= "Syntaxe : ",value = "-je veux m'amuser" ,inline=False)
                    fun_embed.add_field(name= "Description : ",value = "Permet d'afficher le lien vers le site favori de mon créateur adoré" ,inline=False)
                    await message.channel.send(embed = fun_embed)
                elif funTab[0] == "-je" :
                    await message.channel.send("||https://www.pornhub.com||")

            #Commande Pierre Feuille Ciseaux
            elif tabMess[0] == "-pfc":
                tab = message.content.split()
                tabRandom = ["pierre","feuille","ciseaux","papier","ciseau"]
                if message.content == "-pfc help":
                    pdp_embed = discord.Embed(title = "Aide pour la commande \"pfc\"", color = discord.Colour.dark_green())
                    pdp_embed.add_field(name= "Syntaxe : ",value = "-pfc Pierre ou -pfc Feuille ou -pfc Ciseaux" ,inline=False)
                    pdp_embed.add_field(name= "Description : ",value = "Permet de jouer une partie de Pierre Feuille Ciseaux contre un \"bot\"" ,inline=False)
                    await message.channel.send(embed = pdp_embed) 
                elif tab[0] == "-pfc":
                    choix = tab[1].lower()
                    if choix in tabRandom :
                        choixBot = tabRandom[randrange(0,3)]
                        await message.channel.send(choixBot)

                        if choix == choixBot :
                            await message.channel.send("Egalité !")
                        elif choix == "pierre":
                            if choixBot == "feuille":
                                await message.channel.send("Tu as perduuu !")
                            elif choixBot == "ciseaux" or choixBot == "ciseau":
                                await message.channel.send("Bien joué !")
                        elif choix == "feuille" or choix == "papier":
                            if choixBot == "ciseaux":
                                await message.channel.send("Tu as perduuu !")
                            elif choixBot == "pierre":
                                await message.channel.send("Bien joué !")
                        elif choix == "ciseaux":
                            if choixBot == "pierre":
                                await message.channel.send("Tu as perduuu !")
                            elif choixBot == "feuille":
                                await message.channel.send("Bien joué !")
                    else:
                        await message.channel.send(choix + " n'est pas une variable valable !")

                else:
                    await message.channel.send("Mauvaise syntaxe")


            elif tabMess[0] == "-question":
                if message.content == "-question help":
                    question_embed = discord.Embed(title = "Aide pour la commande \"question\"", color = discord.Colour.dark_green())
                    question_embed.add_field(name= "Syntaxe : ",value = "-question Une question sans oublier le \"?\"" ,inline=False)
                    question_embed.add_field(name= "Description : ",value = "Permet de poser une question au bot et il vous répondra !" ,inline=False)
                    await message.channel.send(embed = question_embed) 
                elif "?" in message.content:
                    repBot = tab8ball[randrange(0,len(tab8ball))]
                    await message.channel.send(repBot)
                else:
                    await message.channel.send("Ceci n'est pas une question ou alors n'oubliez pas le \"?\"")


            elif tabMess[0] == "-lovecalc" :
                tab = message.content.split()
                if message.content == "-lovecalc help":
                    love_embed = discord.Embed(title = "Aide pour la commande \"lovecalc\"", color = discord.Colour.dark_green())
                    love_embed.add_field(name= "Syntaxe : ",value = "-lovecalc @personne1 @personne2" ,inline=False)
                    love_embed.add_field(name= "Description : ",value = "Vous donne le pourcentage d'amour entre les deux ping" ,inline=False)
                    await message.channel.send(embed = love_embed) 
                elif tab[0] == "-lovecalc" and len(tab) == 3 and message.mentions != []:
                    print(message.mentions)
                    pourcentage = str(randrange(0,101)) + "%"
                    personne1 = str(message.mentions[0].name)
                    personne2 = str(message.mentions[1].name)
                    result = personne1 + " et " + personne2 + " s'aiment à " + pourcentage
                    await message.channel.send(result)

            #Commande jeu du nombre à compléter
            elif tabMess[0] == "-jeuDuNombre":
                await message.channel.send("Veuillez me dire un nombre entre 1 et 100 !")
                def check_Message(message):
                    return message.author == message.author and message.channel == message.channel
                try:
                    produit = await client.wait_for("message", timeout = 10, check = check_Message)
                except:
                    await message.channel.send("Veuillez réitérer la commande.")
                    return
                message = await message.channel.send(f"La préparation de {produit.content} va commencer. Veuillez valider en réagissant avec ✅. Sinon réagissez avec ❌")
                await message.add_reaction("✅")
                await message.add_reaction("❌")
                def checker_Emoji(reaction, user):
                    return message.author == user and message.id == reaction.message.id and (str(reaction.emoji) == "✅" or str(reaction.emoji) == "❌")
                try:
                    reaction, user = await client.wait_for("reaction_add", timeout = 10, check = checker_Emoji)
                    if reaction.emoji == "✅":
                        await message.channel.send("Passez à la caisse .")
                    else:
                        await message.channel.send("Votre demande d'achat a bien été annulé.")
                except:
                    await message.channel.send("Votre demande d'achat bien été annulé.")

            #Si la commande n'existe pas ou est mal écrite
            else:
                await message.channel.send("Commande non reconnue")

            print(message.content)
    else:
        print(message.content)



#@client.event
#async def on_message_delete(message):
#    print(message.author)
#    await message.channel.send(str(message.author) + " a envoyé " + str(message.content) + " et le message a été supprimé ")



#Lancer le bot
client.run("")
