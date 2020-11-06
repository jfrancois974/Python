""" Auteur: Jean-François BATAILLE

    Date : Mars 2020
    Projet : Apprentissage Python 3

Objectif:

    Écrire un programme qui lit 3 nombres entiers, et qui, si au moins deux d’entre eux ont la même valeur, 
    imprime cette valeur (le programme n’imprime rien dans le cas contraire).


"""

a = int(input())
b = int(input())
c = int(input())


if a == b == c:
    print(a)
if a == b and a != c and b != c:
    print(a)
if a == c and b != c and a !=b:
    print(a)
if b == c and a != b and a != c:
    print(b)