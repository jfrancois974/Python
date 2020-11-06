"""
        Auteur: Jean-François BATAILLE

        Date : AVRIL 2020
        Projet : Apprentissage Python 3

Objectif:

    Écrire une fonction liste_des_mots qui reçoit en paramètre le nom d’un fichier texte,
    que la fonction doit ouvrir, et qui renvoie la liste des mots contenus dans le fichier.


"""


def liste_des_mots(texte):
    # constitution des 2 listes (vides)
    lst0 = []
    lst = []
    # on liste tous les mots du fichier passé en argument
    for mots in open(texte, encoding="utf-8"):
        for i in range(len(mots)):  # on boucle sur la longueur du mot
            if not mots[i].isalpha():  # si la lettre n'est pas un terme alphabétique
                # on remplace la lettre du mot par une chaîne vide (espace)
                mots = mots.replace(mots[i], " ")

        # puis on split chaque mot que l'on additionne à la liste temporaire à chaque tour de boucle
        lst0 = lst0 + mots.split()
        print(lst0)

    for mots in lst0:  # on boucle sur chaque mots de la liste temporaire
        mots = mots.lower()  # on convertit le mot en minuscule
        # si le mot n'est pas dans la liste définitive (supprime les doublons)...
        if mots not in lst:
            lst.append(mots)  # ...on ajoute le mot à la liste
    lst.sort()  # fin de boucle, on classe les mots par ordre alphabétique

    return lst  # ... et on retourne la liste


(liste_des_mots("Zola.txt"))
# print(liste_des_mots("Zola.txt"))
liste_des_mots('le-petit-prince-extrait.txt')
