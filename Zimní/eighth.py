def bin_to_dec(binarni_cislo):
    """
    Funkce spocita hodnotu predavaneho binarniho cisla (binarni_cislo muze byt str i int!!!)
    """
    cislo = str(binarni_cislo)
    cislo = cislo[::-1]  
    vysledek = 0  

    
    for i in range(len(cislo)):
        misto = int(cislo[i])  
        mocnina = 2 ** i       
        decimal = misto * mocnina  
        vysledek += decimal        

    return vysledek

def test_funkce():
    """
    Testovací funkce ověřující správnost bin_to_dec().
    """
    assert bin_to_dec("0") == 0
    assert bin_to_dec(1) == 1
    assert bin_to_dec("100") == 4
    assert bin_to_dec(101) == 5
    assert bin_to_dec("010101") == 21
    assert bin_to_dec(10000000) == 128
    

if __name__ == "__main__":
    test_funkce()

    vstup = input("Zadejte binární číslo: ")
    try:
        vysledek = bin_to_dec(vstup)
        print(f"Binární číslo {vstup} odpovídá desítkovému číslu {vysledek}.")
    except ValueError:
        print("Zadaný vstup není platné binární číslo!")
