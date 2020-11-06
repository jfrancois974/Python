
"""
        Auteur: Jean-François BATAILLE

        Date : AVRIL 2020
        Projet : Apprentissage Python 3


Objectif:

    Écrire une fonction intersection(v, w) qui calcule l’intersection entre deux chaînes de caractères v et w.

    On définit l’intersection de deux mots comme étant la plus grande partie commune à ces deux mots.
    Par exemple, l’intersection de « programme » et « grammaire » est « gramm ».

    Si les deux chaînes n’ont aucun caractère en commun, la fonction retourne la chaîne vide, ''.

    Si plusieurs solutions sont possibles, la fonction retournera la sous-chaîne d’indice minimal dans v.
    Par exemple, intersection('bbaacc', 'aabb') renvoie 'bb'.

Exemples:
    intersection('programme', 'grammaire') doit retourner: 'gramm'
    intersection('salut', 'merci') doit retourner: ''
    intersection('merci', 'adieu') doit retourner: 'e'


"""


def intersection(v, w):
    long_mot_v = len(v)
    # print('### ', v, w)
    for part in range(long_mot_v, 0, -1):
        # print(' -- Par taille', size)
        for i in range(long_mot_v - part + 1):
            commun = v[i:i + part]
            # print('   - Extrait', extrait)
            if commun in w:
                return commun
    return ''


intersection('soigneur', 'guerison')
intersection('abracadabra', 'acdaabrabar')
