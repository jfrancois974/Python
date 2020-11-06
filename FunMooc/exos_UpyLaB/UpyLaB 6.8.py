"""
        Auteur: Jean-François BATAILLE

        Date : AVRIL 2020
        Projet : Apprentissage Python 3

Objectif:

    Écrire une fonction store_email(liste_mails) qui reçoit en paramètre une liste d’adresses e-mail et qui renvoie
    un dictionnaire avec comme clés les domaines des adresses e-mail et comme valeurs les listes d’utilisateurs correspondantes,
    triées par ordre croissant (UTF-8).


   
"""


def store_email(liste_mails):
    dict = {}  # on crée le dictionnaire vide
    for i in liste_mails:
        # slicing pour ne conserver que le domaine, que l'on affecte à la variable cle
        cle = i[i.find('@')+1:]
        # slicing pour ne conserver que ce qui précède @ et constitution du dictionnaire
        dict[cle] = dict.get(cle, []) + [i[:i.find('@')]]
    for j in dict:
        dict[j].sort()
    return dict
