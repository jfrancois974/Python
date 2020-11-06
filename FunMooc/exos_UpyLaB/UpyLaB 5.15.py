"""
        Auteur: Jean-François BATAILLE

        Date : AVRIL 2020
        Projet : Apprentissage Python 3

Objectif:
    Joao vient d’arriver dans notre pays depuis le Portugal. Il a encore du mal avec la langue française.
    Malgré ses efforts considérables, il fait une faute d’orthographe quasi à chaque mot.
    Son souci est qu’il n’arrive pas toujours à écrire un mot correctement sans se tromper à une lettre près.
    Ainsi pour écrire « bonjour », il peut écrire « binjour ».
    Pour remédier à ce problème, Joao utilise un correcteur orthographique.
    Malheureusement, Joao a un examen aujourd’hui et il a oublié son petit correcteur.

    Afin de l’aider, nous vous demandons d’écrire une fonction correcteur(mot, liste_mots)
    où mot est le mot que Joao écrit et liste_mots est une liste qui contient les mots (ayant la bonne orthographe)
    que Joao est susceptible d’utiliser.

    Cette fonction doit retourner le mot dont l’orthographe a été corrigée.

Exemples:
    correcteur("bonvour", ["chien", "chat", "train", "voiture", "bonjour", "merci"])
    doit retourner: "bonjour"

    correcteur("chat", ["chien", "chat", "train", "voiture", "bonjour", "merci"])
    doit retourner: "chat"

 """

def distance_mots(mot_1, mot_2):
	dist_i = [ k for k in range(len(mot_1)+1) ]
	for i in range(1, len(mot_2) + 1):
		dist_prec = dist_i
		dist_i = [i]*(len(mot_1)+1)
		for k in range(1,len(dist_i)):
			cont = int(mot_1[k-1] != mot_2[i-1])
			dist_i[k] = min(dist_i[k-1] + 1, dist_prec[k] + 1, dist_prec[k-1] + cont)
	return dist_i[len(mot_1)]

def correcteur(mot, liste_mots):
    res = ''
    for e in liste_mots:
        if len(mot) == len(e) and (
                res == '' or distance_mots(mot, e)
				< distance_mots(mot, res)):
            res = e
    return res


