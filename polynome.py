from math import sqrt


def polynome_second_degrès ():
    a = float (input ("entrez un nombre"))
    b = float (input ("entrez un nombre"))
    c = float (input ("entrez un nombre"))
    delta = (b ** 2) - (4 * a * c)
    if a == 0 :
        return "Il n y a pas de solution à cette équation"
    else :
        if delta < 0 :
            return "Il n y a pas de solution à cette équation"
        elif delta == 0 :
            solution = - b / (2 * a)
            texte = "La solution de l'équation du polynome du second degrès est " + str (solution)
            return texte
        else :
            solution1 = (-b - sqrt (delta) ) / (2 * a)
            solution2 = (-b + sqrt (delta) ) / (2 * a)
            texte1 = "La solution 1 de l'équation du polynome est : " + str (solution1)
            texte2 = "La solution 2 de l'équation de polynome est : " + str (solution2)
            return texte1, texte2
