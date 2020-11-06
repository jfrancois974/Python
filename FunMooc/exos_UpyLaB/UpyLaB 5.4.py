"""
        Auteur: Jean-François BATAILLE

        Date : AVRIL 2020
        Projet : Apprentissage Python 3

Objectif:

    Écrire une fonction distance_points() qui reçoit en paramètres deux tuples de deux composantes représentant les coordonnées de deux points
    et qui retourne la distance euclidienne séparant ces deux points.

    Pour rappel, la distance euclidienne entre les points (x_1, y_1) et (x_2, y_2) se calcule grâce à la formule :
        sqrt((x[0] - x[1]) ** 2 + (y[0] - y[1]) ** 2)

    où, si a désigne un nombre positif, \sqrt{a} désigne la racine carrée de a et correspond à a^{\frac{1}{2}}.

Exemples:
    distance_points((1.0, 1.0), (2.0, 1.0)) doit retourner : 1.0
    distance_points((-1.0, 0.5), (2.0, 1.0)) doit retourner (approximativement) : 3.0413812651491097


"""

x = ('x1', 'y1')
y = ('x2', 'y2')


def distance_points(x, y):
    X = ((x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2)
    dist = X ** (1 / 2)
    return dist


print(distance_points((-2.0, 3.0), (-2.0, 0.0)))
print(distance_points((3.0, 1.0), (-1.5, -1.5)))
print(distance_points((-2.0, -1.0), (-1.5, 5.0)))
