RESET = "\033[0m"
CIEL1 = "\033[38;2;95;175;255m"
CIEL2 = "\033[38;2;135;175;255m"
CIEL3 = "\033[38;2;135;215;255m"
CIEL4 = "\033[38;2;175;215;255m"
SOLEIL = "\033[38;2;255;255;0m"
SOLEIL2 = "\033[38;2;255;215;0m"
MONT_CLAIR = "\033[38;2;175;175;215m"
MONT_SOMBRE = "\033[38;2;135;135;175m"
BLANC = "\033[38;2;255;255;255m"
NUAGE = "\033[38;2;238;238;238m"
FUMEE1 = "\033[38;2;208;208;208m"
FUMEE2 = "\033[38;2;188;188;188m"
VERT1 = "\033[38;2;0;95;0m"
VERT2 = "\033[38;2;0;135;0m"
VERT3 = "\033[38;2;0;175;0m"
VERT4 = "\033[38;2;0;215;0m"
VERT5 = "\033[38;2;95;175;0m"
VERT6 = "\033[38;2;95;215;0m"
FLEUR_ROUGE = "\033[38;2;255;0;0m"
FLEUR_ROSE = "\033[38;2;255;135;255m"
SABLE = "\033[38;2;255;215;175m"
MUR1 = "\033[38;2;215;175;135m"
MUR2 = "\033[38;2;215;175;95m"
COTE1 = "\033[38;2;175;135;95m"
COTE2 = "\033[38;2;135;95;95m"
PIERRE_SOMBRE = "\033[38;2;88;88;88m"
PIERRE = "\033[38;2;138;138;138m"
TUILE1 = "\033[38;2;175;0;0m"
TUILE2 = "\033[38;2;135;0;0m"
BRIQUE = "\033[38;2;175;95;95m"
BOIS = "\033[38;2;135;95;0m"
BOIS_SOMBRE = "\033[38;2;95;95;0m"
VITRE = "\033[38;2;95;175;215m"

dessin = [
    CIEL1 + 58*"█" + FUMEE1 + 1*"█" + FUMEE2 + 1*"█" + CIEL1 + 38*"█" + RESET,
    CIEL1 + 23*"█" + SOLEIL2 + 3*"█" + CIEL1 + 16*"█" + NUAGE + 9*"█" + CIEL1 + 4*"█" + PIERRE + 6*"█" + CIEL1 + 27*"█" + NUAGE + 7*"█" + CIEL1 + 3*"█" + RESET,
    CIEL1 + 21*"█" + SOLEIL2 + 1*"█" + SOLEIL + 5*"█" + SOLEIL2 + 1*"█" + CIEL1 + 12*"█" + NUAGE + 10*"█" + TUILE1 + 2*"█" + NUAGE + 1*"█" + CIEL1 + 3*"█" + TUILE1 + 3*"█" + TUILE2 + 1*"█" + CIEL1 + 25*"█" + NUAGE + 13*"█" + RESET,
    CIEL1 + 20*"█" + SOLEIL2 + 2*"█" + SOLEIL + 5*"█" + SOLEIL2 + 2*"█" + CIEL1 + 13*"█" + NUAGE + 6*"█" + TUILE1 + 2*"█" + TUILE2 + 4*"█" + CIEL1 + 2*"█" + BRIQUE + 3*"█" + TUILE2 + 1*"█" + CIEL1 + 28*"█" + NUAGE + 7*"█" + CIEL1 + 3*"█" + RESET,
    CIEL2 + 21*"█" + SOLEIL2 + 1*"█" + SOLEIL + 5*"█" + SOLEIL2 + 1*"█" + CIEL2 + 17*"█" + TUILE1 + 3*"█" + TUILE2 + 4*"█" + TUILE1 + 7*"█" + TUILE2 + 1*"█" + CIEL2 + 38*"█" + RESET,
    CIEL2 + 9*"█" + BLANC + 1*"█" + CIEL2 + 13*"█" + SOLEIL2 + 3*"█" + CIEL2 + 16*"█" + TUILE1 + 3*"█" + TUILE2 + 5*"█" + TUILE1 + 5*"█" + TUILE2 + 1*"█" + BRIQUE + 3*"█" + TUILE2 + 1*"█" + CIEL2 + 20*"█" + BLANC + 1*"█" + CIEL2 + 17*"█" + RESET,
    CIEL2 + 8*"█" + BLANC + 3*"█" + CIEL2 + 28*"█" + TUILE1 + 3*"█" + TUILE2 + 5*"█" + TUILE1 + 6*"█" + TUILE2 + 3*"█" + TUILE1 + 3*"█" + TUILE2 + 1*"█" + TUILE1 + 2*"█" + CIEL2 + 17*"█" + BLANC + 3*"█" + CIEL2 + 16*"█" + RESET,
    CIEL2 + 7*"█" + BLANC + 2*"█" + MONT_CLAIR + 1*"█" + BLANC + 2*"█" + CIEL2 + 25*"█" + TUILE1 + 2*"█" + TUILE2 + 5*"█" + TUILE1 + 6*"█" + TUILE2 + 5*"█" + TUILE1 + 1*"█" + BRIQUE + 3*"█" + TUILE2 + 5*"█" + CIEL2 + 14*"█" + BLANC + 2*"█" + MONT_CLAIR + 1*"█" + BLANC + 2*"█" + CIEL2 + 3*"█" + VERT5 + 1*"█" + CIEL2 + 11*"█" + RESET,
    CIEL3 + 6*"█" + BLANC + 1*"█" + VERT5 + 1*"█" + MONT_CLAIR + 2*"█" + MONT_SOMBRE + 1*"█" + BLANC + 2*"█" + CIEL3 + 21*"█" + TUILE1 + 1*"█" + TUILE2 + 1*"█" + TUILE1 + 1*"█" + TUILE2 + 4*"█" + TUILE1 + 6*"█" + TUILE2 + 5*"█" + TUILE1 + 6*"█" + TUILE2 + 4*"█" + TUILE1 + 4*"█" + CIEL3 + 11*"█" + BLANC + 2*"█" + MONT_CLAIR + 2*"█" + MONT_SOMBRE + 1*"█" + BLANC + 1*"█" + VERT5 + 5*"█" + VERT3 + 2*"█" + CIEL3 + 8*"█" + RESET,
    CIEL3 + 4*"█" + VERT5 + 5*"█" + VERT3 + 2*"█" + MONT_SOMBRE + 1*"█" + BLANC + 3*"█" + CIEL3 + 17*"█" + TUILE1 + 1*"█" + TUILE2 + 2*"█" + MUR1 + 1*"█" + TUILE2 + 3*"█" + TUILE1 + 5*"█" + TUILE2 + 5*"█" + TUILE1 + 6*"█" + TUILE2 + 5*"█" + TUILE1 + 4*"█" + TUILE2 + 5*"█" + CIEL3 + 6*"█" + BLANC + 3*"█" + MONT_CLAIR + 3*"█" + MONT_SOMBRE + 1*"█" + VERT5 + 5*"█" + VERT3 + 4*"█" + CIEL3 + 7*"█" + RESET,
    CIEL3 + 3*"█" + VERT5 + 4*"█" + VERT3 + 5*"█" + MONT_SOMBRE + 1*"█" + BLANC + 3*"█" + CIEL3 + 13*"█" + TUILE1 + 1*"█" + TUILE2 + 2*"█" + MUR1 + 7*"█" + TUILE2 + 2*"█" + TUILE1 + 1*"█" + TUILE2 + 4*"█" + TUILE1 + 6*"█" + TUILE2 + 5*"█" + TUILE1 + 5*"█" + TUILE2 + 5*"█" + TUILE1 + 4*"█" + CIEL3 + 3*"█" + BLANC + 3*"█" + MONT_CLAIR + 4*"█" + VERT5 + 4*"█" + VERT3 + 6*"█" + VERT2 + 1*"█" + CIEL3 + 6*"█" + RESET,
    CIEL3 + 2*"█" + BLANC + 1*"█" + VERT5 + 2*"█" + VERT3 + 5*"█" + VERT2 + 2*"█" + MONT_SOMBRE + 3*"█" + BLANC + 2*"█" + CIEL3 + 10*"█" + TUILE1 + 1*"█" + TUILE2 + 2*"█" + MUR1 + 3*"█" + BLANC + 5*"█" + MUR1 + 3*"█" + TUILE2 + 3*"█" + TUILE1 + 5*"█" + TUILE2 + 5*"█" + TUILE1 + 5*"█" + TUILE2 + 6*"█" + TUILE1 + 4*"█" + CIEL3 + 4*"█" + BLANC + 2*"█" + MONT_CLAIR + 6*"█" + VERT5 + 3*"█" + VERT3 + 5*"█" + VERT2 + 3*"█" + CIEL3 + 6*"█" + RESET,
    CIEL4 + 1*"█" + MONT_CLAIR + 1*"█" + VERT5 + 2*"█" + VERT3 + 4*"█" + VERT2 + 4*"█" + VERT1 + 1*"█" + MONT_SOMBRE + 3*"█" + BLANC + 1*"█" + MONT_SOMBRE + 1*"█" + CIEL4 + 7*"█" + TUILE2 + 2*"█" + MUR1 + 6*"█" + BLANC + 1*"█" + VITRE + 1*"█" + BLANC + 1*"█" + VITRE + 1*"█" + BLANC + 1*"█" + MUR1 + 6*"█" + TUILE2 + 2*"█" + TUILE1 + 1*"█" + TUILE2 + 4*"█" + TUILE1 + 5*"█" + TUILE2 + 6*"█" + TUILE1 + 5*"█" + COTE1 + 2*"█" + CIEL4 + 3*"█" + MONT_CLAIR + 1*"█" + BLANC + 1*"█" + MONT_CLAIR + 6*"█" + VERT5 + 2*"█" + VERT3 + 6*"█" + VERT2 + 4*"█" + VERT1 + 1*"█" + CIEL4 + 5*"█" + RESET,
    MONT_CLAIR + 1*"█" + VERT5 + 2*"█" + VERT3 + 4*"█" + VERT2 + 3*"█" + VERT1 + 2*"█" + VERT3 + 2*"█" + MONT_SOMBRE + 6*"█" + CIEL4 + 2*"█" + TUILE2 + 3*"█" + MUR1 + 8*"█" + BLANC + 1*"█" + VITRE + 1*"█" + BLANC + 1*"█" + VITRE + 1*"█" + BLANC + 1*"█" + MUR1 + 8*"█" + TUILE2 + 3*"█" + TUILE1 + 4*"█" + TUILE2 + 6*"█" + TUILE1 + 5*"█" + COTE2 + 1*"█" + COTE1 + 2*"█" + BLANC + 1*"█" + COTE2 + 1*"█" + CIEL4 + 1*"█" + MONT_CLAIR + 10*"█" + VERT5 + 1*"█" + VERT3 + 5*"█" + VERT2 + 4*"█" + VERT1 + 2*"█" + VERT5 + 1*"█" + CIEL4 + 5*"█" + RESET,
    VERT5 + 3*"█" + VERT3 + 2*"█" + VERT2 + 4*"█" + VERT1 + 3*"█" + VERT3 + 3*"█" + MONT_SOMBRE + 5*"█" + TUILE2 + 3*"█" + MUR1 + 10*"█" + BLANC + 5*"█" + MUR1 + 10*"█" + TUILE2 + 2*"█" + TUILE1 + 1*"█" + TUILE2 + 5*"█" + TUILE1 + 5*"█" + COTE2 + 1*"█" + COTE1 + 3*"█" + BLANC + 3*"█" + COTE1 + 1*"█" + MONT_CLAIR + 9*"█" + VERT5 + 3*"█" + VERT3 + 3*"█" + VERT2 + 5*"█" + VERT1 + 3*"█" + VERT3 + 3*"█" + CIEL4 + 3*"█" + RESET,
    VERT5 + 2*"█" + VERT3 + 2*"█" + VERT2 + 3*"█" + VERT1 + 4*"█" + VERT3 + 2*"█" + VERT2 + 2*"█" + MONT_SOMBRE + 3*"█" + TUILE2 + 2*"█" + MUR1 + 31*"█" + TUILE2 + 3*"█" + TUILE1 + 4*"█" + COTE2 + 1*"█" + COTE1 + 3*"█" + BLANC + 3*"█" + VITRE + 2*"█" + BLANC + 1*"█" + COTE2 + 1*"█" + MONT_CLAIR + 8*"█" + VERT5 + 5*"█" + VERT3 + 1*"█" + VERT2 + 4*"█" + VERT1 + 4*"█" + VERT3 + 4*"█" + VERT2 + 1*"█" + VERT1 + 2*"█" + RESET,
    VERT5 + 1*"█" + VERT3 + 4*"█" + VERT5 + 2*"█" + VERT1 + 1*"█" + VERT3 + 3*"█" + VERT2 + 4*"█" + VERT1 + 1*"█" + BOIS + 39*"█" + TUILE1 + 1*"█" + COTE1 + 3*"█" + BLANC + 1*"█" + COTE2 + 2*"█" + BLANC + 1*"█" + VITRE + 1*"█" + BLANC + 4*"█" + COTE1 + 1*"█" + VERT1 + 1*"█" + MONT_CLAIR + 7*"█" + VERT5 + 3*"█" + VERT3 + 3*"█" + VERT2 + 3*"█" + VERT1 + 4*"█" + VERT3 + 3*"█" + VERT2 + 5*"█" + RESET,
    VERT3 + 4*"█" + VERT2 + 2*"█" + VERT3 + 4*"█" + VERT2 + 3*"█" + VERT1 + 5*"█" + COTE1 + 35*"█" + COTE2 + 1*"█" + COTE1 + 2*"█" + BLANC + 4*"█" + COTE1 + 2*"█" + BLANC + 3*"█" + VITRE + 2*"█" + BLANC + 1*"█" + COTE2 + 1*"█" + VERT2 + 1*"█" + VERT1 + 5*"█" + MONT_CLAIR + 1*"█" + VERT5 + 2*"█" + VERT3 + 6*"█" + VERT5 + 2*"█" + VERT1 + 1*"█" + VERT3 + 5*"█" + VERT2 + 4*"█" + VERT1 + 1*"█" + VERT2 + 1*"█" + RESET,
    VERT3 + 2*"█" + VERT2 + 4*"█" + VERT3 + 2*"█" + VERT2 + 4*"█" + VERT1 + 3*"█" + VERT2 + 3*"█" + MUR1 + 35*"█" + COTE1 + 1*"█" + BLANC + 3*"█" + VITRE + 2*"█" + BLANC + 1*"█" + COTE2 + 2*"█" + BLANC + 1*"█" + VITRE + 1*"█" + BLANC + 3*"█" + COTE1 + 2*"█" + VERT2 + 6*"█" + VERT1 + 2*"█" + VERT3 + 5*"█" + VERT2 + 3*"█" + VERT3 + 5*"█" + VERT2 + 4*"█" + VERT1 + 2*"█" + VERT2 + 2*"█" + RESET,
    VERT2 + 4*"█" + VERT1 + 3*"█" + VERT2 + 3*"█" + VERT1 + 4*"█" + VERT2 + 4*"█" + MUR2 + 2*"█" + VERT1 + 2*"█" + BLANC + 6*"█" + VERT1 + 2*"█" + MUR2 + 12*"█" + VERT1 + 2*"█" + BLANC + 6*"█" + VERT1 + 2*"█" + MUR2 + 1*"█" + COTE2 + 1*"█" + BLANC + 1*"█" + VITRE + 1*"█" + BLANC + 4*"█" + COTE1 + 2*"█" + BLANC + 3*"█" + COTE1 + 2*"█" + COTE2 + 2*"█" + VERT2 + 8*"█" + VERT3 + 3*"█" + VERT2 + 4*"█" + VERT1 + 1*"█" + VERT3 + 3*"█" + VERT2 + 4*"█" + VERT1 + 4*"█" + VERT2 + 2*"█" + RESET,
    VERT2 + 4*"█" + VERT1 + 1*"█" + VERT2 + 1*"█" + BOIS + 1*"█" + BOIS_SOMBRE + 1*"█" + VERT2 + 2*"█" + VERT1 + 1*"█" + VERT2 + 7*"█" + MUR1 + 2*"█" + VERT1 + 2*"█" + BLANC + 1*"█" + VITRE + 1*"█" + BLANC + 1*"█" + VITRE + 2*"█" + BLANC + 1*"█" + VERT1 + 2*"█" + MUR1 + 2*"█" + BOIS + 7*"█" + MUR1 + 3*"█" + VERT1 + 2*"█" + BLANC + 1*"█" + VITRE + 1*"█" + BLANC + 1*"█" + VITRE + 2*"█" + BLANC + 1*"█" + VERT1 + 2*"█" + MUR1 + 1*"█" + COTE1 + 1*"█" + BLANC + 3*"█" + VITRE + 2*"█" + BLANC + 1*"█" + COTE2 + 2*"█" + COTE1 + 3*"█" + COTE2 + 2*"█" + COTE1 + 2*"█" + VERT2 + 14*"█" + VERT1 + 3*"█" + VERT2 + 5*"█" + VERT1 + 4*"█" + VERT2 + 3*"█" + RESET,
    VERT6 + 6*"█" + BOIS + 1*"█" + BOIS_SOMBRE + 1*"█" + VERT6 + 10*"█" + MUR2 + 2*"█" + VERT1 + 2*"█" + BLANC + 6*"█" + VERT1 + 2*"█" + MUR2 + 2*"█" + BOIS + 1*"█" + BOIS_SOMBRE + 2*"█" + BOIS + 1*"█" + BOIS_SOMBRE + 2*"█" + BOIS + 1*"█" + MUR2 + 3*"█" + VERT1 + 2*"█" + BLANC + 6*"█" + VERT1 + 2*"█" + MUR2 + 1*"█" + COTE2 + 1*"█" + BLANC + 1*"█" + VITRE + 1*"█" + BLANC + 3*"█" + COTE1 + 3*"█" + COTE2 + 3*"█" + COTE1 + 2*"█" + PIERRE_SOMBRE + 2*"█" + VERT6 + 11*"█" + VERT2 + 1*"█" + VERT1 + 4*"█" + BOIS + 1*"█" + BOIS_SOMBRE + 1*"█" + VERT6 + 1*"█" + VERT2 + 1*"█" + VERT1 + 4*"█" + VERT6 + 5*"█" + RESET,
    VERT6 + 6*"█" + BOIS + 1*"█" + BOIS_SOMBRE + 1*"█" + VERT6 + 10*"█" + MUR1 + 2*"█" + VERT1 + 2*"█" + BLANC + 1*"█" + VITRE + 1*"█" + BLANC + 1*"█" + VITRE + 2*"█" + BLANC + 1*"█" + VERT1 + 2*"█" + MUR1 + 2*"█" + BOIS + 1*"█" + BOIS_SOMBRE + 2*"█" + BOIS + 1*"█" + BOIS_SOMBRE + 2*"█" + BOIS + 1*"█" + MUR1 + 3*"█" + VERT1 + 2*"█" + BLANC + 1*"█" + VITRE + 1*"█" + BLANC + 1*"█" + VITRE + 2*"█" + BLANC + 1*"█" + VERT1 + 2*"█" + MUR1 + 1*"█" + COTE1 + 1*"█" + BLANC + 2*"█" + COTE1 + 3*"█" + COTE2 + 3*"█" + COTE1 + 3*"█" + PIERRE_SOMBRE + 2*"█" + VERT6 + 18*"█" + BOIS + 1*"█" + BOIS_SOMBRE + 1*"█" + VERT6 + 11*"█" + RESET,
    VERT4 + 4*"█" + FLEUR_ROSE + 1*"█" + VERT4 + 1*"█" + BOIS + 1*"█" + BOIS_SOMBRE + 1*"█" + VERT4 + 10*"█" + MUR2 + 2*"█" + VERT1 + 2*"█" + BLANC + 6*"█" + VERT1 + 2*"█" + MUR2 + 2*"█" + BOIS + 1*"█" + BOIS_SOMBRE + 2*"█" + BOIS + 1*"█" + BOIS_SOMBRE + 2*"█" + BOIS + 1*"█" + MUR2 + 3*"█" + VERT1 + 2*"█" + BLANC + 6*"█" + VERT1 + 2*"█" + MUR2 + 1*"█" + COTE2 + 1*"█" + COTE1 + 2*"█" + COTE2 + 3*"█" + COTE1 + 3*"█" + PIERRE_SOMBRE + 3*"█" + VERT4 + 3*"█" + BLANC + 2*"█" + VERT4 + 2*"█" + SOLEIL + 1*"█" + VERT4 + 1*"█" + SOLEIL + 1*"█" + VERT4 + 2*"█" + FLEUR_ROUGE + 1*"█" + FLEUR_ROSE + 1*"█" + VERT4 + 4*"█" + FLEUR_ROUGE + 1*"█" + VERT4 + 1*"█" + BOIS + 1*"█" + BOIS_SOMBRE + 1*"█" + VERT4 + 11*"█" + RESET,
    VERT4 + 6*"█" + BOIS + 1*"█" + BOIS_SOMBRE + 1*"█" + VERT4 + 2*"█" + FLEUR_ROSE + 1*"█" + VERT4 + 4*"█" + VERT5 + 1*"█" + VERT4 + 2*"█" + MUR1 + 14*"█" + BOIS + 5*"█" + SOLEIL2 + 1*"█" + BOIS + 1*"█" + MUR1 + 14*"█" + COTE1 + 1*"█" + COTE2 + 2*"█" + COTE1 + 3*"█" + PIERRE_SOMBRE + 3*"█" + VERT4 + 23*"█" + BOIS + 1*"█" + BOIS_SOMBRE + 1*"█" + VERT4 + 11*"█" + RESET,
    VERT3 + 6*"█" + BOIS + 1*"█" + BOIS_SOMBRE + 1*"█" + VERT3 + 5*"█" + VERT5 + 2*"█" + VERT3 + 3*"█" + MUR2 + 14*"█" + BOIS + 7*"█" + MUR2 + 14*"█" + COTE2 + 1*"█" + COTE1 + 2*"█" + PIERRE_SOMBRE + 3*"█" + SOLEIL + 1*"█" + VERT3 + 25*"█" + BOIS + 1*"█" + BOIS_SOMBRE + 1*"█" + VERT3 + 9*"█" + SOLEIL + 1*"█" + VERT3 + 1*"█" + RESET,
    VERT3 + 6*"█" + BOIS + 1*"█" + BOIS_SOMBRE + 1*"█" + VERT3 + 4*"█" + VERT5 + 1*"█" + VERT3 + 3*"█" + VERT2 + 2*"█" + VERT1 + 1*"█" + MUR1 + 13*"█" + BOIS + 7*"█" + MUR1 + 14*"█" + COTE1 + 1*"█" + PIERRE_SOMBRE + 2*"█" + VERT5 + 2*"█" + VERT3 + 4*"█" + FLEUR_ROUGE + 1*"█" + VERT3 + 2*"█" + SOLEIL + 1*"█" + VERT3 + 1*"█" + BLANC + 1*"█" + VERT3 + 8*"█" + FLEUR_ROSE + 1*"█" + VERT3 + 8*"█" + BOIS + 1*"█" + BOIS_SOMBRE + 1*"█" + VERT3 + 6*"█" + BLANC + 1*"█" + VERT3 + 4*"█" + RESET,
    VERT3 + 6*"█" + BOIS + 1*"█" + BOIS_SOMBRE + 1*"█" + VERT3 + 2*"█" + BLANC + 1*"█" + FLEUR_ROSE + 1*"█" + VERT3 + 2*"█" + VERT2 + 2*"█" + VERT1 + 2*"█" + PIERRE + 12*"█" + FUMEE2 + 11*"█" + PIERRE + 12*"█" + PIERRE_SOMBRE + 1*"█" + VERT3 + 1*"█" + VERT5 + 1*"█" + VERT3 + 3*"█" + VERT2 + 2*"█" + VERT1 + 1*"█" + VERT3 + 11*"█" + FLEUR_ROSE + 1*"█" + VERT3 + 8*"█" + FLEUR_ROSE + 1*"█" + VERT3 + 2*"█" + BOIS + 1*"█" + BOIS_SOMBRE + 1*"█" + VERT3 + 11*"█" + RESET,
    VERT2 + 6*"█" + BOIS + 1*"█" + BOIS_SOMBRE + 1*"█" + VERT2 + 7*"█" + VERT1 + 1*"█" + SOLEIL + 1*"█" + VERT2 + 6*"█" + SOLEIL + 1*"█" + VERT2 + 4*"█" + FLEUR_ROUGE + 1*"█" + VERT2 + 1*"█" + SABLE + 11*"█" + VERT2 + 2*"█" + BLANC + 1*"█" + VERT2 + 12*"█" + VERT3 + 1*"█" + VERT2 + 2*"█" + VERT1 + 2*"█" + VERT2 + 2*"█" + FLEUR_ROSE + 1*"█" + VERT2 + 21*"█" + BOIS + 1*"█" + BOIS_SOMBRE + 1*"█" + VERT2 + 11*"█" + RESET,
    VERT2 + 7*"█" + FLEUR_ROUGE + 2*"█" + VERT2 + 19*"█" + SABLE + 15*"█" + VERT2 + 28*"█" + SOLEIL + 1*"█" + VERT2 + 26*"█" + RESET,
]