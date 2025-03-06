def dec_to_bin(cislo):
    """
    Funkce prevede cislo na binarni reprezentaci (cislo muze byt str i int).
    Vraci binarni reprezentaci jako retezec (str).
    """
    try:
        cislo = int(cislo)
        
        return bin(cislo)[2:]
    except ValueError:
        raise ValueError("Vstup musí být číslo nebo řetězec reprezentující číslo.")

def test_dec_to_bin():
    """
    Testy pro funkci dec_to_bin.
    """
    assert dec_to_bin("0") == "0"      
    assert dec_to_bin(0) == "0"       
    assert dec_to_bin(1) == "1"       
    assert dec_to_bin("100") == "1100100"  
    assert dec_to_bin(101) == "1100101"    
    assert dec_to_bin(127) == "1111111"    
    assert dec_to_bin("128") == "10000000" 
    assert dec_to_bin(167) == "10100111"   
