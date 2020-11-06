"""
        Auteur: Jean-François BATAILLE

        Date : AVRIL 2020
        Projet : Apprentissage Python 3
        
Objectif:

    Écrire une fonction booléenne bonne_planete(diametre) qui reçoit en paramètre un nombre représentant le diamètre, en mètres,
    d'une planète candidate. La fonction retourne la valeur True ou False selon que la planète convient ou non.

    Écrire ensuite un programme qui lit un diamètre depuis l'entrée et affiche 

        la chaîne de caractères "Bonne planète" si le résultat de l'appel à la fonction bonne_planete est True
        la chaîne de caractères "Trop petite" sinon

Exemples:
500 affiche: "Bonne planète"
10 affiche: "Trop petite"


"""

import math


def bonne_planete(diametre):
    aire = math.pi * (diametre ** 2)
    if aire >= 50000:
        return True
    else:
        return False


x = int(input())

if bonne_planete(x) == True:
    print("Bonne planète")
else:
    print("Trop petite")
