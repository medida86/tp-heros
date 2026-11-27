def page1(gameState: dict) -> int:
    res: int = -2

    # on importe ce qui est necessaire

    from OUTILS import afficher_ecran, imprimer, imprimer_ascii, vider
    from ASCII import maison



    # on affiche le dialogue

    imprimer_ascii.f(gameState["zone_principale"], 1, 0, maison.dessin)
    imprimer.f(gameState["zone_dialogue"], 4, f"Bonjour {gameState["nom"]}, voici ta maison")
    afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

    input("Appuie sur Entrée pour continuer")

    imprimer.f(gameState["zone_dialogue"], 4, f"Ton père étant mort il y a 2 ans, et ta mère subvenant aux besoins de ton frère et toi...")
    afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

    input("Appuie sur Entrée pour continuer")

    imprimer.f(gameState["zone_dialogue"], 4, f"tu décides de devenir ingénieur, afin de venir en aide à ta famille")
    afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

    input("Appuie sur Entrée pour continuer")

    imprimer.f(gameState["zone_dialogue"], 4, "La France étant un pays multiculturel, tu prends la décision d'y immigrer afin d'y étudier")
    afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

    input("Appuie sur Entrée pour continuer")



    # on propose les différentes écoles

    while gameState["ecole"] == "?":
        vider.f(gameState["zone_dialogue"])
        imprimer.f(gameState["zone_dialogue"], 3, "Postule dans une école (tape un numéro)")
        imprimer.f(gameState["zone_dialogue"], 5, "1. INSA     2.IMT     3.POLYTECH     4.UTC     5.ESILV")
        afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])
            
        reponse: str = input("REPONSE (entrez un chiffre) : ")

        if reponse == "1":
            gameState["ecole"] = "INSA"
        elif reponse == "2":
            gameState["ecole"] = "IMT"
        elif reponse == "3":
            gameState["ecole"] = "POLYTECH"
        elif reponse == "4":
            gameState["ecole"] = "UTC"
        elif reponse == "5":
            gameState["ecole"] = "ESILV"
        else:
            input("Valeur non conforme, appuyez sur Entrée pour recommencer...")

    vider.f(gameState["zone_dialogue"])
    imprimer.f(gameState["zone_dialogue"], 4, f"Très bien, tu postules donc à l'école : {gameState["ecole"]}")
    afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

    input("Appuie sur Entrée pour continuer")



    # on passe a la page 2

    res = 2

    return res