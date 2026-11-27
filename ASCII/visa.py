RESET = "\033[0m"
NAVY = "\033[38;2;8;8;45m"
BLEU = "\033[38;2;30;60;140m"
CREME = "\033[38;2;245;235;205m"
GRIS = "\033[38;2;150;150;160m"
OMBRE = "\033[38;2;70;80;110m"
CIEL = "\033[38;2;150;195;235m"
ROUGE = "\033[38;2;205;30;40m"

# morceaux réutilisés (largeur totale d'une ligne : 2 + 45 + 4 + 45 + 2 = 98)
BORD = NAVY + 2*"█"
DOS = OMBRE + 1*"█" + NAVY + 2*"█" + OMBRE + 1*"█"
VIDE = CREME + 45*"█"
BARRE = CREME + 3*"█" + BLEU + 39*"█" + CREME + 3*"█"
LIGNE39 = CREME + 3*"█" + GRIS + 39*"█" + CREME + 3*"█"
TAMPON_PLEIN = CREME + 3*"█" + ROUGE + 38*"█" + CREME + 4*"█"
TAMPON_VIDE = (CREME + 3*"█" + ROUGE + 2*"█" + CREME + 34*"█" + ROUGE + 2*"█"
+ CREME + 4*"█")

dessin = [
# 0 : couverture haut
NAVY + 98*"█" + RESET,
# 1-2 : marge des pages
BORD + VIDE + DOS + VIDE + BORD + RESET,
BORD + VIDE + DOS + VIDE + BORD + RESET,
# 3 : bandeau titre des deux pages
BORD + BARRE + DOS + BARRE + BORD + RESET,
# 4 : marge
BORD + VIDE + DOS + VIDE + BORD + RESET,
# 5 : haut du tampon (droite)
BORD + VIDE + DOS + TAMPON_PLEIN + BORD + RESET,
# 6 : photo (haut) + ligne de texte / tampon
BORD + CREME + 3*"█" + CIEL + 14*"█" + CREME + 3*"█" + GRIS + 20*"█" + CREME +
5*"█" + DOS + TAMPON_VIDE + BORD + RESET,
# 7
BORD + CREME + 3*"█" + CIEL + 5*"█" + OMBRE + 4*"█" + CIEL + 5*"█" + CREME +
28*"█" + DOS + TAMPON_VIDE + BORD + RESET,
# 8 : début des lettres VISA
BORD + CREME + 3*"█" + CIEL + 4*"█" + OMBRE + 6*"█" + CIEL + 4*"█" + CREME +
3*"█" + GRIS + 14*"█" + CREME + 11*"█" + DOS +
CREME + 3*"█" + ROUGE + 2*"█" + CREME + 2*"█" + ROUGE + 2*"█" + CREME + 2*"█" +
ROUGE + 2*"█" + CREME + 2*"█" + ROUGE + 6*"█" + CREME + 2*"█" + ROUGE + 6*"█" +
CREME + 4*"█" + ROUGE + 2*"█" + CREME + 4*"█" + ROUGE + 2*"█" + CREME + 4*"█" +
BORD + RESET,
# 9
BORD + CREME + 3*"█" + CIEL + 4*"█" + OMBRE + 6*"█" + CIEL + 4*"█" + CREME +
28*"█" + DOS +
CREME + 3*"█" + ROUGE + 2*"█" + CREME + 2*"█" + ROUGE + 2*"█" + CREME + 2*"█" +
ROUGE + 2*"█" + CREME + 4*"█" + ROUGE + 2*"█" + CREME + 4*"█" + ROUGE + 2*"█" +
CREME + 6*"█" + ROUGE + 2*"█" + CREME + 2*"█" + ROUGE + 2*"█" + CREME + 2*"█" +
ROUGE + 2*"█" + CREME + 4*"█" + BORD + RESET,
# 10
BORD + CREME + 3*"█" + CIEL + 5*"█" + OMBRE + 4*"█" + CIEL + 5*"█" + CREME +
3*"█" + GRIS + 20*"█" + CREME + 5*"█" + DOS +
CREME + 3*"█" + ROUGE + 2*"█" + CREME + 2*"█" + ROUGE + 2*"█" + CREME + 2*"█" +
ROUGE + 2*"█" + CREME + 4*"█" + ROUGE + 2*"█" + CREME + 4*"█" + ROUGE + 6*"█" +
CREME + 2*"█" + ROUGE + 6*"█" + CREME + 2*"█" + ROUGE + 2*"█" + CREME + 4*"█" +
BORD + RESET,
# 11
BORD + CREME + 3*"█" + CIEL + 3*"█" + OMBRE + 8*"█" + CIEL + 3*"█" + CREME +
28*"█" + DOS +
CREME + 3*"█" + ROUGE + 2*"█" + CREME + 2*"█" + ROUGE + 2*"█" + CREME + 2*"█" +
ROUGE + 2*"█" + CREME + 4*"█" + ROUGE + 2*"█" + CREME + 8*"█" + ROUGE + 2*"█" +
CREME + 2*"█" + ROUGE + 2*"█" + CREME + 2*"█" + ROUGE + 2*"█" + CREME + 2*"█" +
ROUGE + 2*"█" + CREME + 4*"█" + BORD + RESET,
# 12
BORD + CREME + 3*"█" + CIEL + 2*"█" + OMBRE + 10*"█" + CIEL + 2*"█" + CREME +
3*"█" + GRIS + 10*"█" + CREME + 15*"█" + DOS +
CREME + 3*"█" + ROUGE + 2*"█" + CREME + 4*"█" + ROUGE + 2*"█" + CREME + 4*"█" +
ROUGE + 6*"█" + CREME + 2*"█" + ROUGE + 6*"█" + CREME + 2*"█" + ROUGE + 2*"█" +
CREME + 2*"█" + ROUGE + 2*"█" + CREME + 2*"█" + ROUGE + 2*"█" + CREME + 4*"█" +
BORD + RESET,
# 13
BORD + CREME + 3*"█" + CIEL + 1*"█" + OMBRE + 12*"█" + CIEL + 1*"█" + CREME +
28*"█" + DOS + TAMPON_VIDE + BORD + RESET,
# 14
BORD + CREME + 3*"█" + CIEL + 1*"█" + OMBRE + 12*"█" + CIEL + 1*"█" + CREME +
3*"█" + GRIS + 16*"█" + CREME + 9*"█" + DOS + TAMPON_VIDE + BORD + RESET,
# 15 : bas de la photo / bas du tampon
BORD + CREME + 3*"█" + CIEL + 14*"█" + CREME + 28*"█" + DOS + TAMPON_PLEIN +
BORD + RESET,
# 16
BORD + VIDE + DOS + VIDE + BORD + RESET,
# 17 : lignes de texte
BORD + LIGNE39 + DOS + LIGNE39 + BORD + RESET,
# 18
BORD + VIDE + DOS + VIDE + BORD + RESET,
# 19
BORD + LIGNE39 + DOS + CREME + 3*"█" + GRIS + 30*"█" + CREME + 12*"█" + BORD +
RESET,
# 20
BORD + VIDE + DOS + VIDE + BORD + RESET,
# 21
BORD + CREME + 3*"█" + GRIS + 30*"█" + CREME + 12*"█" + DOS + LIGNE39 + BORD +
RESET,
# 22
BORD + VIDE + DOS + VIDE + BORD + RESET,
# 23
BORD + LIGNE39 + DOS + CREME + 3*"█" + GRIS + 25*"█" + CREME + 17*"█" + BORD +
RESET,
# 24
BORD + VIDE + DOS + VIDE + BORD + RESET,
# 25 : bas des pages
BORD + LIGNE39 + DOS + CREME + 3*"█" + GRIS + 20*"█" + CREME + 22*"█" + BORD +
RESET,
# 26-28 : marge
BORD + VIDE + DOS + VIDE + BORD + RESET,
BORD + VIDE + DOS + VIDE + BORD + RESET,
BORD + VIDE + DOS + VIDE + BORD + RESET,
# 29 : couverture bas
NAVY + 98*"█" + RESET,
]