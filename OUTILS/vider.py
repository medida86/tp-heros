# cette fonction permet de remettre la zone principale a vide ou la zone de dialogue

def f(zone: list) -> list:
    res: list = zone

    for i in range(1, len(res)-1):
        res[i] = "│" + (98*" ")  + "│"

    return res