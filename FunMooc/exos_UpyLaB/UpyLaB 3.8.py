""" Auteur: Jean-François BATAILLE

    Date : Mars 2020
    Projet : Apprentissage Python 3

Objectif:

    Écrire un programme qui lit :
        la première lettre en majuscule du nom du polyèdre ("T", "C", "O", "D" ou "I"),
        la longueur de l’arête du polyèdre,
    et qui imprime le volume du polyèdre correspondant.

    Si la lettre lue ne fait pas partie des cinq initiales, le programme imprime le message "Polyèdre non connu".

    cf: T = Tétraèdre; C = Cube; O = Octaèdre; D = Dodécaèdre; I = Icosaèdre


"""


from math import sqrt
lettre = input()
long = float(input())

if lettre == "C":
    print(long ** 3)
elif lettre == "T":
    print((sqrt(2) * (long ** 3)) / 12)
elif lettre == "O":
    print((sqrt(2) * (long ** 3)) / 3)
elif lettre == "D":
    print(((15 + (7 * sqrt(5))) * (long ** 3)) / 4)
elif lettre == "I":
    print(((5 * (3 + sqrt(5))) * (long ** 3)) / 12)
else:
    print("Polyèdre non connu")



