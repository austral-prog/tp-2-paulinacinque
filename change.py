def change():
    expense = 23.75
    money = 100
    vuelto = money - expense
    pesos = int(vuelto)
    centavos = int((vuelto - pesos) * 100)
    print(f"Ingresar gasto:{expense}")
    print(f"Dinero recibido:{money}")
    print("Vuelto:")
    print(f"Pesos:{pesos}")
    print(f"Centavos:{centavos}")
