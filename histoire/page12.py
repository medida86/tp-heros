def page12(gameState: dict) -> int:
    res: int = -2

    # on importe ce qui est necessaire

    from OUTILS import afficher_ecran, imprimer, imprimer_ascii, vider, maj_stat
    from ASCII import secretaire, police



    # on affiche le dialogue

    vider.f(gameState["zone_dialogue"])

    imprimer_ascii.f(gameState["zone_principale"], 1, 0, secretaire.dessin)

    imprimer.f(gameState["zone_dialogue"], 4, f"{gameState["nom"]}, la secretaire a bien en possession tes documents")
    afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

    input("Appuie sur Entrée pour continuer")

    imprimer.f(gameState["zone_dialogue"], 4, "Cependant ...")
    afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

    input("Appuie sur Entrée pour continuer")

    imprimer.f(gameState["zone_dialogue"], 4, "Tu as un problème ...")
    gameState["argent"] = 600
    maj_stat.f(gameState["zone_stat"], gameState)
    afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

    input("Appuie sur Entrée pour continuer")

    imprimer.f(gameState["zone_dialogue"], 4, "La secretaire te demande un pot de vin de 300 € pour te rendre ton passeport et visa !")
    gameState["argent"] = 600
    maj_stat.f(gameState["zone_stat"], gameState)
    afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

    input("Appuie sur Entrée pour continuer")



    # on propose les choix (café)

    choix: bool = False

    while not choix:
        imprimer.f(gameState["zone_dialogue"], 2, f"Tu as donc 3 choix")
        imprimer.f(gameState["zone_dialogue"], 4, "1. Lui donner 300 €")
        imprimer.f(gameState["zone_dialogue"], 5, "2. La menacer avec le couteau de ton inventaire")
        imprimer.f(gameState["zone_dialogue"], 6, "3. Lui mettre un coup de couteau")
        afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

            
        reponse: str = input("Réponse (tape un chiffre) : ")

        if reponse == "1":
            choix = True
            
            vider.f(gameState["zone_dialogue"])
            
            imprimer.f(gameState["zone_dialogue"], 4, "Tu cèdes et sort les 300 €")
            
            gameState["argent"] -= 300
            
            maj_stat.f(gameState["zone_stat"], gameState)
            afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])
            
            input("Appuie sur Entrée pour continuer")
            
            res = 13

        elif reponse == "2" or reponse == "3":
            choix = True
            
            vider.f(gameState["zone_dialogue"])
            
            imprimer_ascii.f(gameState["zone_principale"], 1, 0, police.dessin)
            imprimer.f(gameState["zone_dialogue"], 4, "Tu sors ton couteau ...")
            
            afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])
           
            input("Appuie sur Entrée pour continuer")
            
            imprimer.f(gameState["zone_dialogue"], 4, "La police arrive et t'embarque")
            
            afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])
            
            input("Appuie sur Entrée pour continuer")
            
            res = -1
        
        else:
            input("Réponse non conforme, appuie sur Entrée pour recommencer ...")



    # on passe a la prochaine page

    return res