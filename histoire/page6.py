def page6(gameState: dict) -> int:
    res: int = -2

    # on importe ce qui est necessaire

    from OUTILS import afficher_ecran, imprimer, imprimer_ascii
    from ASCII import choque, mail



    # on affiche le dialogue

    imprimer_ascii.f(gameState["zone_principale"], 1, 0, mail.dessin)

    imprimer.f(gameState["zone_dialogue"], 4, f"Le mail est bien envoyé au directeur de {gameState['ecole']}")
    afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

    input("Appuie sur Entrée pour continuer")

    imprimer_ascii.f(gameState["zone_principale"], 1, 0, choque.dessin)

    imprimer.f(gameState["zone_dialogue"], 4, "Il ouvre le mail")
    afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

    input("Appuie sur Entrée pour continuer")

    imprimer.f(gameState["zone_dialogue"], 4, "Il prend peur, et valide ton dossier")
    afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

    input("Appuie sur Entrée pour continuer")

    imprimer.f(gameState["zone_dialogue"], 4, f"BRAVO {gameState["nom"]}, tu peux être fier de toi !")
    afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

    input("Appuie sur Entrée pour continuer")



    # on passe a la prochaine page

    res = 7

    return res