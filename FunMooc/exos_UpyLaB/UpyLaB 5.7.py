
"""
        Auteur: Jean-François BATAILLE

        Date : AVRIL 2020
        Projet : Apprentissage Python 3

Objectif:
    Écrire une fonction plus_grand_bord(w) qui reçoit un mot w et retourne le plus grand bord de ce mot.

    On dit qu’un mot u est un bord du mot w si u est à la fois un préfixe strict et un suffixe strict de w, 
    c’est-à-dire qu’on retrouve le mot u au début et à la fin du mot w, sans que u soit égal à w lui-même.

    Exemples : 'a' et 'abda' sont des bords de 'abdabda'. En effet, 'abdabda' commence et se termine par 'a', ainsi que par 'abda'.
    Le plus grand bord de 'abdabda' est 'abda'.

    Si w n’a pas de bord, la fonction retourne la chaîne de caractères vide.

Exemples:

    plus_grand_bord('abdabda')doit retourner: 'abda'
    plus_grand_bord('abcabd')doit retourner: ''
    plus_grand_bord('abcba')doit retourner: 'a'  
    plus_grand_bord('aaaaa')doit retourner: 'aaaa'


"""


def plus_grand_bord(w):
    long = ""
    for i in range(1, len(w)):
        if w[:i] == w[-i:]:
            long = w[:i]

    return long
