"""
        Auteur: Jean-François BATAILLE

        Date : AVRIL 2020
        Projet : Apprentissage Python 3

Objectif:

    Nous pouvons définir la distance entre deux mots de même longueur (c’est-à-dire 
    ayant le même nombre de lettres) mot_1 et mot_2 comme le nombre minimum de fois où 
    il faut modifier une lettre de mot_1 pour obtenir mot_2 (distance de Hamming).

    Par exemple, les mots « lire » et « bise » sont à une distance de 2, puisqu’il faut changer 
    le “l” et le “r” du mot « lire » pour obtenir « bise ».

    Écrire une fonction distance_mots(mot_1, mot_2) qui retourne la distance entre deux mots.

    Vous pouvez supposer que les deux mots sont de même longueur, et sont écrits sans accents.

Exemples:
    distance_mots("lire", "bise") doit retourner: 2
    distance_mots("Python", "Python") doit retourner: 0
    distance_mots("merci", "adieu") doit retourner: 5


"""
# ma première solution pas la plus simple


def distance_mots(mot_1, mot_2):
    dist_i = [k for k in range(len(mot_1)+1)]
    for i in range(1, len(mot_2) + 1):
        dist_prec = dist_i
        dist_i = [i]*(len(mot_1)+1)
        for k in range(1, len(dist_i)):
            cont = int(mot_1[k-1] != mot_2[i-1])
            dist_i[k] = min(dist_i[k-1] + 1, dist_prec[k] +
                            1, dist_prec[k-1] + cont)
    return dist_i[len(mot_1)]


# ma deuxième solution la plus simple

def distance_mot(mot_1, mot_2):
    res = 0
    for i in range(len(mot_1)):
        if id(mot_1[i]) != id(mot_2[i]):
            res = res + 1
    return res


distance_mot("lire", "bise")
