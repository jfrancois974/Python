""" Auteur: Jean-François BATAILLE

    Date : Mars 2020

    Projet : Apprentissage Python 3

Objectif:

    Écrire un programme qui aide le croupier à déterminer la somme que le casino doit donner au joueur.
    Le programme lira, dans l’ordre, deux nombres entiers en entrée : le pari du joueur (représenté par un nombre entre 0 et 16, voir description plus bas), 
    et le numéro issu du tirage (nombre entre 0 et 12). Le programme affichera alors le montant gagné par le joueur.

    Entrées pour le pari du joueur :

        nombre entre 0 et 12 : le joueur parie sur le numéro correspondant
        13 : le joueur parie sur pair
        14 : le joueur parie sur impair
        15 : le joueur parie sur la couleur rouge
        16 : le joueur parie sur la couleur noire.


"""

mise = 10 #Somme fixe de 10 euros du joueur
gain = mise * 12
gain2 = mise * 2
pari = int(input())
numero = int(input())

if  pari == 13 and (numero == 0 or numero == 2 or numero == 4 or numero == 6 or numero == 8 or numero == 11):
    print (gain2)
elif pari == 14 and (numero == 1 or numero == 3 or numero == 5 or numero == 7 or numero == 9):
    print(gain2)
elif pari == 15 and (numero == 1 or numero == 3 or numero == 5 or numero == 7 or numero == 9):
    print(gain2)
elif pari == 16 and (numero == 2 or numero == 4 or numero == 6 or numero == 8 or numero == 11):
    print (gain2)
elif pari <= 12 and (pari == numero):
    print(gain)
else:
    print("0")