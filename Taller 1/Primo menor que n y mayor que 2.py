n = int(input("ingresa un número entero: "))
x = n
div = 3

if n > 2:
    while div > 2:
        div = 0
        
        for i in range(1, x+1):
            if x % i == 0:
                div = div + 1
        
        if div > 2:
            x = x - 1
    print(f"el número primo menor más cercano a {n} es {x}")
            
else:
    print("ingresar un número mayor a 2")