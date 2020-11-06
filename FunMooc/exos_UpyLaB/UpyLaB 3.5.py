""" Auteur: Jean-François BATAILLE

    Date : Mars 2020

    Projet : Apprentissage Python 3

Objectif:

    Écrire un programme qui lit en entrée deux nombres entiers strictement positifs, et qui vérifie qu’aucun des deux n’est un diviseur de l’autre.
    Si tel est bien le cas, le programme imprime True. Sinon, il imprime False.


"""
# une 1ère solution

nbr1 = int(input())
nbr2 = int(input())
if nbr1 % nbr2 == 0:
    print("False")
elif nbr1 < nbr2:
    print("False")
else:
    print("True")

# une 2ème solution

nbr1 = int(input())
nbr2 = int(input())

if nbr1 % nbr2 != 0 and nbr2 % nbr1 != 0:
    print(True)
else:
    print(False)
