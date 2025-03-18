n = int(input("Número para hallar el siguiente término de fibonacci: "))

penultimo = 0

ultimo = 1

i = False

while i == False:
    
    suma = penultimo + ultimo
    penultimo = ultimo
    ultimo = suma
    
    if ultimo > n:
        
        print(ultimo)
        i = True
