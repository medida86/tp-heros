# jeu du pendu

def f(gameState: dict) -> bool:
    res: bool = False

    # on importe ce qui est necessaire 

    import random
    from OUTILS import imprimer, afficher_ecran, vider, imprimer_ascii



    # on créer les variables necessaires au jeu

    mots: list = [
        "BUISSON",
        "MOISSON",
        "PROGRAMMATION",
        "SURVEILLANCE",
        "INSUPORTABLE",
        "VARIABLE",
        "LABORATOIRE",
        "VICTOIRE",
        "MURAILLE",
        "ECOLE",
        "PAPIER"
    ]

    pendu: list = [
        [
        "+───+",
        "|   |",
        "    |",
        "    |",
        "    |",
        "    |",
        "======="
        ],
        [
        "+───+",
        "|   |",
        "O   |",
        "    |",
        "    |",
        "    |",
        "======="
        ],
        [
        "+───+",
        "|   |",
        "O   |",
        "|   |",
        "    |",
        "    |",
        "======="
        ],
        [
        " +───+",
        " |   |",
        " O   |",
        "─|   |",
        "     |",
        "     |",
        "======="
        ],
        [
        " +───+",
        " |   |",
        " O   |",
        "─|─  |",
        "     |",
        "     |",
        "======="
        ],
        [
        " +───+",
        " |   |",
        " O   |",
        "─|─  |",
        "/    |",
        "     |",
        "======="
        ],
        [
        " +───+",
        " |   |",
        " O   |",
        "─|─  |",
        "/ \\  |",
        "     |",
        "======="
        ]
    ]

    mot: str = random.choice(mots)
    avancement: list = []
    lettres_trouvees: list = []
    lettres_ratees: list = []
    erreurs: int = 0



    # boucle principale du jeu

    while erreurs < 6 and not res:

        avancement: list = []

        vider.f(gameState["zone_principale"])
        imprimer.f(gameState["zone_principale"], 5, "===== JEU DU PENDU =====")
        imprimer_ascii.f(gameState["zone_principale"], 8, 45, pendu[erreurs])

        for lettre in mot:
            if lettre in lettres_trouvees:
                avancement.append(lettre)
            else:
                avancement.append("_")

        imprimer.f(gameState["zone_principale"], 20, f"Mot : {"".join(avancement)}" )
        imprimer.f(gameState["zone_principale"], 22, f"Erreurs : {erreurs} / 6")
        imprimer.f(gameState["zone_principale"], 24, f"Lettres ratées : {lettres_ratees}")

        afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])



        if all(lettre in lettres_trouvees for lettre in mot):
            vider.f(gameState["zone_principale"])
            imprimer.f(gameState["zone_principale"], 15, f"BRAVO !")
            res = True
        else:
            lettre = input("Propose une lettre : ").upper()

            if len(lettre) != 1:
                print("Entre une seule lettre valide !")

            elif lettre in lettres_trouvees or lettre in lettres_ratees:
                print("Tu as deja propose cette lettre !")
                input("Appuie sur Entrée...")

            elif lettre in mot:
                lettres_trouvees.append(lettre)
                print("Bonne reponse !")

            else:
                lettres_ratees.append(lettre)
                erreurs += 1
                print("Mauvaise reponse !")

        input("Appuie sur ENTREE pour continuer...")



    # Résultats

    if erreurs == 6:
        res = False
        vider.f(gameState["zone_principale"])
        imprimer.f(gameState["zone_principale"], 15, f"Perdu, le mot était : {mot}")
        afficher_ecran.f(gameState["zone_principale"], gameState["zone_inventaire"], gameState["zone_dialogue"], gameState["zone_stat"])
        input("Appuie sur ENTREE pour continuer...")
    else:
        res = True



    # on renvoie le resultat du jeu

    return res