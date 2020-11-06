""" Auteur: Jean-François BATAILLE

    Date : Mars 2020
    Projet : Apprentissage Python 3

Objectif:

    Écrire un programme qui lit deux valeurs entières x et y strictement positives suivies de deux valeurs réelles (float) z et t,
    et qui affiche les valeurs des expressions suivantes, chacune sur une nouvelle ligne :


"""
import math

x = int(input())
y = int(input())
z = float(input())
t = float(input())
print((x - y))
print(x + z)
print(z + t)
print(x * z)
print(x / 2)
print(x / (y + 1))
print(((x + y) * z) / (4 * x))
print(x ** (-1/2))
