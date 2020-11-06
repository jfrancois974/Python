
"""
        Auteur: Jean-François BATAILLE

        Date : AVRIL 2020
        Projet : Apprentissage Python 3

Objectif:

    Écrire une fonction rac_eq_2nd_deg(a, b, c) qui reçoit trois paramètres de type float correspondant aux trois coefficients
    de l’équation du second degré ax^2 + bx + c = 0, et qui renvoie la ou les solutions s’il y en a, sous forme d’un tuple.
    
Exemples:

    rac_eq_2nd_deg(1.0,-4.0,4.0) doit retourner: (2.0,)
    rac_eq_2nd_deg(1.0,1.0,-2.0) doit retourner: (-2.0, 1.0)
    rac_eq_2nd_deg(1.0,1.0,1.0) doit retourner: ()


"""

from math import sqrt


def rac_eq_2nd_deg(a, b, c):
    d = b ** 2 - 4 * a * c
    if d < 0:
        return tuple()
    elif d == 0:
        return -b / (2 * a),
    else:
        r1 = ((-b + sqrt(d)) / (2 * a))
        r2 = ((-b - sqrt(d)) / (2 * a))
        return min(r1, r2), max(r1, r2)


print(rac_eq_2nd_deg(1.0, -4.0, 4.0))
print(rac_eq_2nd_deg(1.0, 1.0, -2.0))
print(rac_eq_2nd_deg(-1.0, 8.0, -1.0))
print(rac_eq_2nd_deg(0.5, -2.0, 5.0))
