def page4(gameState: dict) -> int:
    res: int = -2

    # on importe ce qui est necessaire

    from OUTILS import afficher_ecran, imprimer, imprimer_ascii, maj_stat, vider
    from ASCII import chatgpt



    # on affiche le dessin

    imprimer_ascii.f(gameState["zone_principale"], 1, 0, chatgpt.dessin)



    # on affiche le texte

    vider.f(gameState["zone_dialogue"])
    imprimer.f(gameState["zone_dialogue"], 4, "Tu te rends sur ton IA favorite")
    afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])
    input("Appuie sur Entrée pour continuer")


    # on propose les choix

    choix: bool = False

    while not choix:
        imprimer.f(gameState["zone_dialogue"], 2, "Tu as 2 choix :")
        imprimer.f(gameState["zone_dialogue"], 4, "1. Modèle d'IA payante (20 €)")
        imprimer.f(gameState["zone_dialogue"], 5, "2. Modèle d'IA gratuite (20 d'énergie)")
        afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])
        
        reponse: str = input("Réponse (tape un chiffre) : ")

        if reponse == "1":
            if gameState["argent"] >= 20:
                gameState["argent"] -= 20
                choix = True
                maj_stat.f(gameState["zone_stat"], gameState)
            else:
                input("Tu n'avais pas assez d'argent, appuies sur Entrée pour recommenser...")

        elif reponse == "2":
            if gameState["energie"] >= 20:
                gameState["energie"] -= 20
                choix = True
                maj_stat.f(gameState["zone_stat"], gameState)
            else:
                input("Tu n'avais pas assez d'énergie, appuies sur Entrée pour recommenser...")
        
        else:
            input("Réponse non conforme, appuie sur Entrée pour recommencer ...")

        afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

        

    # on passe a la prochaine page

    vider.f(gameState["zone_dialogue"])
    imprimer.f(gameState["zone_dialogue"], 4, "La vidéo IA est bien créée")
    afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

    input("Appuie sur Entrée pour continuer")
    
    res = 6

    return res 