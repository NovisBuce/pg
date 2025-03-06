def obvod_ctverce(delka_strany):
    result = delka_strany * 4
    return result

def obsah_ctverce(delka_strany):
    result = delka_strany ** 2
    return result

def pocet_pismen(text, pismeno):
    count = 0
    j = pismeno
    for pismeno in text:
        if j == pismeno:
            count += 1
    return count

def index_pismene(text, pismeno):
    i = 0
    indexy = []
    while i < len(text):
        if text[i] == pismeno:
            indexy.append(i)
        i += 1
    return indexy
    

def fibonachi(maximum):
    s = [1, 1]
    x = s[-2] + s[-1]
    while x <= maximum:
        s.append(x)
        x = s[-2] + s[-1]
    return s

if __name__ == "__main__":
    print(obvod_ctverce(5))
    print(obsah_ctverce(5))
    print(pocet_pismen("ahoj, jak se mas?", "a"))
    print(index_pismene("ahoj, jak se mas?", "a"))
    print(fibonachi(5))