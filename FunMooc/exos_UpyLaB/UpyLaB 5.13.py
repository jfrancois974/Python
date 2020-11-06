"""
        Auteur: Jean-François BATAILLE

        Date : AVRIL 2020
        Projet : Apprentissage Python 3

Objectif:

    L’exercice est le même que le précédent (5.12), mais ici, si les paramètres ont le type attendu,
    la fonction modifie la liste en place et ne retourne rien. Si les paramètres ne sont pas valides,
    une erreur se produit à l’exécution.

Exemples:
    l = [1, 3, 5]
    my_insert(l, 4)
    print(l)

    doit afficher : [1, 3, 4, 5]

    l = [1, 3, 5]
    my_insert(l, 'a')
    print(l)

    doit provoquer une exception Python, par exemple : AssertionError



"""


def my_insert(liste, nb):
    assert type(nb) == int
    assert type(nb) != str
    liste.append(nb)
    liste.sort()


my_insert('Bonjour UpyLab !', 666)
my_insert([1, 5, 78], -1)
my_insert([17, 32, 38, 38, 39, 40, 59, 64, 80, 96], 125)
