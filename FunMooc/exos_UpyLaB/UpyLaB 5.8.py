
"""
        Auteur: Jean-François BATAILLE

        Date : AVRIL 2020
        Projet : Apprentissage Python 3

Objectif:

    Écrire une fonction prime_numbers qui reçoit comme paramètre un nombre entier nb et qui renvoie la liste des
    nb premiers nombres premiers.

    Si le paramètre n’est pas du type attendu, ou ne correspond pas à un nombre entier positif ou nul, la fonction renvoie None.

Exemples:
    prime_numbers(4)doit retourner : [2, 3, 5, 7]
    prime_numbers(-2)doit retourner : None


"""


def premier(nombre):
    # Fonction qui determine si un nombre est premier ou non.
    nb = True
    if (nombre == 0 or nombre == 1):
        nb = False
    i = 2
    while (i <= (nombre - 1) and i <= (nombre / 2)):
        if (nombre % i == 0):
            nb = False
        i = i + 1
    return nb


def prime_numbers(nb):
    list = []
    # Fonction qui list les nombres premiers jusque X.
    i = 2
    if (type(nb) != int or nb < 0):
        return None
    if (nb == 0):
        return list
    while len(list) < nb:
        if (premier(i)):
            list.append(i)
        i = i + 1
    return list
