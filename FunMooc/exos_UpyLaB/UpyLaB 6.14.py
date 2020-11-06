"""
        Auteur: Jean-François BATAILLE

        Date : AVRIL 2020
        Projet : Apprentissage Python 3

Objectif:

    Écrire une fonction placer_pion(couleur, colonne, grille) où :
        couleur est la couleur du pion, qui peut être soit 'R' (rouge), soit 'J' (jaune),
        colonne est l’indice de la colonne où le joueur souhaite placer le pion (allant de 0 à 6),
        grille est la grille de jeu sous forme de matrice.

    Cette matrice contient donc six listes de lignes contenant chacune sept éléments.
    La ligne à l’indice 0 représente le bas du jeu.
    Les éléments de cette matrice seront soit 'R', soit 'J' ou soit 'V' pour un emplacement encore vide.
    Cette fonction placera un pion dans la grille du jeu et renverra un couple de valeurs :
        si le placement est possible, la valeur booléenne True et la grille modifiée,
        sinon, la valeur booléenne False et la grille non modifiée.

Exemples:

    placer_pion("R", 3, [['V', 'V', 'V', 'J', 'V', 'V', 'V'],
                        ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                        ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                        ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                        ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
                        ['V', 'V', 'V', 'V', 'V', 'V', 'V']])

    doit retourner :

    (True, [['V', 'V', 'V', 'J', 'V', 'V', 'V'],
            ['V', 'V', 'V', 'R', 'V', 'V', 'V'],
            ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
            ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
            ['V', 'V', 'V', 'V', 'V', 'V', 'V'],
            ['V', 'V', 'V', 'V', 'V', 'V', 'V']])


"""


def placer_pion(color, column, rack):
    for line in range(6):
        if rack[line][column] == 'V':
            rack[line][column] = color
            return True, rack
    return False, rack


print(placer_pion('R', 1, [['V', 'V', 'V', 'J', 'V', 'V', 'V'], ['V', 'V', 'V', 'V', 'V', 'V', 'V'], ['V', 'V', 'V', 'V', 'V', 'V', 'V'], [
      'V', 'V', 'V', 'V', 'V', 'V', 'V'], ['V', 'V', 'V', 'V', 'V', 'V', 'V'], ['V', 'V', 'V', 'V', 'V', 'V', 'V']]))

print(placer_pion('J', 2, [['V', 'R', 'V', 'J', 'V', 'V', 'V'], ['V', 'V', 'V', 'V', 'V', 'V', 'V'], ['V', 'V', 'V', 'V', 'V', 'V', 'V'], [
      'V', 'V', 'V', 'V', 'V', 'V', 'V'], ['V', 'V', 'V', 'V', 'V', 'V', 'V'], ['V', 'V', 'V', 'V', 'V', 'V', 'V']]))

print(placer_pion('R', 2, [['J', 'R', 'J', 'J', 'J', 'R', 'V'], ['V', 'V', 'J', 'R', 'V', 'R', 'V'], ['V', 'V', 'R', 'J', 'V', 'J', 'V'], [
      'V', 'V', 'R', 'J', 'V', 'V', 'V'], ['V', 'V', 'R', 'J', 'V', 'V', 'V'], ['V', 'V', 'R', 'V', 'V', 'V', 'V']]))
