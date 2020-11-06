""" Auteur: Jean-François BATAILLE

    Date : Mars 2020

    Projet : Apprentissage Python 3

Objectif:

    Écrire un programme qui teste la parité d’un nombre entier lu sur input et imprime:
    True si le nombre est pair, False dans le cas contraire.


"""

a = int(input())

if a % 2 == 0:
    print(True)
else:
    print(False)