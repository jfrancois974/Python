""" Auteur: Jean-François BATAILLE

    Date : Mars 2020
    Projet : Apprentissage Python

Objectif:

   Écrire un programme qui imprime la valeur du volume d’une sphère de rayon r, float lu en entrée.
   On rappelle que le volume d’une sphère de rayon r est donné par la formule : 4/3 * Pi * r^3


"""
from math import pi

r = float(input())
aire = float((4 /3) * pi * (r **3))

print(aire)