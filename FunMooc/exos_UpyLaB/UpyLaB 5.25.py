"""
        Auteur: Jean-François BATAILLE

        Date : AVRIL 2020
        Projet : Apprentissage Python 3
        
Objectif:

    Écrire une fonction trace(M) qui reçoit en paramètre une matrice M de taille {n}\times{n} contenant des valeurs numériques 
    (de type int ou float), et qui renvoie sa trace, c’est-à-dire la somme de tous les éléments de la première diagonale.


"""


def trace(M):
    res = 0
    for i in range(len(M)):
        res = res + M[i][i]
    return res


print(trace([[9, 3, 6, 9],
             [10, 8, 9, 1],  # pour plus de comprehension
             [7, 2, 0, 2],   # mis sous cet forme
             [2, 0, 5, 3]]))

# retourne 20
#  En effet 20 =  9 + 8 + 0 + 3
