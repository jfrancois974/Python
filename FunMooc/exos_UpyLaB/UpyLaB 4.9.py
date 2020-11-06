"""
        Auteur: Jean-François BATAILLE

        Date : AVRIL 2020
        Projet : Apprentissage Python 3

Objectif:
    En mathématiques, et plus particulièrement en combinatoire, les nombres de Catalan forment une suite d’entiers naturels
    utilisée dans divers problèmes de dénombrement.

    Ils sont nommés ainsi en l’honneur du mathématicien belge Eugène Charles Catalan (1814-1894).

    Les dix premiers nombres de Catalan (pour n de 0 à 9) sont : 
        1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862.

    Le nombre de Catalan d’indice n, appelé n-ième nombre de Catalan, est défini par : c(n)= (2n)! / (n+1)! * n!
    
    Nous vous demandons d’écrire une fonction catalan(n), où n est un nombre entier positif ou nul,
    qui renvoie la valeur du  n-ième nombre de Catalan.    

Exemples:
    catalan(5) doit retourner 42 
    catalan(0) doit retourner 1

"""

from math import factorial


def catalan(n):
    res = factorial(2 * n) / (factorial(n + 1) * factorial(n))
    return int(res)


print(catalan(5))


# Quand on a oublié les factoriels

def catalan(n):
    if n == 0 or n == 1:
        return 1

    catalan = [0 for i in range(n + 1)]

    catalan[0] = 1
    catalan[1] = 1

    for i in range(2, n + 1):
        catalan[i] = 0
        for j in range(i):
            catalan[i] = catalan[i] + catalan[j] * catalan[i - j - 1]
    return catalan[n]
