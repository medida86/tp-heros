RESET = "\033[0m"
CHEVEUX = "\033[38;2;90;50;20m"
PEAU = "\033[38;2;255;205;170m"
NOIR = "\033[38;2;20;20;30m"
LEVRES = "\033[38;2;210;40;60m"
COSTUME = "\033[38;2;40;50;95m"
BLANC = "\033[38;2;245;245;245m"
JAUNE = "\033[38;2;255;185;30m"
BOIS = "\033[38;2;170;110;55m"
TIROIR = "\033[38;2;130;80;40m"
MUR = "\033[38;2;205;218;228m"
PLINTHE = "\033[38;2;140;125;115m"
SOL = "\033[38;2;125;92;68m"
OMBRE = "\033[38;2;70;55;50m"
CADRE = "\033[38;2;250;250;250m"
CIEL = "\033[38;2;130;190;235m"
NUAGE = "\033[38;2;235;245;255m"
ETAGERE = "\033[38;2;110;70;35m"
LIVRE1 = "\033[38;2;200;50;50m"
LIVRE2 = "\033[38;2;50;110;190m"
LIVRE3 = "\033[38;2;60;160;90m"
LIVRE4 = "\033[38;2;240;190;50m"
LIVRE5 = "\033[38;2;140;80;170m"
VERT = "\033[38;2;50;150;70m"
TERRE = "\033[38;2;180;80;50m"
GRIS = "\033[38;2;90;90;100m"
ABAT = "\033[38;2;255;185;30m"

dessin = [
MUR + 41*"█" + CHEVEUX + 16*"█" + MUR + 41*"█" + RESET,
MUR + 37*"█" + CHEVEUX + 24*"█" + MUR + 37*"█" + RESET,
MUR + 6*"█" + CADRE + 18*"█" + MUR + 11*"█" + CHEVEUX + 28*"█" + MUR + 13*"█" +
ETAGERE + 18*"█" + MUR + 4*"█" + RESET,
MUR + 6*"█" + CADRE + 1*"█" + CIEL + 7*"█" + CADRE + 2*"█" + CIEL + 7*"█" + CADRE +
1*"█" + MUR + 10*"█" + CHEVEUX + 6*"█" + PEAU + 18*"█" + CHEVEUX + 6*"█" + MUR +
12*"█" + ETAGERE + 18*"█" + MUR + 4*"█" + RESET,
MUR + 6*"█" + CADRE + 1*"█" + CIEL + 2*"█" + NUAGE + 4*"█" + CIEL + 1*"█" + CADRE +
2*"█" + CIEL + 2*"█" + NUAGE + 3*"█" + CIEL + 2*"█" + CADRE + 1*"█" + MUR + 10*"█" +
CHEVEUX + 6*"█" + PEAU + 18*"█" + CHEVEUX + 6*"█" + MUR + 12*"█" + ETAGERE + 2*"█" +
LIVRE4 + 2*"█" + LIVRE5 + 2*"█" + LIVRE1 + 2*"█" + LIVRE2 + 2*"█" + LIVRE3 + 2*"█" +
LIVRE4 + 2*"█" + LIVRE5 + 2*"█" + ETAGERE + 2*"█" + MUR + 4*"█" + RESET,
MUR + 6*"█" + CADRE + 1*"█" + CIEL + 7*"█" + CADRE + 2*"█" + CIEL + 7*"█" + CADRE +
1*"█" + MUR + 10*"█" + CHEVEUX + 6*"█" + PEAU + 4*"█" + NOIR + 2*"█" + PEAU + 6*"█" +
NOIR + 2*"█" + PEAU + 4*"█" + CHEVEUX + 6*"█" + MUR + 12*"█" + ETAGERE + 2*"█" +
LIVRE4 + 2*"█" + LIVRE5 + 2*"█" + LIVRE1 + 2*"█" + LIVRE2 + 2*"█" + LIVRE3 + 2*"█" +
LIVRE4 + 2*"█" + LIVRE5 + 2*"█" + ETAGERE + 2*"█" + MUR + 4*"█" + RESET,
MUR + 6*"█" + CADRE + 18*"█" + MUR + 10*"█" + CHEVEUX + 6*"█" + PEAU + 18*"█" +
CHEVEUX + 6*"█" + MUR + 12*"█" + ETAGERE + 18*"█" + MUR + 4*"█" + RESET,
MUR + 6*"█" + CADRE + 18*"█" + MUR + 10*"█" + CHEVEUX + 6*"█" + PEAU + 7*"█" +
LEVRES + 4*"█" + PEAU + 7*"█" + CHEVEUX + 6*"█" + MUR + 12*"█" + ETAGERE + 2*"█" +
LIVRE3 + 2*"█" + LIVRE4 + 2*"█" + ETAGERE + 4*"█" + LIVRE2 + 2*"█" + LIVRE3 + 2*"█" +
ETAGERE + 4*"█" + MUR + 4*"█" + RESET,
MUR + 6*"█" + CADRE + 1*"█" + CIEL + 7*"█" + CADRE + 2*"█" + CIEL + 7*"█" + CADRE +
1*"█" + MUR + 10*"█" + CHEVEUX + 8*"█" + PEAU + 14*"█" + CHEVEUX + 8*"█" + MUR +
12*"█" + ETAGERE + 2*"█" + LIVRE3 + 2*"█" + LIVRE4 + 2*"█" + LIVRE5 + 2*"█" +
ETAGERE + 2*"█" + LIVRE2 + 2*"█" + LIVRE3 + 2*"█" + LIVRE4 + 2*"█" + ETAGERE + 2*"█" +
MUR + 4*"█" + RESET,
MUR + 6*"█" + CADRE + 1*"█" + CIEL + 7*"█" + CADRE + 2*"█" + CIEL + 2*"█" + NUAGE +
4*"█" + CIEL + 1*"█" + CADRE + 1*"█" + MUR + 12*"█" + CHEVEUX + 10*"█" + PEAU +
6*"█" + CHEVEUX + 10*"█" + MUR + 14*"█" + ETAGERE + 2*"█" + LIVRE3 + 2*"█" + LIVRE4 +
2*"█" + LIVRE5 + 2*"█" + LIVRE1 + 2*"█" + LIVRE2 + 2*"█" + LIVRE3 + 2*"█" + LIVRE4 +
2*"█" + ETAGERE + 2*"█" + MUR + 4*"█" + RESET,
MUR + 6*"█" + CADRE + 1*"█" + CIEL + 7*"█" + CADRE + 2*"█" + CIEL + 7*"█" + CADRE +
1*"█" + MUR + 3*"█" + COSTUME + 17*"█" + BLANC + 3*"█" + PEAU + 4*"█" + BLANC +
3*"█" + COSTUME + 17*"█" + MUR + 5*"█" + ETAGERE + 2*"█" + LIVRE3 + 2*"█" + LIVRE4 +
2*"█" + LIVRE5 + 2*"█" + LIVRE1 + 2*"█" + LIVRE2 + 2*"█" + LIVRE3 + 2*"█" + LIVRE4 +
2*"█" + ETAGERE + 2*"█" + MUR + 4*"█" + RESET,
MUR + 6*"█" + CADRE + 18*"█" + COSTUME + 22*"█" + BLANC + 6*"█" + COSTUME + 22*"█" +
MUR + 2*"█" + ETAGERE + 18*"█" + MUR + 4*"█" + RESET,
MUR + 14*"█" + VERT + 2*"█" + MUR + 6*"█" + COSTUME + 24*"█" + BLANC + 6*"█" +
COSTUME + 24*"█" + MUR + 22*"█" + RESET,
MUR + 12*"█" + VERT + 6*"█" + MUR + 2*"█" + COSTUME + 26*"█" + BLANC + 6*"█" +
COSTUME + 26*"█" + MUR + 1*"█" + ABAT + 8*"█" + MUR + 11*"█" + RESET,
MUR + 11*"█" + VERT + 8*"█" + MUR + 1*"█" + COSTUME + 26*"█" + BLANC + 6*"█" +
COSTUME + 26*"█" + MUR + 2*"█" + ABAT + 6*"█" + MUR + 12*"█" + RESET,
MUR + 12*"█" + TERRE + 6*"█" + MUR + 2*"█" + COSTUME + 28*"█" + JAUNE + 2*"█" +
COSTUME + 28*"█" + MUR + 4*"█" + GRIS + 2*"█" + MUR + 14*"█" + RESET,
MUR + 13*"█" + TERRE + 4*"█" + MUR + 3*"█" + COSTUME + 20*"█" + PEAU + 6*"█" +
COSTUME + 6*"█" + PEAU + 6*"█" + COSTUME + 20*"█" + MUR + 2*"█" + GRIS + 6*"█" + MUR +
12*"█" + RESET,
MUR + 4*"█" + BOIS + 90*"█" + MUR + 4*"█" + RESET,
MUR + 4*"█" + TIROIR + 90*"█" + MUR + 4*"█" + RESET,
MUR + 6*"█" + TIROIR + 86*"█" + MUR + 6*"█" + RESET,
MUR + 6*"█" + BOIS + 6*"█" + TIROIR + 28*"█" + BOIS + 2*"█" + COSTUME + 14*"█" +
BOIS + 2*"█" + TIROIR + 28*"█" + BOIS + 6*"█" + MUR + 6*"█" + RESET,
MUR + 6*"█" + BOIS + 6*"█" + TIROIR + 12*"█" + JAUNE + 4*"█" + TIROIR + 12*"█" +
BOIS + 2*"█" + COSTUME + 14*"█" + BOIS + 2*"█" + TIROIR + 12*"█" + JAUNE + 4*"█" +
TIROIR + 12*"█" + BOIS + 6*"█" + MUR + 6*"█" + RESET,
MUR + 6*"█" + BOIS + 6*"█" + TIROIR + 28*"█" + BOIS + 2*"█" + PEAU + 4*"█" + OMBRE +
6*"█" + PEAU + 4*"█" + BOIS + 2*"█" + TIROIR + 28*"█" + BOIS + 6*"█" + MUR + 6*"█" +
RESET,
MUR + 6*"█" + BOIS + 6*"█" + TIROIR + 28*"█" + BOIS + 2*"█" + PEAU + 4*"█" + OMBRE +
6*"█" + PEAU + 4*"█" + BOIS + 2*"█" + TIROIR + 28*"█" + BOIS + 6*"█" + MUR + 6*"█" +
RESET,
MUR + 6*"█" + BOIS + 36*"█" + PEAU + 4*"█" + OMBRE + 6*"█" + PEAU + 4*"█" + BOIS +
36*"█" + MUR + 6*"█" + RESET,
PLINTHE + 6*"█" + BOIS + 6*"█" + TIROIR + 28*"█" + BOIS + 2*"█" + PEAU + 4*"█" +
OMBRE + 6*"█" + PEAU + 4*"█" + BOIS + 2*"█" + TIROIR + 28*"█" + BOIS + 6*"█" +
PLINTHE + 6*"█" + RESET,
SOL + 6*"█" + BOIS + 6*"█" + TIROIR + 12*"█" + JAUNE + 4*"█" + TIROIR + 12*"█" +
BOIS + 2*"█" + PEAU + 4*"█" + OMBRE + 6*"█" + PEAU + 4*"█" + BOIS + 2*"█" + TIROIR +
12*"█" + JAUNE + 4*"█" + TIROIR + 12*"█" + BOIS + 6*"█" + SOL + 6*"█" + RESET,
SOL + 6*"█" + BOIS + 6*"█" + TIROIR + 28*"█" + BOIS + 2*"█" + PEAU + 4*"█" + OMBRE +
6*"█" + PEAU + 4*"█" + BOIS + 2*"█" + TIROIR + 28*"█" + BOIS + 6*"█" + SOL + 6*"█" +
RESET,
SOL + 6*"█" + BOIS + 6*"█" + TIROIR + 28*"█" + BOIS + 2*"█" + NOIR + 5*"█" + OMBRE +
4*"█" + NOIR + 5*"█" + BOIS + 2*"█" + TIROIR + 28*"█" + BOIS + 6*"█" + SOL + 6*"█" +
RESET,
SOL + 6*"█" + BOIS + 86*"█" + SOL + 6*"█" + RESET,
]
