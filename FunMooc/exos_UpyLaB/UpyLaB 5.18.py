"""
        Auteur: Jean-François BATAILLE

        Date : AVRIL 2020
        Projet : Apprentissage Python 3
        
Objectif:

    Écrire une fonction my_filter qui reçoit une liste lst et une fonction booléenne f en paramètres et
    renvoie une nouvelle liste constituée des éléments de lst pour lesquels la fonction f renvoie True.

Exemples:
    my_filter(['hello', 666, 42, 'Thierry', 1.5], lambda x : isinstance(x, int))
    doit retourner: [666, 42]

    my_filter([-2, 0, 4, -5, -6], lambda x : x < 0)
    doit retourner: [-2, -5, -6]


"""


""" 
Solution avec boucle for

def my_filter(lst, f):
    res = []
    for elem in lst:
        if f(elem):  # if f(elem) == True:
            res.append(elem)
    return res
    
"""


def my_filter(lst, f):
    return [e for e in lst if f(e)]


my_filter(['a', 2, 'toc', 3, '5'], lambda e: isinstance(e, int))
my_filter([7, 8, 9, 1, 8, 7, 5, 3, 6, 3, 10, 2, 3, 8,
           10, 10, 1, 5, 6, 8, 10], lambda e: e > 2)
