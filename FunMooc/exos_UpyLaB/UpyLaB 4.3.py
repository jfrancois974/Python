"""
    Auteur: Jean-François BATAILLE

    Date : AVRIL 2020
    Projet : Apprentissage Python 3

Objectif:
    Écrire une fonction booléenne premier(n) qui reçoit un nombre entier positif n et qui renvoie
    True si n est un nombre premier,et False sinon.

    Ensuite, écrire un programme qui lit une valeur entière x et affiche, grâce à des appels à la fonction premier,
    tous les nombres premiers strictement inférieurs à x, chacun sur sa propre ligne.


"""

from math import sqrt

from math import sqrt


def premier(n):
    """ renvoie vrai si n est un nombre premier"""
    i = 2
    while i <= sqrt(n) and n % i != 0:
        i += 1
    if i * i > n > 1:
        return True
    elif a == 1:
        pass
    else:
        return False


# code principal

a = int(input())

for i in range(a):
    if premier(i):
        print(i)

"""
Exemple
Avec la donnée lue suivante :

9

le résultat à imprimer vaudra donc

2
3
5
7
"""
