""" Auteur: Jean-François BATAILLE

    Date : Mars 2020
    Projet : Apprentissage Python 3

Objectif:

    Écrire un programme qui lit des valeurs de type float pour a, b et c et qui affiche la valeur de d correspondant à la règle de trois.

Consignes:

    Attention, nous rappelons que votre code sera évalué en fonction de ce qu’il affiche, donc veuillez à n’imprimer que le résultat attendu.

    En particulier, il ne faut rien écrire à l’intérieur des appels à input (float(input()) et non float(input("Entrer un nombre : ")) par exemple),
    ni ajouter du texte dans ce qui est imprimé (print(res) et non print("résultat :", res) par exemple).

"""

a = float(input())
b = float(input())
c = float(input())
d = (b * c) / a
print(d)