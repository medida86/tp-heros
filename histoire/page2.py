def page2(gameState: dict) -> int:
    res: int = -2

    # on importe ce qui est necessaire

    from OUTILS import afficher_ecran, imprimer, imprimer_ascii, vider, maj_stat
    from ASCII import bureau
    import random



    # on affiche le dialogue

    imprimer_ascii.f(gameState["zone_principale"], 1, 0, bureau.dessin)

    imprimer.f(gameState["zone_dialogue"], 4, "Te voici dans ton bureau")
    afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

    input("Appuie sur Entrée pour continuer")

    imprimer.f(gameState["zone_dialogue"], 4, f"Tu dois désormais envoyer ta candidature à : {gameState["ecole"]}")
    afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

    input("Appuie sur Entrée pour continuer")



    # on propose les différents dossiers

    acceptation: bool = False

    while not acceptation:

        vider.f(gameState["zone_dialogue"])
        imprimer.f(gameState["zone_dialogue"], 2, "Choisis ton dossier (tape un numéro)")
        imprimer.f(gameState["zone_dialogue"], 4, "1.Dossier baclé (0 € / peu de chance d'être accepté)")
        imprimer.f(gameState["zone_dialogue"], 5, "2.Dossier solide (60 € / bonne chance d'être accepté)")
        imprimer.f(gameState["zone_dialogue"], 6, "3.Pistonné (100 € / sûre d'être accepté)")
        afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])
        
        reponse: str = input("REPONSE (entrez un chiffre) : ")
        chance: int = random.randint(1, 100)

        if reponse == "1":
            if chance == 1:
                acceptation = True
                res = 3
            else:
                input("Dossier refusé, tape Entrée pour réessayer...")


        elif reponse == "2":
            if gameState["argent"] >= 60:
                gameState["argent"] -= 60
                if chance <= 50:
                    acceptation = True
                    res = 3
                else:
                    input("Dossier refusé, tape Entrée pour réessayer...")
            else:
                input("Tu n'avais pas assez d'argent, appuies sur Entrée pour recommenser...")

        elif reponse == "3":
            if gameState["argent"] >= 100:
                gameState["argent"] -= 100
                acceptation = True
                res = 3
            else:
                input("Tu n'avais pas assez d'argent, appuies sur Entrée pour recommenser...")

        else:
            input("Valeur non conforme, appuyez sur Entrée pour recommencer...")

        maj_stat.f(gameState["zone_stat"], gameState)



    # on passe a la prochaine page

    vider.f(gameState["zone_dialogue"])
    imprimer.f(gameState["zone_dialogue"], 4, f"Très bien, tu es donc accepté à l'école : {gameState["ecole"]}")
    afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])
    input("Appuie sur Entrée pour continuer")

    return res