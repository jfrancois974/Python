
"""
        Auteur: Jean-François BATAILLE

        Date : AVRIL 2020
        Projet : Apprentissage Python 3


Objectif:
    Écrire une fonction anagrammes(v, w) qui renvoie la valeur booléenne True si les mots v et w sont des anagrammes.

Exemples:
    anagrammes('marion', 'romina')doit retourner: True
    anagrammes('bonjour', 'jour')doit retourner: False
    anagrammes('pate', 'patte')doit retourner: False


"""


def anagrammes(v, w):
    if sorted(v.lower()) == sorted(w.lower()):
        return True
    else:
        return False


anagrammes('bbonjour', 'bbonjour')
anagrammes('bbonjour', 'abonjour')
