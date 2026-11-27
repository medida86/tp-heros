# cette fonction permet de mettre un dessin ascii dans l'une de nos 4 zone (liste) du jeu en choisissant la ligne 
# et le decalage vers la droite

def f(zone: list, ligne: int, decalage: int, dessin: list) -> list:
    res: list = zone
    largeur_zone = len(zone[0]) - 2

    for i, ligne_dessin in enumerate(dessin):
        largeur = ligne_dessin.count("█") + ligne_dessin.count(" ") + ligne_dessin.count("=") + ligne_dessin.count("|") + ligne_dessin.count("\\")  + ligne_dessin.count("/")  + ligne_dessin.count("O")  + ligne_dessin.count("─") + ligne_dessin.count("+")
        reste = largeur_zone - largeur - decalage
        res[ligne + i] = "│" + decalage * " " + ligne_dessin + reste * " " + "│"

    return res


# cette fonction permet de mettre deux dessin ascii dans l'une de nos 4 zone (liste) du jeu en choisissant la ligne 
# et le decalage vers la droite, et l'espace entre les joueurs

def f2(zone: list, ligne: int, decalage: int, dessin: list, decalage2: int, dessin2: list) -> list:
    res: list = zone

    for i in range(len(dessin)):
        largeur: int = 0
        largeur2: int = 0

        for j in dessin[i]:
            if j == "█" or j == " ":
                largeur += 1
        for l in dessin2[i]:
            if l == "█" or l == " ":
                largeur2 += 1
        
        res[ligne+i] = "│" + decalage*" " + dessin[i] + (((len(res[i])-2)//2)-largeur-decalage)*" " + decalage2*" " + dessin2[i] + (((len(res[i])-2)//2)-largeur2-decalage2)*" " + "│"

    return res