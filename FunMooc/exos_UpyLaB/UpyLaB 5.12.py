"""
        Auteur: Jean-François BATAILLE

        Date : AVRIL 2020
        Projet : Apprentissage Python 3


Objectif:

    Écrire une fonction my_insert qui reçoit comme premier paramètre une liste d’entiers relatifs triée par ordre croissant
    et comme deuxième paramètre un entier relatif n, et qui renvoie une liste correspondant à la liste reçue,
    mais dans laquelle le nombre n a été inséré à la bonne place.

    La liste donnée en paramètre ne doit pas être modifiée par votre fonction.

    Vous pouvez supposer que le premier paramètre sera bien une liste triée d’entiers, mais si le deuxième paramètre
    n’est pas du bon type, la fonction retourne None.

Exemples:
    my_insert([1, 3, 5], 4) doit retourner: [1, 3, 4, 5]
    my_insert([2, 3, 5], 1) doit retourner: [1, 2, 3, 5]
    my_insert([2, 3, 5], 0.5) doit retourner: None
    
"""


def my_insert(liste, n):
    if type(n) != int:
        return None

    return sorted(liste + [n, ])


my_insert([25, 40, 44, 60, 61, 65, 95], 149)
my_insert([1, 5, 78], p)
my_insert([1], 1.7)
