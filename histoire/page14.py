def page14(gameState: dict) -> int:
    res: int = -2

    # on importe ce qui est necessaire

    from OUTILS import afficher_ecran, imprimer, imprimer_ascii, vider, maj_stat
    from ASCII import maintenance



    # on affiche le dialogue

    vider.f(gameState["zone_dialogue"])

    imprimer_ascii.f(gameState["zone_principale"], 1, 0, maintenance.dessin)

    imprimer.f(gameState["zone_dialogue"], 4, "Tu choisis donc d'immigrer en avion")
    afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

    input("Appuie sur Entrée pour continuer")

    imprimer.f(gameState["zone_dialogue"], 4, f"Tu te rends sur le site de la compagnie AIR-{gameState["pays"].upper()}")
    afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

    input("Appuie sur Entrée pour continuer")



    # on propose les choix

    choix: bool = False

    while not choix:
        imprimer.f(gameState["zone_dialogue"], 2, f"Tu as 3 choix :")
        imprimer.f(gameState["zone_dialogue"], 4, "1. Classe économique (100 €)")
        imprimer.f(gameState["zone_dialogue"], 5, "2. Classe affaires (200 €)")
        imprimer.f(gameState["zone_dialogue"], 6, "3. Première classe (300 €)")
        afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

            
        reponse: str = input("Réponse (tape un chiffre) : ")

        if reponse == "1":
            choix = True
            gameState["argent"] -= 100
            gameState["billet"] = "eco"

        elif reponse == "2":
            choix = True
            gameState["argent"] -= 200
            gameState["bilet"] = "affaire"

        elif reponse == "3":
            choix = True
            gameState["argent"] -= 300
            gameState["capitale"] = "premiere"
        
        else:
            input("Réponse non conforme, appuie sur Entrée pour recommencer ...")

    maj_stat.f(gameState["zone_stat"], gameState)
    afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])
    input("Appuie sur Entrée pour continuer")

    # on passe a la prochaine page

    res = 16

    return res