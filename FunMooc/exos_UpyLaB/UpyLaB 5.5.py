"""
        Auteur: Jean-François BATAILLE

        Date : AVRIL 2020
        Projet : Apprentissage Python 3

Objectif:

    Écrire une fonction longueur(*points) qui reçoit en paramètres un nombre arbitraire de points (tuples de deux composantes),
    et retourne la longueur de la ligne brisée correspondante.

    Cette longueur se calcule en additionnant les longueurs des segments formés par deux points consécutifs.

Exemples:
    longueur((1.0, 1.0), (2.0, 1.0), (3.0, 1.0)) doit retourner :2.0
    longueur((0.5, 1.0), (2.0, 1.0), (2.5, -0.5), (-1.5, -1.0)) doit retourner (approximativement) :7.1122677042334645


"""

x = ('x1', 'y1')
y = ('x2', 'y2')


def distance_points(x, y):
    X = ((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)
    dist = X ** (1 / 2)
    return dist


def longueur(*points):
    distanceTotale = 0
    cote = 0

    for i in range(len(points) - 1):
        cote = distance_points(points[i], points[i + 1])
        distanceTotale = distanceTotale + cote

    return distanceTotale
