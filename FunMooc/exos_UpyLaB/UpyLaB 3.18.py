"""
        Auteur: Jean-François BATAILLE

        Date : AVRIL 2020
        Projet : Apprentissage Python 3

Objectif:
    Écrire un programme qui lit un nombre entier strictement positif n et imprime une pyramide de chiffres de hauteur n (sur n lignes complètes,
        c'est-à-dire toutes terminées par une fin de ligne).
        La première ligne imprime un “1” (au milieu de la pyramide).
        La ligne i commence par le chiffre i % 10 et tant que l’on n’est pas au milieu, le chiffre suivant a la valeur suivante ((i+1) % 10).
        Après le milieu de la ligne, les chiffres vont en décroissant modulo 10 (symétriquement au début de la ligne).

    Notons qu’à la dernière ligne, aucune espace n’est imprimée avant d’écrire les chiffres 0123....


"""

N=int(input())
for i in range(1,N+1):
    for j in range(N,i,-1):
        print(" ", end="")
    for k in range(1,i+1):
        if i == 1:
            print(i%10, end="")
        else:
            print(i%10, end="")
            i=i+1
    for q in range(i-1,0,-1):
        if (i != j):
            i=i-1
            if i == j == k == q == N:
                break
            else:
                print((i-1)%10,end="")
    print()


# 2ème solution   près bcp d'effort mdr'

n = int(input("Veuillez entrer un nombre : "))
for i in range(1, n+1):

    for j in range(n - i):
        print(" ", end="")

    for j in range(1, i +1):
        i = i%10
        print(i, end="")
        i = (i + 1) % 10

    for j in range(j-1, 0, -1):
        j = (i-2)%10
        print(j, end="")
        i = (i-1) % 10

    print()