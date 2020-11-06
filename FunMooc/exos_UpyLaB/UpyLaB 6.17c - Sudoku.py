"""
        Auteur: Jean-François BATAILLE

        Date : AVRIL 2020
        Projet : Apprentissage Python 3

Objectif:

  Écrire une fonction check_regions qui prend en paramètre une grille sous forme de matrice à deux dimensions et vérifie
  si toutes les régions sont valides (c’est-à-dire que dans chaque région, chaque chiffre apparaît une et une seule fois).


"""


def check_regions(grid):
    for line in range(0, 9, 3):
        for column in range(0, 9, 3):
            lst = []
            for l in range(line, line + 3):
                for c in range(column, column + 3):
                    lst.append(grid[l][c])
            if sum(lst) != 45:
                return False
    return True


print(check_regions([[5, 3, 4, 6, 7, 8, 9, 1, 2], [6, 7, 2, 1, 9, 5, 3, 4, 8], [1, 9, 8, 3, 4, 2, 5, 6, 7], [8, 5, 9, 7, 6, 1, 4, 2, 3], [
      4, 2, 6, 8, 5, 3, 7, 9, 1], [7, 1, 3, 9, 2, 4, 8, 5, 6], [9, 6, 1, 5, 3, 7, 2, 8, 4], [2, 8, 7, 4, 1, 9, 6, 3, 5], [3, 4, 5, 2, 8, 6, 1, 7, 9]]))

print(check_regions([[6, 9, 3, 1, 7, 4, 2, 5, 8], [1, 7, 8, 3, 2, 5, 6, 4, 9], [2, 5, 9, 6, 8, 4, 7, 3, 1], [8, 2, 1, 4, 3, 7, 5, 9, 6], [
      4, 9, 6, 8, 5, 2, 3, 1, 7], [7, 3, 5, 9, 6, 1, 8, 2, 4], [5, 8, 9, 7, 1, 3, 4, 6, 2], [3, 1, 7, 2, 4, 6, 9, 8, 5], [6, 4, 2, 5, 9, 8, 1, 7, 3]]))
