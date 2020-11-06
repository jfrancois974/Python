"""
        Auteur: Jean-François BATAILLE

        Date : AVRIL 2020
        Projet : Apprentissage Python 3

Objectif:

    Écrire une fonction construction_dict_amis qui reçoit une liste de couples (prenom1, prenom2) signifiant que prenom1 déclare prenom2 comme étant son ami.

    La fonction construit et renvoie un dictionnaire dont les clés sont les prénoms des personnes nommées, et la valeur de chaque entrée est l’ensemble des amis de la personne.


"""


def construction_dict_amis(personnes):
    dic = {}
    for name1, name2 in personnes:
        if name1 not in dic:
            dic[name1] = {name2}
        else:
            dic[name1].add(name2)
        if name2 not in dic:
            dic[name2] = set()
    return dic


print(construction_dict_amis([('Quidam', 'Pierre'),
                              ('Thierry', 'Michelle'),
                              ('Thierry', 'Pierre')]))
print(construction_dict_amis([('Pierre', 'Michelle'), ('Bernadette', 'Ariane'), ('Michelle', 'Thierry'), ('Ariane', 'Bernadette'), ('Pierre', 'Ariane'), ('Michelle', 'Ariane'), ('Bernadette', 'Ariane'), ('Michelle', 'Thierry'), ('Quidam', 'Quidam'), (
    'Michelle', 'Pierre'), ('Michelle', 'Thierry'), ('Quidam', 'Quidam'), ('Thierry', 'Pierre'), ('Thierry', 'Ariane'), ('Pierre', 'Bernadette'), ('Pierre', 'Quidam'), ('Pierre', 'Michelle'), ('Pierre', 'Quidam'), ('Ariane', 'Thierry')]))
