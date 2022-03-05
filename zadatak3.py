def unos():
    global x1
    global x2
    global y1
    global y2
    x1 = (input("X koordinata prve točke: "))
    y1 = (input("Y koordinata prve točke: "))
    x2 = (input("X koordinata druge točke: "))
    y2 = (input("Y koordinata druge točke: "))
def racun():
    a = float(y2) - float(y1)
    b = float(x1) - float(x2)
    c = a*(float(x1)) + b*(float(y1))
    print("Jednadžba pravca je y= -(",a/b,")*x +", c/b)
def funkcija():
    unos()
    a = 0
    lista = []
    lista2 = []
    lista.append(x1)
    lista.append(x2)
    lista.append(y1)
    lista.append(y2)
    for i in lista:
        try:
            b = float(i)
            lista2.append(b)
        except ValueError:
            pass
    for e in lista2:
        if isinstance(e, float):
            a += 1
    if a == 4:
        racun()
    else:
        print("Pogrešan unos, unesite ponovno:")
        funkcija()
funkcija()