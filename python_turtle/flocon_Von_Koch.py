
""" Auteur: Jean-François BATAILLE

    Date : Avril 2020
    Projet : Apprentissage Python 3

Objectif:

    Creer le flocon de Von Koch :

    - faire une fonction pour dessiner un flocon de Von Koch en fonction de la longueur des côtés du triangle ainsi que du nombre d’étapes permettant choisir le nombre de pics de notre flocon (par exemple, avec 0 et une longueur non nulle, nous avons juste un triangle équilatéral).
    

"""

#!/usr/bin/env python3

import turtle


def courbe_koch(longueur, etape):
    """Fonction récursive pour dessiner une courbe de Von Koch
    (une fonction récursive étant une fonction s'appelant elle-même"""

    if etape == 0:
        turtle.forward(longueur)
    else:
        courbe_koch(longueur/3, etape-1)
        turtle.left(60)
        courbe_koch(longueur/3, etape-1)
        turtle.right(120)
        courbe_koch(longueur/3, etape-1)
        turtle.left(60)
        courbe_koch(longueur/3, etape-1)


def flocon_koch(longueur, etape):
    """Fonction pour dessiner un flocon de Von Koch
    depuis le coin haut gauche"""

    for i in range(3):  # Pour chaque côté du triangle initial
        turtle.color('blue')
        turtle.begin_fill()
        courbe_koch(longueur, etape)  # Courbe de Von Koch
        turtle.right(120)
        turtle.end_fill()
        turtle.done


if __name__ == "__main__":
    flocon_koch(100, 3)
