""" Auteur: Jean-François BATAILLE

    Date : AVRIL 2020
    Projet : Apprentissage Python 3

Objectif:
    Écrire un programme qui additionne des valeurs naturelles lues sur entrée et affiche le résultat.
    La première donnée lue ne fait pas partie des valeurs à sommer.
    Elle détermine si la liste contient un nombre déterminé à l’avance de valeurs à lire ou non :

        si cette valeur est un nombre positif ou nul, elle donne le nombre de valeurs à lire et à sommer ;

        si elle est négative, cela signifie qu’elle est suivie d’une liste de données à lire qui sera terminée par le caractère "F" signifiant que la liste est terminée.

"""


lst = []
num = int(input())
if num >=0:
    for n in range(num):
        numbers = int(input())
        lst.append(numbers)
    print(sum(lst))
elif num < 0:
    somme = 0
    numbers = 0
    while numbers != 'F':
        numbers = input()
        if numbers == 'F':
            print(int(somme))
        else:
            somme = int(numbers) + somme


# b = int(input())
# n = 0
# s = 0
# total = 0
# if b > 0:
#     for number in range(b):
#         n = int(input())
#         total += n
#     print(total)
#
# if b == 0:
#     print(0)
#
# if b < 0:
#     b = int()
#     while b != 'F':
#         s = s + int(b)
#         b = input()
#     else:
#         print(s)