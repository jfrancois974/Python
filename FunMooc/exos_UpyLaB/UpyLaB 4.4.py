"""
    Auteur: Jean-François BATAILLE

    Date : AVRIL 2020
    Projet : Apprentissage Python 3

Objectif:
    Écrire une fonction fibo(n) qui reçoit un nombre entier n et qui renvoie la valeur du nombre de Fibonacci F_n.

    On rappelle que :
        F_0 vaut 0 ;
        F_1 vaut 1 ;
        F_{i + 1} vaut F_i + F_{i-1} pour i > 0 ;
        F_i vaut None pour i < 0.

    Ensuite, écrire un programme qui lit une valeur entière strictement positive x et affiche le résultat de fibo(i)
    pour i allant de 0 compris à x non compris, avec chaque valeur sur sa propre ligne.

"""


def fibo(n):
    if n < 0:
        return None
    temp = 1
    v = 0
    for i in range(n):
        v += temp
        temp = v - temp  # or à ce stade v = v + temp, il faut donc soustraire temp
    return v


x = int(input())
for i in range(x):
    print(fibo(i))

"""def
Exemple:
Avec la donnée lue suivante :

5

le résultat à imprimer vaudra donc

0
1
1
2
3
"""
