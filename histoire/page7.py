def page7(gameState: dict) -> int:
    res: int = -2

    # on importe ce qui est necessaire

    from OUTILS import afficher_ecran, imprimer, imprimer_ascii
    from ASCII import content



    # on affiche le dialogue

    imprimer_ascii.f(gameState["zone_principale"], 1, 0, content.dessin)

    imprimer.f(gameState["zone_dialogue"], 4, f"{gameState["nom"]}, tu as desormais une école, cependant ...")
    afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

    input("Appuie sur Entrée pour continuer")

    imprimer.f(gameState["zone_dialogue"], 4, "Il faut encore venir en France !")
    afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

    input("Appuie sur Entrée pour continuer")



    # on propose les choix

    choix: bool = False

    while not choix:
        imprimer.f(gameState["zone_dialogue"], 2, f"Tu as 2 choix pour quitter le {gameState["pays"]} (toute la suite en dépend) :")
        imprimer.f(gameState["zone_dialogue"], 4, "1. Immigrer en France de façon légale")
        imprimer.f(gameState["zone_dialogue"], 5, "2. Immigrer en France de façon illégale")
        afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

            
        reponse: str = input("Réponse (tape un chiffre) : ")

        if reponse == "1":
            choix = True
            res = 8

        elif reponse == "2":
            choix = True
            res = 9
        
        else:
            input("Réponse non conforme, appuie sur Entrée pour recommencer ...")



    # on passe a la prochaine page

    return res