"""
        Auteur: Jean-François BATAILLE

        Date : AVRIL 2020
        Projet : Apprentissage Python 3
        
Objectif:

    Écrire une fonction valeurs(dico) qui doit fournir, à partir du dictionnaire donné en paramètre,
    une lst des valeurs du dictionnaire triées selon leur clé.


"""


def valeurs(dico):
    lst = []  # on crée la lst
    for key in sorted(dico):  # on parcours les clés (par ordre alphabétique) passées dans dico
        lst.append(dico[key])  # puis on ajoute à la lst les valeurs
    return lst


print(valeurs({'Michel': ['Luc'], 'Luc': [], 'Bernadette': ['Luc', 'Michel', 'Jules'], 'Jules': [
      'Bernadette'], 'Germaine': ['Catherine'], 'Catherine': ['Jean'], 'Jean': ['Germaine']}))


print(valeurs({'4': 'quatre', '2': 'deux', '1': 'un',
               '6': 'six', '3': 'trois', '5': 'cinq'}))
