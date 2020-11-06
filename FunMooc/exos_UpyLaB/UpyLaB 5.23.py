"""
        Auteur: Jean-François BATAILLE

        Date : AVRIL 2020
        Projet : Apprentissage Python 3

Objectif:

    Écrire une fonction init_mat(m, n) qui construit et renvoie une matrice d’entiers initialisée
    à la matrice nulle et de dimension m x n.


"""


def init_mat(x, y):
    matrice = [[0] * y for i in range(x)]
    return matrice


print(init_mat(2, 3))
print(init_mat(4, 2))
