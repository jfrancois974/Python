"""
Projet Vasarely (MOOC Python)
Auteur : Jeff
Date : Mai 2020

Programme permettant de dessiner un pavage d'hexagone à la manière d'un tableau  de Vasarely.
Entrée du programme : coordonnées du centre inférieur gauche (une seule valeur), coordonnées du centre supérieur droit
(une seule valeur), longueur du segment d'un losange avant déformation, couleur (tuple de 3 couleurs) du pavé, coordonnées
du centre de la sphère de déformation (tuple de 3 valeurs), rayon du centre de déformation
Sortie : pavage selon Vasarely

"""
# importation des modules nécessaires à l'éxécution du programme
import turtle
import math

# importation du fichier fourni pour la déformation
from deformation import deformation


def hexagone(point, longueur, col, centre, rayon):
    """ Fonction qui dessine avec turtle un pave hexagonal
        paramètres :
        - point : tuple des 2 coordonnées du centre du pavé
        - longueur : longueur de chaque segment du pavé
        - col : tuple de 3 couleurs (1 couleur pour chaque pavé composant l'hexagone)"""

    turtle.up()  # on lève la tortue pour ne pas dessiner pendant son déplacement jusqu'au point central du pavé)

    # calcul des coordonnées du centre de l'hexagone déformé
    point_deforme = (deformation((point[0], point[1], 0), centre, rayon)[
                     0], deformation((point[0], point[1], 0), centre, rayon)[1])

    # déplacement de la tortue au centre de l'hexagon déformé, point de départ du tracé
    turtle.goto(point_deforme[0], point_deforme[1])

    # position des sommets du 1er pavé partir des cordonnées du centre (variable point)
    losange1_sommet1 = [(point[0] + longueur), point[1]]
    losange1_sommet2 = [(point[0] + (longueur * math.cos(math.pi / 3))),
                        (point[1] + (longueur * math.sin(math.pi / 3)))]
    losange1_sommet3 = [(point[0] - (longueur * math.cos(math.pi / 3))),
                        (point[1] + (longueur * math.sin(math.pi / 3)))]

    # position des sommets du 2ème losange à partir des cordonnées du centre (variable point)
    losange2_sommet1 = [(point[0] - (longueur * math.cos(math.pi/3))),
                        (point[1] + (longueur * math.sin(math.pi/3)))]
    losange2_sommet2 = [(point[0] - longueur), point[1]]
    losange2_sommet3 = [(point[0] - (longueur * math.cos(math.pi/3))),
                        (point[1] - (longueur * math.sin(math.pi/3)))]

    # position des sommets du 3ème losange à partir des cordonnées du centre (variable point)
    losange3_sommet1 = [(point[0] - (longueur * math.cos(math.pi/3))),
                        (point[1] - (longueur * math.sin(math.pi/3)))]
    losange3_sommet2 = [(point[0] + (longueur * math.cos(math.pi/3))),
                        (point[1] - (longueur * math.sin(math.pi/3)))]
    losange3_sommet3 = [(point[0] + longueur), point[1]]

    # coordonnées des points de chaque losange
    losange1 = [losange1_sommet1, losange1_sommet2, losange1_sommet3, point]
    losange2 = [losange2_sommet1, losange2_sommet2, losange2_sommet3, point]
    losange3 = [losange3_sommet1, losange3_sommet2, losange3_sommet3, point]

    # coordonnées de chaque losange qui constituent l'hexagone
    losange_hexagone = [losange1, losange2, losange3]

    for i in range(3):  # on boucle sur chacun des 3 pavés composant 1 hexagone
        los = losange_hexagone[i]  # losange à dessiner
        turtle.color(col[i])  # choix de la couleur pour le remplissage
        # on commence le remplissage avec la couleur col[i]
        turtle.begin_fill()
        for i in range(4):  # on bouche sur chacun des 4 segments composant 1 losange
            pt = los[i]  # désignation du point suivant à atteindre

            # déplacement du pointeur jusqu'aux coordonnées après déformation
            turtle.goto((deformation((pt[0], pt[1], 0), centre, rayon)[
                        0], deformation((pt[0], pt[1], 0), centre, rayon)[1]))
        turtle.end_fill()  # fin du remplissage


def pavage(inf_gauche, sup_droit, longueur, col, centre, rayon):
    """ Fonction qui dessine avec turtle un pavage hexagonal à partir de la fonction hexagone
        paramètres :
        - bornes graphiques (inf_gauche et sup_droit) : tuple des 2 coordonnées du centre du pavé
        - longueur : longueur de chaque segment du pavé
        - col : tuple de 3 couleurs (1 couleur pour chaque pavé composant l'hexagone)
        - centre : coordonnées (tuple de 3 valeurs) du centre de la sphère de déformation
        - rayon : rayon de la sphère de déformation
        """
    x_max = sup_droit[0]  # coordonnée selon x du dernier pavé en haut à droite
    # coordonnée selon y du dernier pavé en haut à droite (égal à x_max dans la consigne
    y_max = sup_droit[1]
    # mais pourrait être différente
    x_min = inf_gauche[0]  # coordonnée selon x du premier pavé en bas à gauche
    # coordonnée selon y du premier pavé en bas à gauche (égal à x_min dans la consigne
    y_min = inf_gauche[1]
    # mais pourrait être différente
    position = [x_min, y_min]  # tuple des coordonnées minimales
    num_ligne = 0  # variable pour savoir sur quel type de ligne on trace les pavés : paire ou impair
    while position[1] <= y_max:  # on boucle tant qu'on n'atteint pas le haut de la fenêtre
        # on boucle tant qu'on n'atteint pas le bord droit de la fenêtre
        while position[0] <= x_max:
            # on trace l'hexagone en partant du bas gauche
            hexagone((position[0], position[1]), longueur, col, centre, rayon)
            # on décale de 3 longueurs l'hexagone suivant pour qu'ils se touchent
            position[0] = position[0]+3*longueur
        # décalage y du pavé de rang supérieur
        position[1] = position[1] + longueur * math.cos(30 * math.pi / 180)
        num_ligne = num_ligne+1  # incrémentation du numéro de ligne
        if num_ligne % 2 == 0:  # si la ligne est paire, on doit décaler le début du pavage
            position[0] = x_min
        else:
            # si la ligne est impaire, on commence la pavage à x_min
            position[0] = x_min+1.5*longueur


"""Programme principal qui récupère les données saisies par l'utilisateur puis qui lance le pavage
"""

# demande à l'utilisateur des coordonnées des positions extrêmes du pavage
bord_gauche = int(input("coordonnée du bord inférieur gauche : "))
inf_gauche = (bord_gauche, bord_gauche)
bord_droit = int(input("coordonnée du bord supérieur droit : "))
sup_droit = (bord_droit, bord_droit)

# demande à l'utilisateur de la longueur des segments
longueur = int(input("longueur du segment du pavé : "))

# demande à l'utilisateur des couleurs de remplissage du pavage
col1 = str(input("couleur du 1er pavé (en haut à droite) : "))
col2 = str(input("couleur du 2ème pavé (en gauche) : "))
col3 = str(input("couleur du 3ème pavé (en bas à droite) : "))
col = (col1, col2, col3)  # création du tuple des 3 couleurs

# demande à l'utilisateur des coordonnées du centre de la sphère de formation
x_centre = int(input("coordonnées x du centre : "))
y_centre = int(input("coordonnées y du centre : "))
z_centre = int(input("coordonnées z du centre : "))
# création du tuple des coordonnées du centre de la sphère de déformation
centre = (x_centre, y_centre, z_centre)

# demande à l'utilisateur du rayon de la sphère de déformation
rayon = int(input("rayon de la sphère de déformation : "))

# Let's go pour le pavage !
pavage(inf_gauche, sup_droit, longueur, col, centre,
       rayon)  # fonction pour créer le pavage

turtle.getcanvas().postscript(file="pavage.eps")
turtle.done()


"""
Exécution du programme
Exemple d'entrée :
((-300,300,20),('blue','black','red'),(-50,-50,-50),200)
"""
