def page10(gameState: dict) -> int:
    res: int = -2

    # on importe ce qui est necessaire

    from OUTILS import afficher_ecran, imprimer, imprimer_ascii, vider, jeu_pendu, maj_inv, maj_stat
    from ASCII import passeport



    # on affiche le dialogue

    imprimer_ascii.f(gameState["zone_principale"], 1, 0, passeport.dessin)

    vider.f(gameState["zone_dialogue"])

    imprimer.f(gameState["zone_dialogue"], 4, f"{gameState["nom"]}, gagne au jeu du pendu pour obtenir ton passeport !")
    afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

    input("Appuie sur Entrée pour lancer le jeu du pendu (je ne réexplique pas les règles, elles sont assez connues ...)")




    # on lance le jeu du pendu

    passeport: bool = jeu_pendu.f(gameState)



    # resultats du jeu

    if passeport:
        if "Visa" in gameState["inventaire"]:
            imprimer.f(gameState["zone_principale"], 15, "Victoire, tu obtiens ton passeport dans ton inventaire")
            
            gameState["inventaire"].append("Passeport")
            maj_inv.f(gameState["zone_inventaire"], gameState)
            
            afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])
            res = 12
        else:
            imprimer.f(gameState["zone_principale"], 15, "Victoire, tu obtiens ton passeport dans ton inventaire")
            imprimer.f(gameState["zone_principale"], 17, "Tu dois désormais obtenir ton visa")

            gameState["inventaire"].append("Passeport")
            maj_inv.f(gameState["zone_inventaire"], gameState)

            afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])
            res = 11
    else:
        vider.f(gameState["zone_dialogue"])

        imprimer.f(gameState["zone_dialogue"], 4, "Tu as perdu, tu perds 15 vies !")

        gameState["vie"] -= 15
        maj_stat.f(gameState["zone_stat"], gameState)

        if gameState["vie"] > 0:
            vider.f(gameState["zone_principale"])
            imprimer.f(gameState["zone_principale"], 15, "Recommence, tu vas y arriver !")
            afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])
            res = 10
        else:
            vider.f(gameState["zone_principale"])
            imprimer.f(gameState["zone_principale"], 15, "Tu n'as plus de vies !")
            afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])
            res = -1



    # on passe a la prochaine page

    input("Appuie sur Entrée pour continuer")

    return res