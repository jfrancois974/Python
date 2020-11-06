"""
        Auteur: Jean-François BATAILLE

        Date : AVRIL 2020
        Projet : Apprentissage Python 3

Objectif:

    On considère une liste qui décrit une séquence t. Chaque élément de cette liste est un tuple de deux composantes :
    le nombre de répétitions successives de l’élément x dans la séquence t, et l’élément x lui-même.

    Par exemple, la liste [(1, 'He'), (2, 'l'), (1,'o')] décrit la séquence "Hello".

    Écrire une fonction decompresse qui reçoit une telle liste en paramètre et renvoie la séquence t sous forme
    d’une nouvelle liste.

Exemples:
    decompresse([(4, 1), (0, 2), (2, 'test'), (3, 3), (1, 'bonjour')])
    doit retourner: [1, 1, 1, 1, 'test', 'test', 3, 3, 3, 'bonjour']


"""


def decompresse(liste):
	res = []
	for i in range(len(liste)):
		res += liste[i][0] * [liste[i][1]]
	return res


decompresse([(4, 'b'), (0, 'x'), (2, 'on'), (3, 'j'), (1, 'our')])
# [1, 1, 1, 1, 2, 2, 'test', 'test', 3, 3, 3, 'bonjour']

