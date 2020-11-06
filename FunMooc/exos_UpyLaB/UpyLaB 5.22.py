"""
        Auteur: Jean-François BATAILLE

        Date : AVRIL 2020
        Projet : Apprentissage Python 3

Objectif:

    Écrire une fonction wc(nomFichier) qui ouvre le fichier en question et renvoie un tuple de trois nombres :
        le nombre de caractères (y compris les caractères de retour à la ligne)
        le nombre d, nb_mots
        le nombre denb_lignes.


"""


def wc(nomFichier):
    (nb_carateres, nb_mots, nb_lignes) = (0, 0, 0)
    with open(nomFichier, 'r', encoding='utf-8') as mon_texte:
        for txt in mon_texte:
            nb_lignes = nb_lignes + 1
            nb_carateres = nb_carateres + len(txt)
            for i in range(len(txt)):
                if txt[i].isalnum() and not txt[i-1].isalnum():
                    nb_mots = nb_mots + 1
    return nb_carateres, nb_mots, nb_lignes


print(wc('wc1.txt'))
print(wc('le-petit-prince.txt'))
print(wc('Zola.txt'))
# wc('wc1.txt') doit retourner (8, 2, 1)
# wc('Zola.txt') doit retourner (1356, 219, 1)
# wc('le-petit-prince.txt') doit retourner (82650, 15317, 1550)
