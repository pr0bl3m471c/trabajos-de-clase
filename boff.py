n = int(input("ingrese un número mayor que dos: "))

div = 3
x = n

if n > 2:

    while div > 2:
        
        div = 0
        
        for i in range(1, n+1):
            
            if n % i == 0:
                div = div + 1
        n = n + 1
    print("==================================================")
    print(f"el número primo más cercano a {x} es: " + str(n-1))

else:
    print("el número debe ser mayor a dos")        