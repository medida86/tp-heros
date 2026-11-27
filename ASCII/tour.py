RESET = "\033[0m"
CIEL = "\033[38;2;135;206;235m"
NUAGE = "\033[38;2;245;250;255m"
CLAIR = "\033[38;2;190;140;80m"
FER = "\033[38;2;120;80;45m"
SOMBRE = "\033[38;2;60;38;22m"
LOIN = "\033[38;2;85;55;35m"
HERBE = "\033[38;2;60;140;60m"
HERBE2 = "\033[38;2;45;115;50m"
ALLEE = "\033[38;2;215;190;140m"
DRAP_BLEU = "\033[38;2;0;35;149m"
DRAP_BLANC = "\033[38;2;255;255;255m"
DRAP_ROUGE = "\033[38;2;237;41;57m"

dessin = [
    CIEL + 49*"█" + FER + 1*"█" + DRAP_BLEU + 3*"█" + DRAP_BLANC + 3*"█" + DRAP_ROUGE + 3*"█" + CIEL + 39*"█" + RESET,
    CIEL + 48*"█" + CLAIR + 1*"█" + FER + 1*"█" + DRAP_BLEU + 3*"█" + DRAP_BLANC + 3*"█" + DRAP_ROUGE + 3*"█" + CIEL + 39*"█" + RESET,
    CIEL + 48*"█" + CLAIR + 1*"█" + FER + 1*"█" + DRAP_BLEU + 3*"█" + DRAP_BLANC + 3*"█" + DRAP_ROUGE + 3*"█" + CIEL + 39*"█" + RESET,
    CIEL + 48*"█" + CLAIR + 1*"█" + FER + 1*"█" + CIEL + 48*"█" + RESET,
    CIEL + 48*"█" + SOMBRE + 2*"█" + CIEL + 48*"█" + RESET,
    CIEL + 10*"█" + NUAGE + 10*"█" + CIEL + 27*"█" + CLAIR + 1*"█" + SOMBRE + 1*"█" + FER + 1*"█" + SOMBRE + 1*"█" + CIEL + 47*"█" + RESET,
    CIEL + 8*"█" + NUAGE + 14*"█" + CIEL + 24*"█" + SOMBRE + 6*"█" + CIEL + 46*"█" + RESET,
    CIEL + 11*"█" + NUAGE + 10*"█" + CIEL + 26*"█" + SOMBRE + 2*"█" + FER + 2*"█" + CIEL + 47*"█" + RESET,
    CIEL + 46*"█" + CLAIR + 1*"█" + SOMBRE + 2*"█" + FER + 3*"█" + CIEL + 24*"█" + NUAGE + 12*"█" + CIEL + 10*"█" + RESET,
    CIEL + 46*"█" + SOMBRE + 1*"█" + CLAIR + 1*"█" + SOMBRE + 2*"█" + FER + 1*"█" + SOMBRE + 1*"█" + CIEL + 22*"█" + NUAGE + 16*"█" + CIEL + 8*"█" + RESET,
    CIEL + 45*"█" + SOMBRE + 1*"█" + CLAIR + 2*"█" + SOMBRE + 1*"█" + FER + 1*"█" + SOMBRE + 1*"█" + FER + 2*"█" + CIEL + 24*"█" + NUAGE + 10*"█" + CIEL + 11*"█" + RESET,
    CIEL + 43*"█" + SOMBRE + 12*"█" + CIEL + 43*"█" + RESET,
    CIEL + 42*"█" + CLAIR + 7*"█" + FER + 7*"█" + CIEL + 42*"█" + RESET,
    CIEL + 43*"█" + SOMBRE + 1*"█" + CLAIR + 3*"█" + SOMBRE + 2*"█" + FER + 3*"█" + SOMBRE + 2*"█" + FER + 1*"█" + CIEL + 43*"█" + RESET,
    CIEL + 43*"█" + CLAIR + 1*"█" + SOMBRE + 1*"█" + CLAIR + 1*"█" + SOMBRE + 1*"█" + CLAIR + 1*"█" + SOMBRE + 2*"█" + FER + 1*"█" + SOMBRE + 1*"█" + FER + 2*"█" + SOMBRE + 1*"█" + CIEL + 43*"█" + RESET,
    CIEL + 18*"█" + NUAGE + 5*"█" + CIEL + 19*"█" + CLAIR + 3*"█" + SOMBRE + 1*"█" + CLAIR + 2*"█" + SOMBRE + 1*"█" + FER + 1*"█" + SOMBRE + 1*"█" + FER + 4*"█" + SOMBRE + 1*"█" + CIEL + 42*"█" + RESET,
    CIEL + 16*"█" + NUAGE + 9*"█" + CIEL + 16*"█" + SOMBRE + 1*"█" + CLAIR + 2*"█" + SOMBRE + 1*"█" + CLAIR + 1*"█" + SOMBRE + 1*"█" + CLAIR + 1*"█" + SOMBRE + 2*"█" + FER + 1*"█" + SOMBRE + 1*"█" + FER + 2*"█" + SOMBRE + 1*"█" + FER + 1*"█" + SOMBRE + 1*"█" + CIEL + 41*"█" + RESET,
    CIEL + 40*"█" + CLAIR + 2*"█" + SOMBRE + 2*"█" + CLAIR + 3*"█" + SOMBRE + 2*"█" + FER + 3*"█" + SOMBRE + 2*"█" + FER + 3*"█" + SOMBRE + 1*"█" + CIEL + 28*"█" + NUAGE + 4*"█" + CIEL + 8*"█" + RESET,
    CIEL + 39*"█" + CLAIR + 3*"█" + SOMBRE + 2*"█" + CLAIR + 3*"█" + SOMBRE + 2*"█" + FER + 3*"█" + SOMBRE + 2*"█" + FER + 3*"█" + SOMBRE + 2*"█" + CIEL + 25*"█" + NUAGE + 8*"█" + CIEL + 6*"█" + RESET,
    CIEL + 34*"█" + SOMBRE + 30*"█" + CIEL + 34*"█" + RESET,
    CIEL + 33*"█" + CLAIR + 16*"█" + FER + 16*"█" + CIEL + 33*"█" + RESET,
    CIEL + 35*"█" + CLAIR + 1*"█" + SOMBRE + 1*"█" + CLAIR + 2*"█" + SOMBRE + 1*"█" + CLAIR + 1*"█" + SOMBRE + 1*"█" + CLAIR + 2*"█" + SOMBRE + 1*"█" + CLAIR + 1*"█" + CIEL + 6*"█" + FER + 2*"█" + SOMBRE + 1*"█" + FER + 1*"█" + SOMBRE + 1*"█" + FER + 2*"█" + SOMBRE + 1*"█" + FER + 1*"█" + SOMBRE + 1*"█" + FER + 1*"█" + CIEL + 35*"█" + RESET,
    CIEL + 33*"█" + SOMBRE + 1*"█" + CLAIR + 3*"█" + SOMBRE + 2*"█" + CLAIR + 3*"█" + SOMBRE + 2*"█" + CIEL + 3*"█" + LOIN + 4*"█" + CIEL + 3*"█" + FER + 3*"█" + SOMBRE + 2*"█" + FER + 3*"█" + SOMBRE + 2*"█" + FER + 1*"█" + CIEL + 33*"█" + RESET,
    CIEL + 32*"█" + SOMBRE + 2*"█" + CLAIR + 3*"█" + SOMBRE + 2*"█" + CLAIR + 3*"█" + CIEL + 5*"█" + LOIN + 4*"█" + CIEL + 5*"█" + FER + 1*"█" + SOMBRE + 2*"█" + FER + 3*"█" + SOMBRE + 2*"█" + FER + 2*"█" + CIEL + 32*"█" + RESET,
    CIEL + 30*"█" + CLAIR + 1*"█" + SOMBRE + 1*"█" + CLAIR + 2*"█" + SOMBRE + 1*"█" + CLAIR + 1*"█" + SOMBRE + 1*"█" + CLAIR + 2*"█" + CIEL + 8*"█" + LOIN + 4*"█" + CIEL + 8*"█" + SOMBRE + 1*"█" + FER + 1*"█" + SOMBRE + 1*"█" + FER + 2*"█" + SOMBRE + 1*"█" + FER + 1*"█" + SOMBRE + 1*"█" + FER + 1*"█" + CIEL + 30*"█" + RESET,
    CIEL + 29*"█" + CLAIR + 1*"█" + SOMBRE + 1*"█" + CLAIR + 4*"█" + SOMBRE + 1*"█" + CLAIR + 1*"█" + CIEL + 10*"█" + LOIN + 4*"█" + CIEL + 10*"█" + FER + 4*"█" + SOMBRE + 1*"█" + FER + 3*"█" + CIEL + 29*"█" + RESET,
    CIEL + 27*"█" + CLAIR + 2*"█" + SOMBRE + 1*"█" + CLAIR + 1*"█" + SOMBRE + 1*"█" + CLAIR + 2*"█" + CIEL + 13*"█" + LOIN + 4*"█" + CIEL + 13*"█" + SOMBRE + 1*"█" + FER + 1*"█" + SOMBRE + 1*"█" + FER + 2*"█" + SOMBRE + 1*"█" + FER + 1*"█" + CIEL + 27*"█" + RESET,
    HERBE + 1*"█" + HERBE2 + 1*"█" + HERBE + 6*"█" + HERBE2 + 1*"█" + HERBE + 6*"█" + HERBE2 + 1*"█" + HERBE + 6*"█" + HERBE2 + 1*"█" + HERBE + 6*"█" + HERBE2 + 1*"█" + HERBE + 6*"█" + HERBE2 + 1*"█" + HERBE + 6*"█" + ALLEE + 12*"█" + HERBE + 2*"█" + HERBE2 + 1*"█" + HERBE + 6*"█" + HERBE2 + 1*"█" + HERBE + 6*"█" + HERBE2 + 1*"█" + HERBE + 6*"█" + HERBE2 + 1*"█" + HERBE + 6*"█" + HERBE2 + 1*"█" + HERBE + 6*"█" + HERBE2 + 1*"█" + HERBE + 5*"█" + RESET,
    HERBE2 + 1*"█" + HERBE + 6*"█" + HERBE2 + 1*"█" + HERBE + 6*"█" + HERBE2 + 1*"█" + HERBE + 6*"█" + HERBE2 + 1*"█" + HERBE + 6*"█" + HERBE2 + 1*"█" + HERBE + 6*"█" + HERBE2 + 1*"█" + HERBE + 3*"█" + ALLEE + 20*"█" + HERBE + 4*"█" + HERBE2 + 1*"█" + HERBE + 6*"█" + HERBE2 + 1*"█" + HERBE + 6*"█" + HERBE2 + 1*"█" + HERBE + 6*"█" + HERBE2 + 1*"█" + HERBE + 6*"█" + HERBE2 + 1*"█" + HERBE + 6*"█" + RESET,
    HERBE + 6*"█" + HERBE2 + 1*"█" + HERBE + 6*"█" + HERBE2 + 1*"█" + HERBE + 6*"█" + HERBE2 + 1*"█" + HERBE + 6*"█" + HERBE2 + 1*"█" + HERBE + 6*"█" + HERBE2 + 1*"█" + ALLEE + 28*"█" + HERBE + 6*"█" + HERBE2 + 1*"█" + HERBE + 6*"█" + HERBE2 + 1*"█" + HERBE + 6*"█" + HERBE2 + 1*"█" + HERBE + 6*"█" + HERBE2 + 1*"█" + HERBE + 6*"█" + HERBE2 + 1*"█" + RESET,
]