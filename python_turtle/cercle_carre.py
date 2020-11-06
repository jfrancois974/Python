#!/usr/bin/env python3


from turtle import *
import turtle

# Une fonction carré décalé
turtle.bgcolor('gray')


def carre(avance):
    forward(avance)
    left(90)
    forward(avance)
    left(90)
    forward(avance)
    left(90)
    forward(avance)
    left(95)


# On défini nos variables
couleurs = ["blue", "green", "yellow", "orange", "red", "purple"]
i = 0

# On tooooouuuurne
speed('fast')  # vite
left(90)
while i <= 23:
    color(couleurs[i % 6])

    carre(200)
    carre(200)
    carre(200)

    i += 1
done()
