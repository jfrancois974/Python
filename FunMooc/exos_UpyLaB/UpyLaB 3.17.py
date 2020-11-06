"""
    Auteur: Jean-François BATAILLE

    Date : AVRIL 2020
    Projet : Apprentissage Python 3

Objectif:
    Écrire un programme qui lit une valeur flottante x en entrée et imprime une approximation de sin(x)

    Cette approximation sera obtenue en additionnant successivement les différents termes de la série jusqu’à ce que la valeur du terme
    devienne inférieure (en valeur absolue) à une constante \epsilon que l’on fixera à 10^{-6}.


Conseils:
    Dans cet exercice, notre programme doit calculer une approximation du sinus d’un nombre mais il ne faut pas utiliser la fonction sin du module math.
    Pour éviter de calculer explicitement la valeur des factorielles, on pourra chercher à exprimer chacun des termes en fonction du précédent.
    Notez bien que les exposants de x ne sont que les nombres impairs, et que le signe alterne entre + et -.


"""
from math import factorial

x = float(input())
S = 1
s = 0
n = 0

while abs(S) > 1e-6:
    S = (-1) ** n * x ** (2 * n + 1) / factorial(2 * n + 1)
    s += S
    n += 1

print(s)