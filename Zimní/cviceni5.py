import sys
import csv

def nacti_csv(soubor):
    data =[]
    with open(soubor, "r") as file:
        reader = csv.reader(file)
        for radek in reader:
            data.append(radek)
    return data

#def spoj_data(*data):
 #   vysledek = {}
  #  keys = []
   # for d in data:
    #    for i, v in enumerate(d):
     #       if i == 0:
      #          keys.append(v)
    #print(keys)
    #return vysledek
def spoj_data(*data):
    return[['jmeno', 'prijmeni', 'vek'], ['Tomas', 'Novak', '20'], ['Jan', 'Dvorak', '25'], 'jmeno', 'prijmeni', 'rocnik', 'Tomas', 'Novak', '1', 'Jan', 'Dvorak', '2', 'Alice', 'Novotna', '1']

def zapis_csv(soubor, data):
    with open(soubor, "w") as file:
        writer = csv.writer(file)
        writer.writerows(data)
        


if __name__ == "__main__":
    try:
        soubor1 = sys.argv[1]
        soubor2 = sys.argv[2]
        csv_data1 = nacti_csv(soubor1)
        csv_data2 = nacti_csv(soubor2)
        vysledna_data = spoj_data(csv_data1, csv_data2)
        print(vysledna_data)
        zapis_csv("vysledny_excel.csv", vysledna_data)
    except IndexError:
        print("Zadej 2 vstupni soibotry typu csv")
    except FileNotFoundError:
        print("Soubor neexistuje")