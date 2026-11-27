def menu() -> dict:

    # on importe ce qui est necessaire

    from OUTILS import afficher_ecran, imprimer, imprimer_ascii, maj_inv, maj_stat, vider
    from ASCII import logo, perso_f, perso_m

    # on defini le gameState

    gameState: dict ={
    "nom" : "?",
    "age" : 18,
    "pays" : "?",
    "argent" : 500,
    "energie" : 90,
    "vie" : 99,
    "reputation" : 60,
    "ecole" : "?",
    "zone_principale" : ["┌" + (98*"─") + "┐", *["│" + (98*" ")  + "│"]* 30, "└" + (98*"─") + "┘"],
    "zone_dialogue" : ["┌" + (98*"─") + "┐", *["│" + (98*" ")  + "│"]* 7, "└" + (98*"─") + "┘"],
    "zone_inventaire" : ["┌" + (28*"─") + "┐", *["│" + (28*" ")  + "│"]* 30, "└" + (28*"─") + "┘"],
    "zone_stat" : ["┌" + (28*"─") + "┐", *["│" + (28*" ")  + "│"]* 7, "└" + (28*"─") + "┘"],
    "inventaire" : ["gâteaux prince", "Téléphone", "Carte d'identité", "Couteau"]
    }



    # on demande au joueur de passer en plein ecran

    print("\033[H\033[J", end="")
    print("┌────────────────────────────────────────────────────────┐")
    print("│                                                        │")
    print("│         Pour une expérience optimale, passez           │")
    print("│             votre terminal en PLEIN ÉCRAN              │")
    print("│                                                        │")
    print("└────────────────────────────────────────────────────────┘")
    input("\nAppuyez sur Entrée une fois le terminal en plein écran ...")



    # on lance le jeu

    imprimer_ascii.f(gameState["zone_principale"], 8, 0, logo.dessin)
    afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])
    input("COMMENCER -> appuyer sur Entrée")



    # on rempli la zone de stat

    maj_stat.f(gameState["zone_stat"], gameState)
    afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])



    # on demande au joueur les info manquantes

    # le nom

    imprimer.f(gameState["zone_dialogue"], 4, "Quel est votre nom ?")
    afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])
    
    reponse = input("Réponse : ")
    gameState["nom"] = reponse

    # le pays d'origine

    while gameState["pays"] == "?":
        imprimer.f(gameState["zone_dialogue"], 4, "Pays :   1.Togo   2.Maroc   3.Congo   4.Liban   5.Vietnam   6.Mali")
        afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])
        
        reponse = input("REPONSE (entrez un chiffre) : ")
        
        if reponse == "1":
            gameState["pays"] = "Togo"
        elif reponse == "2":
            gameState["pays"] = "Maroc"
        elif reponse == "3":
            gameState["pays"] = "Congo"
        elif reponse == "4":
            gameState["pays"] = "Liban"
        elif reponse == "5":
            gameState["pays"] = "Vietnam"
        elif reponse == "6":
            gameState["pays"] = "Mali"
        else:
            input("Valeur non conforme, appuyez sur Entrée pour recommencer...")



    # on met a jour les info et on affiche a l'ecran

    maj_stat.f(gameState["zone_stat"], gameState)
    maj_inv.f(gameState["zone_inventaire"], gameState)
    imprimer.f(gameState["zone_dialogue"], 4, "Pays :   1.Togo   2.Maroc   3.Congo   4.Liban   5.Vietnam   6.Mali")
    afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])



    # le joueur choisi une photo

    vider.f(gameState["zone_principale"])

    reponse=""

    while reponse == "":
        imprimer.f(gameState["zone_dialogue"], 4, "Choisi une photo de profil, tape 1 (gauche) ou 2 (droite)")
        imprimer_ascii.f2(gameState["zone_principale"], 13, 10, perso_m.dessin, 15, perso_f.dessin)
        afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])
        
        reponse = input("Réponse : ")

        if reponse == "1":
            imprimer_ascii.f(gameState["zone_inventaire"], 19, 3, perso_m.dessin)
            afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])
        
        elif reponse == "2":
            imprimer_ascii.f(gameState["zone_inventaire"], 19, 3, perso_f.dessin)
            afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])
        
        else:
            reponse = ""
            imprimer.f(gameState["zone_dialogue"], 4, "Réponse incorrect, appuyer sur Entrée pour recommencer")
            afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])
            input("")

    vider.f(gameState["zone_principale"])



    # on passe a la page 1

    vider.f(gameState["zone_dialogue"])

    imprimer.f(gameState["zone_principale"], 13, "Avant de commencer, tu as :")
    imprimer.f(gameState["zone_principale"], 15, "en haut à gauche la zone principale                       en haut à droite ton inventaire")
    imprimer.f(gameState["zone_principale"], 17, "en bas à gauche la zone de dialogue                 en bas à droite tes stats (argent...)")
    afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

    input("Appuie sur Entrée")

    imprimer.f(gameState["zone_dialogue"], 4, "Appuie sur Entrée pour lancer l'aventure")
    afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])
    input("")


    return gameState