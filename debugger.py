import sys
import importlib


def creer_gameState() -> dict:
    gameState: dict = {
        "nom": "Adam",
        "age": 18,
        "pays": "Maroc",
        "argent": 500,
        "energie": 90,
        "vie": 99,
        "reputation": 60,
        "ecole": "IMT",

        "inventaire": [
            "gâteaux prince",
            "Téléphone",
            "Carte d'identité",
            "Couteau"
        ],

        "zone_principale": [
            "┌" + 98 * "─" + "┐",
            *["│" + 98 * " " + "│"] * 30,
            "└" + 98 * "─" + "┘"
        ],

        "zone_dialogue": [
            "┌" + 98 * "─" + "┐",
            *["│" + 98 * " " + "│"] * 7,
            "└" + 98 * "─" + "┘"
        ],

        "zone_inventaire": [
            "┌" + 28 * "─" + "┐",
            *["│" + 28 * " " + "│"] * 30,
            "└" + 28 * "─" + "┘"
        ],

        "zone_stat": [
            "┌" + 28 * "─" + "┐",
            *["│" + 28 * " " + "│"] * 7,
            "└" + 28 * "─" + "┘"
        ]
    }

    return gameState


def initialiser_affichage(gameState: dict) -> None:
    from OUTILS import afficher_ecran, maj_inv, maj_stat

    maj_inv.f(gameState["zone_inventaire"], gameState)
    maj_stat.f(gameState["zone_stat"], gameState)

    afficher_ecran.f(
        gameState["zone_principale"],
        gameState["zone_inventaire"],
        gameState["zone_dialogue"],
        gameState["zone_stat"]
    )


def jouer_page(page_depart: int) -> None:
    from ASCII.ascii_gameover import ascii_gameover

    gameState: dict = creer_gameState()
    page_actuelle: int = page_depart
    continuer: bool = True

    initialiser_affichage(gameState)

    input("\nPersonnage Adam prêt ! Appuie sur Entrée pour commencer...")

    while continuer:

        nom_page: str = "page" + str(page_actuelle)

        try:
            module = importlib.import_module(
                "histoire." + nom_page
            )

            fonction = getattr(module, nom_page)

            print("\n" + "=" * 50)
            print(f"PAGE {page_actuelle}")
            print("=" * 50)

            resultat = fonction(gameState)

            if isinstance(resultat, bool) or not isinstance(resultat, int):
                print("ERREUR : la page doit retourner un entier.")
                continuer = False

            elif resultat == -2:
                print("ERREUR : cas non prévu (-2).")
                continuer = False

            elif resultat < -2:
                print("ERREUR : numéro de retour invalide.")
                continuer = False

            elif resultat == 0:
                print("\nFIN DU JEU !")
                continuer = False

            elif resultat == -1:
                print("\nGAME OVER !")
                ascii_gameover()

                choix: str = input(
                    "\nR pour recommencer au début du test, Q pour quitter : "
                ).upper()

                if choix == "R":
                    page_actuelle = page_depart
                    gameState = creer_gameState()
                    initialiser_affichage(gameState)
                else:
                    continuer = False

            else:
                print(f"\nPassage automatique à la page {resultat}...")
                page_actuelle = resultat

        except ModuleNotFoundError:
            print(f"\nERREUR : la page {page_actuelle} n'existe pas.")
            continuer = False

        except AttributeError:
            print(f"\nERREUR : fonction {nom_page} introuvable.")
            continuer = False

        except Exception as erreur:
            print(f"\nERREUR pendant l'exécution : {erreur}")
            continuer = False

    print("\nFin du mode test.")


def lancer_test() -> None:
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Utilisation : python test.py NUMERO_PAGE")
    else:
        page_depart: int = int(sys.argv[1])

        if page_depart < 1:
            print("Le numéro de départ doit être supérieur ou égal à 1.")
        else:
            jouer_page(page_depart)


if __name__ == "__main__":
    lancer_test()
