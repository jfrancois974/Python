#! /usr/bin/env python3
""" 
auteur: Jean Francois BATAILLE
    date : Avril 2020
    but du programme : tracer une spirale\
            selon certains paramètres donnés en entrée
"""

import turtle


def spirale(couleur, largeur):
    """ Dessine avec turtle une spirale
    paramètres :
    - couleur : la couleur à utiliser
    - largeur : la largeur du tracé"""
    turtle.color(couleur)
    turtle.width(largeur)
    for i in range(100):
        turtle.circle(i*(largeur/2), 90)


while True:
    turtle.reset()
    turtle.speed(0)
    spirale('purple', 5)
