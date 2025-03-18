n = int(input("Número límite para la serie: "))

penultimo = 0

ultimo = 1

i = 2

print(penultimo)

print(ultimo)

while i < n:
    
    suma = penultimo + ultimo
    penultimo = ultimo
    ultimo = suma
    
    if ultimo <= n:
        
        print(ultimo)
        
    i = i + 1
