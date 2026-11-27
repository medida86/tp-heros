def page17(gameState: dict) -> int:
    res: int = -2

    # on importe ce qui est necessaire

    from OUTILS import afficher_ecran, imprimer, imprimer_ascii, vider, maj_inv, maj_stat, combat
    from ASCII import maintenance



    # on affiche le dialogue

    vider.f(gameState["zone_dialogue"])

    imprimer_ascii.f(gameState["zone_principale"], 1, 0, maintenance.dessin)

    imprimer.f(gameState["zone_dialogue"], 4, "Tu baisse le regard, tu avance comme si de rien était")
    afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

    input("Appuie sur Entrée pour continuer")

    imprimer.f(gameState["zone_dialogue"], 4, "Il t'appel")
    afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

    input("Appuie sur Entrée pour continuer")

    imprimer_ascii.f(gameState["zone_principale"], 1, 0, maintenance.dessin)

    imprimer.f(gameState["zone_dialogue"], 4, "'EH OH, tu n'as pas quelque chose pour moi ?'")
    afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

    input("Appuie sur Entrée pour continuer")

    imprimer.f(gameState["zone_dialogue"], 4, "Tu lui répond que non, et lui demande de te laisser tranquille")
    afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

    input("Appuie sur Entrée pour continuer")

    imprimer_ascii.f(gameState["zone_principale"], 1, 0, maintenance.dessin)

    imprimer.f(gameState["zone_dialogue"], 4, "Il se lève et t'attrappe par la veste, en te poustillonnant à la figure")
    afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

    input("Appuie sur Entrée pour continuer")


    # on propose les choix

    choix: bool = False

    sdf: dict = {
            "nom": "SDF",
            "vie": 70,
            "degats": 15,
            "attaques": ["VISAGE", "JAMBES", "VENTRE"]
    }

    while not choix:
        imprimer.f(gameState["zone_dialogue"], 2, f"Tu as donc 2 choix")
        imprimer.f(gameState["zone_dialogue"], 4, "1. Lui donner ce qu'il demande")
        imprimer.f(gameState["zone_dialogue"], 5, "2. Se battre avec lui")
        imprimer.f(gameState["zone_dialogue"], 6, "3. Lui mettre un coup de couteau")
        afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

            
        reponse: str = input("Réponse (tape un chiffre) : ")

        if reponse == "1":
            choix = True

            res = 18

        elif reponse == "2":
            choix = True

            if combat.f(gameState, sdf):

                vider.f(gameState["zone_dialogue"])
                
                imprimer.f(gameState["zone_dialogue"], 4, "BRAVO, tu lui as mis une raclé")
                afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

                res = 19
            else:

                vider.f(gameState["zone_dialogue"])
                
                imprimer.f(gameState["zone_dialogue"], 4, "Bah alors, on est nul ...")
                afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

                res = -1

        elif reponse == "3":
            choix = True

            vider.f(gameState["zone_dialogue"])

            imprimer.f(gameState["zone_dialogue"], 4, "Tu sors ton couteau")
            afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

            input("Appuie sur Entrée pour continuer")

            imprimer.f(gameState["zone_dialogue"], 4, "Tu tentes de le poignarder")
            afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

            input("Appuie sur Entrée pour continuer")

            imprimer.f(gameState["zone_dialogue"], 4, "Il te projette au sol et te désarmes")
            afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

            input("Appuie sur Entrée pour continuer")

            imprimer.f(gameState["zone_dialogue"], 4, "(tu aurais peu être du remarquer ses oreilles en chou)")
            afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

            input("Appuie sur Entrée pour continuer")

            imprimer.f(gameState["zone_dialogue"], 4, "Tu est au sol, il te dépouille")
            afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

            input("Appuie sur Entrée pour continuer")

            imprimer.f(gameState["zone_dialogue"], 4, "il te prend ton argent, tes gâteaux, ta carte d'identité, et ton téléphone")
            gameState["inventaire"].remove("gâteaux prince")
            gameState["inventaire"].remove("Carte d'identité")
            gameState["inventaire"].remove("Téléphone")
            gameState["inventaire"].remove("Couteau")

            gameState["argent"] = 0
            gameState["vie"] = 15
            gameState["reputation"] = 10
            gameState["energie"] = 12

            maj_stat.f(gameState["zone_stat"], gameState)
            maj_inv.f(gameState["zone_inventaire"], gameState)
            afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

            input("Appuie sur Entrée pour continuer")

            imprimer.f(gameState["zone_dialogue"], 4, "Heureusement qu'il n'a pas trouvé ton passeport et visa")
            afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

            input("Appuie sur Entrée pour continuer")

            res = 19

        else:
            input("Réponse non conforme, appuie sur Entrée pour recommencer ...")



    # on passe a la prochaine page

    return res