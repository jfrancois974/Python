""" Auteur: Jean-François BATAILLE

    Date : AVRIL 2020
    Projet : Apprentissage Python 3

Objectif:

    Écrire un programme qui demande à l’utilisateur combien de plis de papier sont nécessaires pour se rendre sur la Lune, 
    et pose la question tant que l’utilisateur n’a pas saisi la bonne réponse.

    Si la réponse saisie par l’utilisateur n’est pas correcte, le programme affiche le message "Mauvaise réponse.", 
    puis pose à nouveau la question. Si la réponse saisie par l’utilisateur est correcte, le programme affiche le message "Bravo !", et s’arrête. Exemple

    Dans cet exemple d’exécution, le texte est affiché par le programme, alors que les nombres sont saisis par l’utilisateur :

    Combien de plis sont-ils nécessaires pour se rendre sur la Lune ? : 666
        Mauvaise réponse.
    Combien de plis sont-ils nécessaires pour se rendre sur la Lune ? : 3
        Mauvaise réponse.
    Combien de plis sont-ils nécessaires pour se rendre sur la Lune ? : 42
        Bravo !


"""

n = 42
while n >=0:
    n = int(input("Combien de plis sont-ils nécessaires pour se rendre sur la Lune ? : "))
    if n == 42:
        print("Bravo !")
        break
    else:
        print("Mauvaise réponse.")
        continue