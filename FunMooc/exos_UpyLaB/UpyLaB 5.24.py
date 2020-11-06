"""
        Auteur: Jean-François BATAILLE

        Date : AVRIL 2020
        Projet : Apprentissage Python 3
        
Objectif:

    Écrire une fonction print_mat(M) qui reçoit une matrice M en paramètre et affiche son contenu.
    Les éléments d’une même ligne de la matrice seront affichés sur une même ligne, et séparés par une espace,
    les éléments de la ligne suivante étant affichés sur une nouvelle ligne.


"""


def print_mat(M):
    for lst in M:
        res = ""
        for elem in lst:
            res = res + str(elem)
        print(res)


# input: [['H','E','L','L','O'],['W','O','R','L','D']]
ma_matrice = eval(input())
print_mat(ma_matrice)
