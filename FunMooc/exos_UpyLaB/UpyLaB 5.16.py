"""
        Auteur: Jean-François BATAILLE

        Date : AVRIL 2020
        Projet : Apprentissage Python 3

Objectif:

    Écrire une fonction my_pow qui prend comme paramètres un nombre entier m et un nombre flottant b,
    et qui renvoie une liste contenant les m premières puissances de b, c’est-à-dire une liste contenant
    les nombres allant de b^0 à b^{m - 1}.

    Si le type des paramètres n’est pas celui attendu, la fonction retournera la valeur None.

Exemples:
    my_pow(3, 5.0) doit retourner: [1.0, 5.0, 25.0]
    my_pow(3.0, 5.0) doit retourner: None
    my_pow('a', 'b') doit retourner: None


"""


def my_pow(m, b):
    if isinstance(m, int) and isinstance(b, float):
        return [b**i for i in range(int(m))]
