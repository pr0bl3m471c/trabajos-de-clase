n = int(input("número a revisar: "))

if n ** (1/2) - int(n ** (1/2)) == 0:
    print(f"la raíz cuadrada de {n} es {n ** (1/2)}")

else:
    print(f"el número {n} no tiene raíz")    