"""
        Auteur: Jean-François BATAILLE

        Date : AVRIL 2020
        Projet : Apprentissage Python 3

Objectif:

    Écrire une fonction substitue(message, abréviation) qui renvoie une copie de la chaîne de caractères message dans laquelle 
    les mots qui figurent parmi les clés du dictionnaire abréviation sont remplacés par leur signification (valeur).


"""


def substitue(message, abreviation):
    for c in abreviation:
        message = message.replace(c, abreviation[c])
    return message


# ~L’appel suivant de la fonction :


print(substitue('C. N. cpt 2 to inf', {'C.': 'Chuck',
                                       'N.': 'Norris',
                                       'cpt': 'counted',
                                       '2': 'two times',
                                       'inf': 'infinity'}))
# doit retourner : 'Chuck Norris counted two times to infinity'

print(substitue('viva C. N. : C. N. cpt 2 to inf and even further', {
      'N.': 'Norris', '2': '2 times', 'C.': 'Chuck', 'inf': 'infinity', 'cpt': 'counted'}))
