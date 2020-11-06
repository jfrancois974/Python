"""  Auteur: Jean-François BATAILLE

    Date : AVRIL 2020
    Projet : Apprentissage Python 3

Objectif:

    Écrire un programme qui lit en entrée une valeur naturelle n et qui affiche
     à l’écran un triangle supérieur droit formé de X (voir exemples plus bas).


"""
# 1ère solution avec while

nbr = int(input("Entrez votre nombre : "))
lettre = "X"
y = 0
z = 0
nbr2 = nbr
print (nbr2 * lettre)
espace = " "
while y != nbr:
#   print ((z * (" ")), nbr2 * lettre)
    print("", nbr2 * lettre, sep=z * espace, end='\n')
    y = y + 1
    z = z + 1
    nbr2 = nbr2 -1


espace = " "
print("", nbr2 * lettre, sep=espace, end='\n')

# 2ème solution avec une code simplifié avec une boucle for

x = int(input("Entrez votre nombre : "))
s = 0
for s in range(x):
    x -= 1
    s += 1
    print(((s - 1) * ' ' ) + (x + 1) * 'X')