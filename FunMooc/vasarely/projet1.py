"""
Projet Vasarely
Auteur : Jeff
Date : Mai 2020
Ce programme permet de réaliser une sorte de damier constitué d'hexagones. Celui-ci pourra si on le souhaite être déformé par une sphère dont on donnera
les paramètres. Les hexagones sont eux même formés de trois pavés dont on pourra paramétrer les couleurs.
La fonction demandera successivement tous les paramètres a l'utilisateur.

Entrées : 
    inf_gauche : définit le coin inférieur gauche de la figure
    sup_droit : définit le coin supérieur droit
    longueur : longueur entre le centre et n’importe quel coin des hexagones
    col=(col1,col2,col3) : donne les trois couleurs des pavés formant les hexagones
    centre=(c_x,c_y,c_z) : définit le centre de la sphère déformant le damier
    rayon : définit le rayon de la sphère déformant le damier

Résultat :
   Une fenêtre turtle s'ouvre et dessine sous vos yeux la figure demandée.
   Le résultat est enregistré dans le répertoire de Pycharm sous le nom : projet_vasarely.eps


Le programme a besoin de 3 fonctions pour fonctionner :

    deformation(p, centre, rayon) : fonction importée du module_deformation qui calcule des coordonnées d'un point suite à la
déformation engendrée par la sphère émergeante.

Deux autres fonctions internes sont présentes dans le programme :

    hexagone(point, longueur, col, centre, rayon) qui dessine UN hexagone

    pavage(inf_gauche,sup_droit, longueur, col, centre, rayon) qui dessine TOUS les hexagones en damier


"""


import turtle
from math import cos, sin, pi, sqrt
from deformation import deformation


"""
Fonction hexagone déssinant un hexagone comme association de 3 pavés. Celle ci comporte 5 paramètres, respectivement :
    Entrées :
        point : triple donnant la valeur des trois coordonnées du centre, avant déformation de l’hexagone
        longueur : longueur entre le centre et n’importe quel coin de l’hexagone
        col :  tuple contenant les trois couleurs (col1, col2, col3) qui vont être utilisées pour dessiner les pavés formant l'hexagone
        centre :  triple de la forme (c_x, c_y, c_z) qui donne le centre de la sphère de déformation
        rayon : rayon de la spère de déformation
    
    Sortie : hexagone avec les paramètres désirés tracé dans une nouvelle fenêtre avec le module turtle
"""


def hexagone(point, longueur, col, centre, rayon):

    # centre de l'hexagone auquel on applique la déformation
    origine_hexagone = deformation(point, centre, rayon)

    # Tortue devient lièvre !
    turtle.speed(0)

    # tracé du premier pavé dont les sommets correspondent aux angles 0,pi/3 et 2pi/3 sur le cercle circonscrit à l'hexagone' auxquels on applique la déformation
    turtle.up()
    turtle.goto((origine_hexagone[0], origine_hexagone[1]))
    turtle.down()
    turtle.color(col[0])
    turtle.begin_fill()
    for i in range(0, 3):
        sommet_hexagone = deformation((longueur * cos(i * pi / 3) + point[0], longueur * sin(i * pi / 3) + point[1], point[2]),
                                      centre, rayon)
        # seules les deux premières composantes des coordonnées des sommets déformés sont donnés à turtle.goto
        turtle.goto((sommet_hexagone[0], sommet_hexagone[1]))
    turtle.goto((origine_hexagone[0], origine_hexagone[1]))
    turtle.end_fill()

    # tracé du second pavé dont les sommets correspondent aux angles 2pi/3,pi et 4pi/3 sur le cercle circonscrit à l'hexagone auxquels on applique la déformation
    turtle.color(col[1])
    turtle.begin_fill()
    for i in range(2, 5):
        sommet_hexagone = deformation(
            (longueur * cos(i * pi / 3) +
             point[0], longueur * sin(i * pi / 3) + point[1], point[2]),
            centre, rayon)
        turtle.goto((sommet_hexagone[0], sommet_hexagone[1]))
    turtle.goto((origine_hexagone[0], origine_hexagone[1]))
    turtle.end_fill()

    # tracé du troisième pavé dont les sommets correspondent aux angles 4pi/3,5pi/3 et 2pi sur le cercle circonscrit à l'hexagone auquels on applique la déformation
    turtle.color(col[2])
    turtle.begin_fill()
    for i in range(4, 7):
        sommet_hexagone = deformation(
            (longueur * cos(i * pi / 3) +
             point[0], longueur * sin(i * pi / 3) + point[1], point[2]),
            centre, rayon)
        turtle.goto((sommet_hexagone[0], sommet_hexagone[1]))
    turtle.goto((origine_hexagone[0], origine_hexagone[1]))
    turtle.end_fill()
    return()


"""
Fonction pavage 
Cette fonction dessine le damier d'hexagones incluant la déformation visuelle : une sphère de centre et de rayon donnés qui ressort du plan
La fonction pavage trace les hexagones en les supperposant et forme ainsi des colonnes, celles ci forment deux groupes : celles dont l'ordonnée du centre de l'hexagone du bas est égal à inf_gauche 
et celles dont l'ordonnée du centre de l'hexagone du bas est égal à inf_gauche+longueur+sqrt(longueur**2-(longueur**2)*(sin(pi/3)**2)), le décalage formant le damier.
    Entrées :
        inf_gauche : entier définissant le coin inférieur gauche de la fenetre turtle
        sup_droit : entier définissant le coin supérieur droit de la fenetre turtle
        longueur : longueur entre le centre et n’importe quel coin de l’hexagone
        col : tuple contenant les trois couleurs (col1, col2, col3) qui vont être utilisées pour dessiner les pavés formant l'hexagone
        centre : triple de la forme (c_x, c_y, c_z) qui donne le centre de la sphère de déformation
        rayon : rayon de la spère de déformation
"""


def pavage(inf_gauche, sup_droit, longueur, col, centre, rayon):

    # ouverture d'une fenêtre turtle dont le coin inférieur gauche est (inf_gauche, inf_gauche) et le coin supérieur droit est (sup_droit, sup_droit)
    turtle.setworldcoordinates(inf_gauche, inf_gauche, sup_droit, sup_droit)

    # Tracé du premier groupe de colonne : celles dont l'ordonnée du centre de l'hexagone du bas est égal à inf_gauche
    # Coordonnées du centre du premier hexagone de la première colonne du damier
    centre_hexagone = (inf_gauche, inf_gauche, 0)

    # Calcul du nombre d'hexagone à tracer dans le sens de la hauteur de l'écran
    nombre_centre_vertical = int(
        (sup_droit-inf_gauche)/(2*longueur*sin(pi/3)))+1

    # Calcul du nombre d'hexagone à tracer dans le sens de la largeur l'écran
    nombre_centre_horizontal = int((sup_droit-inf_gauche)/(longueur*3))+1

    for i in range(0, nombre_centre_vertical):
        for j in range(0, nombre_centre_horizontal):
            hexagone((centre_hexagone[0]+j*3*longueur, centre_hexagone[1] +
                      i*2*longueur*sin(pi/3), 0), longueur, col, centre, rayon)

    # Coordonnées du centre du premier hexagone de la seconde colonne du damier
    centre_hexagone = (inf_gauche+longueur+sqrt(longueur**2-(longueur**2)
                                                * (sin(pi/3)**2)), inf_gauche+longueur*sin(pi/3), 0)

    # Calcul du nombre d'hexagone à tracer dans le sens de la hauteur de l'écran
    nombre_centre_vertical = int(
        (sup_droit-inf_gauche+longueur*sin(pi/3))/(2*longueur*sin(pi/3)))+1

    # Calcul du nombre d'hexagone à tracer dans le sens de la largeur l'écran
    nombre_centre_horizontal = int(
        (sup_droit-inf_gauche+sqrt(2)*longueur)/(longueur*3))+1

    for i in range(0, nombre_centre_vertical):
        for j in range(0, nombre_centre_horizontal):
            hexagone((centre_hexagone[0]+j*3*longueur, centre_hexagone[1] +
                      i*2*longueur*sin(pi/3), 0), longueur, col, centre, rayon)
    return()


"""
Fonction principale du projet demandant successivement à l'utilisateur tous les paramètres nécéssaires au tracé de la figure sous turtle, à savoir :
    Entrées :
        inf_gauche : coin inférieur gauche de la fenetre turtle (entier)
        sup_droit : coin supérieur droit (entier)
        longeur : longueur entre le centre et n’importe quel coin de l’hexagone (entier positif)
        col1 : couleur du pavé "nord-est" de l'hexagone (chaine de caractères)
        col2 : couleur du pavé "ouest" de l'hexagone (chaine de caractères)
        col3 : couleur du pavé "sud-est" de l'hexagone (chaine de caractères)
        c_x : abscisse du centre de la sphère de déformation (entier)
        c_y : ordonnée du centre de la sphère de déformation (entier)
        c_z : hauteur du centre de la sphère de déformation (entier)
        r : rayon de la sphère en déformation (entier)
    
    Sortie : Une fenêtre turtle dessine la figure et un fichier projet_vasarely.eps est enregistré dans le répertoire courant de Pycharm


"""


def projet_vasarely():
    print("Définissez d'abord le cadre inférieur gauche de votre figure (valeur entière) :")
    inf_gauche = int(input())

    print("Définissez ensuite le coin supérieur droit (valeur entière) :")
    sup_droit = int(input())

    print("La longueur d'un segment de pavé avant déformation est (valeur entière strictement positive) :")
    longueur = int(input())
    if longueur <= 0:
        print("Entrez plutôt une valeur strictement positive svp :")
        longueur = int(input())

    print("Entrez successivement les 3 couleurs de vos hexagones parmis par exemple : ")
    print("yellow, gold, orange, red, maroon, violet, magenta, purple, navy, blue, skyblue, cyan, turquoise, lightgreen, green, darkgreen, chocolate, brown, black, gray, white")

    col1 = str(input())
    col2 = str(input())
    col3 = str(input())
    col = (col1, col2, col3)

    print("Entrez successivement les coordonnées cartésiennes du centre de la déformation (valeurs entières) :")
    c_x = int(input())
    c_y = int(input())
    c_z = int(input())
    centre = (c_x, c_y, c_z)

    print("Entrez enfin le rayon de la sphère de déformation (valeur entière):")
    r = int(input())

    pavage(inf_gauche, sup_droit, longueur, col, centre, r)
    turtle.getcanvas().postscript(file="projet_vasarely.eps")
    turtle.done()

    return()


"""
Exécution du programme
Exemple d'entrée :
((-300,300,20),('blue','black','red'),(-50,-50,-50),200)
"""
projet_vasarely()
