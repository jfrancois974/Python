"""
        Auteur: Jean-François BATAILLE

        Date : AVRIL 2020
        Projet : Apprentissage Python 3

Objectif:

    Écrire une fonction symetrise_amis qui reçoit un dtionnaire d d’amis où les clés sont des prénoms et les valeurs, des ensembles de prénoms représentant les amis de chacun.

    Cette fonction modifie le dtionnaire d de sorte que si une clé prenom1 contient prenom2 dans l’ensemble de ses amis, l’inverse soit vrai aussi.

    La fonction accepte un second paramètre englobe.

    Si englobe est vrai, la fonction ajoutera les éléments nécessaires pour symétriser le dtionnaire d.

    Sinon, la fonction enlèvera les éléments nécessaires pour symétriser d.


"""


def symetrise_amis(d, englobe):
    for amis in d:
        lst = []
        for i in d[amis]:
            if i in d and englobe:
                d[i].add(amis)
            elif i not in d or amis not in d[i]:
                lst.append(i)
        for i in lst:
            d[amis].remove(i)


d = {'Pierre': {'Pierre'}, 'Thierry': {'Ariane'}, 'Ariane': set()}
symetrise_amis(d, True)

print(d)
