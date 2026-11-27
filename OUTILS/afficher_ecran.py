# cette fontion prend en argument nos 4 zones d'affichage (listes) et les affiches sur le terminal

def f(z1: list, z2: list, z3: list, z4: list) -> None:
    res: None = None
    print("\033[H\033[J", end="")

    for i in range(32):
        print(z1[i], z2[i])
    for i in range(9):
        print(z3[i], z4[i])

    return res