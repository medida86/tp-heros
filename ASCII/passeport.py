RESET = "\033[0m"
CIEL = "\033[38;2;135;206;235m"
OMBRE = "\033[38;2;95;155;190m"
DOS = "\033[38;2;70;8;28m"
BORD = "\033[38;2;120;20;45m"
CLAIR = "\033[38;2;160;38;68m"
DORE = "\033[38;2;240;195;60m"
DORE2 = "\033[38;2;195;145;30m"

GAUCHE = CIEL + 30*"█"
DROITE = OMBRE + 2*"█" + CIEL + 30*"█" + RESET
SP = DOS + 2*"█" + CLAIR + 1*"█"
CADRE_G = BORD + 2*"█" + DORE2 + 1*"█"
CADRE_D = DORE2 + 1*"█" + BORD + 2*"█"

dessin = [
# 2 lignes de ciel en haut
CIEL + 98*"█" + RESET,
CIEL + 98*"█" + RESET,
# bord haut (arête éclairée, coins arrondis)
CIEL + 31*"█" + CLAIR + 34*"█" + CIEL + 33*"█" + RESET,
# marge de la couverture
GAUCHE + SP + BORD + 33*"█" + DROITE,
GAUCHE + SP + BORD + 33*"█" + DROITE,
# cadre doré (haut)
GAUCHE + SP + BORD + 2*"█" + DORE2 + 29*"█" + BORD + 2*"█" + DROITE,
# intérieur du cadre : ligne vide
GAUCHE + SP + CADRE_G + BORD + 27*"█" + CADRE_D + DROITE,
# texte du haut (pays)
GAUCHE + SP + CADRE_G + BORD + 5*"█" + 5*(DORE + 2*"█" + BORD + 1*"█") + DORE +
2*"█" + BORD + 5*"█" + CADRE_D + DROITE,
GAUCHE + SP + CADRE_G + BORD + 27*"█" + CADRE_D + DROITE,
# titre PASSEPORT (2 lignes)
GAUCHE + SP + CADRE_G + BORD + 2*"█" + 7*(DORE + 2*"█" + BORD + 1*"█") + DORE +
2*"█" + BORD + 2*"█" + CADRE_D + DROITE,
GAUCHE + SP + CADRE_G + BORD + 2*"█" + 7*(DORE + 2*"█" + BORD + 1*"█") + DORE +
2*"█" + BORD + 2*"█" + CADRE_D + DROITE,
GAUCHE + SP + CADRE_G + BORD + 27*"█" + CADRE_D + DROITE,
# emblème : globe doré avec méridiens et ombre sur la droite
GAUCHE + SP + CADRE_G + BORD + 10*"█" + DORE + 3*"█" + BORD + 1*"█" + DORE2 +
3*"█" + BORD + 10*"█" + CADRE_D + DROITE,
GAUCHE + SP + CADRE_G + BORD + 7*"█" + DORE + 3*"█" + BORD + 1*"█" + DORE +
2*"█" + BORD + 1*"█" + DORE + 2*"█" + BORD + 1*"█" + DORE2 + 3*"█" + BORD +
7*"█" + CADRE_D + DROITE,
GAUCHE + SP + CADRE_G + BORD + 6*"█" + DORE + 3*"█" + BORD + 1*"█" + DORE +
3*"█" + BORD + 1*"█" + DORE + 3*"█" + BORD + 1*"█" + DORE2 + 3*"█" + BORD +
6*"█" + CADRE_D + DROITE,
GAUCHE + SP + CADRE_G + BORD + 5*"█" + DORE + 3*"█" + BORD + 1*"█" + DORE +
4*"█" + BORD + 1*"█" + DORE + 4*"█" + BORD + 1*"█" + DORE2 + 3*"█" + BORD +
5*"█" + CADRE_D + DROITE,
GAUCHE + SP + CADRE_G + BORD + 5*"█" + DORE + 3*"█" + BORD + 1*"█" + DORE +
4*"█" + BORD + 1*"█" + DORE + 4*"█" + BORD + 1*"█" + DORE2 + 3*"█" + BORD +
5*"█" + CADRE_D + DROITE,
GAUCHE + SP + CADRE_G + BORD + 6*"█" + DORE + 3*"█" + BORD + 1*"█" + DORE +
3*"█" + BORD + 1*"█" + DORE + 3*"█" + BORD + 1*"█" + DORE2 + 3*"█" + BORD +
6*"█" + CADRE_D + DROITE,
GAUCHE + SP + CADRE_G + BORD + 7*"█" + DORE + 3*"█" + BORD + 1*"█" + DORE +
2*"█" + BORD + 1*"█" + DORE + 2*"█" + BORD + 1*"█" + DORE2 + 3*"█" + BORD +
7*"█" + CADRE_D + DROITE,
GAUCHE + SP + CADRE_G + BORD + 10*"█" + DORE + 3*"█" + BORD + 1*"█" + DORE2 +
3*"█" + BORD + 10*"█" + CADRE_D + DROITE,
# espace sous le globe
GAUCHE + SP + CADRE_G + BORD + 27*"█" + CADRE_D + DROITE,
# puce biométrique dorée
GAUCHE + SP + CADRE_G + BORD + 9*"█" + DORE + 9*"█" + BORD + 9*"█" + CADRE_D + DROITE,
GAUCHE + SP + CADRE_G + BORD + 9*"█" + DORE2 + 9*"█" + BORD + 9*"█" + CADRE_D + DROITE,
GAUCHE + SP + CADRE_G + BORD + 27*"█" + CADRE_D + DROITE,
# cadre doré (bas)
GAUCHE + SP + BORD + 2*"█" + DORE2 + 29*"█" + BORD + 2*"█" + DROITE,
# marge basse
GAUCHE + SP + BORD + 33*"█" + DROITE,
GAUCHE + SP + BORD + 33*"█" + DROITE,
# bord bas (arête dans l'ombre, coins arrondis)
CIEL + 31*"█" + DOS + 34*"█" + CIEL + 1*"█" + OMBRE + 2*"█" + CIEL + 30*"█" + RESET,
# ombre portée sous le passeport
CIEL + 32*"█" + OMBRE + 36*"█" + CIEL + 30*"█" + RESET,
# 1 ligne de ciel en bas
CIEL + 98*"█" + RESET,
]