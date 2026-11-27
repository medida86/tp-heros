def page3(gameState: dict) -> int:
    res: int = -2

    # on importe ce qui est necessaire

    from OUTILS import afficher_ecran, imprimer, imprimer_ascii, vider
    from ASCII import mail



    # on affiche le dialogue

    imprimer_ascii.f(gameState["zone_principale"], 1, 0, mail.dessin)

    imprimer.f(gameState["zone_dialogue"], 4, "Oh ...")
    afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

    input("Appuie sur Entrée pour continuer")



    # on propose au joueur d'ouvrir le mail

    mail_lu: bool = False

    while not mail_lu:
        imprimer.f(gameState["zone_dialogue"], 4, "Tu reçois un mail, veux-tu l'ouvrir ? (Tape oui ou non)")
        afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])
        
        reponse: str = input("Réponse : ")

        if reponse.lower() == "oui":
            mail_lu = True

        elif reponse.lower() == "non":
            imprimer.f(gameState["zone_dialogue"], 4, "Bah éteint ton ordi si tu veux pas jouer ... recommence et dit oui !")
            afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])
            input("Appuie sur Entrée pour continuer")
        
        else:
            print("Réponse non conforme, appuie sur Entrée pour recommencer ...")
            input("Appuie sur Entrée pour continuer")



    # le mail est ouvert

    imprimer.f(gameState["zone_dialogue"], 4, f"Très bien {gameState["nom"]}, tu lis le contenu du mail")
    afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

    input("Appuie sur Entrée pour continuer")

    imprimer.f(gameState["zone_dialogue"], 4, "Alors ...")
    afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

    input("Appuie sur Entrée pour continuer")

    imprimer.f(gameState["zone_dialogue"], 4, f"Le directeur de {gameState["ecole"]} t'écrit pour te dire ...")
    afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

    input("Appuie sur Entrée pour continuer")

    imprimer.f(gameState["zone_dialogue"], 4, f"'Je n'aime pas les gens du {gameState["pays"]}, je vais annuler ton dossier !'")
    afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

    input("Appuie sur Entrée pour continuer")



    # on propose les choix

    reponse: str = ""

    while reponse != "1" and reponse != "2":
        vider.f(gameState["zone_dialogue"])
        imprimer.f(gameState["zone_dialogue"], 2, "Tu as 2 choix :")
        imprimer.f(gameState["zone_dialogue"], 4, "1.Tu créés une vidéo IA compromettante pour le menacer")
        imprimer.f(gameState["zone_dialogue"], 5, "2.Tu lui envoies son adresse et une photo de ses enfants pour le menacer")
        afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

        reponse: str = input("Réponse (tape un chiffre) : ")

        if reponse == "1":
            res = 4
        elif reponse == "2":
            res = 5
        else:
            input("Valeur non conforme, appuie sur Entrée pour continuer ...")

    return res