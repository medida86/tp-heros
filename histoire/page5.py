def page5(gameState: dict) -> int:
    res: int = -2

    # on importe ce qui est necessaire

    from OUTILS import afficher_ecran, imprimer, imprimer_ascii, maj_stat, vider
    from ASCII import hacker



    # on affiche le dessin

    imprimer_ascii.f(gameState["zone_principale"], 1, 0, hacker.dessin)



    # on affiche le texte

    vider.f(gameState["zone_dialogue"])
    imprimer.f(gameState["zone_dialogue"], 4, "Tu te rends sur le dark web")
    afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])
    input("Appuie sur Entrée pour continuer")


    # on propose les choix

    choix: bool = False

    while not choix:
        imprimer.f(gameState["zone_dialogue"], 2, "Tu as 2 choix :")
        imprimer.f(gameState["zone_dialogue"], 4, "1. Tu recherches son adresse")
        imprimer.f(gameState["zone_dialogue"], 5, "2. Tu recherches une photo de sa femme et ses enfants")
        afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])
        
        reponse: str = input("Réponse (tape un chiffre) : ")

        if reponse == "1":
            choix = True
        elif reponse == "2":
            choix = True
        else:
            input("Réponse non conforme, appuie sur Entrée pour recommencer ...")

        afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

        

    # on passe a la prochaine page

    vider.f(gameState["zone_dialogue"])
    imprimer.f(gameState["zone_dialogue"], 4, "Tu as bien récupéré les infos que tu cherchais")
    afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

    input("Appuie sur Entrée pour continuer")
    
    res = 6

    return res 