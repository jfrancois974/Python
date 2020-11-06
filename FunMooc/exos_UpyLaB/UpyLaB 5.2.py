"""
        Auteur: Jean-François BATAILLE

        Date : AVRIL 2020
        Projet : Apprentissage Python 3

Objectif:

    On représente un brin d’ADN par une chaîne de caractères dont les caractères sont parmi les quatre suivants :
    'A' (Adénine), 'C' (Cytosine), 'G' (Guanine) et 'T' (Thymine).

    Écrire une fonction est_adn qui reçoit une chaîne de caractères en paramètre et qui retourne True si cette chaîne de caractères
    n'est pas vide et peut représenter un brin d’ADN, False sinon.

Exemples:
    est_adn("ATGGT") doit retourner: True
    est_adn("ISA") doit retourner: False
    est_adn("CTaG") doit retourner: False


"""

chaîne = 'A', 'C', 'G', 'T'


def est_adn(s):
    res = True
    if s == "":
        res = False
    for c in s:
        if c not in chaîne:
            res = False
    return res


print(est_adn('yzgtzaayCtAxx'))
