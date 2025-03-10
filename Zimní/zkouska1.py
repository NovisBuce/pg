# Příklad 1: Práce s podmínkami a řetězci
# Zadání:
# Napište funkci `find_divisible`, která přijme číslo max_number a dělitel divisor. 
# Funkce vrátí seznam všech čísel menších nebo rovno max_number, která jsou dělitelná beze zbytku dělitelem divisor.
# Příklad: find_divisible(5, 2) vrátí [2, 4].


def find_divisible(max_number, divisor):
    vysledek = []
    for i in range(1, max_number + 1):
        if i % divisor == 0:
            vysledek.append(i)
    return vysledek
    
    

# Unit testy
def test_find_divisible():
    assert find_divisible(25, 5) == [5, 10, 15, 20, 25]
    assert find_divisible(9, 3) == [3, 6, 9]
    assert find_divisible(13, 2) == [2, 4, 6, 8, 10, 12]


if __name__ == "__main__":
    max_number = 100
    divisor = int(input("Enter divisor: "))
    result = find_divisible(max_number, divisor)
    print(f'Numbers divisible by {divisor} less than or equal to {max_number}: {result}')