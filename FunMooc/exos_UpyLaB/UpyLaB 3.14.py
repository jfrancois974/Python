""" Auteur: Jean-François BATAILLE

    Date : AVRIL 2020
    Projet : Apprentissage Python 3

Objectif:

    Écrire un programme qui génère de manière (pseudo) aléatoire un entier (nombre secret) compris entre 0 et 100.
    Ensuite, le joueur doit deviner ce nombre en utilisant le moins d’essais possible.

    À chaque tour, le joueur est invité à proposer un nombre et le programme doit donner une réponse parmi les suivantes :
        « Trop grand » : si le nombre secret est plus petit que la proposition et qu’on n’est pas au maximum d’essais
        « Trop petit » : si le nombre secret est plus grand que la proposition et qu’on n’est pas au maximum d’essais
        « Gagné en n essais ! » : si le nombre secret est trouvé
        « Perdu ! Le secret était nombre » : si le joueur a utilisé six essais sans trouver le nombre secret.


"""

import random

NB_ESSAIS_MAX = 6
secret = random.randint(0, 100)
nbre_secret = int(input())
nbre_essai = 1

while nbre_essai <= NB_ESSAIS_MAX:
    if nbre_secret < secret:
        print("Trop petit")
        nbre_secret = int(input())
        nbre_essai += 1

    elif nbre_secret > secret:
        print("Trop grand ")
        nbre_secret = int(input())
        nbre_essai += 1

    elif nbre_secret == secret:
        print("Gagné en {} essais !".format(nbre_essai))
        break
else:
    print("Perdu ! Le secret était {}".format(secret))

