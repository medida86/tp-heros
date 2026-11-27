# cette fonction permet de print dans une zone, sans decaler les bords

def f(zone: list, ligne: int, text: str) -> list:
    res: list = zone
    largeur: int = len(res[ligne])-2

    if len(text)%2 == 0:
        res[ligne] = "│" + ((largeur//2)-(len(text)//2))*" " + text + ((largeur//2)-(len(text)//2))*" " + "│"
    else:
        res[ligne] = "│" + (int(largeur/2)-(len(text)//2))*" " + text + ((int(largeur//2)-(len(text)//2))-1)*" " + "│"


    return res