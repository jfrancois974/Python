
"""
        Auteur: Jean-François BATAILLE

        Date : AVRIL 2020
        Projet : Apprentissage Python 3

Objectif:
    Écrire une fonction bat(joueur_1, joueur_2) où joueur_1 et joueur_2 ont chacun une valeur entière 0, 1 ou 2, qui encode ce que le joueur a fait comme coup (0 : PIERRE, 1 : FEUILLE, 2 : CISEAUX) qui renvoie un résultat booléen :
        vrai si joueur_1 bat le joueur_2 :
        faux si joueur_2 bat joueur_1 ou fait match nul contre lui.
   
Exemples:
    bat(0, 0)doit retourner: False
    bat(0, 1)doit retourner: False
    bat(2, 1)doit retourner: True

Consignes:
    Dans cet exercice, il vous est demandé d’écrire seulement la fonction bat.
    Le code que vous soumettez à UpyLaB doit donc comporter uniquement la définition de cette fonction, éventuellement accompagné
    des trois définitions des constantes PIERRE, FEUILLE, CISEAUX , et ne fait en particulier aucun appel à input ou à print.

    Il n’est pas demandé que la fonction bat teste le type ou les valeurs des paramètres reçus.
"""

def bat(joueur_1, joueur_2):
    if (joueur_1 == joueur_2) or (joueur_2 == joueur_1 + 1) or (joueur_1 == joueur_2 + 2):
        return False
    else:
        return True


print(bat(2, 1))