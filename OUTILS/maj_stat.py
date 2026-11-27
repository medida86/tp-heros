# fonction qui met a jour les infos de la zone statistiques a partir du gameState


def f(zone_stat: list, gameState: dict) -> list:
    res: list = zone_stat

    rouge: str = "\033[31m"
    vert: str = "\033[32m"
    fin: str = "\033[0m"

    # on affiche le nom

    if len(str(gameState["nom"]))%2 == 1 : 
        res[1] = "│" + (11-int(len(str(gameState["nom"]))/2))*" " + "Nom : " + str(gameState["nom"]) + (10-int(len(str(gameState["nom"]))/2))*" " + "│"
    else :
        res[1] = "│" + (11-len(str(gameState["nom"]))//2)*" " + "Nom : " + str(gameState["nom"]) + (11-len(str(gameState["nom"]))//2)*" " + "│"

    # on affiche l'age

    res[2] = "│" + 8*" " + f"Age : {gameState["age"]} ans" + 8*" "  + "│"

    # on affiche le pays

    if len(str(gameState["pays"]))%2 == 1 : 
        res[3] = "│" + (10-int(len(str(gameState["pays"]))/2))*" " + "Pays : " + str(gameState["pays"]) + (10-int(len(str(gameState["pays"]))/2))*" " + "│"
    else :
        res[3] = "│" + (10-len(str(gameState["pays"]))//2)*" " + "Pays : " + str(gameState["pays"]) + (11-len(str(gameState["pays"]))//2)*" " + "│"

    # on affiche l'argent

    if len(str(gameState["argent"]))%2 == 1 : 
        res[4] = "│" + (7-int(len(str(gameState["argent"]))/2))*" " + "Economies : " + str(gameState["argent"]) + " €" + (6-int(len(str(gameState["argent"]))/2))*" " + "│"
    else :
        res[4] = "│" + (7-len(str(gameState["argent"]))//2)*" " + "Economies : " + str(gameState["argent"]) + " €" + (7-len(str(gameState["argent"]))//2)*" " + "│"

    # on affiche les barres d'energie, de social et de vie

    res[5] = "│" + f"Energie : {(vert + round(gameState["energie"]/10)*"█") + (rouge + (10-round(gameState["energie"]/10))*"░") + fin}" + f" {gameState['energie']}/100" + " │"


    res[6] = "│" + f"Social  : {(vert + round(gameState["reputation"]/10)*"█") + (rouge + (10-round(gameState["reputation"]/10))*"░") + fin}" + f" {gameState['reputation']}/100" + " │"


    res[7] = "│" + f"Vie     : {(vert + round(gameState["vie"]/10)*"█") + (rouge + (10-round(gameState["vie"]/10))*"░") + fin}" + f" {gameState['vie']}/100" + " │"

    return res