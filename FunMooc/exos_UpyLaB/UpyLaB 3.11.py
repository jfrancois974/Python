"""
    Auteur: Jean-François BATAILLE

        Date : AVRIL 2020
        Projet : Apprentissage Python 3

Objectif:

    Écrire un programme qui lit sur input une valeur naturelle n et qui affiche
     à l’écran un carré de n caractères X (majuscule) de côté.

"""

x = int(input())
s = 0
while s != x:
    s = s + 1
    print('X' * x)