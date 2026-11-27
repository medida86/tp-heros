# fonction de combat

def f(gameState: dict, adversaire: dict) -> bool:
    res: bool = False

    # on importe ce qui est necessaire

    import random
    from OUTILS import imprimer, afficher_ecran, vider, maj_inv, maj_stat

    # variables

    nom: str = adversaire['nom']
    vie_adversaire: int = adversaire['vie']
    degats_adversaire: int = adversaire['degats']
    attaques: list = adversaire['attaques']
    defenses: dict = {'VISAGE': '3', 'JAMBES': '4', 'VENTRE': '5'}
    defenses.update(adversaire.get('defenses', {}))
    zone: list = gameState['zone_principale']
    inventaire: list = gameState['inventaire']
    bandage: str = 'Bandage'
    boisson: str = 'Boisson energie'
    manche: int = 0
    message: str = ""
    gain: int = 0

    # on conserve les truc au debut du combat

    inventaire.extend([bandage, bandage, boisson, boisson])
    maj_inv.f(gameState['zone_inventaire'], gameState)

    # Tutoriel affiche avant la premiere manche

    vider.f(zone)
    imprimer.f(zone, 2, '===== TUTORIEL DU COMBAT =====')
    imprimer.f(zone, 5, 'Le combat se deroule au tour par tour.')
    imprimer.f(zone, 7, 'A ton tour, attaque ou utilise un objet :')
    imprimer.f(zone, 9, '1 - Poing : 20 degats / 15 energie.')
    imprimer.f(zone, 10, '2 - Pied : 30 degats / 25 energie.')
    imprimer.f(zone, 12, '6 - Bandage : +25 vie.')
    imprimer.f(zone, 13, '7 - Boisson : +30 energie.')
    imprimer.f(zone, 15, 'Puis ton adversaire attaque sans annoncer sa cible.')
    imprimer.f(zone, 17, '3 - Se baisser : esquive du visage.')
    imprimer.f(zone, 18, '4 - Sauter : esquive des jambes.')
    imprimer.f(zone, 19, '5 - Reculer : esquive du ventre.')
    imprimer.f(zone, 21, 'Une bonne esquive annule les degats et coute 10 energie.')
    imprimer.f(zone, 22, 'Une mauvaise esquive coute aussi 10 energie et tu prends le coup.')
    imprimer.f(zone, 23, '0 - Encaisser sans depenser d energie.')
    imprimer.f(zone, 25, 'Gagne en mettant la vie adverse a zero.')
    imprimer.f(zone, 26, 'Sans assez d energie pour attaquer ni boisson, tu perds.')
    imprimer.f(zone, 28, 'Appuie sur ENTREE pour commencer le combat.')
    afficher_ecran.f(zone, gameState['zone_inventaire'], gameState['zone_dialogue'], gameState['zone_stat'])
    input('Appuie sur ENTREE...')



    # boucle principale du jeu

    while (gameState['vie'] > 0 and vie_adversaire > 0 and
           (gameState['energie'] >= 15 or boisson in inventaire)):
        manche += 1

        # premier tour : le joueur attaque ou utilise un objet

        vider.f(zone)
        imprimer.f(zone, 3, f'===== MANCHE {manche} : TON TOUR =====')
        imprimer.f(zone, 7, f'Adversaire : {nom} - Vie : {vie_adversaire}')
        imprimer.f(zone, 10, f'Ta vie : {gameState["vie"]} - Energie : {gameState["energie"]}')
        imprimer.f(zone, 15, '1 - Coup de poing (20 degats / 15 energie)')
        imprimer.f(zone, 17, '2 - Coup de pied (30 degats / 25 energie)')
        imprimer.f(zone, 21, f'6 - Bandage (+25 vie) : {inventaire.count(bandage)} restant(s)')
        imprimer.f(zone, 23, f'7 - Boisson (+30 energie) : {inventaire.count(boisson)} restante(s)')
        afficher_ecran.f(zone, gameState['zone_inventaire'], gameState['zone_dialogue'], gameState['zone_stat'])

        choix: str = input('Ton action (1, 2, 6 ou 7) : ')
        while not ((choix == '1' and gameState['energie'] >= 15) or
                   (choix == '2' and gameState['energie'] >= 25) or
                   (choix == '6' and bandage in inventaire and gameState['vie'] < 100) or
                   (choix == '7' and boisson in inventaire and gameState['energie'] < 100)):
            choix = input('Action impossible, choisis une autre action : ')

        if choix == '1':
            gameState['energie'] -= 15
            vie_adversaire = max(0, vie_adversaire - 20)
            message = 'Tu donnes un coup de poing !'
        elif choix == '2':
            gameState['energie'] -= 25
            vie_adversaire = max(0, vie_adversaire - 30)
            message = 'Tu donnes un coup de pied !'
        elif choix == '6':
            inventaire.remove(bandage)
            gain = min(25, 100 - gameState['vie'])
            gameState['vie'] += gain
            message = f'Tu utilises un bandage : +{gain} vie !'
        else:
            inventaire.remove(boisson)
            gain = min(30, 100 - gameState['energie'])
            gameState['energie'] += gain
            message = f'Tu bois une boisson : +{gain} energie !'

        maj_inv.f(gameState['zone_inventaire'], gameState)
        maj_stat.f(gameState['zone_stat'], gameState)
        vider.f(zone)
        imprimer.f(zone, 8, message)
        imprimer.f(zone, 13, f'Vie de {nom} : {vie_adversaire}')


        # un adversaire vaincu ne peut pas riposter

        if vie_adversaire == 0:
            imprimer.f(zone, 20, 'VICTOIRE !')
            afficher_ecran.f(zone, gameState['zone_inventaire'], gameState['zone_dialogue'], gameState['zone_stat'])
            input('Appuie sur ENTREE...')


        # deuxieme tour : attaque secrete de l'adversaire
        
        if vie_adversaire > 0:
            attaque: str = random.choice(attaques)
            imprimer.f(zone, 16, f'AU TOUR DE {nom} !')
            imprimer.f(zone, 19, '3 - Se baisser (10 energie)')
            imprimer.f(zone, 21, '4 - Sauter (10 energie)')
            imprimer.f(zone, 23, '5 - Reculer (10 energie)')
            imprimer.f(zone, 25, '0 - Encaisser sans esquiver (0 energie)')
            afficher_ecran.f(zone, gameState['zone_inventaire'], gameState['zone_dialogue'], gameState['zone_stat'])

            choix = input('Ton esquive (0, 3, 4 ou 5) : ')
            while choix not in ['0', '3', '4', '5'] or (choix != '0' and gameState['energie'] < 10):
                choix = input('Esquive impossible, choisis a nouveau : ')

            if choix != '0':
                gameState['energie'] -= 10

            if choix != '0' and choix == defenses.get(attaque):
                message = 'BIEN JOUE ! Tu as esquive son attaque !'
            else:
                gameState['vie'] = max(0, gameState['vie'] - degats_adversaire)
                message = f'Tu encaisses le coup ! -{degats_adversaire} vie.'

            maj_stat.f(gameState['zone_stat'], gameState)
            vider.f(zone)
            imprimer.f(zone, 5, '===== RESULTAT DE LA MANCHE =====')
            imprimer.f(zone, 10, f'{nom} a attaque : {attaque}')
            imprimer.f(zone, 14, message)
            imprimer.f(zone, 19, f'Vie de {nom} : {vie_adversaire}')
            imprimer.f(zone, 22, f'Ta vie : {gameState["vie"]}')
            imprimer.f(zone, 24, f'Ton energie : {gameState["energie"]}')
            afficher_ecran.f(zone, gameState['zone_inventaire'], gameState['zone_dialogue'], gameState['zone_stat'])
            input('Appuie sur ENTREE pour continuer...')

    if vie_adversaire <= 0 and gameState['vie'] > 0:
        res = True
    elif gameState['vie'] > 0:
        vider.f(zone)
        imprimer.f(zone, 15, 'Tu es trop epuise pour continuer le combat !')
        afficher_ecran.f(zone, gameState['zone_inventaire'], gameState['zone_dialogue'], gameState['zone_stat'])
        input('Appuie sur ENTREE...')

    return res