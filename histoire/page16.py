def page16(gameState: dict) -> int:
    res: int = -2

    # on importe ce qui est necessaire

    from OUTILS import afficher_ecran, imprimer, imprimer_ascii, vider
    from ASCII import maintenance



    # le joueur se rend a l'aeroport

    if gameState["pays"] == "Togo":
        gameState["capitale"] = "Lomé"
    elif gameState["pays"] == "Maroc":
        gameState["capitale"] = "Rabat"
    elif gameState["pays"] == "Congo":
        gameState["capitale"] = "Kinshasa"
    elif gameState["pays"] == "Liban":
        gameState["capitale"] = "Beyrouth"
    elif gameState["pays"] == "Vietnam":
        gameState["capitale"] = "Hanoï"
    elif gameState["pays"] == "Mali":
        gameState["capitale"] = "Bamako"

            

    vider.f(gameState["zone_dialogue"])

    imprimer_ascii.f(gameState["zone_principale"], 1, 0, maintenance.dessin)

    imprimer.f(gameState["zone_dialogue"], 4, f"Tu te rends à l'aéroport de {gameState["capitale"]}")
    afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

    input("Appuie sur Entrée pour continuer")

    imprimer.f(gameState["zone_dialogue"], 4, "Tu arrives sur le parking de l'aeroport")
    afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

    input("Appuie sur Entrée pour continuer")

    imprimer_ascii.f(gameState["zone_principale"], 1, 0, maintenance.dessin)

    imprimer.f(gameState["zone_dialogue"], 4, "Tu croise un SDF sur le paking")
    afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

    input("Appuie sur Entrée pour continuer")


    # on propose les choix

    choix: bool = False

    while not choix:
        imprimer.f(gameState["zone_dialogue"], 2, f"Tu as 2 choix :")
        imprimer.f(gameState["zone_dialogue"], 4, "1. Tu l'ignore")
        imprimer.f(gameState["zone_dialogue"], 5, "2. Tu lui donnes les gâteaux de ton inventaire")
        afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

            
        reponse: str = input("Réponse (tape un chiffre) : ")

        if reponse == "1":
            choix = True
            res = 17

        elif reponse == "2":
            choix = True
            res = 19
            
        else:
            input("Réponse non conforme, appuie sur Entrée pour recommencer ...")



    # on passe a la prochaine page

    return res