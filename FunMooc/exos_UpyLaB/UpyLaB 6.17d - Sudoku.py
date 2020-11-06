"""
        Auteur: Jean-François BATAILLE

        Date : AVRIL 2020
        Projet : Apprentissage Python 3

Objectif:

    Écrire une fonction check_sudoku capable de vérifier si la grille passée en paramètre, sous forme d’une matrice 9 x 9 d’entiers, est une solution au problème du sudoku. La fonction retournera la réponse (True ou False).

    Cette fonction devra utiliser les trois fonctions suivantes (que vous devez aussi définir) :
            check_rows qui prend en paramètre une grille sous forme de matrice à deux dimensions et vérifie si toutes les lignes sont valides (c’est-à-dire que sur chaque ligne, chaque chiffre apparaît une et une seule fois).

            check_cols qui prend en paramètre une grille sous forme de matrice à deux dimensions et vérifie si toutes les colonnes sont valides (c’est-à-dire que sur chaque colonne, chaque chiffre apparaît une et une seule fois).

            check_regions qui prend en paramètre une grille sous forme de matrice à deux dimensions et vérifie si toutes les régions sont valides (c’est-à-dire que dans chaque région, chaque chiffre apparaît une et une seule fois).



"""


def check_sudoku(grid):
    if check_rows(grid) != 45:
        return False
    elif check_cols(grid) != 45:
        return False
    elif check_regions(grid) != 45:
        return False
    else:
        return True

# on retourne la somme des valeurs de chaque rangées


def check_rows(grid):
    for line in grid:
        return sum(line)

# on retourne la somme des valeurs de chaque colonnes


def check_cols(grid):
    for line in range(len(grid)):
        somme = 0
        for col in range(len(grid)):
            somme += int(grid[col][line])
        return somme

# on retourne la somme des valeurs de chaque carrés


def check_regions(grid):
    for ligne in range(0, 9, 3):
            for colonne in range(0, 9, 3):
                liste = []
                for l in range(ligne, ligne + 3):
                    for c in range(colonne, colonne + 3):
                        liste.append(grid[l][c])
            return sum(liste)


print(check_sudoku([[5, 3, 4, 6, 7, 8, 9, 1, 2], [6, 7, 2, 1, 9, 5, 3, 4, 8], [1, 9, 8, 3, 4, 2, 5, 6, 7], [8, 5, 9, 7, 6, 1, 4, 2, 3], [
      4, 2, 6, 8, 5, 3, 7, 9, 1], [7, 1, 3, 9, 2, 4, 8, 5, 6], [9, 6, 1, 5, 3, 7, 2, 8, 4], [2, 8, 7, 4, 1, 9, 6, 3, 5], [3, 4, 5, 2, 8, 6, 1, 7, 9]]))

print(check_sudoku([[1, 2, 3, 4, 5, 6, 7, 8, 9], [9, 1, 2, 3, 4, 5, 6, 7, 8], [8, 9, 1, 2, 3, 4, 5, 6, 7], [7, 8, 9, 1, 2, 3, 4, 5, 6], [6, 7, 8, 9, 1, 2, 3, 4, 5], [5, 6, 7, 8, 9, 1, 2, 3, 4], [4, 5, 6, 7, 8, 9, 1, 2, 3], [3, 4, 5, 6, 7, 8, 9, 1, 2], [2, 3, 4, 5, 6, 7, 8, 9, 1]])

print(check_sudoku([[9, 6, 1, 5, 3, 7, 2, 8, 4], [2, 8, 7, 4, 1, 9, 6, 3, 5], [3, 4, 5, 2, 8, 6, 1, 7, 9], [5, 3, 4, 6, 7, 8, 9, 1, 2], [
      6, 7, 2, 1, 9, 5, 3, 4, 8], [1, 9, 8, 3, 4, 2, 5, 6, 7], [8, 5, 9, 7, 6, 1, 4, 2, 3], [4, 2, 6, 8, 5, 3, 7, 9, 1], [7, 1, 3, 9, 2, 4, 8, 5, 6]]))
