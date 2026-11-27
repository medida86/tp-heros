fin: str = "\033[0m"
cheveux: str = "\033[38;2;184;75;16m"
peau: str = "\033[38;2;245;222;179m"
yeux: str = "\033[38;2;46;178;107m"
bouche: str = "\033[38;2;219;11;42m"

dessin = [
    f"  {cheveux}███████████████████{fin}",
    f" {cheveux}█████████████████████{fin}",
    f"{cheveux}███████████████████████{fin}",
    f"{cheveux}███{peau}█████████████████{cheveux}███{fin}",
    f"{cheveux}███{peau}█████{yeux}██{peau}███{yeux}██{peau}█████{cheveux}███{fin}",
    f"{cheveux}███{peau}█████████████████{cheveux}███{fin}",
    f"{cheveux}███{peau}█████████████████{cheveux}███{fin}",
    f"{cheveux}███{peau}██████{bouche}█████{peau}██████{cheveux}███{fin}",
    f"{cheveux}████{peau}███████████████{cheveux}████{fin}",
    f"{cheveux}█████{peau}█████████████{cheveux}█████{fin}",
    f"{cheveux}██████{peau}███████████{cheveux}██████{fin}",
    f"{cheveux}██████{peau}███████████{cheveux}██████{fin}",
]