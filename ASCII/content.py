RESET = "\033[0m"
MUR = "\033[38;2;165;190;235m"
SOL = "\033[38;2;150;105;65m"
PLINTHE = "\033[38;2;105;70;40m"
CIEL = "\033[38;2;135;206;250m"
BLANC = "\033[38;2;245;245;245m"
PEAU = "\033[38;2;255;205;160m"
PEAU2 = "\033[38;2;225;160;115m"
CHEVEUX = "\033[38;2;60;35;20m"
NOIR = "\033[38;2;15;15;15m"
ROSE = "\033[38;2;255;130;150m"
BOUCHE = "\033[38;2;200;30;50m"
CHEMISE = "\033[38;2;40;120;220m"
PANTALON = "\033[38;2;50;50;95m"
CHAUSSURE = "\033[38;2;30;30;30m"
JAUNE = "\033[38;2;255;215;40m"
ROUGE = "\033[38;2;235;60;60m"
VERT = "\033[38;2;60;200;90m"
VIOLET = "\033[38;2;170;80;220m"
ORANGE = "\033[38;2;255;140;30m"
LIT = "\033[38;2;190;60;100m"
BOIS = "\033[38;2;130;85;50m"

dessin = [
BLANC + 5*"█" + MUR + 9*"█" + BLANC + 9*"█" + MUR + 9*"█" + BLANC + 4*"█" + MUR + 13*"█" +
VIOLET + 1*"█" + MUR + 5*"█" + ORANGE + 1*"█" + MUR + 12*"█" + BLANC + 9*"█" + MUR +
9*"█" + BLANC + 9*"█" + MUR + 3*"█" + RESET,
MUR + 1*"█" + ROUGE + 1*"█" + MUR + 2*"█" + JAUNE + 1*"█" + BLANC + 4*"█" + MUR + 1*"█" +
BLANC + 4*"█" + MUR + 2*"█" + ROUGE + 1*"█" + MUR + 2*"█" + JAUNE + 1*"█" + MUR + 2*"█" +
VERT + 1*"█" + BLANC + 4*"█" + MUR + 1*"█" + BLANC + 4*"█" + MUR + 2*"█" + JAUNE + 1*"█" +
MUR + 4*"█" + BLANC + 1*"█" + MUR + 8*"█" + JAUNE + 1*"█" + ROUGE + 2*"█" + MUR + 13*"█" +
BLANC + 4*"█" + MUR + 2*"█" + VIOLET + 1*"█" + MUR + 2*"█" + ORANGE + 1*"█" + MUR +
2*"█" + ROUGE + 1*"█" + BLANC + 4*"█" + MUR + 1*"█" + BLANC + 4*"█" + MUR + 2*"█" +
ORANGE + 1*"█" + MUR + 2*"█" + ROUGE + 1*"█" + MUR + 2*"█" + JAUNE + 1*"█" + BLANC +
3*"█" + RESET,
MUR + 1*"█" + ROUGE + 1*"█" + MUR + 5*"█" + VERT + 1*"█" + MUR + 1*"█" + BLANC + 1*"█" +
VIOLET + 1*"█" + MUR + 2*"█" + ORANGE + 1*"█" + MUR + 5*"█" + JAUNE + 1*"█" + MUR +
5*"█" + VIOLET + 1*"█" + MUR + 1*"█" + BLANC + 1*"█" + ORANGE + 1*"█" + MUR + 2*"█" +
ROUGE + 1*"█" + MUR + 12*"█" + VERT + 1*"█" + MUR + 2*"█" + JAUNE + 1*"█" + ROUGE +
2*"█" + JAUNE + 2*"█" + MUR + 2*"█" + CIEL + 1*"█" + MUR + 8*"█" + BLANC + 1*"█" + JAUNE +
1*"█" + MUR + 2*"█" + VERT + 1*"█" + MUR + 5*"█" + ORANGE + 1*"█" + MUR + 5*"█" + JAUNE +
1*"█" + MUR + 1*"█" + BLANC + 1*"█" + VERT + 1*"█" + MUR + 2*"█" + VIOLET + 1*"█" + MUR +
5*"█" + ROUGE + 1*"█" + MUR + 5*"█" + VERT + 1*"█" + RESET,
MUR + 7*"█" + VERT + 1*"█" + MUR + 5*"█" + ORANGE + 1*"█" + MUR + 11*"█" + VIOLET +
1*"█" + MUR + 5*"█" + ROUGE + 1*"█" + MUR + 14*"█" + JAUNE + 1*"█" + ROUGE + 2*"█" +
JAUNE + 2*"█" + ROUGE + 2*"█" + MUR + 14*"█" + VERT + 1*"█" + MUR + 11*"█" + JAUNE +
1*"█" + MUR + 5*"█" + VIOLET + 1*"█" + MUR + 11*"█" + VERT + 1*"█" + RESET,
MUR + 2*"█" + JAUNE + 1*"█" + MUR + 10*"█" + VERT + 1*"█" + MUR + 2*"█" + JAUNE + 1*"█" +
MUR + 28*"█" + JAUNE + 1*"█" + ROUGE + 2*"█" + JAUNE + 2*"█" + ROUGE + 2*"█" + JAUNE +
2*"█" + MUR + 4*"█" + ROSE + 1*"█" + MUR + 2*"█" + ORANGE + 1*"█" + ROUGE + 1*"█" + MUR +
14*"█" + VERT + 1*"█" + JAUNE + 1*"█" + MUR + 19*"█" + RESET,
MUR + 16*"█" + ROSE + 1*"█" + MUR + 14*"█" + ORANGE + 1*"█" + ROUGE + 1*"█" + MUR +
2*"█" + VERT + 1*"█" + MUR + 7*"█" + CHEVEUX + 13*"█" + MUR + 15*"█" + ROSE + 1*"█" +
VIOLET + 1*"█" + MUR + 1*"█" + VIOLET + 1*"█" + MUR + 8*"█" + JAUNE + 1*"█" + MUR +
14*"█" + RESET,
MUR + 4*"█" + BLANC + 1*"█" + MUR + 3*"█" + ORANGE + 1*"█" + BLANC + 10*"█" + VERT +
1*"█" + BLANC + 5*"█" + MUR + 8*"█" + VIOLET + 1*"█" + MUR + 7*"█" + CHEVEUX + 3*"█" +
PEAU + 11*"█" + CHEVEUX + 3*"█" + MUR + 7*"█" + JAUNE + 1*"█" + MUR + 11*"█" + JAUNE +
1*"█" + MUR + 4*"█" + JAUNE + 1*"█" + MUR + 2*"█" + ROSE + 1*"█" + MUR + 11*"█" + CIEL +
1*"█" + RESET,
MUR + 8*"█" + BLANC + 1*"█" + CIEL + 7*"█" + BLANC + 1*"█" + CIEL + 1*"█" + ROSE + 1*"█" +
CIEL + 5*"█" + BLANC + 1*"█" + MUR + 4*"█" + JAUNE + 1*"█" + MUR + 10*"█" + CHEVEUX +
1*"█" + PEAU + 17*"█" + CHEVEUX + 1*"█" + MUR + 1*"█" + JAUNE + 1*"█" + MUR + 7*"█" +
ROSE + 1*"█" + MUR + 9*"█" + CIEL + 1*"█" + MUR + 19*"█" + RESET,
MUR + 8*"█" + BLANC + 1*"█" + CIEL + 7*"█" + BLANC + 1*"█" + CIEL + 7*"█" + BLANC +
1*"█" + MUR + 2*"█" + PEAU + 3*"█" + MUR + 5*"█" + JAUNE + 1*"█" + MUR + 3*"█" + PEAU +
4*"█" + NOIR + 2*"█" + PEAU + 8*"█" + NOIR + 2*"█" + PEAU + 5*"█" + MUR + 4*"█" + VERT +
1*"█" + MUR + 4*"█" + PEAU + 3*"█" + MUR + 7*"█" + ROUGE + 1*"█" + MUR + 18*"█" + RESET,
MUR + 6*"█" + VIOLET + 1*"█" + MUR + 1*"█" + BLANC + 1*"█" + CIEL + 5*"█" + ORANGE +
1*"█" + CIEL + 1*"█" + BLANC + 1*"█" + CIEL + 7*"█" + BLANC + 1*"█" + MUR + 2*"█" + PEAU +
3*"█" + MUR + 9*"█" + PEAU + 3*"█" + NOIR + 1*"█" + PEAU + 2*"█" + NOIR + 1*"█" + PEAU +
6*"█" + NOIR + 1*"█" + PEAU + 2*"█" + NOIR + 1*"█" + PEAU + 4*"█" + MUR + 1*"█" + BLANC +
1*"█" + MUR + 7*"█" + PEAU + 3*"█" + MUR + 16*"█" + ROUGE + 1*"█" + MUR + 3*"█" + VERT +
1*"█" + MUR + 5*"█" + RESET,
MUR + 7*"█" + JAUNE + 1*"█" + BLANC + 1*"█" + CIEL + 7*"█" + BLANC + 1*"█" + CIEL +
7*"█" + BLANC + 1*"█" + MUR + 2*"█" + PEAU + 5*"█" + MUR + 1*"█" + ROSE + 1*"█" + MUR +
4*"█" + CHEVEUX + 1*"█" + PEAU + 10*"█" + PEAU2 + 1*"█" + PEAU + 10*"█" + CHEVEUX +
1*"█" + MUR + 6*"█" + PEAU + 5*"█" + MUR + 26*"█" + RESET,
MUR + 6*"█" + ROUGE + 1*"█" + MUR + 1*"█" + BLANC + 5*"█" + CIEL + 1*"█" + BLANC + 5*"█" +
VIOLET + 1*"█" + BLANC + 5*"█" + MUR + 3*"█" + PEAU + 5*"█" + MUR + 6*"█" + PEAU + 1*"█" +
ROSE + 2*"█" + PEAU + 15*"█" + ROSE + 2*"█" + PEAU + 1*"█" + MUR + 4*"█" + ORANGE +
1*"█" + MUR + 1*"█" + PEAU + 5*"█" + MUR + 5*"█" + ORANGE + 1*"█" + MUR + 4*"█" + VIOLET +
1*"█" + MUR + 3*"█" + VERT + 1*"█" + MUR + 12*"█" + RESET,
ROSE + 1*"█" + MUR + 2*"█" + VIOLET + 1*"█" + MUR + 4*"█" + JAUNE + 1*"█" + CIEL + 7*"█" +
BLANC + 1*"█" + CIEL + 1*"█" + VERT + 1*"█" + CIEL + 4*"█" + VERT + 1*"█" + BLANC +
1*"█" + MUR + 5*"█" + PEAU + 4*"█" + MUR + 5*"█" + PEAU + 4*"█" + BOUCHE + 1*"█" + BLANC +
11*"█" + BOUCHE + 1*"█" + PEAU + 4*"█" + MUR + 5*"█" + PEAU + 4*"█" + MUR + 19*"█" +
CIEL + 1*"█" + MUR + 5*"█" + CIEL + 1*"█" + MUR + 3*"█" + RESET,
MUR + 8*"█" + BLANC + 1*"█" + CIEL + 7*"█" + BLANC + 1*"█" + CIEL + 7*"█" + BLANC +
1*"█" + MUR + 6*"█" + PEAU + 4*"█" + MUR + 5*"█" + PEAU + 4*"█" + BOUCHE + 11*"█" + PEAU +
4*"█" + MUR + 2*"█" + JAUNE + 1*"█" + MUR + 2*"█" + PEAU + 4*"█" + MUR + 5*"█" + VERT +
1*"█" + MUR + 11*"█" + JAUNE + 1*"█" + MUR + 12*"█" + RESET,
MUR + 8*"█" + BLANC + 1*"█" + CIEL + 5*"█" + ROUGE + 1*"█" + CIEL + 1*"█" + BLANC +
1*"█" + CIEL + 7*"█" + BLANC + 1*"█" + VIOLET + 1*"█" + MUR + 3*"█" + VIOLET + 1*"█" +
MUR + 2*"█" + PEAU + 4*"█" + MUR + 5*"█" + PEAU + 5*"█" + BOUCHE + 7*"█" + PEAU + 5*"█" +
MUR + 5*"█" + PEAU + 4*"█" + MUR + 14*"█" + JAUNE + 1*"█" + MUR + 6*"█" + BOIS + 1*"█" +
JAUNE + 1*"█" + BOIS + 6*"█" + VERT + 1*"█" + BOIS + 1*"█" + RESET,
MUR + 8*"█" + BLANC + 1*"█" + CIEL + 7*"█" + BLANC + 1*"█" + CIEL + 7*"█" + BLANC +
1*"█" + MUR + 2*"█" + VERT + 1*"█" + MUR + 5*"█" + PEAU + 3*"█" + CHEMISE + 1*"█" + MUR +
6*"█" + PEAU + 13*"█" + MUR + 3*"█" + VERT + 1*"█" + MUR + 2*"█" + CHEMISE + 1*"█" +
PEAU + 3*"█" + VERT + 1*"█" + MUR + 17*"█" + VERT + 1*"█" + ROUGE + 1*"█" + MUR + 2*"█" +
BOIS + 4*"█" + ROUGE + 1*"█" + BOIS + 5*"█" + RESET,
MUR + 8*"█" + BLANC + 17*"█" + MUR + 5*"█" + VIOLET + 1*"█" + MUR + 3*"█" + CHEMISE +
4*"█" + MUR + 7*"█" + ROUGE + 1*"█" + MUR + 1*"█" + VIOLET + 1*"█" + MUR + 1*"█" + PEAU +
1*"█" + BLANC + 1*"█" + MUR + 10*"█" + CHEMISE + 4*"█" + MUR + 22*"█" + VIOLET + 1*"█" +
BOIS + 4*"█" + CIEL + 1*"█" + BOIS + 5*"█" + RESET,
MUR + 17*"█" + JAUNE + 1*"█" + ROSE + 1*"█" + MUR + 16*"█" + CHEMISE + 4*"█" + MUR +
4*"█" + VIOLET + 1*"█" + MUR + 2*"█" + PEAU + 7*"█" + MUR + 7*"█" + CHEMISE + 4*"█" +
MUR + 1*"█" + VERT + 1*"█" + MUR + 4*"█" + ORANGE + 1*"█" + MUR + 9*"█" + BLANC + 11*"█" +
BOIS + 7*"█" + RESET,
MUR + 5*"█" + VERT + 1*"█" + MUR + 20*"█" + VERT + 1*"█" + MUR + 9*"█" + CHEMISE + 4*"█" +
CIEL + 1*"█" + MUR + 5*"█" + PEAU + 7*"█" + MUR + 6*"█" + CHEMISE + 4*"█" + MUR + 1*"█" +
ROUGE + 1*"█" + MUR + 10*"█" + VERT + 1*"█" + MUR + 4*"█" + BLANC + 10*"█" + BOIS +
3*"█" + ORANGE + 1*"█" + BOIS + 4*"█" + RESET,
MUR + 1*"█" + VERT + 1*"█" + MUR + 11*"█" + BLANC + 1*"█" + MUR + 23*"█" + CHEMISE +
25*"█" + MUR + 3*"█" + VIOLET + 1*"█" + MUR + 1*"█" + ROSE + 1*"█" + LIT + 8*"█" + CIEL +
1*"█" + LIT + 7*"█" + BLANC + 1*"█" + LIT + 6*"█" + BOIS + 7*"█" + RESET,
MUR + 25*"█" + CIEL + 1*"█" + ROSE + 1*"█" + MUR + 10*"█" + VIOLET + 1*"█" + CHEMISE +
23*"█" + MUR + 6*"█" + ROUGE + 1*"█" + LIT + 19*"█" + CIEL + 1*"█" + LIT + 3*"█" + BOIS +
6*"█" + ORANGE + 1*"█" + RESET,
MUR + 11*"█" + BLANC + 1*"█" + MUR + 1*"█" + ROUGE + 1*"█" + MUR + 19*"█" + BLANC +
1*"█" + MUR + 6*"█" + CHEMISE + 19*"█" + MUR + 6*"█" + CIEL + 1*"█" + MUR + 2*"█" + ROSE +
1*"█" + LIT + 1*"█" + VERT + 1*"█" + LIT + 20*"█" + BOIS + 7*"█" + RESET,
MUR + 7*"█" + JAUNE + 1*"█" + MUR + 2*"█" + ORANGE + 1*"█" + MUR + 2*"█" + VIOLET +
1*"█" + MUR + 26*"█" + CHEMISE + 19*"█" + MUR + 9*"█" + LIT + 5*"█" + BLANC + 1*"█" +
LIT + 4*"█" + ROSE + 1*"█" + LIT + 3*"█" + CIEL + 1*"█" + LIT + 8*"█" + BOIS + 6*"█" +
ROSE + 1*"█" + RESET,
PLINTHE + 26*"█" + BLANC + 1*"█" + PLINTHE + 13*"█" + CHEMISE + 19*"█" + PLINTHE + 2*"█" +
ROUGE + 1*"█" + PLINTHE + 6*"█" + LIT + 10*"█" + CIEL + 1*"█" + LIT + 12*"█" + BOIS +
7*"█" + RESET,
SOL + 2*"█" + JAUNE + 1*"█" + SOL + 16*"█" + ORANGE + 1*"█" + SOL + 8*"█" + ROUGE +
1*"█" + SOL + 10*"█" + ORANGE + 1*"█" + SOL + 2*"█" + PANTALON + 7*"█" + SOL + 1*"█" +
PANTALON + 7*"█" + SOL + 4*"█" + ROSE + 1*"█" + SOL + 6*"█" + BOIS + 2*"█" + SOL +
18*"█" + BOIS + 2*"█" + SOL + 8*"█" + RESET,
SOL + 9*"█" + VIOLET + 1*"█" + BLANC + 1*"█" + SOL + 31*"█" + PANTALON + 7*"█" + SOL +
1*"█" + PANTALON + 7*"█" + SOL + 1*"█" + BLANC + 1*"█" + SOL + 4*"█" + BLANC + 1*"█" +
ORANGE + 1*"█" + SOL + 3*"█" + BOIS + 2*"█" + SOL + 18*"█" + BOIS + 2*"█" + SOL + 8*"█" +
RESET,
SOL + 16*"█" + ROUGE + 1*"█" + SOL + 1*"█" + ROUGE + 1*"█" + ROSE + 1*"█" + SOL + 3*"█" +
VIOLET + 1*"█" + SOL + 12*"█" + BLANC + 1*"█" + SOL + 5*"█" + PANTALON + 7*"█" + VIOLET +
1*"█" + PANTALON + 7*"█" + SOL + 3*"█" + JAUNE + 1*"█" + SOL + 6*"█" + VIOLET + 1*"█" +
SOL + 30*"█" + RESET,
SOL + 2*"█" + VIOLET + 1*"█" + SOL + 4*"█" + ORANGE + 1*"█" + SOL + 8*"█" + VIOLET +
1*"█" + SOL + 25*"█" + PANTALON + 7*"█" + SOL + 1*"█" + PANTALON + 7*"█" + ROSE + 1*"█" +
SOL + 9*"█" + VERT + 1*"█" + SOL + 11*"█" + JAUNE + 1*"█" + ORANGE + 1*"█" + SOL + 9*"█" +
VERT + 1*"█" + SOL + 7*"█" + RESET,
SOL + 5*"█" + JAUNE + 1*"█" + SOL + 34*"█" + CHAUSSURE + 9*"█" + SOL + 1*"█" + CHAUSSURE +
9*"█" + SOL + 8*"█" + VIOLET + 1*"█" + SOL + 30*"█" + RESET,
SOL + 40*"█" + CHAUSSURE + 9*"█" + SOL + 1*"█" + CHAUSSURE + 9*"█" + SOL + 39*"█" +
RESET,
]