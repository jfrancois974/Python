"""
        Auteur: Jean-François BATAILLE

        Date : AVRIL 2020
        Projet : Apprentissage Python 3

Objectif:

    Écrire une fonction duree qui reçoit deux paramètres debut et fin. Ces derniers sont des couples (tuples de deux composantes)
    dont la première composante représente une heure et la seconde les minutes.
    Cette fonction doit calculer la durée qui s’est écoulée entre ces deux instants. Le résultat sera donné sous la forme d’un tuple(heure, minutes).

Exemples:
    duree ((14, 39), (18, 45)) doit retourner: (4, 6)
    duree ((6, 0), (5, 15)) doit retourner: (23, 15)


"""

debut = ('heure', 'fin')
fin = ('heure', 'fin')


def duree(debut, fin):
    if fin[0] - debut[0] == 0 and fin[1] - debut[1] > 0:
        return fin[0] - debut[0], fin[1] - debut[1]
    elif fin[0] - debut[0] == 0 and fin[1] - debut[1] < 0:
        return fin[0] - debut[0] + 23, fin[1] - debut[1] + 60
    elif fin[0] - debut[0] < 0 and fin[1] - debut[1] < 0:
        return fin[0] - debut[0] + 23, fin[1] - debut[1] + 60
    elif fin[1] - debut[1] < 0:
        return fin[0] - debut[0] - 1, fin[1] - debut[1] + 60
    else:
        return fin[0] - debut[0], fin[1] - debut[1]


print(duree((3, 45), (13, 22)))
print(duree((5, 37), (20, 0)))
