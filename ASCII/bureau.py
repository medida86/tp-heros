RESET = "\033[0m"
MUR1 = "\033[38;2;255;236;194m"
MUR2 = "\033[38;2;255;248;214m"
MUR3 = "\033[38;2;240;215;170m"
VERT_LAMBRIS = "\033[38;2;120;178;92m"
VERT_LAMBRIS2 = "\033[38;2;92;150;76m"
PLINTHE = "\033[38;2;120;66;40m"
SOL1 = "\033[38;2;128;214;196m"
SOL2 = "\033[38;2;98;180;176m"
OMBRE = "\033[38;2;64;118;132m"
BOIS_CLAIR = "\033[38;2;240;160;86m"
BOIS = "\033[38;2;208;118;52m"
BOIS_SOMBRE = "\033[38;2;146;74;42m"
BOIS_NOIR = "\033[38;2;96;46;34m"
BLEU_CLAIR = "\033[38;2;104;116;200m"
BLEU = "\033[38;2;62;70;146m"
BLEU_SOMBRE = "\033[38;2;36;40;96m"
NOIR = "\033[38;2;26;16;42m"
GRIS_CLAIR = "\033[38;2;214;214;222m"
GRIS = "\033[38;2;152;152;170m"
GRIS_SOMBRE = "\033[38;2;100;100;124m"
ECRAN = "\033[38;2;96;232;216m"
ECRAN2 = "\033[38;2;150;250;236m"
BLANC = "\033[38;2;252;252;252m"
CREME = "\033[38;2;255;246;222m"
FEUILLE = "\033[38;2;70;170;78m"
FEUILLE_SOMBRE = "\033[38;2;36;112;58m"
FEUILLE_CLAIR = "\033[38;2;130;210;96m"
POT = "\033[38;2;206;64;52m"
POT_SOMBRE = "\033[38;2;150;40;46m"
LIVRE_ROUGE = "\033[38;2;190;48;52m"
LIVRE_BLEU = "\033[38;2;52;92;172m"
LIVRE_TURQ = "\033[38;2;60;192;190m"
LIVRE_JAUNE = "\033[38;2;242;204;72m"
LIVRE_ORANGE = "\033[38;2;242;132;50m"
LIVRE_VERT = "\033[38;2;60;150;90m"
CIEL = "\033[38;2;150;216;246m"
CIEL2 = "\033[38;2;196;238;255m"
ROUGE = "\033[38;2;214;52;48m"
LAMPE = "\033[38;2;255;214;80m"

dessin = [
    MUR3 + 6*"█" + MUR2 + 17*"█" + MUR3 + 9*"█" + BOIS_CLAIR + 14*"█" + MUR3 + 52*"█" + RESET,
    MUR1 + 6*"█" + MUR2 + 1*"█" + CREME + 1*"█" + BLANC + 1*"█" + CREME + 1*"█" + BLANC + 1*"█" + CREME + 1*"█" + BLANC + 1*"█" + CREME + 1*"█" + BLANC + 1*"█" + CREME + 1*"█" + BLANC + 1*"█" + CREME + 1*"█" + BLANC + 1*"█" + CREME + 1*"█" + BLANC + 1*"█" + CREME + 1*"█" + MUR2 + 1*"█" + MUR1 + 7*"█" + BOIS_CLAIR + 15*"█" + BOIS_SOMBRE + 1*"█" + MUR1 + 11*"█" + ROUGE + 3*"█" + MUR1 + 8*"█" + BOIS + 11*"█" + MUR1 + 19*"█" + RESET,
    MUR1 + 6*"█" + BOIS + 1*"█" + CIEL2 + 7*"█" + BOIS + 1*"█" + CIEL2 + 7*"█" + BOIS + 1*"█" + MUR1 + 5*"█" + BOIS_SOMBRE + 14*"█" + BOIS_CLAIR + 1*"█" + BOIS_SOMBRE + 3*"█" + MUR1 + 10*"█" + ROUGE + 1*"█" + BLANC + 1*"█" + NOIR + 1*"█" + BLANC + 1*"█" + ROUGE + 1*"█" + MUR1 + 7*"█" + BOIS + 1*"█" + LIVRE_ORANGE + 4*"█" + CREME + 1*"█" + LIVRE_VERT + 4*"█" + BOIS + 1*"█" + MUR1 + 5*"█" + BOIS + 9*"█" + MUR1 + 5*"█" + RESET,
    MUR1 + 6*"█" + BOIS + 1*"█" + CIEL2 + 7*"█" + BOIS + 1*"█" + CIEL2 + 7*"█" + BOIS + 1*"█" + MUR1 + 5*"█" + BOIS_SOMBRE + 1*"█" + BOIS_NOIR + 1*"█" + LIVRE_ORANGE + 2*"█" + LIVRE_TURQ + 1*"█" + BOIS_NOIR + 2*"█" + LIVRE_JAUNE + 1*"█" + LIVRE_ROUGE + 2*"█" + BOIS_NOIR + 1*"█" + LIVRE_TURQ + 2*"█" + BOIS_SOMBRE + 5*"█" + MUR1 + 10*"█" + ROUGE + 1*"█" + BLANC + 1*"█" + NOIR + 2*"█" + ROUGE + 1*"█" + MUR1 + 7*"█" + BOIS + 1*"█" + LIVRE_ORANGE + 4*"█" + CREME + 1*"█" + LIVRE_VERT + 4*"█" + BOIS + 1*"█" + MUR1 + 5*"█" + BOIS + 1*"█" + ECRAN + 2*"█" + BLANC + 3*"█" + ECRAN + 2*"█" + BOIS + 1*"█" + MUR1 + 5*"█" + RESET,
    MUR1 + 6*"█" + BOIS + 1*"█" + BLANC + 15*"█" + BOIS + 1*"█" + MUR1 + 5*"█" + BOIS_SOMBRE + 1*"█" + LIVRE_ROUGE + 1*"█" + LIVRE_ORANGE + 2*"█" + LIVRE_TURQ + 1*"█" + LIVRE_BLEU + 2*"█" + LIVRE_JAUNE + 1*"█" + LIVRE_ROUGE + 2*"█" + LIVRE_ORANGE + 1*"█" + LIVRE_TURQ + 2*"█" + BOIS_SOMBRE + 5*"█" + MUR1 + 10*"█" + ROUGE + 1*"█" + BLANC + 3*"█" + ROUGE + 1*"█" + MUR1 + 7*"█" + BOIS + 1*"█" + LIVRE_ORANGE + 4*"█" + CREME + 1*"█" + LIVRE_VERT + 4*"█" + BOIS + 1*"█" + MUR1 + 5*"█" + BOIS + 1*"█" + ECRAN + 1*"█" + BLANC + 5*"█" + ECRAN + 1*"█" + BOIS + 1*"█" + MUR1 + 5*"█" + RESET,
    MUR1 + 6*"█" + BOIS + 1*"█" + CIEL + 7*"█" + BOIS + 1*"█" + CIEL + 7*"█" + BOIS + 1*"█" + MUR1 + 5*"█" + BOIS_CLAIR + 14*"█" + BOIS_SOMBRE + 4*"█" + MUR1 + 11*"█" + ROUGE + 3*"█" + MUR1 + 8*"█" + BOIS + 11*"█" + MUR1 + 5*"█" + BOIS + 1*"█" + ECRAN + 2*"█" + BLANC + 3*"█" + ECRAN + 2*"█" + BOIS + 1*"█" + MUR1 + 5*"█" + RESET,
    MUR1 + 6*"█" + BOIS + 1*"█" + CIEL + 7*"█" + BOIS + 1*"█" + CIEL + 7*"█" + BOIS + 1*"█" + MUR1 + 5*"█" + BOIS_SOMBRE + 1*"█" + BOIS_NOIR + 1*"█" + LIVRE_VERT + 2*"█" + LIVRE_ROUGE + 1*"█" + BOIS_NOIR + 2*"█" + LIVRE_ORANGE + 1*"█" + CREME + 4*"█" + LIVRE_ORANGE + 1*"█" + BOIS_SOMBRE + 5*"█" + MUR1 + 38*"█" + BOIS + 9*"█" + MUR1 + 5*"█" + RESET,
    VERT_LAMBRIS + 5*"█" + BOIS_CLAIR + 3*"█" + FEUILLE_CLAIR + 3*"█" + FEUILLE + 2*"█" + BOIS_CLAIR + 11*"█" + VERT_LAMBRIS + 4*"█" + BOIS_SOMBRE + 1*"█" + LIVRE_BLEU + 1*"█" + LIVRE_VERT + 2*"█" + LIVRE_ROUGE + 1*"█" + LIVRE_BLEU + 2*"█" + LIVRE_ORANGE + 6*"█" + BOIS_SOMBRE + 5*"█" + VERT_LAMBRIS + 31*"█" + LAMPE + 5*"█" + FEUILLE_CLAIR + 2*"█" + FEUILLE + 1*"█" + VERT_LAMBRIS + 13*"█" + RESET,
    VERT_LAMBRIS2 + 7*"█" + FEUILLE_CLAIR + 2*"█" + FEUILLE + 4*"█" + FEUILLE_SOMBRE + 1*"█" + VERT_LAMBRIS2 + 14*"█" + BOIS_CLAIR + 14*"█" + BOIS_SOMBRE + 4*"█" + VERT_LAMBRIS2 + 13*"█" + NOIR + 14*"█" + VERT_LAMBRIS2 + 4*"█" + LAMPE + 4*"█" + FEUILLE_CLAIR + 1*"█" + FEUILLE + 4*"█" + VERT_LAMBRIS2 + 12*"█" + RESET,
    PLINTHE + 7*"█" + FEUILLE_CLAIR + 1*"█" + FEUILLE + 4*"█" + FEUILLE_SOMBRE + 2*"█" + PLINTHE + 14*"█" + BOIS_SOMBRE + 1*"█" + BOIS_NOIR + 1*"█" + BLEU_SOMBRE + 2*"█" + LIVRE_TURQ + 1*"█" + BOIS_NOIR + 2*"█" + NOIR + 1*"█" + BLEU_SOMBRE + 2*"█" + BOIS_NOIR + 1*"█" + BLEU_SOMBRE + 2*"█" + BOIS_SOMBRE + 5*"█" + PLINTHE + 3*"█" + GRIS_CLAIR + 3*"█" + GRIS_SOMBRE + 1*"█" + PLINTHE + 6*"█" + NOIR + 1*"█" + ECRAN + 1*"█" + ECRAN2 + 1*"█" + ECRAN + 1*"█" + ECRAN2 + 1*"█" + ECRAN + 1*"█" + ECRAN2 + 1*"█" + ECRAN + 6*"█" + NOIR + 1*"█" + PLINTHE + 6*"█" + GRIS + 1*"█" + PLINTHE + 1*"█" + FEUILLE + 4*"█" + FEUILLE_SOMBRE + 1*"█" + PLINTHE + 12*"█" + RESET,
    SOL2 + 6*"█" + SOL1 + 1*"█" + FEUILLE + 3*"█" + FEUILLE_SOMBRE + 4*"█" + SOL2 + 8*"█" + SOL1 + 6*"█" + BOIS_SOMBRE + 1*"█" + NOIR + 1*"█" + BLEU_SOMBRE + 2*"█" + LIVRE_TURQ + 1*"█" + BLEU_SOMBRE + 2*"█" + NOIR + 1*"█" + BLEU_SOMBRE + 2*"█" + LIVRE_TURQ + 1*"█" + BLEU_SOMBRE + 2*"█" + BOIS_SOMBRE + 5*"█" + SOL2 + 3*"█" + GRIS + 3*"█" + GRIS_SOMBRE + 1*"█" + SOL2 + 1*"█" + SOL1 + 5*"█" + NOIR + 1*"█" + ECRAN + 7*"█" + ECRAN2 + 1*"█" + ECRAN + 4*"█" + NOIR + 1*"█" + SOL1 + 5*"█" + SOL2 + 1*"█" + GRIS + 1*"█" + SOL2 + 1*"█" + FEUILLE + 2*"█" + FEUILLE_SOMBRE + 3*"█" + SOL1 + 8*"█" + SOL2 + 4*"█" + RESET,
    SOL2 + 4*"█" + SOL1 + 4*"█" + FEUILLE + 1*"█" + FEUILLE_SOMBRE + 4*"█" + SOL2 + 7*"█" + SOL1 + 8*"█" + BOIS_CLAIR + 14*"█" + BOIS_SOMBRE + 3*"█" + SOL2 + 4*"█" + GRIS + 1*"█" + LIVRE_ORANGE + 1*"█" + GRIS + 1*"█" + GRIS_SOMBRE + 1*"█" + SOL1 + 6*"█" + NOIR + 1*"█" + ECRAN + 8*"█" + ECRAN2 + 1*"█" + ECRAN + 3*"█" + NOIR + 1*"█" + SOL1 + 3*"█" + SOL2 + 3*"█" + GRIS + 1*"█" + SOL2 + 2*"█" + FEUILLE_SOMBRE + 3*"█" + SOL1 + 7*"█" + SOL2 + 6*"█" + RESET,
    SOL2 + 2*"█" + SOL1 + 7*"█" + POT + 2*"█" + POT_SOMBRE + 1*"█" + BOIS_CLAIR + 8*"█" + SOL1 + 6*"█" + SOL2 + 2*"█" + BOIS + 14*"█" + BOIS_SOMBRE + 1*"█" + SOL2 + 6*"█" + GRIS + 3*"█" + GRIS_SOMBRE + 1*"█" + BOIS_CLAIR + 6*"█" + NOIR + 14*"█" + BOIS_CLAIR + 6*"█" + GRIS + 1*"█" + BOIS_CLAIR + 2*"█" + POT + 2*"█" + POT_SOMBRE + 1*"█" + BOIS_CLAIR + 4*"█" + SOL1 + 1*"█" + SOL2 + 8*"█" + RESET,
    SOL1 + 7*"█" + BOIS_CLAIR + 2*"█" + POT + 2*"█" + POT_SOMBRE + 1*"█" + BOIS_CLAIR + 7*"█" + BOIS_SOMBRE + 1*"█" + SOL1 + 4*"█" + SOL2 + 2*"█" + OMBRE + 22*"█" + BOIS_CLAIR + 1*"█" + GRIS + 1*"█" + LIVRE_ROUGE + 1*"█" + ECRAN + 1*"█" + GRIS_SOMBRE + 1*"█" + BOIS_SOMBRE + 2*"█" + BOIS_CLAIR + 9*"█" + GRIS + 4*"█" + BOIS_CLAIR + 10*"█" + GRIS_SOMBRE + 3*"█" + BOIS_CLAIR + 1*"█" + POT + 2*"█" + POT_SOMBRE + 1*"█" + BOIS_CLAIR + 3*"█" + BOIS_SOMBRE + 1*"█" + SOL2 + 7*"█" + SOL1 + 2*"█" + RESET,
    SOL2 + 5*"█" + BOIS_CLAIR + 12*"█" + BOIS_SOMBRE + 3*"█" + SOL2 + 2*"█" + SOL1 + 8*"█" + SOL2 + 1*"█" + MUR1 + 1*"█" + BLEU + 8*"█" + MUR1 + 1*"█" + SOL1 + 5*"█" + BOIS_CLAIR + 3*"█" + GRIS + 3*"█" + GRIS_SOMBRE + 1*"█" + BLANC + 2*"█" + GRIS_CLAIR + 1*"█" + BOIS_CLAIR + 6*"█" + GRIS_CLAIR + 8*"█" + BOIS_CLAIR + 16*"█" + BOIS_SOMBRE + 1*"█" + CREME + 7*"█" + SOL2 + 4*"█" + RESET,
    SOL2 + 3*"█" + BOIS + 11*"█" + BOIS_CLAIR + 1*"█" + BOIS_SOMBRE + 5*"█" + SOL1 + 8*"█" + SOL2 + 3*"█" + BLEU_CLAIR + 9*"█" + BLEU_SOMBRE + 1*"█" + SOL1 + 3*"█" + BOIS_CLAIR + 3*"█" + BLANC + 6*"█" + BOIS_CLAIR + 6*"█" + BLANC + 1*"█" + GRIS_CLAIR + 1*"█" + BLANC + 1*"█" + GRIS_CLAIR + 1*"█" + BLANC + 1*"█" + GRIS_CLAIR + 1*"█" + BLANC + 1*"█" + GRIS_CLAIR + 1*"█" + BLANC + 1*"█" + GRIS_CLAIR + 1*"█" + BLANC + 1*"█" + GRIS_CLAIR + 1*"█" + BLANC + 1*"█" + BOIS_CLAIR + 2*"█" + BLEU_SOMBRE + 1*"█" + BOIS_CLAIR + 9*"█" + BOIS_SOMBRE + 1*"█" + BLANC + 7*"█" + CREME + 1*"█" + GRIS_CLAIR + 1*"█" + SOL2 + 4*"█" + RESET,
    SOL2 + 2*"█" + SOL1 + 1*"█" + BOIS + 4*"█" + GRIS_CLAIR + 3*"█" + BOIS + 4*"█" + BOIS_SOMBRE + 6*"█" + SOL1 + 6*"█" + SOL2 + 5*"█" + BLEU_CLAIR + 1*"█" + BLEU + 8*"█" + BLEU_SOMBRE + 1*"█" + SOL1 + 1*"█" + BOIS_CLAIR + 3*"█" + CREME + 6*"█" + BOIS_CLAIR + 6*"█" + GRIS_CLAIR + 1*"█" + BLANC + 1*"█" + GRIS_CLAIR + 1*"█" + BLANC + 1*"█" + GRIS_CLAIR + 1*"█" + BLANC + 1*"█" + GRIS_CLAIR + 1*"█" + BLANC + 1*"█" + GRIS_CLAIR + 1*"█" + BLANC + 1*"█" + GRIS_CLAIR + 1*"█" + BLANC + 1*"█" + GRIS_CLAIR + 1*"█" + BOIS_CLAIR + 2*"█" + BLEU + 2*"█" + BOIS_CLAIR + 8*"█" + BOIS_SOMBRE + 3*"█" + BLANC + 1*"█" + GRIS_CLAIR + 5*"█" + BLANC + 1*"█" + GRIS_CLAIR + 2*"█" + BOIS_CLAIR + 4*"█" + RESET,
    SOL1 + 3*"█" + BOIS + 11*"█" + BOIS_SOMBRE + 6*"█" + SOL1 + 4*"█" + SOL2 + 7*"█" + BLEU_CLAIR + 1*"█" + BLEU + 8*"█" + BLEU_SOMBRE + 1*"█" + BOIS + 38*"█" + BOIS_CLAIR + 1*"█" + BOIS_SOMBRE + 5*"█" + BLANC + 1*"█" + LIVRE_TURQ + 5*"█" + BLANC + 1*"█" + GRIS_CLAIR + 1*"█" + BOIS_CLAIR + 5*"█" + RESET,
    SOL2 + 3*"█" + BOIS_SOMBRE + 17*"█" + SOL2 + 2*"█" + SOL1 + 2*"█" + BLEU + 4*"█" + SOL1 + 2*"█" + SOL2 + 1*"█" + BLEU_CLAIR + 1*"█" + BLEU_SOMBRE + 5*"█" + BLEU + 4*"█" + BOIS + 3*"█" + BOIS_NOIR + 22*"█" + BOIS_SOMBRE + 1*"█" + BOIS + 12*"█" + BOIS_SOMBRE + 5*"█" + BOIS_CLAIR + 12*"█" + BOIS_SOMBRE + 2*"█" + RESET,
    SOL2 + 3*"█" + BOIS + 11*"█" + BOIS_SOMBRE + 5*"█" + SOL2 + 1*"█" + SOL1 + 5*"█" + BLEU_SOMBRE + 2*"█" + SOL1 + 1*"█" + SOL2 + 3*"█" + BLEU_CLAIR + 1*"█" + BLEU + 6*"█" + BLEU_SOMBRE + 3*"█" + BOIS + 3*"█" + BOIS_NOIR + 22*"█" + BOIS_SOMBRE + 1*"█" + BOIS + 4*"█" + GRIS_CLAIR + 3*"█" + BOIS + 5*"█" + BOIS_SOMBRE + 3*"█" + BOIS + 11*"█" + BOIS_CLAIR + 1*"█" + BOIS_SOMBRE + 4*"█" + RESET,
    SOL2 + 2*"█" + SOL1 + 1*"█" + BOIS + 4*"█" + GRIS_CLAIR + 3*"█" + BOIS + 4*"█" + BOIS_SOMBRE + 3*"█" + SOL2 + 1*"█" + SOL1 + 7*"█" + BLEU_SOMBRE + 2*"█" + SOL2 + 4*"█" + BLEU_CLAIR + 1*"█" + BLEU + 6*"█" + BLEU_SOMBRE + 3*"█" + BOIS + 3*"█" + BOIS_NOIR + 22*"█" + BOIS_SOMBRE + 16*"█" + BOIS + 4*"█" + GRIS_CLAIR + 3*"█" + BOIS + 4*"█" + BOIS_SOMBRE + 5*"█" + RESET,
    SOL1 + 3*"█" + BOIS + 11*"█" + BOIS_SOMBRE + 1*"█" + SOL2 + 1*"█" + SOL1 + 8*"█" + SOL2 + 1*"█" + BLEU_SOMBRE + 2*"█" + SOL2 + 3*"█" + BLEU_CLAIR + 11*"█" + BOIS + 3*"█" + BOIS_NOIR + 22*"█" + BOIS_SOMBRE + 1*"█" + BOIS + 4*"█" + GRIS_CLAIR + 3*"█" + BOIS + 5*"█" + BOIS_SOMBRE + 3*"█" + BOIS + 11*"█" + BOIS_SOMBRE + 5*"█" + RESET,
    SOL2 + 2*"█" + OMBRE + 6*"█" + BOIS_CLAIR + 16*"█" + OMBRE + 1*"█" + BLEU_SOMBRE + 2*"█" + SOL1 + 1*"█" + BLEU_CLAIR + 12*"█" + BLEU_SOMBRE + 1*"█" + BOIS + 3*"█" + BOIS_NOIR + 22*"█" + BOIS_SOMBRE + 32*"█" + RESET,
    SOL2 + 4*"█" + SOL1 + 2*"█" + BOIS_CLAIR + 1*"█" + FEUILLE_CLAIR + 1*"█" + LIVRE_VERT + 5*"█" + BOIS_CLAIR + 1*"█" + CREME + 4*"█" + BOIS_CLAIR + 5*"█" + SOL1 + 3*"█" + BLEU + 11*"█" + BLEU_CLAIR + 1*"█" + BLEU_SOMBRE + 2*"█" + BOIS + 4*"█" + BOIS_SOMBRE + 23*"█" + BOIS + 4*"█" + GRIS_CLAIR + 3*"█" + BOIS + 5*"█" + BOIS_SOMBRE + 1*"█" + SOL2 + 2*"█" + BOIS + 11*"█" + BOIS_SOMBRE + 5*"█" + RESET,
    SOL2 + 2*"█" + SOL1 + 2*"█" + BOIS_CLAIR + 1*"█" + LIVRE_VERT + 2*"█" + FEUILLE_CLAIR + 1*"█" + LIVRE_VERT + 3*"█" + BOIS_CLAIR + 2*"█" + BLANC + 4*"█" + BOIS_CLAIR + 4*"█" + SOL1 + 5*"█" + BLEU + 11*"█" + BLEU_SOMBRE + 1*"█" + OMBRE + 44*"█" + BOIS + 4*"█" + GRIS_CLAIR + 3*"█" + BOIS + 4*"█" + BOIS_SOMBRE + 3*"█" + SOL2 + 2*"█" + RESET,
    SOL1 + 2*"█" + BOIS + 16*"█" + BOIS_CLAIR + 1*"█" + SOL1 + 5*"█" + SOL2 + 6*"█" + GRIS_SOMBRE + 2*"█" + SOL1 + 8*"█" + SOL2 + 8*"█" + SOL1 + 8*"█" + SOL2 + 2*"█" + GRIS_CLAIR + 1*"█" + BLANC + 2*"█" + GRIS_CLAIR + 2*"█" + SOL2 + 1*"█" + SOL1 + 8*"█" + SOL2 + 8*"█" + SOL1 + 2*"█" + BOIS + 11*"█" + BOIS_SOMBRE + 1*"█" + SOL2 + 2*"█" + SOL1 + 2*"█" + RESET,
    SOL2 + 2*"█" + OMBRE + 1*"█" + BOIS_SOMBRE + 1*"█" + OMBRE + 4*"█" + BOIS_NOIR + 1*"█" + OMBRE + 7*"█" + BOIS_SOMBRE + 1*"█" + OMBRE + 8*"█" + SOL1 + 5*"█" + GRIS_SOMBRE + 2*"█" + SOL2 + 6*"█" + SOL1 + 8*"█" + SOL2 + 8*"█" + SOL1 + 4*"█" + GRIS + 4*"█" + GRIS_SOMBRE + 1*"█" + SOL2 + 7*"█" + SOL1 + 8*"█" + SOL2 + 2*"█" + OMBRE + 17*"█" + SOL2 + 1*"█" + RESET,
    SOL2 + 2*"█" + OMBRE + 1*"█" + BOIS_SOMBRE + 1*"█" + OMBRE + 12*"█" + BOIS_SOMBRE + 1*"█" + OMBRE + 1*"█" + SOL2 + 2*"█" + SOL1 + 4*"█" + NOIR + 14*"█" + SOL1 + 6*"█" + SOL2 + 8*"█" + SOL1 + 6*"█" + GRIS + 4*"█" + GRIS_SOMBRE + 1*"█" + SOL2 + 5*"█" + SOL1 + 8*"█" + SOL2 + 8*"█" + SOL1 + 8*"█" + SOL2 + 6*"█" + RESET,
    SOL2 + 2*"█" + SOL1 + 1*"█" + BOIS_SOMBRE + 1*"█" + SOL1 + 6*"█" + SOL2 + 6*"█" + BOIS_SOMBRE + 1*"█" + SOL2 + 1*"█" + SOL1 + 6*"█" + NOIR + 1*"█" + SOL1 + 1*"█" + SOL2 + 2*"█" + NOIR + 1*"█" + SOL2 + 2*"█" + NOIR + 1*"█" + SOL2 + 2*"█" + NOIR + 1*"█" + SOL1 + 2*"█" + NOIR + 1*"█" + SOL1 + 4*"█" + SOL2 + 8*"█" + SOL1 + 8*"█" + GRIS + 4*"█" + GRIS_SOMBRE + 1*"█" + SOL2 + 3*"█" + SOL1 + 8*"█" + SOL2 + 8*"█" + SOL1 + 8*"█" + SOL2 + 8*"█" + RESET,
    SOL1 + 3*"█" + BOIS_SOMBRE + 1*"█" + SOL1 + 4*"█" + SOL2 + 8*"█" + BOIS_SOMBRE + 1*"█" + SOL1 + 7*"█" + SOL2 + 8*"█" + SOL1 + 8*"█" + SOL2 + 8*"█" + SOL1 + 8*"█" + SOL2 + 1*"█" + OMBRE + 7*"█" + SOL1 + 8*"█" + SOL2 + 8*"█" + SOL1 + 8*"█" + SOL2 + 8*"█" + SOL1 + 2*"█" + RESET,
]