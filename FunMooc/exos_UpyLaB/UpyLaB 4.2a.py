"""
     Auteur: Jean-François BATAILLE

        Date : AVRIL 2020
        Projet : Apprentissage Python 3

Objectif:
    Le Petit Prince vient de débarquer sur la planète U357, et il apprend qu'il peut y voir de belles aurores boréales !

    La planète U357 a deux soleils : les étoiles E1515 et E666.  C'est pour cela que les tempêtes magnétiques sont permanentes,
    ce qui est excellent pour avoir des aurores boréales.

    Par contre, il y fait souvent jour, sauf bien évidemment quand les deux soleils sont couchés en même temps.

    Heureusement pour nous, une journée U357 s'écoule sur 24 heures comme sur notre Terre, et pour simplifier,
    nous ne prendrons pas en compte les minutes (on ne donne que les heures avec des valeurs entières entre 0 et 23). 

    Nous vous demandons d'aider le Petit Prince à déterminer les périodes de jour et de nuit.

    UPYLAB 4.2A

    Pour cela, vous allez dans un premier temps écrire une fonction soleil_leve qui, pour un soleil particulier, reçoit trois valeurs entières en argument pour la planète :
     - l'heure de lever du soleil (entre 0 et 23)
     - l'heure du coucher du soleil (entre 0 et 23)
     - l'heure actuelle (entre 0 et 23)

    et qui renvoie une valeur booléenne vraie si le soleil est levé sur la planète à l'heure donnée en troisième argument et fausse, s'il est couché.

    On supposera que chacun des soleils ne se lève et ne se couche au plus qu'une seule fois par jour.
    Il est toutefois possible que le lever ait lieu après l'heure du coucher, ce qui signifie dans ce cas que le soleil est levé au début de la journée, puis qu'il se couche, puis qu'il se lève à nouveau plus tard dans la journée.
    Enfin, si l'heure du lever est la même que l'heure du coucher :
     - soit toutes deux valent 12, cela signifie que le soleil ne se lève pas de la journée,
     - soit toutes les deux valent 0, cela signifie que le soleil ne se couche pas de la journée.


"""

def soleil_leve(a, b, c):
    if a == 0 and b == 0:
        return True
    elif a == 12 and b == 12:
        return False
    elif c > b and b > a:
        return False
    elif b == c and c != a:
        return False
    elif c < a and a < b:
        return False
    elif c > b and c < a:
        return False
    elif c >= a and c < b:
        return True
    elif a > b and c > a and c > b:
        return True
    elif c < b and b < a:
        return True


"""
    simplification avec une seule condition

    def soleil_leve(heure_leve, heure_coucher, heure_actuelle):
        if heure_leve <= heure_actuelle < heure_coucher or heure_coucher < heure_leve <= heure_actuelle 
        or heure_leve==heure_coucher==0 or heure_actuelle < heure_coucher < heure_leve:
            return True
        return False
"""
print(soleil_leve(12, 12, 23))
print(soleil_leve(6, 18, 10))
print(soleil_leve(15, 8, 12))




