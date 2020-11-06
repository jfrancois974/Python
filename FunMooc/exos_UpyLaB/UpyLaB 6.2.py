"""
        Auteur: Jean-François BATAILLE

        Date : AVRIL 2020
        Projet : Apprentissage Python 3

Objectif:

    Écrire une fonction calcul_prix(produits, catalogue) où :
        produits est un dictionnaire contenant, comme clés, les produits souhaités par Monsieur Germain et comme valeurs associées, 
        la quantité désirée de chacun d’entre eux, catalogue est un dictionnaire contenant tous les produits du magasin avec leur prix associé.

    La fonction retourne le montant total des achats de Monsieur Germain.


"""


def calcul_prix(produits, catalogue):
    s = 0
    for _, prix in enumerate(produits):  # _ unused variable
        s += produits[prix] * catalogue[prix]
    return s


print(calcul_prix({'shampooing': 2, 'farine': 1, 'viande': 1, 'pack de légumes': 1, 'savon': 1, 'dentifrice': 2, 'brocoli': 1, 'huile': 1, 'yaourts': 2, 'vin': 2, 'sucre': 2, 'fromage': 2, 'confiture': 1, 'pâtes': 2, 'pain': 2}, {'shampooing': 2.5, 'café': 4.75, 'farine': 0.95, 'pack de légumes': 4.2, 'jus de fruits': 2.25, 'bière': 2, 'dentifrice': 1.95, 'fromage': 2.65,
                                                                                                                                                                                                                                      'brocoli': 1.5, "bouteilles d'eau": 1, 'sucre': 0.65, 'confiture': 3.15, 'mouchoirs': 0.8, 'riz': 3.1, 'pâtes': 1.1, 'viande': 5.2, 'déodorant': 2.2, 'jambon': 2.1, 'frites': 3.55, 'tomate': 0.75, 'citron': 0.9, 'petits gâteaux': 4.35, 'pain': 1.25, 'huile': 1.65, 'yaourts': 2.85, 'vin': 6.3, 'savon': 1.9, 'pack de fruits': 3.3, 'poisson': 6.45, 'chocolats': 3.2}))


print(calcul_prix({'farine': 1, 'viande': 1, 'frites': 1, 'tomate': 1, 'dentifrice': 1, 'fromage': 1, 'chocolats': 1, 'huile': 2, 'yaourts': 2, 'savon': 1, 'confiture': 3, 'mouchoirs': 1, 'déodorant': 1, 'pâtes': 1, 'poisson': 1}, {'shampooing': 2.5, 'café': 4.75, 'farine': 0.95, 'pack de légumes': 4.2, 'jus de fruits': 2.25, 'bière': 2, 'dentifrice': 1.95, 'fromage': 2.65,
                                                                                                                                                                                                                                        'brocoli': 1.5, "bouteilles d'eau": 1, 'sucre': 0.65, 'confiture': 3.15, 'mouchoirs': 0.8, 'riz': 3.1, 'pâtes': 1.1, 'viande': 5.2, 'déodorant': 2.2, 'jambon': 2.1, 'frites': 3.55, 'tomate': 0.75, 'citron': 0.9, 'petits gâteaux': 4.35, 'pain': 1.25, 'huile': 1.65, 'yaourts': 2.85, 'vin': 6.3, 'savon': 1.9, 'pack de fruits': 3.3, 'poisson': 6.45, 'chocolats': 3.2}))
