# fonction qui met a jour les infos dans la zone inventaire a partir de l'inventaire (dans gameState)

def f(zone_inventaire: list, gameState: dict) -> list:
    res: list = zone_inventaire

    res[2] = f"│{9*" "}INVENTAIRE{9*" "}│"

    # On efface les anciennes lignes

    for i in range(5, len(res)-1):
        res[i] = "│" + 28*" " + "│"

    # On réaffiche les objets présents

    for i in range(min(len(gameState["inventaire"]), len(res)-6)):
        objet = gameState["inventaire"][i]

        if len(objet) % 2 == 0:
            res[i+5] = "│" + (14-(len(objet)//2))*" " + objet + (14-(len(objet)//2))*" " + "│"
        else:
            res[i+5] = "│" + (14-int(len(objet)/2))*" " + objet + (13-int(len(objet)/2))*" " + "│"

    return res
