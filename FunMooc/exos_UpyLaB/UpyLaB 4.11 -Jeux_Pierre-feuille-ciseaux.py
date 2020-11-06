
"""
        Auteur: Jean-François BATAILLE

        Date : AVRIL 2020
        Projet : Apprentissage Python 3

Objectif:

    Écrire un programme qui réalise 5 manches du jeu Pierre-feuille-ciseaux entre l’ordinateur et le joueur.
    Chaque manche va consister en :

        la génération (pseudo) aléatoire d’un nombre entre 0 et 2 compris, à l’aide de la fonction randint du module random, qui va représenter le coup de l’ordinateur (0 valant Pierre, 1, Feuille et 2, Ciseaux) ;
        la lecture en entrée (input) d’une valeur entière entre 0 et 2 compris qui représente le coup du joueur ;
        l’affichage du résultat sous une des formes :
            coup_o bat coup_j : points
            coup_o est battu par coup_j : points
            coup_o annule coup_j : points
        où
            coup_o et coup_j sont respectivement le coup de l’ordinateur et du joueur : "Pierre" s’il a joué 0, "Feuille" s’il a joué 1 et "Ciseaux" s’il a joué 2.
            points donne le résultat des manches jusqu’à présent sachant que le compteur points part de zéro, et est incrémenté de un
            chaque fois que le joueur gagne une manche, et décrémenté de un chaque fois que l’ordinateur gagne une manche
            (les match nuls ne modifiant pas le compteur points).

À la fin des cinq manches, votre programme affichera : Perdu, Nul ou Gagné suivant que le compteur est négatif, nul ou strictement positif.

"""

import random

PIERRE = 0
FEUILLE = 1
CISEAUX = 2
score_joueur = 0


def joueur1():
    choix_joueur = int(input())
    if choix_joueur == 0:
        return "Pierre"
    elif choix_joueur == 1:
        return "Feuille"
    else:
        return "Ciseaux"


def ordinateur1():
    choix_ordinateur = random.randint(0, 2)
    if choix_ordinateur == 0:
        return "Pierre"
    elif choix_ordinateur == 1:
        return "Feuille"
    else:
        return "Ciseaux"


def chifoumi(joueur, ordinateur):
    global score_joueur
    if joueur == ordinateur:
        score_joueur = score_joueur
        print(ordinateur, "annule", joueur, ":", score_joueur)

    elif joueur == "Pierre":
        if ordinateur == "Feuille":
            score_joueur = score_joueur - 1
            print(ordinateur, "bat", joueur, ":", score_joueur)

        elif ordinateur == "Ciseaux":
            score_joueur = score_joueur + 1
            print(ordinateur, "est battu par", joueur, ":", score_joueur)

    elif joueur == "Feuille":
        if ordinateur == "Pierre":
            score_joueur = score_joueur + 1
            print(ordinateur, "est battu par", joueur, ":", score_joueur)

        elif ordinateur == "Ciseaux":
            score_joueur = score_joueur - 1
            print(ordinateur, "bat", joueur, ":", score_joueur)

    elif joueur == "Ciseaux":
        if ordinateur == "Pierre":
            score_joueur = score_joueur - 1
            print(ordinateur, "bat", joueur, ":", score_joueur)

        if ordinateur == "Feuille":
            score_joueur = score_joueur + 1
            print(ordinateur, "est battu par", joueur, ":", score_joueur, )


def jeu():
    joueur = joueur1()
    ordinateur = ordinateur1()
    chifoumi(joueur, ordinateur)


s = int(input())
random.seed(s)
for i in range(5):
    jeu()
if score_joueur == 0:
    print("Nul")
elif score_joueur > 0:
    print("Gagné")
else:
    print("Perdu")
