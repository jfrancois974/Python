
"""
        Auteur: Jean-François BATAILLE

        Date : AVRIL 2020
        Projet : Apprentissage Python 3

Objectif:

    Écrire une fonction dupliques qui reçoit une séquence en paramètre.

    La fonction doit renvoyer la valeur booléenne True si la séquence passée en paramètre contient des éléments dupliqués
    et la valeur booléenne False sinon.

Exemples:
    dupliques([1, 2, 3, 4]) doit retourner: False
    dupliques(['a', 'b', 'c', 'a']) doit retourner: True
    dupliques('abcda') doit retourner: True


"""


def dupliques(s):
    d = list(s)
    d.sort()
    for i in range(len(d)-1):
        if d[i] == d[i+1]:
            return True
    return False


dupliques(['a', 'b', 'c', 'a'])
dupliques('TAGCGGGATACTCTGG')
