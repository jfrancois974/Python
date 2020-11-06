"""
        Auteur: Jean-François BATAILLE

        Date : AVRIL 2020
        Projet : Apprentissage Python 3

Objectif:

    Écrire une fonction prime_odd_numbers(numbers) qui reçoit une lst de nombres et qui renvoie un couple d’ensembles contenant
    respectivement les nombres premiers présents dans la lst et les nombres impairs.

    Pour cela, nous vous demandons d’écrire deux fonctions annexes qui seront appelées dans le corps de la fonction prime_odd_numbers :
        la fonction even(max_nb) qui renvoie l’ensemble des nombres naturels pairs inférieurs ou égaux à max_nb
        la fonction prime_numbers(max_nb) qui renvoie l’ensemble des nombres premiers inférieurs ou égaux à max_nb.

Exemples:
    prime_odd_numbers([1, 2, 6, 5, 11, 9, 13, 14, 12, 15, 17, 18])
    retourne, à l’ordre près, : ({2, 5, 11, 13, 17}, {1, 5, 11, 9, 13, 15, 17})
    
    prime_odd_numbers([1, 4, 6, 12, 9, 15, 16, 21, 18])
    retourne, à l’ordre près, : (set(), {1, 9, 15, 21})


"""


def prime_numbers(max_nb):
    lst = set()
    for n in range(2, max_nb+1):
        c = 1
        for i in range(2, int(n**(1/2))+1):
            if n % i == 0:
                c = 0
        if c or n == 2:
            lst.add(n)
    return lst


def even(max_nb):
    lst = set()
    for i in range((max_nb+2)//2):
        lst.add(2*i)
    return lst


def prime_odd_numbers(numbers):
    ensemble1 = set()
    ensemble2 = set()
    max_nb = max(numbers)
    l1, l2 = prime_numbers(max_nb), even(max_nb)
    for i in numbers:
        if i in l1:
            ensemble1.add(i)
        if i not in l2:
            ensemble2.add(i)
    return ensemble1, ensemble2


print(even(36))
# retourne {0, 32, 2, 34, 4, 36, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30}

print(prime_numbers(62))
# retourne {2, 3, 5, 37, 7, 41, 11, 43, 13, 47, 17, 19, 61, 53, 23, 59, 29, 31})

print(prime_odd_numbers([1, 5, 9, 13, 17, 21, 25, 29, 33, 37,
                         41, 45, 49, 53, 57, 61, 65, 69, 73, 77, 81, 85, 89, 93, 97]))
# doit retourner ({97, 37, 5, 41, 73, 13, 17, 61, 53, 89, 29}, {1, 5, 9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53, 57, 61, 65, 69, 73, 77, 81, 85, 89, 93, 97})
