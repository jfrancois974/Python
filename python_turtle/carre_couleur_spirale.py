
""" Auteur: Jean-François BATAILLE

    Date : Avril 2020
    Projet : Apprentissage Python 3

Objectif:

   Apprentissage de randint
   turtle 

    
"""
from turtle import *

from random import randint  # on a besoin de random

speed(0)

bgcolor('blue')

x = 1

while x < 400:

    r = randint(0, 255)  # nombres aléatoires
    g = randint(0, 255)  # definition de r, g, b
    b = randint(0, 255)

    colormode(255)

    pencolor(r, g, b)  # integration des couleurs

    fd(1 + x)
    rt(90.911)

    x = x+1

exitonclick()
