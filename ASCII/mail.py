RESET = "\033[0m"
NAVY = "\033[38;2;8;8;45m"
JAUNE = "\033[38;2;255;185;30m"
ORANGE = "\033[38;2;255;125;10m"
ROUGE = "\033[38;2;235;75;10m"
MUR = "\033[38;2;70;55;120m"
CADRE = "\033[38;2;28;28;36m"
ECRAN = "\033[38;2;80;160;235m"
ECRAN_FONCE = "\033[38;2;35;95;175m"
BLANC = "\033[38;2;250;250;250m"
GRIS_CLAIR = "\033[38;2;185;190;205m"
GRIS_FONCE = "\033[38;2;85;85;100m"
BOIS = "\033[38;2;150;95;55m"
BOIS_FONCE = "\033[38;2;115;70;40m"
PEAU = "\033[38;2;240;190;150m"
VERT = "\033[38;2;60;190;110m"
MARRON = "\033[38;2;90;50;30m"

dessin = [
    MUR + 98*"█" + RESET,
    MUR + 19*"█" + CADRE + 60*"█" + MUR + 19*"█" + RESET,
    MUR + 19*"█" + CADRE + 60*"█" + MUR + 19*"█" + RESET,
    MUR + 3*"█" + BLANC + 11*"█" + MUR + 5*"█" + CADRE + 2*"█" + ECRAN_FONCE + 2*"█" + ROUGE + 1*"█" + ECRAN_FONCE + 1*"█" + JAUNE + 1*"█" + ECRAN_FONCE + 1*"█" + VERT + 1*"█" + ECRAN_FONCE + 49*"█" + CADRE + 2*"█" + MUR + 19*"█" + RESET,
    MUR + 3*"█" + BLANC + 1*"█" + NAVY + 9*"█" + BLANC + 1*"█" + MUR + 5*"█" + CADRE + 2*"█" + ECRAN + 26*"█" + ORANGE + 4*"█" + ECRAN + 9*"█" + ROUGE + 3*"█" + ECRAN + 14*"█" + CADRE + 2*"█" + MUR + 4*"█" + BLANC + 10*"█" + MUR + 5*"█" + RESET,
    MUR + 3*"█" + BLANC + 1*"█" + NAVY + 3*"█" + JAUNE + 3*"█" + NAVY + 3*"█" + BLANC + 1*"█" + MUR + 5*"█" + CADRE + 2*"█" + ECRAN + 3*"█" + VERT + 4*"█" + ECRAN + 13*"█" + BLANC + 16*"█" + ECRAN + 2*"█" + ROUGE + 2*"█" + BLANC + 1*"█" + ROUGE + 2*"█" + ECRAN + 6*"█" + BLANC + 4*"█" + ECRAN + 3*"█" + CADRE + 2*"█" + MUR + 4*"█" + BLANC + 1*"█" + NAVY + 6*"█" + JAUNE + 1*"█" + NAVY + 1*"█" + BLANC + 1*"█" + MUR + 5*"█" + RESET,
    MUR + 3*"█" + BLANC + 1*"█" + NAVY + 3*"█" + JAUNE + 3*"█" + NAVY + 3*"█" + BLANC + 1*"█" + MUR + 5*"█" + CADRE + 2*"█" + ECRAN + 3*"█" + VERT + 4*"█" + ECRAN + 11*"█" + ORANGE + 2*"█" + BLANC + 2*"█" + GRIS_CLAIR + 12*"█" + BLANC + 2*"█" + ORANGE + 2*"█" + ECRAN + 1*"█" + ROUGE + 3*"█" + ECRAN + 7*"█" + BLANC + 4*"█" + ECRAN + 3*"█" + CADRE + 2*"█" + MUR + 4*"█" + BLANC + 1*"█" + NAVY + 2*"█" + JAUNE + 1*"█" + NAVY + 5*"█" + BLANC + 1*"█" + MUR + 5*"█" + RESET,
    MUR + 3*"█" + BLANC + 1*"█" + NAVY + 2*"█" + ORANGE + 5*"█" + NAVY + 2*"█" + BLANC + 1*"█" + MUR + 5*"█" + CADRE + 2*"█" + ECRAN + 15*"█" + ORANGE + 5*"█" + BLANC + 2*"█" + GRIS_CLAIR + 9*"█" + BLANC + 5*"█" + ORANGE + 5*"█" + ECRAN + 15*"█" + CADRE + 2*"█" + MUR + 4*"█" + BLANC + 1*"█" + NAVY + 1*"█" + JAUNE + 1*"█" + NAVY + 6*"█" + BLANC + 1*"█" + MUR + 5*"█" + RESET,
    MUR + 3*"█" + BLANC + 1*"█" + NAVY + 4*"█" + ROUGE + 1*"█" + NAVY + 4*"█" + BLANC + 1*"█" + MUR + 5*"█" + CADRE + 2*"█" + ECRAN + 15*"█" + ORANGE + 2*"█" + JAUNE + 22*"█" + ORANGE + 2*"█" + ECRAN + 15*"█" + CADRE + 2*"█" + MUR + 4*"█" + BLANC + 1*"█" + NAVY + 5*"█" + JAUNE + 1*"█" + NAVY + 2*"█" + BLANC + 1*"█" + MUR + 5*"█" + RESET,
    MUR + 3*"█" + BLANC + 1*"█" + NAVY + 3*"█" + ROUGE + 3*"█" + NAVY + 3*"█" + BLANC + 1*"█" + MUR + 5*"█" + CADRE + 2*"█" + ECRAN + 3*"█" + JAUNE + 4*"█" + ECRAN + 8*"█" + JAUNE + 2*"█" + ORANGE + 2*"█" + JAUNE + 18*"█" + ORANGE + 2*"█" + JAUNE + 2*"█" + ECRAN + 8*"█" + ORANGE + 4*"█" + ECRAN + 3*"█" + CADRE + 2*"█" + MUR + 4*"█" + BLANC + 1*"█" + NAVY + 8*"█" + BLANC + 1*"█" + MUR + 5*"█" + RESET,
    MUR + 3*"█" + BLANC + 1*"█" + NAVY + 1*"█" + ROUGE + 7*"█" + NAVY + 1*"█" + BLANC + 1*"█" + MUR + 5*"█" + CADRE + 2*"█" + ECRAN + 3*"█" + JAUNE + 4*"█" + ECRAN + 8*"█" + JAUNE + 4*"█" + ORANGE + 2*"█" + JAUNE + 14*"█" + ORANGE + 2*"█" + JAUNE + 4*"█" + ECRAN + 8*"█" + ORANGE + 4*"█" + ECRAN + 3*"█" + CADRE + 2*"█" + MUR + 4*"█" + BLANC + 10*"█" + MUR + 5*"█" + RESET,
    MUR + 3*"█" + BLANC + 11*"█" + MUR + 5*"█" + CADRE + 2*"█" + ECRAN + 15*"█" + JAUNE + 6*"█" + ORANGE + 2*"█" + JAUNE + 10*"█" + ORANGE + 2*"█" + JAUNE + 6*"█" + ECRAN + 15*"█" + CADRE + 2*"█" + MUR + 19*"█" + RESET,
    MUR + 19*"█" + CADRE + 2*"█" + ECRAN + 15*"█" + JAUNE + 8*"█" + ORANGE + 2*"█" + JAUNE + 6*"█" + ORANGE + 2*"█" + JAUNE + 8*"█" + ECRAN + 15*"█" + CADRE + 2*"█" + MUR + 19*"█" + RESET,
    MUR + 19*"█" + CADRE + 2*"█" + ECRAN + 3*"█" + ROUGE + 4*"█" + ECRAN + 8*"█" + JAUNE + 10*"█" + ORANGE + 2*"█" + JAUNE + 2*"█" + ORANGE + 2*"█" + JAUNE + 10*"█" + ECRAN + 15*"█" + CADRE + 2*"█" + MUR + 19*"█" + RESET,
    MUR + 19*"█" + CADRE + 2*"█" + ECRAN + 3*"█" + ROUGE + 4*"█" + ECRAN + 8*"█" + JAUNE + 12*"█" + ORANGE + 2*"█" + JAUNE + 12*"█" + ECRAN + 15*"█" + CADRE + 2*"█" + MUR + 19*"█" + RESET,
    MUR + 19*"█" + CADRE + 2*"█" + ECRAN + 15*"█" + JAUNE + 26*"█" + ECRAN + 15*"█" + CADRE + 2*"█" + MUR + 19*"█" + RESET,
    MUR + 19*"█" + CADRE + 2*"█" + ECRAN + 56*"█" + CADRE + 2*"█" + MUR + 19*"█" + RESET,
    MUR + 19*"█" + CADRE + 2*"█" + ECRAN_FONCE + 1*"█" + BLANC + 2*"█" + ECRAN_FONCE + 48*"█" + BLANC + 4*"█" + ECRAN_FONCE + 1*"█" + CADRE + 2*"█" + MUR + 19*"█" + RESET,
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