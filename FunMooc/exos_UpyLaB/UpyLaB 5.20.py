"""
        Auteur: Jean-François BATAILLE

        Date : AVRIL 2020
        Projet : Apprentissage Python 3

Objectif:

    Écrire une fonction nouveaux_heros dont le but consiste à remplacer les héros d'une histoire.
    La fonction acceptera deux paramètres :
        le premier sera une chaîne de caractères précisant le nom du fichier contenant l'histoire initiale ;
        le deuxième sera une chaîne de caractères précisant le nom du fichier dans lequel sera sauvegardée
        l'histoire modifiée comme précisé ci-dessous.

Exemple:
    Sachant que le fichier histoire_1.txt contient le texte :
        Si Pierre est le fils de Paul, et si Paul est le frère de Jacqueline, qui est Pierre pour Jacqueline ?

    après l'appel suivant de la fonction :
        nouveaux_heros("histoire_1.txt", "nouvelle_histoire_1.txt")

    le fichier dont le nom est nouvelle_histoire_1.txt doit contenir le texte :
        Si Paul est le fils de Tom, et si Tom est le frère de Mathilde, qui est Paul pour Mathilde ?

"""


def nouveaux_heros(histoire, nouv_histoire):
    with open(histoire, 'r', encoding='utf-8') as f:
        texte = f.read()
        texte = texte.replace('Jacqueline', 'Mathilde').\
            replace('Paul', 'Tom').replace('Pierre', 'Paul')
        with open(nouv_histoire, 'w', encoding='utf-8') as res:
            res.write(texte)


nouveaux_heros("histoire_1.txt", "nouvelle_histoire_1.txt")
#nouveaux_heros("histoire_2.txt", "nouvelle_histoire_2.txt")
