
"""
        Auteur: Jean-François BATAILLE

        Date : AVRIL 2020
        Projet : Apprentissage Python 3

Objectif:

    Considérons les billets et pièces de valeurs suivantes : 20 euros, 10 euros, 5 euros, 2 euros et 1 euro.

    Écrire une fonction rendre_monnaie qui reçoit en paramètre un entier prix et cinq valeurs entières x20, x10, x5, x2 et x1,
    qui représentent le nombre de billets ou de pièces de chaque valeur que donne un client pour l’achat d’un objet dont le prix est mentionné.

    La fonction doit renvoyer cinq valeurs, représentant le nombre de billets et pièces de chaque sorte qu’il faut rendre au client,
    dans le même ordre que précédemment. Cette décomposition doit être faite en rendant le plus possible de billets et pièces de grosses valeurs.

    Si la somme d’argent avancée par le client n’est pas suffisante pour effectuer l’achat, la fonction retournera cinq valeurs None.


"""

def rendre_monnaie(prix, x20, x10, x5, x2, x1):
    liste_valeur_billet = (20, 10, 5, 2, 1)
    n = len(liste_valeur_billet)
    somme = x20 * 20 + x10 * 10 + x5 * 5 + x2 * 2 + x1 * 1
    reste = somme - prix
    if somme <= prix:
        res20 = None
        res10 = None
        res5 = None
        res2 = None
        res1 = None
    else:
        res20 = reste // 20
        reste -= res20 * 20
        res10 = reste // 10
        reste -= res10 * 10
        res5 = reste // 5
        reste -= res5 * 5
        res2 = reste // 2
        reste -= res2 * 2
        res1 = reste // 1
    return res20, res10, res5, res2, res1


print(rendre_monnaie(100, 0, 14, 5, 5, 1))
# return (3, 1, 1, 0, 1)

print(rendre_monnaie(647, 8, 6, 7, 7, 7))

# return (None, None, None, None, None)

