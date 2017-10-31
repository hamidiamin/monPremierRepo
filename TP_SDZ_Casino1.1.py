
 

import os #Permet de mettre en pause le programme
from random import randrange #Génère un nombre aléatoire
from math import ceil #Arrondir à l'entier supérieur
 
 
def fonctionSaisie(type, min=0, max=100000):
        #Vérifier la saisie de l'utilisateur
        saisie = min 
        while saisie <= min or saisie > max: # Boucle tant que la saisie n'appartient pas à l'intervalle défini
                 
                #On demande différentes variables à l'utilisateur
                if type == 1: 
                        saisie = input("Quelle somme d'argent êtes-vous prêt à déposer ? ")
                elif type == 2: 
                        print("Sur quel nombre (compris entre ", min, "et ", max, ")vous parier", end="")
                        saisie = input(" ? ")
                elif type == 3: 
                        saisie = input("Combien voulez-vous miser sur ce nombre ? ")
                elif type == 4: 
                        saisie = input("\nVoulez-vous continuer à jouer ? (entrez 0 si vous voulez quitter, entrez tout autre nombre si vous voulez continuer) ")
                                                 
                try: #On teste la valeur saisie en la transformant en nombre entier
                        saisie = int(saisie)
                        saisie = ceil(saisie)
                except ValueError: #Jestion des erreur
                        print("Vous n'avez pas saisi de nombre ! ...\n")
                        saisie = min
                        continue
 
                #On verifie si la valeur est en-dessous ou au-dessus de l'intervalle défini
                if saisie < min and type != 4:
                        if type == 2:
                                print("Vous avez saisi une valeur inférieure à", min, "! Ce n'est pas acceptable...\n")
                        else:
                                print("Vous avez saisi une valeur inférieure à", min, "euros ! Ce n'est pas acceptable...\n")
                elif saisie == min and type != 2 and type != 4:
                                print("Vous avez saisi une valeur égale à", min, "euros ! Ce n'est pas acceptable...\n")
                elif saisie > max and type != 4:
                        if type == 2:
                                print("Vous avez saisi une valeur supérieure à", max, "! Ce n'est pas acceptable...\n")
                        else:
                                print("Vous avez saisi une valeur supérieure à", max, "euros ! Ce n'est pas acceptable...\n")
                else:
                        return(saisie)
 
 
def fonctionRoulette(nombreJoueur, miseJoueur, argentTotalJoueur, min, max):
        nombreGagnant = randrange(min, max) #On génère un nombre aleatoire (roulette)
        print("\nLa roulette tourne et s'arrête sur le numéro", nombreGagnant, "...")
 
        #On teste les 3 différentes options du casino
        if nombreJoueur == nombreGagnant: 
                argentTotalJoueur += ceil(2 * miseJoueur)
                print("Félicitations ! Vous avez misé sur le bon nombre !\nVous avez gagné", ceil(3 * miseJoueur), "euros !")
        elif nombreJoueur % 2 == nombreGagnant % 2: 
                argentTotalJoueur += ceil(-0.5 * miseJoueur)
                print("Ouf ! Vous avez misé sur la bonne couleur !\nVous récupérez", ceil(0.5 * miseJoueur), "euros !")
        else: 
                argentTotalJoueur += ceil(-1 * miseJoueur)
                print("Pas de bol ! Vous avez perdu", ceil(miseJoueur), "euros...")
        #On affiche l'argent du joueur après chaque tour
        print("Votre capital s'élève à", argentTotalJoueur, "euros !")
        return argentTotalJoueur
 
 
#Début du jeu
print("Bienvenue a la roulette...")
 
#Initialisation des variables
borneRouletteMin = 0
borneRouletteMax = 49
continuerPartie = 1
i = 0
argentTotalJoueur = 0
 
#Boucle while permettant de continuer ou d'arrêter de jouer au jeu
while continuerPartie != 0:
 
        #On affiche le numéro du tour
        i += 1
        print("\nTour n°", i)
 
        #On vérifie si l'utilisateur a deposé ou non de l'argent (début de partie ou non)
        if argentTotalJoueur == 0:
                
                type = 1
                argentTotalJoueur = fonctionSaisie(type, 0, 100000)
                argentInitialJoueur = argentTotalJoueur
 
        
                type = 2
                nombreJoueur = fonctionSaisie(type, borneRouletteMin, borneRouletteMax)
 
        
                type = 3
                miseJoueur = fonctionSaisie(type, 0, argentTotalJoueur)
 
        
                argentTotalJoueur = fonctionRoulette(nombreJoueur, miseJoueur, argentTotalJoueur, borneRouletteMin, borneRouletteMax)
 
        
        if argentTotalJoueur > 0:
                type = 4
                continuerPartie = fonctionSaisie(type)
        else:
                continuerPartie = 0
#Sortie de la boucle while (fin du jeu)
 
#Si l'utilisateur a un solde negatif, il doit de l'argent au casino         
if argentTotalJoueur < 0:
        print("\nPlus de thune\n Cu soon, Vous devez", argentTotalJoueur, "euros au casino...")
#Si l'utilisateur a un solde nul, il a donc perdu sa somme initiale
elif argentTotalJoueur == 0:
        print("\nPlus de thune Vous êtes jeté dehors !\nVous avez perdu", argentInitialJoueur, "euros...")
#Sinon (si l'utilisateur a un solde positif)...
else:
        print("\nVous vous retirez du jeu avec", argentTotalJoueur, "euros !")
        #Si l'utilisateur a realisé un profit
        if argentTotalJoueur > argentInitialJoueur:
                print(" Vous avez realisé un gain de", argentTotalJoueur - argentInitialJoueur, "euros !")
        #Si l'utilisateur repart avec la somme qu'il avait au depart
        elif argentTotalJoueur == argentInitialJoueur:
                print(" Vous repartez avec la somme que vous aviez au depart !")
        #Si l'utilisateur repart avec moins que ce qu'il avait au départ
        else:
                print("Vous avez perdu", argentInitialJoueur - argentTotalJoueur, "euros...")
#Message bienveillant du casino (après cette belle arnaque)
print("\n A bientôt :)")
 
# pause system
os.system("pause")