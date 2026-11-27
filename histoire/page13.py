def page13(gameState: dict) -> int:
    res: int = -2

    # on importe ce qui est necessaire

    from OUTILS import afficher_ecran, imprimer, imprimer_ascii, vider
    from ASCII import bureau



    # on affiche le dialogue

    vider.f(gameState["zone_dialogue"])

    imprimer_ascii.f(gameState["zone_principale"], 1, 0, bureau.dessin)

    imprimer.f(gameState["zone_dialogue"], 4, "Te voila de retour dans ton bureau")
    afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

    input("Appuie sur Entrée pour continuer")

    imprimer.f(gameState["zone_dialogue"], 4, f"Pour quitter le {gameState["pays"]}, tu dois desormais prendre un moyen de transport")
    afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

    input("Appuie sur Entrée pour continuer")

    imprimer.f(gameState["zone_dialogue"], 4, f"Tu te rends donc sur internet")
    afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

    input("Appuie sur Entrée pour continuer")



    # on propose les choix

    choix: bool = False

    while not choix:
        imprimer.f(gameState["zone_dialogue"], 2, f"Tu as 2 choix :")
        imprimer.f(gameState["zone_dialogue"], 4, "1. Avion")
        imprimer.f(gameState["zone_dialogue"], 5, "2. Bateau")
        afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

            
        reponse: str = input("Réponse (tape un chiffre) : ")

        if reponse == "1":
            choix = True
            res = 14

        elif reponse == "2":
            choix = True
            res = 15
        
        else:
            input("Réponse non conforme, appuie sur Entrée pour recommencer ...")


    # on passe a la prochaine page

    return res