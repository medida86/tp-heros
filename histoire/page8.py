def page8(gameState: dict) -> int:
    res: int = -2

    # on importe ce qui est necessaire

    from OUTILS import afficher_ecran, imprimer, imprimer_ascii, vider, maj_stat
    from ASCII import secretaire, content



    # on affiche le dialogue

    vider.f(gameState["zone_dialogue"])

    imprimer_ascii.f(gameState["zone_principale"], 1, 0, content.dessin)

    imprimer.f(gameState["zone_dialogue"], 4, f"{gameState["nom"]}, tu décides d'immigrer de façon légale")
    afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

    input("Appuie sur Entrée pour continuer")

    imprimer.f(gameState["zone_dialogue"], 4, "C'est sûrement le choix le plus sage")
    afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

    input("Appuie sur Entrée pour continuer")

    imprimer.f(gameState["zone_dialogue"], 4, "Pour te récompenser, je met tes économies à 600 €")
    gameState["argent"] = 600
    maj_stat.f(gameState["zone_stat"], gameState)
    afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

    input("Appuie sur Entrée pour continuer")

    imprimer_ascii.f(gameState["zone_principale"], 1, 0, secretaire.dessin)

    imprimer.f(gameState["zone_dialogue"], 4, "Tu te rends donc à la mairie afin de préparer ton dossier administratif")
    afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

    input("Appuie sur Entrée pour continuer")



    # on propose les choix (café)

    choix: bool = False

    while not choix:
        imprimer.f(gameState["zone_dialogue"], 2, f"Te voici a la mairie, la secretaire te propose un café")
        imprimer.f(gameState["zone_dialogue"], 4, "1. Boire")
        imprimer.f(gameState["zone_dialogue"], 5, "2. Refuser")
        afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

            
        reponse: str = input("Réponse (tape un chiffre) : ")

        if reponse == "1":
            choix = True
            vider.f(gameState["zone_dialogue"])
            imprimer.f(gameState["zone_dialogue"], 4, "Très bien, tu accèptes : Barre d'énergie à 100 %")
            gameState["energie"] = 99
            maj_stat.f(gameState["zone_stat"], gameState)
            afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])
            input("Appuie sur Entrée pour continuer")

        elif reponse == "2":
            choix = True
            vider.f(gameState["zone_dialogue"])
            imprimer.f(gameState["zone_dialogue"], 4, "Très bien, tu refuses")
            afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])
            input("Appuie sur Entrée pour continuer")
        
        else:
            input("Réponse non conforme, appuie sur Entrée pour recommencer ...")



    # on propose les choix (visa/passeport)

    vider.f(gameState["zone_dialogue"])
    imprimer.f(gameState["zone_dialogue"], 4, f"La secretaire te demande 2 documents pour ton dossier")
    afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

    input("Appuie sur Entrée pour continuer")

    imprimer.f(gameState["zone_dialogue"], 4, f"Pour aller en France, tu as besoin de ton passeport, et un visa")
    afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

    input("Appuie sur Entrée pour continuer")



    choix: bool = False

    while not choix:
        imprimer.f(gameState["zone_dialogue"], 2, f"Par quel document veux-tu commencer ?")
        imprimer.f(gameState["zone_dialogue"], 4, "1. Commencer par le passeport")
        imprimer.f(gameState["zone_dialogue"], 5, "2. Commencer par le visa")
        afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

            
        reponse: str = input("Réponse (tape un chiffre) : ")

        if reponse == "1":
            choix = True
            vider.f(gameState["zone_dialogue"])
            imprimer.f(gameState["zone_dialogue"], 4, "Très bien, tu commence par le passeport")
            res = 10

        elif reponse == "2":
            choix = True
            vider.f(gameState["zone_dialogue"])
            imprimer.f(gameState["zone_dialogue"], 4, "Très bien, tu commence par le visa")
            res = 11
        
        else:
            input("Réponse non conforme, appuie sur Entrée pour recommencer ...")

        afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])


    # on passe a la prochaine page

    input("Appuie sur Entrée pour continuer")

    return res