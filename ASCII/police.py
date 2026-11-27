RESET = "\033[0m"
NOIR = "\033[38;2;15;15;20m"
GRIS = "\033[38;2;70;75;85m"
ARGENT = "\033[38;2;170;175;185m"
BLANC = "\033[38;2;240;240;245m"
BLEU = "\033[38;2;20;70;255m"
BLEU2 = "\033[38;2;15;35;110m"
ROUGE = "\033[38;2;240;20;20m"
ROUGE2 = "\033[38;2;110;15;15m"
VITRE = "\033[38;2;110;190;235m"
JAUNE = "\033[38;2;255;240;120m"
JAUNE2 = "\033[38;2;150;135;55m"
JAUNE3 = "\033[38;2;75;68;30m"
ASPHALTE = "\033[38;2;45;45;50m"
CIEL = "\033[38;2;8;10;38m"
CIEL2 = "\033[38;2;22;24;70m"
ETOILE = "\033[38;2;255;255;255m"
LUNE = "\033[38;2;245;240;200m"
VILLE1 = "\033[38;2;42;44;95m"
VILLE2 = "\033[38;2;20;20;48m"
FENETRE = "\033[38;2;255;205;80m"
FENETRE2 = "\033[38;2;130;120;75m"
TROTTOIR = "\033[38;2;110;110;120m"

dessin = [
CIEL + 12*"█" + ETOILE + 1*"█" + CIEL + 34*"█" + ETOILE + 1*"█" + CIEL + 22*"█" + ETOILE
+ 1*"█" + CIEL + 27*"█" + RESET,
CIEL + 3*"█" + ETOILE + 1*"█" + CIEL + 54*"█" + ETOILE + 1*"█" + CIEL + 25*"█" + LUNE +
3*"█" + CIEL + 6*"█" + ETOILE + 1*"█" + CIEL + 4*"█" + RESET,
CIEL + 24*"█" + ETOILE + 1*"█" + CIEL + 29*"█" + VILLE1 + 10*"█" + CIEL + 15*"█" +
ETOILE + 1*"█" + CIEL + 1*"█" + LUNE + 9*"█" + CIEL + 8*"█" + RESET,
CIEL + 32*"█" + VILLE1 + 10*"█" + CIEL + 12*"█" + VILLE1 + 10*"█" + CIEL + 2*"█" +
ETOILE + 1*"█" + CIEL + 14*"█" + LUNE + 9*"█" + CIEL + 8*"█" + RESET,
CIEL + 8*"█" + ETOILE + 1*"█" + CIEL + 1*"█" + VILLE1 + 10*"█" + CIEL + 12*"█" + VILLE1
+ 10*"█" + CIEL + 12*"█" + VILLE1 + 2*"█" + FENETRE2 + 2*"█" + VILLE1 + 2*"█" + FENETRE2
+ 2*"█" + VILLE1 + 2*"█" + CIEL + 17*"█" + LUNE + 7*"█" + VILLE1 + 10*"█" + RESET,
CIEL + 10*"█" + VILLE1 + 10*"█" + CIEL + 8*"█" + BLEU2 + 5*"█" + VILLE1 + 1*"█" +
FENETRE2 + 2*"█" + VILLE1 + 2*"█" + FENETRE2 + 2*"█" + VILLE1 + 2*"█" + CIEL + 9*"█" +
ROUGE2 + 5*"█" + VILLE1 + 20*"█" + CIEL + 5*"█" + LUNE + 7*"█" + VILLE1 + 10*"█" + RESET,
CIEL + 10*"█" + VILLE1 + 10*"█" + CIEL + 12*"█" + VILLE1 + 3*"█" + NOIR + 14*"█" +
VILLE1 + 27*"█" + CIEL + 8*"█" + LUNE + 3*"█" + CIEL + 1*"█" + VILLE1 + 2*"█" + FENETRE2
+ 2*"█" + VILLE1 + 2*"█" + FENETRE2 + 2*"█" + VILLE1 + 2*"█" + RESET,
CIEL + 10*"█" + VILLE1 + 20*"█" + BLEU2 + 5*"█" + VILLE1 + 1*"█" + BLEU + 6*"█" + ROUGE
+ 6*"█" + VILLE1 + 1*"█" + ROUGE2 + 5*"█" + VILLE1 + 12*"█" + FENETRE2 + 2*"█" + VILLE1
+ 2*"█" + FENETRE2 + 2*"█" + VILLE1 + 26*"█" + RESET,
VILLE1 + 34*"█" + FENETRE2 + 2*"█" + BLEU + 6*"█" + ROUGE + 6*"█" + FENETRE2 + 2*"█" +
VILLE1 + 48*"█" + RESET,
VILLE1 + 12*"█" + FENETRE2 + 2*"█" + VILLE1 + 2*"█" + VILLE2 + 12*"█" + VILLE1 + 4*"█" +
BLANC + 4*"█" + NOIR + 12*"█" + BLANC + 7*"█" + VILLE1 + 19*"█" + VILLE2 + 12*"█" +
VILLE1 + 4*"█" + FENETRE2 + 2*"█" + VILLE1 + 2*"█" + FENETRE2 + 2*"█" + VILLE1 + 2*"█" +
RESET,
VILLE1 + 2*"█" + FENETRE2 + 2*"█" + VILLE1 + 2*"█" + FENETRE2 + 2*"█" + VILLE1 + 8*"█" +
VILLE2 + 12*"█" + VILLE1 + 2*"█" + BLANC + 3*"█" + VITRE + 11*"█" + BLANC + 2*"█" +
VITRE + 9*"█" + BLANC + 3*"█" + VILLE1 + 16*"█" + VILLE2 + 12*"█" + VILLE1 + 12*"█" +
RESET,
VILLE1 + 2*"█" + VILLE2 + 12*"█" + VILLE1 + 2*"█" + VILLE2 + 8*"█" + FENETRE + 2*"█" +
VILLE2 + 2*"█" + BLANC + 3*"█" + VITRE + 13*"█" + BLANC + 2*"█" + VITRE + 12*"█" + BLANC
+ 3*"█" + VILLE2 + 11*"█" + VILLE1 + 2*"█" + VILLE2 + 8*"█" + FENETRE + 2*"█" + VILLE2 +
2*"█" + VILLE1 + 11*"█" + JAUNE3 + 1*"█" + RESET,
VILLE1 + 2*"█" + VILLE2 + 12*"█" + VILLE1 + 2*"█" + VILLE2 + 10*"█" + BLANC + 3*"█" +
VITRE + 15*"█" + BLANC + 2*"█" + VITRE + 15*"█" + BLANC + 3*"█" + VILLE2 + 8*"█" +
VILLE1 + 2*"█" + VILLE2 + 12*"█" + VILLE1 + 2*"█" + VILLE2 + 6*"█" + JAUNE3 + 4*"█" +
RESET,
VILLE1 + 2*"█" + VILLE2 + 2*"█" + FENETRE + 2*"█" + VILLE2 + 8*"█" + VILLE1 + 2*"█" +
VILLE2 + 9*"█" + BLANC + 3*"█" + VITRE + 16*"█" + BLANC + 2*"█" + VITRE + 18*"█" + BLANC
+ 3*"█" + VILLE2 + 5*"█" + VILLE1 + 2*"█" + VILLE2 + 12*"█" + VILLE1 + 2*"█" + VILLE2 +
3*"█" + JAUNE3 + 7*"█" + RESET,
VILLE1 + 2*"█" + VILLE2 + 12*"█" + VILLE1 + 2*"█" + VILLE2 + 2*"█" + FENETRE + 2*"█" +
VILLE2 + 4*"█" + BLANC + 3*"█" + VITRE + 17*"█" + BLANC + 2*"█" + VITRE + 22*"█" + BLANC
+ 3*"█" + VILLE2 + 1*"█" + VILLE1 + 2*"█" + VILLE2 + 2*"█" + FENETRE + 2*"█" + VILLE2 +
8*"█" + VILLE1 + 1*"█" + JAUNE2 + 3*"█" + JAUNE3 + 8*"█" + RESET,
VILLE1 + 2*"█" + VILLE2 + 5*"█" + BLANC + 36*"█" + NOIR + 1*"█" + BLANC + 33*"█" + JAUNE
+ 2*"█" + VILLE2 + 5*"█" + JAUNE2 + 6*"█" + JAUNE3 + 8*"█" + RESET,
VILLE1 + 2*"█" + VILLE2 + 4*"█" + ROUGE + 2*"█" + BLANC + 35*"█" + NOIR + 1*"█" + BLANC
+ 33*"█" + JAUNE + 7*"█" + JAUNE2 + 6*"█" + JAUNE3 + 8*"█" + RESET,
VILLE1 + 2*"█" + VILLE2 + 4*"█" + ROUGE + 2*"█" + BLANC + 35*"█" + NOIR + 1*"█" + BLANC
+ 33*"█" + JAUNE + 7*"█" + JAUNE2 + 6*"█" + JAUNE3 + 8*"█" + RESET,
VILLE1 + 2*"█" + VILLE2 + 4*"█" + BLEU + 37*"█" + NOIR + 1*"█" + BLEU + 36*"█" + JAUNE +
4*"█" + JAUNE2 + 6*"█" + JAUNE3 + 8*"█" + RESET,
VILLE1 + 2*"█" + VILLE2 + 4*"█" + GRIS + 14*"█" + NOIR + 5*"█" + GRIS + 35*"█" + NOIR +
5*"█" + GRIS + 15*"█" + VILLE2 + 4*"█" + JAUNE2 + 6*"█" + JAUNE3 + 8*"█" + RESET,
VILLE1 + 2*"█" + VILLE2 + 4*"█" + GRIS + 11*"█" + NOIR + 4*"█" + ARGENT + 3*"█" + NOIR +
4*"█" + GRIS + 29*"█" + NOIR + 4*"█" + ARGENT + 3*"█" + NOIR + 4*"█" + GRIS + 12*"█" +
VILLE2 + 6*"█" + VILLE1 + 1*"█" + JAUNE2 + 3*"█" + JAUNE3 + 8*"█" + RESET,
VILLE1 + 2*"█" + VILLE2 + 5*"█" + GRIS + 9*"█" + NOIR + 3*"█" + ARGENT + 7*"█" + NOIR +
3*"█" + GRIS + 27*"█" + NOIR + 3*"█" + ARGENT + 7*"█" + NOIR + 3*"█" + GRIS + 10*"█" +
VILLE2 + 7*"█" + VILLE1 + 2*"█" + VILLE2 + 3*"█" + JAUNE3 + 7*"█" + RESET,
VILLE1 + 2*"█" + VILLE2 + 2*"█" + FENETRE + 2*"█" + VILLE2 + 1*"█" + FENETRE + 2*"█" +
VILLE2 + 5*"█" + VILLE1 + 1*"█" + NOIR + 3*"█" + ARGENT + 3*"█" + NOIR + 3*"█" + ARGENT
+ 3*"█" + NOIR + 3*"█" + VILLE2 + 10*"█" + VILLE1 + 6*"█" + VILLE2 + 9*"█" + NOIR +
3*"█" + ARGENT + 3*"█" + NOIR + 3*"█" + ARGENT + 3*"█" + NOIR + 3*"█" + VILLE2 + 2*"█" +
VILLE1 + 2*"█" + VILLE2 + 12*"█" + VILLE1 + 2*"█" + VILLE2 + 6*"█" + JAUNE3 + 4*"█" +
RESET,
VILLE1 + 2*"█" + VILLE2 + 12*"█" + VILLE1 + 2*"█" + NOIR + 3*"█" + ARGENT + 7*"█" + NOIR
+ 3*"█" + VILLE1 + 1*"█" + VILLE2 + 5*"█" + FENETRE + 2*"█" + VILLE2 + 3*"█" + VILLE1 +
4*"█" + FENETRE2 + 2*"█" + VILLE2 + 10*"█" + NOIR + 3*"█" + ARGENT + 7*"█" + NOIR +
3*"█" + VILLE2 + 3*"█" + VILLE1 + 2*"█" + VILLE2 + 2*"█" + FENETRE + 2*"█" + VILLE2 +
1*"█" + FENETRE + 2*"█" + VILLE2 + 5*"█" + VILLE1 + 2*"█" + VILLE2 + 5*"█" + FENETRE +
2*"█" + VILLE2 + 2*"█" + JAUNE3 + 1*"█" + RESET,
VILLE1 + 2*"█" + VILLE2 + 12*"█" + VILLE1 + 2*"█" + VILLE2 + 1*"█" + NOIR + 4*"█" +
ARGENT + 3*"█" + NOIR + 4*"█" + VILLE1 + 2*"█" + VILLE2 + 10*"█" + VILLE1 + 6*"█" +
VILLE2 + 8*"█" + FENETRE + 2*"█" + VILLE2 + 1*"█" + NOIR + 4*"█" + ARGENT + 3*"█" + NOIR
+ 4*"█" + VILLE2 + 4*"█" + VILLE1 + 2*"█" + VILLE2 + 12*"█" + VILLE1 + 2*"█" + VILLE2 +
10*"█" + RESET,
TROTTOIR + 20*"█" + NOIR + 5*"█" + TROTTOIR + 35*"█" + NOIR + 5*"█" + TROTTOIR + 33*"█"
+ RESET,
ASPHALTE + 98*"█" + RESET,
ASPHALTE + 98*"█" + RESET,
JAUNE + 8*"█" + ASPHALTE + 6*"█" + JAUNE + 8*"█" + ASPHALTE + 6*"█" + JAUNE + 8*"█" +
ASPHALTE + 6*"█" + JAUNE + 8*"█" + ASPHALTE + 6*"█" + JAUNE + 8*"█" + ASPHALTE + 6*"█" +
JAUNE + 8*"█" + ASPHALTE + 6*"█" + JAUNE + 8*"█" + ASPHALTE + 6*"█" + RESET,
ASPHALTE + 98*"█" + RESET,
]