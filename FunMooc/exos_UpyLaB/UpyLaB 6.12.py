"""
        Auteur: Jean-François BATAILLE

        Date : AVRIL 2020
        Projet : Apprentissage Python 3

Objectif:

    Écrire une fonction belongs_to_file(word, txt) qui reçoit deux chaînes de caractères en paramètre.
    La première correspond à un mot, et la deuxième au nom d’un fichier contenant une liste de mots, chacun sur sa propre ligne.
    La fonction vérifie si le mot figure dans cette liste, et retourne True si c’est bien le cas, False sinon.

"""


def belongs_to_file(word, txt):
    with open(txt, encoding="utf-8") as mon_fichier:
        res = False
        for line in mon_fichier:
            for m in line.split():
                if word == m:
                    res = True
        return res


print(belongs_to_file("renard", "words.txt"))  # retourne : False
print(belongs_to_file("prince", "words.txt"))  # retourne : True
print(belongs_to_file('princess', 'words.txt'))  # retourne : True
