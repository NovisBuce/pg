
def stars_while():
    print('zacatek')

    i = 0

    while i<5:
        print('*')
        i += 1

    print('konec')

def stars_for():
    print('zacatek')

    for i in range(5):
        print('*', i)

    print('konec')

def in_range(min_number, max_number, number):
    if number <= max_number and number >= min_number:
        print('Is in range')
    else:
        print('Is not in range')

in_range(100, 1000, 1)

