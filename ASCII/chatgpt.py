RESET = "\033[0m"
NAVY = "\033[38;2;8;8;45m"
JAUNE = "\033[38;2;255;185;30m"
ORANGE = "\033[38;2;255;125;10m"
ROUGE = "\033[38;2;235;75;10m"
MUR = "\033[38;2;70;55;120m"
CADRE = "\033[38;2;28;28;36m"
ECRAN = "\033[38;2;80;160;235m"
ECRAN_FONCE = "\033[38;2;35;95;175m"
ECRAN_SOMBRE = "\033[38;2;38;40;48m"
BARRE = "\033[38;2;20;20;26m"
BLANC = "\033[38;2;250;250;250m"
GRIS_CLAIR = "\033[38;2;185;190;205m"
GRIS_FONCE = "\033[38;2;85;85;100m"
BOIS = "\033[38;2;150;95;55m"
BOIS_FONCE = "\033[38;2;115;70;40m"
PEAU = "\033[38;2;240;190;150m"
VERT = "\033[38;2;60;190;110m"
VERT_GPT = "\033[38;2;16;163;127m"
MARRON = "\033[38;2;90;50;30m"

dessin = [
    MUR + 98*"█" + RESET,
    MUR + 19*"█" + CADRE + 60*"█" + MUR + 19*"█" + RESET,
    MUR + 19*"█" + CADRE + 60*"█" + MUR + 19*"█" + RESET,
    MUR + 3*"█" + BLANC + 11*"█" + MUR + 5*"█" + CADRE + 2*"█" + BARRE + 2*"█" + ROUGE + 1*"█" + BARRE + 1*"█" + JAUNE + 1*"█" + BARRE + 1*"█" + VERT + 1*"█" + BARRE + 49*"█" + CADRE + 2*"█" + MUR + 19*"█" + RESET,
    MUR + 3*"█" + BLANC + 1*"█" + NAVY + 9*"█" + BLANC + 1*"█" + MUR + 5*"█" + CADRE + 2*"█" + ECRAN_SOMBRE + 56*"█" + CADRE + 2*"█" + MUR + 4*"█" + BLANC + 10*"█" + MUR + 5*"█" + RESET,
    MUR + 3*"█" + BLANC + 1*"█" + NAVY + 3*"█" + JAUNE + 3*"█" + NAVY + 3*"█" + BLANC + 1*"█" + MUR + 5*"█" + CADRE + 2*"█" + ECRAN_SOMBRE + 56*"█" + CADRE + 2*"█" + MUR + 4*"█" + BLANC + 1*"█" + NAVY + 6*"█" + JAUNE + 1*"█" + NAVY + 1*"█" + BLANC + 1*"█" + MUR + 5*"█" + RESET,
    MUR + 3*"█" + BLANC + 1*"█" + NAVY + 3*"█" + JAUNE + 3*"█" + NAVY + 3*"█" + BLANC + 1*"█" + MUR + 5*"█" + CADRE + 2*"█" + ECRAN_SOMBRE + 56*"█" + CADRE + 2*"█" + MUR + 4*"█" + BLANC + 1*"█" + NAVY + 2*"█" + JAUNE + 1*"█" + NAVY + 5*"█" + BLANC + 1*"█" + MUR + 5*"█" + RESET,
    MUR + 3*"█" + BLANC + 1*"█" + NAVY + 2*"█" + ORANGE + 5*"█" + NAVY + 2*"█" + BLANC + 1*"█" + MUR + 5*"█" + CADRE + 2*"█" + ECRAN_SOMBRE + 1*"█" + BLANC + 6*"█" + ECRAN_SOMBRE + 2*"█" + BLANC + 2*"█" + ECRAN_SOMBRE + 6*"█" + BLANC + 6*"█" + ECRAN_SOMBRE + 4*"█" + BLANC + 2*"█" + ECRAN_SOMBRE + 4*"█" + BLANC + 6*"█" + ECRAN_SOMBRE + 2*"█" + BLANC + 6*"█" + ECRAN_SOMBRE + 2*"█" + BLANC + 6*"█" + ECRAN_SOMBRE + 1*"█" + CADRE + 2*"█" + MUR + 4*"█" + BLANC + 1*"█" + NAVY + 1*"█" + JAUNE + 1*"█" + NAVY + 6*"█" + BLANC + 1*"█" + MUR + 5*"█" + RESET,
    MUR + 3*"█" + BLANC + 1*"█" + NAVY + 4*"█" + ROUGE + 1*"█" + NAVY + 4*"█" + BLANC + 1*"█" + MUR + 5*"█" + CADRE + 2*"█" + ECRAN_SOMBRE + 1*"█" + BLANC + 2*"█" + ECRAN_SOMBRE + 6*"█" + BLANC + 2*"█" + ECRAN_SOMBRE + 10*"█" + BLANC + 2*"█" + ECRAN_SOMBRE + 2*"█" + BLANC + 6*"█" + ECRAN_SOMBRE + 2*"█" + BLANC + 2*"█" + ECRAN_SOMBRE + 6*"█" + BLANC + 2*"█" + ECRAN_SOMBRE + 2*"█" + BLANC + 2*"█" + ECRAN_SOMBRE + 4*"█" + BLANC + 2*"█" + ECRAN_SOMBRE + 3*"█" + CADRE + 2*"█" + MUR + 4*"█" + BLANC + 1*"█" + NAVY + 5*"█" + JAUNE + 1*"█" + NAVY + 2*"█" + BLANC + 1*"█" + MUR + 5*"█" + RESET,
    MUR + 3*"█" + BLANC + 1*"█" + NAVY + 3*"█" + ROUGE + 3*"█" + NAVY + 3*"█" + BLANC + 1*"█" + MUR + 5*"█" + CADRE + 2*"█" + ECRAN_SOMBRE + 1*"█" + BLANC + 2*"█" + ECRAN_SOMBRE + 6*"█" + BLANC + 6*"█" + ECRAN_SOMBRE + 2*"█" + BLANC + 6*"█" + ECRAN_SOMBRE + 4*"█" + BLANC + 2*"█" + ECRAN_SOMBRE + 4*"█" + BLANC + 2*"█" + ECRAN_SOMBRE + 2*"█" + BLANC + 2*"█" + ECRAN_SOMBRE + 2*"█" + BLANC + 6*"█" + ECRAN_SOMBRE + 4*"█" + BLANC + 2*"█" + ECRAN_SOMBRE + 3*"█" + CADRE + 2*"█" + MUR + 4*"█" + BLANC + 1*"█" + NAVY + 8*"█" + BLANC + 1*"█" + MUR + 5*"█" + RESET,
    MUR + 3*"█" + BLANC + 1*"█" + NAVY + 1*"█" + ROUGE + 7*"█" + NAVY + 1*"█" + BLANC + 1*"█" + MUR + 5*"█" + CADRE + 2*"█" + ECRAN_SOMBRE + 1*"█" + BLANC + 2*"█" + ECRAN_SOMBRE + 6*"█" + BLANC + 2*"█" + ECRAN_SOMBRE + 2*"█" + BLANC + 2*"█" + ECRAN_SOMBRE + 2*"█" + BLANC + 2*"█" + ECRAN_SOMBRE + 2*"█" + BLANC + 2*"█" + ECRAN_SOMBRE + 4*"█" + BLANC + 2*"█" + ECRAN_SOMBRE + 4*"█" + BLANC + 2*"█" + ECRAN_SOMBRE + 2*"█" + BLANC + 2*"█" + ECRAN_SOMBRE + 2*"█" + BLANC + 2*"█" + ECRAN_SOMBRE + 8*"█" + BLANC + 2*"█" + ECRAN_SOMBRE + 3*"█" + CADRE + 2*"█" + MUR + 4*"█" + BLANC + 10*"█" + MUR + 5*"█" + RESET,
    MUR + 3*"█" + BLANC + 11*"█" + MUR + 5*"█" + CADRE + 2*"█" + ECRAN_SOMBRE + 1*"█" + BLANC + 6*"█" + ECRAN_SOMBRE + 2*"█" + BLANC + 2*"█" + ECRAN_SOMBRE + 2*"█" + BLANC + 2*"█" + ECRAN_SOMBRE + 2*"█" + BLANC + 6*"█" + ECRAN_SOMBRE + 4*"█" + BLANC + 4*"█" + ECRAN_SOMBRE + 2*"█" + BLANC + 6*"█" + ECRAN_SOMBRE + 2*"█" + BLANC + 2*"█" + ECRAN_SOMBRE + 8*"█" + BLANC + 2*"█" + ECRAN_SOMBRE + 3*"█" + CADRE + 2*"█" + MUR + 19*"█" + RESET,
    MUR + 19*"█" + CADRE + 2*"█" + ECRAN_SOMBRE + 56*"█" + CADRE + 2*"█" + MUR + 19*"█" + RESET,
    MUR + 19*"█" + CADRE + 2*"█" + ECRAN_SOMBRE + 1*"█" + VERT_GPT + 54*"█" + ECRAN_SOMBRE + 1*"█" + CADRE + 2*"█" + MUR + 19*"█" + RESET,
    MUR + 19*"█" + CADRE + 2*"█" + ECRAN_SOMBRE + 56*"█" + CADRE + 2*"█" + MUR + 19*"█" + RESET,
    MUR + 19*"█" + CADRE + 2*"█" + ECRAN_SOMBRE + 9*"█" + GRIS_FONCE + 2*"█" + GRIS_CLAIR + 2*"█" + GRIS_FONCE + 34*"█" + ECRAN_SOMBRE + 9*"█" + CADRE + 2*"█" + MUR + 19*"█" + RESET,
    MUR + 19*"█" + CADRE + 2*"█" + ECRAN_SOMBRE + 9*"█" + GRIS_FONCE + 2*"█" + GRIS_CLAIR + 2*"█" + GRIS_FONCE + 34*"█" + ECRAN_SOMBRE + 9*"█" + CADRE + 2*"█" + MUR + 19*"█" + RESET,
    MUR + 19*"█" + CADRE + 2*"█" + BARRE + 1*"█" + BLANC + 2*"█" + BARRE + 48*"█" + BLANC + 4*"█" + BARRE + 1*"█" + CADRE + 2*"█" + MUR + 19*"█" + RESET,
    MUR + 19*"█" + CADRE + 60*"█" + MUR + 19*"█" + RESET,
    MUR + 19*"█" + CADRE + 29*"█" + GRIS_CLAIR + 2*"█" + CADRE + 29*"█" + MUR + 19*"█" + RESET,
    MUR + 45*"█" + GRIS_FONCE + 8*"█" + MUR + 45*"█" + RESET,
    BOIS_FONCE + 34*"█" + GRIS_FONCE + 30*"█" + BOIS_FONCE + 34*"█" + RESET,
    BOIS + 82*"█" + BLANC + 1*"█" + MARRON + 4*"█" + BLANC + 1*"█" + BOIS + 10*"█" + RESET,
    BOIS + 4*"█" + BOIS_FONCE + 4*"█" + CADRE + 6*"█" + BOIS_FONCE + 1*"█" + BOIS + 9*"█" + GRIS_FONCE + 50*"█" + BOIS + 8*"█" + BLANC + 8*"█" + BOIS + 8*"█" + RESET,
    BOIS + 8*"█" + CADRE + 1*"█" + ECRAN + 3*"█" + BLANC + 1*"█" + CADRE + 1*"█" + BOIS + 10*"█" + GRIS_FONCE + 1*"█" + GRIS_CLAIR + 3*"█" + GRIS_FONCE + 1*"█" + GRIS_CLAIR + 2*"█" + PEAU + 2*"█" + GRIS_CLAIR + 1*"█" + PEAU + 2*"█" + GRIS_FONCE + 1*"█" + PEAU + 2*"█" + GRIS_CLAIR + 1*"█" + PEAU + 2*"█" + GRIS_CLAIR + 2*"█" + GRIS_FONCE + 1*"█" + GRIS_CLAIR + 3*"█" + GRIS_FONCE + 1*"█" + GRIS_CLAIR + 3*"█" + GRIS_FONCE + 1*"█" + GRIS_CLAIR + 3*"█" + PEAU + 2*"█" + GRIS_CLAIR + 1*"█" + PEAU + 2*"█" + GRIS_CLAIR + 1*"█" + PEAU + 2*"█" + GRIS_FONCE + 1*"█" + PEAU + 2*"█" + GRIS_CLAIR + 1*"█" + GRIS_FONCE + 1*"█" + GRIS_CLAIR + 3*"█" + GRIS_FONCE + 2*"█" + BOIS + 8*"█" + BLANC + 6*"█" + BOIS + 1*"█" + BLANC + 1*"█" + BOIS + 8*"█" + RESET,
    BOIS + 2*"█" + BOIS_FONCE + 5*"█" + BOIS + 1*"█" + CADRE + 1*"█" + ECRAN + 4*"█" + CADRE + 1*"█" + BOIS + 10*"█" + GRIS_FONCE + 1*"█" + GRIS_CLAIR + 1*"█" + GRIS_FONCE + 1*"█" + GRIS_CLAIR + 3*"█" + PEAU + 13*"█" + GRIS_CLAIR + 3*"█" + GRIS_FONCE + 1*"█" + GRIS_CLAIR + 3*"█" + GRIS_FONCE + 1*"█" + GRIS_CLAIR + 3*"█" + GRIS_FONCE + 1*"█" + PEAU + 13*"█" + GRIS_CLAIR + 2*"█" + GRIS_FONCE + 1*"█" + GRIS_CLAIR + 2*"█" + GRIS_FONCE + 1*"█" + BOIS + 8*"█" + BLANC + 8*"█" + BOIS + 8*"█" + RESET,
    BOIS + 8*"█" + CADRE + 1*"█" + ECRAN + 4*"█" + CADRE + 1*"█" + BOIS + 10*"█" + GRIS_FONCE + 1*"█" + GRIS_CLAIR + 3*"█" + GRIS_FONCE + 1*"█" + GRIS_CLAIR + 1*"█" + PEAU + 13*"█" + GRIS_CLAIR + 12*"█" + PEAU + 13*"█" + GRIS_FONCE + 1*"█" + GRIS_CLAIR + 3*"█" + GRIS_FONCE + 2*"█" + BOIS + 24*"█" + RESET,
    BOIS + 8*"█" + CADRE + 6*"█" + BOIS + 10*"█" + GRIS_FONCE + 8*"█" + PEAU + 9*"█" + GRIS_FONCE + 16*"█" + PEAU + 9*"█" + GRIS_FONCE + 8*"█" + BOIS + 24*"█" + RESET,
    BOIS + 29*"█" + ORANGE + 15*"█" + BOIS + 10*"█" + ORANGE + 15*"█" + BOIS + 11*"█" + BOIS_FONCE + 14*"█" + BOIS + 4*"█" + RESET,
    BOIS + 25*"█" + ORANGE + 23*"█" + BOIS + 2*"█" + ORANGE + 23*"█" + BOIS + 25*"█" + RESET,
]