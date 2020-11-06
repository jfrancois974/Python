"""
        Auteur: Jean-François BATAILLE

        Date : AVRIL 2020
        Projet : Apprentissage Python 3
        
Objectif:

    Après avoir longuement réfléchi et un peu visité notre monde, le Petit Prince décide de ne pas rentrer sur sa planète
    mais de s’installer dans les Cévennes pour profiter de la belle nature qu’on y trouve.
    Il y trouve une petite demeure pour y habiter, et plusieurs de ses amis veulent l’aider en lui proposant des meubles,
    des denrées, des livres ou d’autres choses qui pourraient l’intéresser pour aménager son nouveau domicile.

    Nous vous proposons de l'aider.
    Écrire une fonction inventaire(offres, objets) où :

        offres est un dictionnaire contenant, comme clés, les objets proposés par les amis du Petit Prince,
        et comme valeurs associées, le nom de l'ami proposant cet objet,
        
        objets est une liste contenant tous les objets dont a besoin le Petit Prince.

    La fonction retourne l'ensemble des amis chez qui il lui faut se rendre pour sa récolte.

"""


def inventaire(offres, objets):
    amis = set()
    for i in range(len(objets)):
        print(offres[objets[i]])
        amis |= {offres[objets[i]]}
    return amis


print(inventaire({'lit': 'Antoine', 'bibliothèque': 'Sébastien', 'chaise': 'Isabelle',
                  'livre "le vieil homme et la mer"': 'Ernest', 'sac de bonbons': 'Thierry', 'smartphone': 'Ted',
                  'table': 'Sophie'}, ['sac de bonbons', 'table', 'chaise', 'lit', 'livre "le vieil homme et la mer"']))


# res = {'Thierry', 'Sophie', 'Isabelle', 'Antoine', 'Ernest'}

print(inventaire({'livre "le vieil homme et la mer"': 'Ernest', 'bibliothèque': 'Sébastien', 'chaise': 'Isabelle', 'smartphone': 'Ted', 'table': 'Isabelle',
                  'sac de bonbons': 'Sébastien', 'lit': 'Sébastien'}, ['sac de bonbons', 'table', 'chaise', 'lit', 'livre "le vieil homme et la mer"']))

# res = {'Sébastien', 'Isabelle', 'Ernest'}
