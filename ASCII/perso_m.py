cheveux: str = "\033[38;2;100;65;23m"
peau: str = "\033[38;2;245;222;179m"
yeux: str = "\033[38;2;50;120;220m"
bouche: str = "\033[38;2;219;11;42m"
vetements: str = "\033[38;2;60;90;140m"
fin: str = "\033[0m"

dessin = [
    f"  {cheveux}█████████████████{fin}",
    f"{cheveux}████████████████████{fin}",
    f"{peau}█████████████████{cheveux}█████{fin}",
    f"{peau}████{yeux}███{peau}████{yeux}███{peau}████{cheveux}███{fin}",
    f"{peau}██████████████████{cheveux}██{fin}",
    f"{peau}██████████████████{fin}",
    f"{peau}███████{bouche}████{peau}███████{fin}",
    f" {peau}████████████████{fin}",
    f"     {peau}████████{fin}",
    f"     {peau}████████{fin}",
    f"{vetements}██████████████████{fin}",
    f"{vetements}██████████████████{fin}"
]