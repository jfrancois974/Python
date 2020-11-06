
"""
        Auteur: Jean-François BATAILLE

        Date : AVRIL 2020
        Projet : Apprentissage Python 3

Objectif:

    Écrire une fonction transcription_arn(brin) qui reçoit une chaîne de caractères en paramètre, correspondant à un brin d'ADN,
    et qui retourne une chaîne de caractère correspondant à la transcription ARN de ce brin.

    Nous rappelons qu'un brin d'ADN peut être modélisé par une chaîne de caractères, dont les caractères sont pris parmi les quatre suivants:
    'A'(Adénine), 'C' (Cytosine),'G' (Guanine) et 'T' (Thymine).
    La transcription en ARN se traduit par le remplacement des nucléotides de Thymine par des nucléotides d'Uracile,
    que l'on représenterapar le caractère 'U'.

Exemples:
    transcription_arn('AGTCTTACCGATCCAT') doit retourner: 'AGUCUUACCGAUCCAU'


"""

gene_1 = 'ACGT'


def transcription_arn(brin):
    arn = ''
    for caractere in brin:
        if caractere == 'T':
            caractere = 'U'
        arn = arn+caractere
    return arn


transcription_arn('AGTCTTACCGATCCAT')
