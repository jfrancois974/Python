"""
        Auteur: Jean-François BATAILLE

        Date : AVRIL 2020
        Projet : Apprentissage Python 3

Objectif:

    Écrire une fonction check_cols qui prend en paramètre une grille sous forme de matrice à deux dimensions et vérifie
    si toutes les colonnes sont valides (c’est-à-dire que sur chaque colonne, chaque chiffre apparaît une et une seule fois).


"""


def check_cols(grid):
    for line in range(len(grid)):
        somme = 0
        for col in range(len(grid)):
            somme += int(grid[col][line])
        if somme != 45:
            return False
    return True


print(check_cols([[1, 2, 3, 4, 5, 6, 7, 8, 9], [9, 1, 2, 3, 4, 5, 6, 7, 8], [8, 9, 1, 2, 3, 4, 5, 6, 7], [7, 8, 9, 1, 2, 3, 4, 5, 6], [
      6, 7, 8, 9, 1, 2, 3, 4, 5], [5, 6, 7, 8, 9, 1, 2, 3, 4], [4, 5, 6, 7, 8, 9, 1, 2, 3], [3, 4, 5, 6, 7, 8, 9, 1, 2], [2, 3, 4, 5, 6, 7, 8, 9, 1]]))

print(check_cols([[6, 9, 3, 1, 7, 4, 2, 5, 8], [1, 7, 8, 3, 2, 5, 6, 4, 9], [2, 5, 4, 6, 8, 9, 7, 3, 1], [8, 2, 1, 4, 3, 7, 5, 9, 6], [
      4, 9, 6, 8, 5, 2, 3, 1, 7], [7, 3, 5, 9, 6, 1, 8, 2, 4], [5, 8, 9, 7, 1, 3, 4, 6, 2], [3, 1, 7, 2, 4, 6, 9, 8, 5], [6, 4, 2, 5, 9, 8, 1, 7, 3]]))
