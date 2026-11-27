RESET = "\033[0m"
FOND = "\033[38;2;0;25;8m"
HALO = "\033[38;2;0;70;25m"
SOMBRE = "\033[38;2;0;120;40m"
VERT = "\033[38;2;0;200;60m"
CLAIR = "\033[38;2;150;255;170m"
CAPUCHE = "\033[38;2;28;28;32m"
NOIR = "\033[38;2;5;5;5m"
GRIS = "\033[38;2;95;95;100m"
BLANC = "\033[38;2;245;245;238m"
OMBRE = "\033[38;2;190;190;182m"
ROSE = "\033[38;2;225;85;85m"

dessin = [
    FOND + 4*"█" + SOMBRE + 1*"█" + FOND + 7*"█" + SOMBRE + 1*"█" + FOND + 24*"█" + HALO + 6*"█" + GRIS + 12*"█" + HALO + 6*"█" + FOND + 3*"█" + SOMBRE + 1*"█" + FOND + 33*"█" + RESET,
    FOND + 4*"█" + SOMBRE + 1*"█" + FOND + 7*"█" + SOMBRE + 1*"█" + FOND + 21*"█" + HALO + 4*"█" + GRIS + 5*"█" + CAPUCHE + 12*"█" + GRIS + 5*"█" + HALO + 4*"█" + SOMBRE + 1*"█" + FOND + 33*"█" + RESET,
    FOND + 4*"█" + SOMBRE + 1*"█" + FOND + 7*"█" + SOMBRE + 1*"█" + FOND + 19*"█" + HALO + 3*"█" + GRIS + 3*"█" + CAPUCHE + 4*"█" + NOIR + 14*"█" + CAPUCHE + 4*"█" + GRIS + 3*"█" + HALO + 3*"█" + FOND + 32*"█" + RESET,
    FOND + 4*"█" + VERT + 1*"█" + FOND + 7*"█" + VERT + 1*"█" + FOND + 1*"█" + SOMBRE + 1*"█" + FOND + 15*"█" + HALO + 3*"█" + GRIS + 2*"█" + CAPUCHE + 4*"█" + NOIR + 2*"█" + OMBRE + 1*"█" + BLANC + 14*"█" + OMBRE + 1*"█" + NOIR + 2*"█" + CAPUCHE + 4*"█" + GRIS + 2*"█" + HALO + 3*"█" + FOND + 30*"█" + RESET,
    FOND + 4*"█" + VERT + 1*"█" + FOND + 7*"█" + VERT + 1*"█" + FOND + 1*"█" + SOMBRE + 1*"█" + FOND + 13*"█" + HALO + 4*"█" + GRIS + 1*"█" + CAPUCHE + 4*"█" + NOIR + 1*"█" + OMBRE + 1*"█" + BLANC + 20*"█" + OMBRE + 1*"█" + NOIR + 1*"█" + CAPUCHE + 4*"█" + GRIS + 1*"█" + HALO + 4*"█" + FOND + 28*"█" + RESET,
    FOND + 4*"█" + CLAIR + 1*"█" + FOND + 7*"█" + CLAIR + 1*"█" + FOND + 1*"█" + SOMBRE + 1*"█" + FOND + 12*"█" + HALO + 3*"█" + GRIS + 2*"█" + CAPUCHE + 4*"█" + NOIR + 1*"█" + OMBRE + 1*"█" + BLANC + 2*"█" + NOIR + 6*"█" + BLANC + 6*"█" + NOIR + 6*"█" + BLANC + 2*"█" + OMBRE + 1*"█" + NOIR + 1*"█" + CAPUCHE + 4*"█" + GRIS + 2*"█" + HALO + 3*"█" + FOND + 27*"█" + RESET,
    FOND + 14*"█" + VERT + 1*"█" + FOND + 11*"█" + HALO + 3*"█" + GRIS + 2*"█" + CAPUCHE + 4*"█" + NOIR + 1*"█" + OMBRE + 1*"█" + BLANC + 1*"█" + NOIR + 2*"█" + BLANC + 6*"█" + NOIR + 2*"█" + BLANC + 2*"█" + NOIR + 2*"█" + BLANC + 6*"█" + NOIR + 2*"█" + BLANC + 1*"█" + OMBRE + 1*"█" + NOIR + 1*"█" + CAPUCHE + 4*"█" + GRIS + 2*"█" + HALO + 3*"█" + FOND + 10*"█" + SOMBRE + 1*"█" + FOND + 15*"█" + RESET,
    FOND + 14*"█" + VERT + 1*"█" + FOND + 10*"█" + HALO + 3*"█" + GRIS + 2*"█" + CAPUCHE + 4*"█" + NOIR + 2*"█" + OMBRE + 1*"█" + BLANC + 3*"█" + NOIR + 6*"█" + BLANC + 6*"█" + NOIR + 6*"█" + BLANC + 3*"█" + OMBRE + 1*"█" + NOIR + 2*"█" + CAPUCHE + 4*"█" + GRIS + 2*"█" + HALO + 3*"█" + FOND + 9*"█" + SOMBRE + 1*"█" + FOND + 15*"█" + RESET,
    FOND + 14*"█" + CLAIR + 1*"█" + FOND + 10*"█" + HALO + 3*"█" + GRIS + 1*"█" + CAPUCHE + 4*"█" + NOIR + 3*"█" + ROSE + 3*"█" + BLANC + 2*"█" + NOIR + 4*"█" + BLANC + 8*"█" + NOIR + 4*"█" + BLANC + 2*"█" + ROSE + 3*"█" + NOIR + 3*"█" + CAPUCHE + 4*"█" + GRIS + 1*"█" + HALO + 3*"█" + FOND + 9*"█" + SOMBRE + 1*"█" + FOND + 15*"█" + RESET,
    FOND + 24*"█" + HALO + 3*"█" + GRIS + 1*"█" + CAPUCHE + 4*"█" + NOIR + 4*"█" + ROSE + 4*"█" + BLANC + 1*"█" + OMBRE + 4*"█" + BLANC + 3*"█" + OMBRE + 2*"█" + BLANC + 3*"█" + OMBRE + 4*"█" + BLANC + 1*"█" + ROSE + 4*"█" + NOIR + 4*"█" + CAPUCHE + 4*"█" + GRIS + 1*"█" + HALO + 3*"█" + FOND + 8*"█" + VERT + 1*"█" + FOND + 15*"█" + RESET,
    FOND + 24*"█" + HALO + 3*"█" + GRIS + 1*"█" + CAPUCHE + 4*"█" + NOIR + 4*"█" + ROSE + 1*"█" + NOIR + 1*"█" + ROSE + 1*"█" + BLANC + 8*"█" + OMBRE + 4*"█" + BLANC + 8*"█" + ROSE + 1*"█" + NOIR + 1*"█" + ROSE + 1*"█" + NOIR + 4*"█" + CAPUCHE + 4*"█" + GRIS + 1*"█" + HALO + 3*"█" + FOND + 8*"█" + VERT + 1*"█" + FOND + 15*"█" + RESET,
    FOND + 24*"█" + HALO + 3*"█" + GRIS + 1*"█" + CAPUCHE + 4*"█" + NOIR + 4*"█" + OMBRE + 1*"█" + BLANC + 1*"█" + NOIR + 5*"█" + BLANC + 3*"█" + OMBRE + 6*"█" + BLANC + 3*"█" + NOIR + 5*"█" + BLANC + 1*"█" + OMBRE + 1*"█" + NOIR + 4*"█" + CAPUCHE + 4*"█" + GRIS + 1*"█" + HALO + 3*"█" + FOND + 8*"█" + CLAIR + 1*"█" + FOND + 5*"█" + SOMBRE + 1*"█" + FOND + 9*"█" + RESET,
    FOND + 24*"█" + HALO + 3*"█" + GRIS + 1*"█" + CAPUCHE + 4*"█" + NOIR + 5*"█" + OMBRE + 1*"█" + BLANC + 5*"█" + NOIR + 5*"█" + BLANC + 2*"█" + NOIR + 5*"█" + BLANC + 5*"█" + OMBRE + 1*"█" + NOIR + 5*"█" + CAPUCHE + 4*"█" + GRIS + 1*"█" + HALO + 3*"█" + FOND + 12*"█" + SOMBRE + 1*"█" + FOND + 1*"█" + SOMBRE + 1*"█" + FOND + 9*"█" + RESET,
    FOND + 24*"█" + HALO + 3*"█" + GRIS + 1*"█" + CAPUCHE + 4*"█" + NOIR + 5*"█" + OMBRE + 1*"█" + BLANC + 2*"█" + NOIR + 4*"█" + BLANC + 10*"█" + NOIR + 4*"█" + BLANC + 2*"█" + OMBRE + 1*"█" + NOIR + 5*"█" + CAPUCHE + 4*"█" + GRIS + 1*"█" + HALO + 3*"█" + FOND + 12*"█" + SOMBRE + 1*"█" + FOND + 1*"█" + SOMBRE + 1*"█" + FOND + 9*"█" + RESET,
    FOND + 25*"█" + HALO + 3*"█" + GRIS + 1*"█" + CAPUCHE + 3*"█" + NOIR + 6*"█" + OMBRE + 1*"█" + BLANC + 5*"█" + NOIR + 10*"█" + BLANC + 5*"█" + OMBRE + 1*"█" + NOIR + 6*"█" + CAPUCHE + 3*"█" + GRIS + 1*"█" + HALO + 3*"█" + FOND + 13*"█" + SOMBRE + 1*"█" + FOND + 1*"█" + VERT + 1*"█" + FOND + 9*"█" + RESET,
    FOND + 25*"█" + HALO + 3*"█" + GRIS + 2*"█" + CAPUCHE + 3*"█" + NOIR + 6*"█" + OMBRE + 1*"█" + BLANC + 6*"█" + NOIR + 6*"█" + BLANC + 6*"█" + OMBRE + 1*"█" + NOIR + 6*"█" + CAPUCHE + 3*"█" + GRIS + 2*"█" + HALO + 3*"█" + FOND + 13*"█" + VERT + 1*"█" + FOND + 1*"█" + VERT + 1*"█" + FOND + 9*"█" + RESET,
    FOND + 10*"█" + SOMBRE + 1*"█" + FOND + 15*"█" + HALO + 3*"█" + GRIS + 2*"█" + CAPUCHE + 3*"█" + NOIR + 6*"█" + OMBRE + 1*"█" + BLANC + 5*"█" + NOIR + 6*"█" + BLANC + 5*"█" + OMBRE + 1*"█" + NOIR + 6*"█" + CAPUCHE + 3*"█" + GRIS + 2*"█" + HALO + 3*"█" + FOND + 14*"█" + VERT + 1*"█" + FOND + 1*"█" + CLAIR + 1*"█" + FOND + 9*"█" + RESET,
    FOND + 10*"█" + SOMBRE + 1*"█" + FOND + 7*"█" + SOMBRE + 1*"█" + FOND + 8*"█" + HALO + 3*"█" + GRIS + 2*"█" + CAPUCHE + 3*"█" + NOIR + 6*"█" + OMBRE + 1*"█" + BLANC + 5*"█" + NOIR + 4*"█" + BLANC + 5*"█" + OMBRE + 1*"█" + NOIR + 6*"█" + CAPUCHE + 3*"█" + GRIS + 2*"█" + HALO + 3*"█" + FOND + 1*"█" + SOMBRE + 1*"█" + FOND + 1*"█" + SOMBRE + 1*"█" + FOND + 11*"█" + CLAIR + 1*"█" + FOND + 11*"█" + RESET,
    FOND + 10*"█" + SOMBRE + 1*"█" + FOND + 7*"█" + SOMBRE + 1*"█" + FOND + 9*"█" + HALO + 4*"█" + GRIS + 1*"█" + CAPUCHE + 3*"█" + NOIR + 7*"█" + OMBRE + 1*"█" + BLANC + 3*"█" + NOIR + 4*"█" + BLANC + 3*"█" + OMBRE + 1*"█" + NOIR + 7*"█" + CAPUCHE + 3*"█" + GRIS + 1*"█" + HALO + 4*"█" + SOMBRE + 1*"█" + FOND + 1*"█" + SOMBRE + 1*"█" + FOND + 1*"█" + SOMBRE + 1*"█" + FOND + 23*"█" + RESET,
    FOND + 6*"█" + SOMBRE + 1*"█" + FOND + 1*"█" + SOMBRE + 1*"█" + FOND + 1*"█" + VERT + 1*"█" + FOND + 7*"█" + SOMBRE + 1*"█" + FOND + 6*"█" + CAPUCHE + 8*"█" + GRIS + 2*"█" + CAPUCHE + 2*"█" + NOIR + 8*"█" + OMBRE + 1*"█" + BLANC + 1*"█" + NOIR + 4*"█" + BLANC + 1*"█" + OMBRE + 1*"█" + NOIR + 8*"█" + CAPUCHE + 2*"█" + GRIS + 2*"█" + CAPUCHE + 8*"█" + FOND + 1*"█" + SOMBRE + 1*"█" + FOND + 23*"█" + RESET,
    FOND + 6*"█" + SOMBRE + 1*"█" + FOND + 1*"█" + SOMBRE + 1*"█" + FOND + 1*"█" + VERT + 1*"█" + FOND + 7*"█" + VERT + 1*"█" + FOND + 1*"█" + CAPUCHE + 15*"█" + GRIS + 3*"█" + CAPUCHE + 1*"█" + NOIR + 8*"█" + OMBRE + 1*"█" + BLANC + 2*"█" + OMBRE + 1*"█" + NOIR + 8*"█" + CAPUCHE + 1*"█" + GRIS + 3*"█" + CAPUCHE + 15*"█" + FOND + 20*"█" + RESET,
    FOND + 6*"█" + SOMBRE + 1*"█" + FOND + 1*"█" + SOMBRE + 1*"█" + FOND + 1*"█" + CLAIR + 1*"█" + FOND + 4*"█" + CAPUCHE + 23*"█" + GRIS + 5*"█" + NOIR + 12*"█" + GRIS + 5*"█" + CAPUCHE + 23*"█" + FOND + 15*"█" + RESET,
    FOND + 6*"█" + VERT + 1*"█" + FOND + 1*"█" + VERT + 1*"█" + FOND + 1*"█" + CAPUCHE + 33*"█" + GRIS + 12*"█" + CAPUCHE + 33*"█" + FOND + 10*"█" + RESET,
    FOND + 5*"█" + CAPUCHE + 38*"█" + GRIS + 1*"█" + CAPUCHE + 4*"█" + NOIR + 2*"█" + CAPUCHE + 4*"█" + GRIS + 1*"█" + CAPUCHE + 38*"█" + FOND + 5*"█" + RESET,
    CAPUCHE + 43*"█" + GRIS + 1*"█" + CAPUCHE + 4*"█" + NOIR + 2*"█" + CAPUCHE + 4*"█" + GRIS + 1*"█" + CAPUCHE + 43*"█" + RESET,
    CAPUCHE + 43*"█" + GRIS + 1*"█" + CAPUCHE + 4*"█" + NOIR + 2*"█" + CAPUCHE + 4*"█" + GRIS + 1*"█" + CAPUCHE + 43*"█" + RESET,
    CAPUCHE + 43*"█" + GRIS + 1*"█" + CAPUCHE + 4*"█" + NOIR + 2*"█" + CAPUCHE + 4*"█" + GRIS + 1*"█" + CAPUCHE + 43*"█" + RESET,
    CAPUCHE + 43*"█" + GRIS + 1*"█" + CAPUCHE + 4*"█" + NOIR + 2*"█" + CAPUCHE + 4*"█" + GRIS + 1*"█" + CAPUCHE + 43*"█" + RESET,
    CAPUCHE + 48*"█" + NOIR + 2*"█" + CAPUCHE + 48*"█" + RESET,
    CAPUCHE + 48*"█" + NOIR + 2*"█" + CAPUCHE + 48*"█" + RESET,
]