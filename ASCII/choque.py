RESET = "\033[0m"
FORET = "\033[38;2;15;75;40m"
NAVY = "\033[38;2;25;35;95m"
MARINE = "\033[38;2;8;8;45m"
BLANC = "\033[38;2;255;255;255m"
PEAU = "\033[38;2;255;205;165m"
OMBRE = "\033[38;2;225;160;120m"
CHEVEUX = "\033[38;2;75;45;25m"
NOIR = "\033[38;2;0;0;0m"
ROUGE = "\033[38;2;235;40;40m"
BORDEAUX = "\033[38;2;150;20;40m"
CYAN = "\033[38;2;120;200;255m"
GRIS = "\033[38;2;60;62;75m"
ECRAN = "\033[38;2;205;220;240m"
BLEU = "\033[38;2;45;110;225m"
ARGENT = "\033[38;2;170;175;190m"
TEXTE = "\033[38;2;150;160;185m"

dessin = [
    FORET + 23*"█" + CHEVEUX + 11*"█" + FORET + 64*"█" + RESET,
    FORET + 19*"█" + CHEVEUX + 19*"█" + FORET + 60*"█" + RESET,
    FORET + 17*"█" + CHEVEUX + 23*"█" + FORET + 58*"█" + RESET,
    FORET + 15*"█" + CHEVEUX + 27*"█" + FORET + 18*"█" + GRIS + 38*"█" + RESET,
    FORET + 13*"█" + CHEVEUX + 31*"█" + FORET + 16*"█" + GRIS + 38*"█" + RESET,
    FORET + 15*"█" + PEAU + 5*"█" + NOIR + 6*"█" + PEAU + 5*"█" + NOIR + 6*"█" + PEAU + 5*"█" + FORET + 18*"█" + GRIS + 2*"█" + BLEU + 2*"█" + BLANC + 15*"█" + BLEU + 17*"█" + GRIS + 2*"█" + RESET,
    FORET + 14*"█" + PEAU + 2*"█" + NOIR + 4*"█" + PEAU + 17*"█" + NOIR + 4*"█" + PEAU + 2*"█" + FORET + 17*"█" + GRIS + 2*"█" + BLEU + 34*"█" + GRIS + 2*"█" + RESET,
    FORET + 12*"█" + PEAU + 33*"█" + FORET + 15*"█" + GRIS + 2*"█" + ECRAN + 34*"█" + GRIS + 2*"█" + RESET,
    FORET + 12*"█" + PEAU + 4*"█" + BLANC + 6*"█" + NOIR + 2*"█" + BLANC + 1*"█" + PEAU + 7*"█" + BLANC + 6*"█" + NOIR + 2*"█" + BLANC + 1*"█" + PEAU + 4*"█" + FORET + 15*"█" + GRIS + 2*"█" + ECRAN + 23*"█" + ROUGE + 3*"█" + BLANC + 1*"█" + ROUGE + 3*"█" + ECRAN + 4*"█" + GRIS + 2*"█" + RESET,
    FORET + 8*"█" + PEAU + 7*"█" + BLANC + 7*"█" + NOIR + 2*"█" + BLANC + 2*"█" + PEAU + 5*"█" + BLANC + 7*"█" + NOIR + 2*"█" + BLANC + 2*"█" + PEAU + 7*"█" + FORET + 11*"█" + GRIS + 2*"█" + ECRAN + 22*"█" + ROUGE + 4*"█" + BLANC + 1*"█" + ROUGE + 4*"█" + ECRAN + 3*"█" + GRIS + 2*"█" + RESET,
    FORET + 8*"█" + PEAU + 1*"█" + OMBRE + 1*"█" + PEAU + 6*"█" + BLANC + 9*"█" + PEAU + 7*"█" + BLANC + 9*"█" + PEAU + 6*"█" + OMBRE + 1*"█" + PEAU + 1*"█" + FORET + 11*"█" + GRIS + 2*"█" + ECRAN + 21*"█" + ROUGE + 5*"█" + BLANC + 1*"█" + ROUGE + 5*"█" + ECRAN + 2*"█" + GRIS + 2*"█" + RESET,
    FORET + 8*"█" + PEAU + 1*"█" + OMBRE + 1*"█" + PEAU + 18*"█" + OMBRE + 1*"█" + PEAU + 18*"█" + OMBRE + 1*"█" + PEAU + 1*"█" + FORET + 11*"█" + GRIS + 2*"█" + ECRAN + 8*"█" + ARGENT + 14*"█" + ROUGE + 9*"█" + ECRAN + 3*"█" + GRIS + 2*"█" + RESET,
    FORET + 8*"█" + PEAU + 1*"█" + OMBRE + 1*"█" + PEAU + 18*"█" + OMBRE + 1*"█" + PEAU + 14*"█" + CYAN + 1*"█" + PEAU + 3*"█" + OMBRE + 1*"█" + PEAU + 1*"█" + FORET + 11*"█" + GRIS + 2*"█" + ECRAN + 8*"█" + ARGENT + 3*"█" + BLANC + 12*"█" + ROUGE + 3*"█" + BLANC + 1*"█" + ROUGE + 3*"█" + ECRAN + 4*"█" + GRIS + 2*"█" + RESET,
    FORET + 8*"█" + PEAU + 18*"█" + OMBRE + 5*"█" + PEAU + 11*"█" + CYAN + 3*"█" + PEAU + 4*"█" + FORET + 11*"█" + GRIS + 2*"█" + ECRAN + 8*"█" + ARGENT + 1*"█" + BLANC + 2*"█" + ARGENT + 2*"█" + BLANC + 8*"█" + ARGENT + 2*"█" + BLANC + 2*"█" + ARGENT + 1*"█" + ECRAN + 8*"█" + GRIS + 2*"█" + RESET,
    FORET + 12*"█" + PEAU + 13*"█" + BLANC + 7*"█" + PEAU + 10*"█" + CYAN + 3*"█" + FORET + 15*"█" + GRIS + 2*"█" + ECRAN + 8*"█" + ARGENT + 1*"█" + BLANC + 4*"█" + ARGENT + 2*"█" + BLANC + 4*"█" + ARGENT + 2*"█" + BLANC + 4*"█" + ARGENT + 1*"█" + ECRAN + 8*"█" + GRIS + 2*"█" + RESET,
    FORET + 12*"█" + PEAU + 12*"█" + NOIR + 9*"█" + PEAU + 10*"█" + CYAN + 1*"█" + PEAU + 1*"█" + FORET + 15*"█" + GRIS + 2*"█" + ECRAN + 8*"█" + ARGENT + 1*"█" + BLANC + 6*"█" + ARGENT + 4*"█" + BLANC + 6*"█" + ARGENT + 1*"█" + ECRAN + 8*"█" + GRIS + 2*"█" + RESET,
    FORET + 14*"█" + PEAU + 9*"█" + NOIR + 11*"█" + PEAU + 9*"█" + FORET + 17*"█" + GRIS + 2*"█" + ECRAN + 8*"█" + ARGENT + 1*"█" + BLANC + 16*"█" + ARGENT + 1*"█" + ECRAN + 8*"█" + GRIS + 2*"█" + RESET,
    FORET + 15*"█" + PEAU + 9*"█" + NOIR + 2*"█" + BORDEAUX + 5*"█" + NOIR + 2*"█" + PEAU + 9*"█" + FORET + 18*"█" + GRIS + 2*"█" + ECRAN + 8*"█" + ARGENT + 1*"█" + BLANC + 16*"█" + ARGENT + 1*"█" + ECRAN + 8*"█" + GRIS + 2*"█" + RESET,
    FORET + 17*"█" + PEAU + 8*"█" + NOIR + 1*"█" + BORDEAUX + 5*"█" + NOIR + 1*"█" + PEAU + 8*"█" + FORET + 20*"█" + GRIS + 2*"█" + ECRAN + 8*"█" + ARGENT + 18*"█" + ECRAN + 8*"█" + GRIS + 2*"█" + RESET,
    FORET + 20*"█" + PEAU + 17*"█" + FORET + 23*"█" + GRIS + 2*"█" + ECRAN + 34*"█" + GRIS + 2*"█" + RESET,
    FORET + 22*"█" + OMBRE + 6*"█" + PEAU + 1*"█" + OMBRE + 6*"█" + FORET + 25*"█" + GRIS + 2*"█" + ECRAN + 4*"█" + TEXTE + 25*"█" + ECRAN + 5*"█" + GRIS + 2*"█" + RESET,
    FORET + 16*"█" + NAVY + 3*"█" + MARINE + 2*"█" + BLANC + 15*"█" + MARINE + 2*"█" + NAVY + 3*"█" + FORET + 19*"█" + GRIS + 2*"█" + ECRAN + 34*"█" + GRIS + 2*"█" + RESET,
    FORET + 13*"█" + NAVY + 8*"█" + MARINE + 2*"█" + BLANC + 3*"█" + ROUGE + 5*"█" + BLANC + 3*"█" + MARINE + 2*"█" + NAVY + 8*"█" + FORET + 16*"█" + GRIS + 2*"█" + ECRAN + 4*"█" + TEXTE + 15*"█" + ECRAN + 15*"█" + GRIS + 2*"█" + RESET,
    FORET + 9*"█" + NAVY + 13*"█" + MARINE + 2*"█" + BLANC + 2*"█" + ROUGE + 5*"█" + BLANC + 2*"█" + MARINE + 2*"█" + NAVY + 13*"█" + FORET + 12*"█" + GRIS + 2*"█" + ECRAN + 34*"█" + GRIS + 2*"█" + RESET,
    FORET + 7*"█" + NAVY + 16*"█" + MARINE + 2*"█" + BLANC + 2*"█" + ROUGE + 3*"█" + BLANC + 2*"█" + MARINE + 2*"█" + NAVY + 16*"█" + FORET + 10*"█" + GRIS + 38*"█" + RESET,
    FORET + 4*"█" + NAVY + 20*"█" + MARINE + 2*"█" + BLANC + 1*"█" + ROUGE + 3*"█" + BLANC + 1*"█" + MARINE + 2*"█" + NAVY + 20*"█" + FORET + 7*"█" + GRIS + 38*"█" + RESET,
    FORET + 3*"█" + NAVY + 22*"█" + MARINE + 2*"█" + ROUGE + 3*"█" + MARINE + 2*"█" + NAVY + 22*"█" + FORET + 4*"█" + ARGENT + 40*"█" + RESET,
    FORET + 1*"█" + NAVY + 25*"█" + MARINE + 1*"█" + ROUGE + 3*"█" + MARINE + 1*"█" + NAVY + 25*"█" + FORET + 4*"█" + GRIS + 38*"█" + RESET,
    FORET + 1*"█" + NAVY + 26*"█" + ROUGE + 3*"█" + NAVY + 26*"█" + FORET + 42*"█" + RESET,
    NAVY + 27*"█" + ROUGE + 3*"█" + NAVY + 27*"█" + FORET + 41*"█" + RESET,
]