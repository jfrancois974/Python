"""
        Auteur: Jean-François BATAILLE

        Date : AVRIL 2020
        Projet : Apprentissage Python 3

Objectif:

    Écrire une fonction symetrie_horizontale(A) qui reçoit une matrice carrée A (de taille {n}\times{n}) et qui renvoie l’image
    de A par symétrie horizontale par rapport à la ligne du milieu : la première ligne devenant la dernière, la seconde,
    l’avant-dernière, etc.

Exemples:
    symetrie_horizontale([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) doit retourner: [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
    symetrie_horizontale([['a', 'b'], ['c', 'd']]) doit retourner: [['c', 'd'], ['a', 'b']]
    symetrie_horizontale([]) doit retourner: []



"""


def symetrie_horizontale(A):
    lst = []
    image = (len(A) - 1)
    if A == []:
        return []
    for i in range(image, -1, -1):
        lst.append(A[i])
    return lst


symetrie_horizontale([[2, 7, 6], [9, 5, 1], [4, 3, 8]])
symetrie_horizontale([[8, 8, 10, 9], [4, 1, 3, 9],
                      [6, 6, 5, 9], [3, 10, 7, 8]])
