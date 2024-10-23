def je_prvocislo(cislo):
    """
    Funkce overi, zda zadane cislo je nebo neni prvocislo a vrati True nebo False

    Prvocislo je takove cislo vetsi nez 1, ktere neni delitelne zadnym jinym cislem jenom 1 a samo sebou.
    """
    if cislo <= 1:
        return False
    for i in range(2, int(cislo ** 0.5) + 1):
        if cislo % i == 0:
            return False
    return True

def vrat_prvocisla(maximum):
    """
    Funkce vrátí seznam všech prvočísel od 1 do zadaného maxima (včetně).
    """
    seznam_prvocisel = []
    for cislo in range(2, maximum + 1):
        if je_prvocislo(cislo):
            seznam_prvocisel.append(cislo)
    return seznam_prvocisel

if __name__ == "__main__":
    cislo = int(input("Zadej maximum: "))  # Ošetření vstupu jako celé číslo
    prvocisla = vrat_prvocisla(cislo)
    print(prvocisla)
