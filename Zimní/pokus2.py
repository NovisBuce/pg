# funkce vrati treti prvek ze seznamu
#def vrat_treti(seznam):
   # if len(seznam) <= 2:
    #    return None
    #else:
    #    return seznam[2]



# funkce spocita prumer z hodnot v seznamu
def udelej_prumer(seznam):
    return sum(seznam) / len(seznam)

# funkce naformatuje retezec, aby vratila text ve formatu:
# "Jmeno: Jan, Prijmeni: Novak, Vek: 20, Prumerna znamka: 2.5"
def naformatuj_text(slovnik):
    jmeno = slovnik["jmeno"]
    prijmeni = slovnik["prijmeni"]
    vek = slovnik["vek"]
    return f"Jmeno: {jmeno} Příjmení: {prijmeni} Věk:  {vek} Průměrná známka: {sum(student['znamky'])/len(student['znamky'])}"


if __name__ == "__main__":
    #seznam = [9,8]
    #vysledek = vrat_treti(seznam)
   # print(vysledek)
    obalka = [9,8,7,6,5]
    vysledek = udelej_prumer(obalka)
    print(vysledek)


    print(udelej_prumer([9,8,7,6,5]))
    student = {
        "jmeno": "Matěj",
        "prijmeni": "Dvořák",
        "vek": 21,
        "znamky": [1, 2, 1, 1, 3, 2]
    }

    vysledek = naformatuj_text(student)
    print(naformatuj_text(student))

