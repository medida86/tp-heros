# jeu pierre feuille ciseau

def f(gameState: dict) -> bool:
    res: bool = False

    # on importe ce qui est necessaire

    import random
    from OUTILS import imprimer, afficher_ecran, vider



    # on créer les variables necessaires au jeu

    choix: list = ["PIERRE", "FEUILLE", "CISEAUX"]

    victoires_joueur: int = 0
    victoires_ordinateur: int = 0
    manche: int = 0


    # boucle principale du jeu

    while victoires_joueur < 5 and victoires_ordinateur < 5:

        manche += 1

        vider.f(gameState["zone_principale"])

        imprimer.f(gameState["zone_principale"], 3, "===== PIERRE - FEUILLE - CISEAUX =====")
        imprimer.f(gameState["zone_principale"], 7, f"MANCHE {manche}")
        imprimer.f(gameState["zone_principale"], 11, f"{gameState["nom"]} : {victoires_joueur} victoire")
        imprimer.f(gameState["zone_principale"], 12, f"Secretaire : {victoires_ordinateur} victoire")

        imprimer.f(gameState["zone_principale"], 16, "1 - PIERRE")
        imprimer.f(gameState["zone_principale"], 18, "2 - FEUILLE")
        imprimer.f(gameState["zone_principale"], 20, "3 - CISEAUX")

        afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])


        # choix du joueur

        saisie: str = input("Ton choix (1, 2 ou 3) : ")

        while saisie != "1" and saisie != "2" and saisie != "3":
            print("Choix invalide !")
            saisie = input("Entre 1, 2 ou 3 : ")
            afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

        joueur: str = choix[int(saisie) - 1]



        # choix de l'ordinateur

        ordinateur: str = random.choice(choix)



        # affichage des choix

        vider.f(gameState["zone_principale"])

        imprimer.f(gameState["zone_principale"], 4, "===== RESULTAT DE LA MANCHE =====")

        imprimer.f(gameState["zone_principale"], 10, f"Toi : {joueur}")
        imprimer.f(gameState["zone_principale"], 13, f"Ordinateur : {ordinateur}")



        # comparaison des choix

        if joueur == ordinateur:

            imprimer.f(gameState["zone_principale"], 18, "EGALITE !")
            imprimer.f(gameState["zone_principale"], 20, "Cette manche ne compte pas.")

        elif (
            (joueur == "PIERRE" and ordinateur == "CISEAUX")
            or (joueur == "FEUILLE" and ordinateur == "PIERRE")
            or (joueur == "CISEAUX" and ordinateur == "FEUILLE")
        ):

            imprimer.f(gameState["zone_principale"], 18, "TU GAGNES CETTE MANCHE !")
            victoires_joueur += 1

        else:

            imprimer.f(gameState["zone_principale"], 18, "TU PERDS CETTE MANCHE !")
            victoires_ordinateur += 1



        # affichage du score

        imprimer.f(gameState["zone_principale"], 23, f"Score : {victoires_joueur} - {victoires_ordinateur}")

        afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

        input("Appuie sur ENTREE pour continuer...")



    # resultats du jeu

    vider.f(gameState["zone_principale"])

    if victoires_joueur == 5:

        imprimer.f(gameState["zone_principale"], 12, "BRAVO ! TU AS GAGNE !")
        res = True

    else:

        imprimer.f(gameState["zone_principale"], 12, "DOMMAGE ! TU AS PERDU !")
        res = False


    imprimer.f(
        gameState["zone_principale"], 16, f"Score final : {victoires_joueur} - {victoires_ordinateur}")

    afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])

    input("Appuie sur ENTREE pour continuer...")



    # on renvoie le resultat du jeu

    return res