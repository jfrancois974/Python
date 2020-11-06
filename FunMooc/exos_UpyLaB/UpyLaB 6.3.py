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


def top_3_candidats(moyennes):
    l = []
    for i in range(3):
        l.extend([c for c in moyennes if moyennes[c] ==
                  max(moyennes[d] for d in moyennes)])
        moyennes.pop(l[-1])
    return tuple(l)


top_3_candidats({'Candidat 3': 43, 'Candidat 5': 94,
                 'Candidat 2': 76, 'Candidat 1': 84, 'Candidat 4': 22})


top_3_candidats({'Candidat 3': 43, 'Candidat 5': 94,
                 'Candidat 2': 76, 'Candidat 1': 84, 'Candidat 4': 22})
