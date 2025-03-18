end = False

p = 0 #contador de positivos
n = 0 #contador de negativos
pSuma = 0 #suma de positivos
nSuma = 0 #suma de negativos

while end == False:
    
    entrada = int(input("Ingrese un número entero positivo o negativo: "))
    
    if entrada > 0:
        pSuma = entrada + pSuma
        p = p + 1
        print(f"el número {entrada} es positivo")
        
    elif entrada < 0:
        nSuma = entrada + nSuma
        n = n + 1
        print(f"el número {entrada} es negativo")
    
    elif entrada == 0:
        end = True
    
   
if p == 0:
    print("no hay números positivos")
    print(f"la cantidad de números negativos es {n} y el promedio es {nSuma/n}")
    
elif n == 0:
    print(f"la cantidad de números positivos es {p} y el promedio es {pSuma/p}")
    print("no hay números negativos")
    
else:        
    print(f"la cantidad de números positivos es {p} y el promedio es {pSuma/p}") 
    print(f"la cantidad de números negativos es {n} y el promedio es {nSuma/n}")