"""
    Auteur: Jean-François BATAILLE

    Date : AVRIL 2020
    Projet : Apprentissage Python 3

Objectif:
    Le Petit Prince vient de débarquer sur la planète U357, et il apprend qu'il peut y voir de belles aurores boréales !

    La planète U357 a deux soleils : les étoiles E1515 et E666.  C'est pour cela que les tempêtes magnétiques sont permanentes,
    ce qui est excellent pour avoir des aurores boréales.

    Par contre, il y fait souvent jour, sauf bien évidemment quand les deux soleils sont couchés en même temps.

    Heureusement pour nous, une journée U357 s'écoule sur 24 heures comme sur notre Terre, et pour simplifier,
    nous ne prendrons pas en compte les minutes (on ne donne que les heures avec des valeurs entières entre 0 et 23). 

    Nous vous demandons d'aider le Petit Prince à déterminer les périodes de jour et de nuit.

    UPYLAB 4.2B

    Il vous faut maintenant écrire un programme qui lit en entrée :

    . l'heure de lever du soleil E1515
    . l'heure du coucher du soleil E1515
    . l'heure de lever du soleil E666
    . l'heure du coucher du soleil E666

    et qui utilise la fonction soleil_leve pour afficher ligne par ligne chacune des heures de la journée, depuis 0 jusqu'à 23,
    suivies d'une espace et d'une astérisque s'il fait nuit à cette heure.

    Attention, il ne fera nuit que si E1515 et E666 sont tous deux couchés.


"""

def soleil_leve(lever, coucher, heure):
    cas1 = lever == coucher == 0
    cas2 = lever <= heure < coucher
    cas3 = coucher < lever and (heure < coucher or lever <= heure)
    return cas1 or cas2 or cas3


lE1515 = int(input())  # lever_e1515
cE1515 = int(input())  # coucher_e1515
lE666 = int(input())  # lever_e666
cE666 = int(input())  # coucher_e666

for heure in range(24):
    if soleil_leve(lE1515, cE1515, heure) or soleil_leve(lE666, cE666, heure):
        print(heure)
    else:
        print(heure, '*')

"""
Avec les données lues suivantes :

6
18
10
21

0 *
1 *
2 *
3 *
4 *
5 *
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21 *
22 *
23 
"""

