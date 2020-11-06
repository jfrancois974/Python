"""
        Auteur: Jean-François BATAILLE

        Date : AVRIL 2020
        Projet : Apprentissage Python 3
        
Objectif:

    Écrire une fonction compteur_lettres(texte) qui renvoie un dictionnaire contenant toutes les lettres 
    de l’alphabet associées à leur nombre d’apparition dans texte.


"""


def compteur_lettres(texte):
    dico = {}
    dico.update(dict.fromkeys(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'], 0))

    for c in texte:
        if c.isalpha():
            dico[c.lower()] = dico[c.lower()] + 1
    return dico
