def page18(gameState: dict) -> int:
    res: int = -2

    # on importe ce qui est necessaire

    from OUTILS import afficher_ecran, imprimer, imprimer_ascii, vider, maj_inv, maj_stat
    from ASCII import maintenance



    # on affiche le dialogue

    imprimer_ascii.f(gameState["zone_principale"], 1, 0, maintenance.dessin)

    vider.f(gameState["zone_dialogue"])

    imprimer.f(gameState["zone_dialogue"], 4, "Tu lui donnes donc les gâteaux")
    
    gameState["inventaire"].remove("gâteaux prince")
    gameState["reputation"] = 99

    maj_inv.f(gameState["zone_inventaire"], gameState)
    maj_stat.f(gameState["zone_stat"], gameState)
    afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])
    
    input("Appuie sur Entrée pour continuer")



    # on passe a la prochaine page

    res = 19

    return res