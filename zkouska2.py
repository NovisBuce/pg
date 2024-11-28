def operace(typ, a , b):
    matem_operace == 0
    if typ == "+":
        matem_operace = a + b
    elif typ == "-":
        matem_operace = a - b
    elif typ == "*":
        matem_operace = a * b
    elif typ == "/":
        matem_operace = a / b

    

if __name__ == "__main__":
    operace("+", 1, 2)
    operace("-", 2, 1)
    operace("*", 0, 5)
    operace("/", 4, 2)