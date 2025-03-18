n = int(input("ingrese el número a convertir: "))

c = str(n)

numero = ""

for i in c:
    
    if int(i) + 1 > 9:
        numero = numero + "0"
        
    else:
        numero = numero + str(int(i)+1)
        
print(numero)