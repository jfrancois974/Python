
"""
        Auteur: Jean-François BATAILLE

        Date : AVRIL 2020
        Projet : Apprentissage Python 3

Objectif:

    Une matrice M = \{m_{ij}\} de taille {n}\times{n} est dite antisymétrique lorsque, pour toute paire d’indices i, j, on a m_{ij} = - m_{ji}.
    Écrire une fonction booléenne antisymetrique(M) qui teste si la matrice M reçue est antisymétrique.

Exemples:
    antisymetrique([[0, 1, 1], [-1, 0, 1], [-1, -1, 0]]) doit retourner: True
    antisymetrique([[0, 1], [1, 0]]) doit retourner: False
    antisymetrique([[1, -2], [2, 1]]) doit retourner: False


"""


def antisymetrique(M):
    if M == []:
        return True
    numRows = len(M)     # number of rows)
    numCols = len(M[0])  # number of columns
    if not (numRows == numCols):
        return False
    i = 0
    while i <= (numRows - 1):
        j = 0
        while j <= (numRows - 1):
            if not (M[i][j] == -M[j][i]):
                return False
            j = j + 1
        i = i + 1
    return True


antisymetrique([[0, 10, 2, 1], [4, 1, 3, 3], [4, 2, 4, 9], [10, 3, 6, 9]])
# doit retourner :False

antisymetrique([[0, 0, -1, -4, -10], [0, 0, -6, -10, -4],
                [1, 6, 0, -9, -7], [4, 10, 9, 0, -1], [10, 4, 7, 1, 0]])
# doit retourner : True
