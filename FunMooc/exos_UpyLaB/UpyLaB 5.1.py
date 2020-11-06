
"""
        Auteur: Jean-François BATAILLE

        Date : AVRIL 2020
        Projet : Apprentissage Python 3

Objectif:

    Écrire une fonction signature qui reçoit un paramètre identite. Ce paramètre est un couple (tuple de deux composantes)
    dont la première composante représente un nom et la seconde un prénom.

    Cette fonction doit retourner la chaîne de caractères formée du prénom suivi du nom, séparés par une espace.

Exemples:
    signature(('de Saint-Exupéry', 'Antoine')) doit retourner : 'Antoine de Saint-Exupéry'


"""


def signature(identite):
    res = identite[-1] + " " + identite[0]
    return res


print(signature(('BATAILLE', 'Jean-François')))
