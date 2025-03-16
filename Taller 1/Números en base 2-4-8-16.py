n = int(input("insterte un número para representar: "))


base = int(input("Seleccione la base a la que desea presentar el número (opciones: 2 - 4 - 8 - 16): "))

#variables 

m = 0 
fact = 1
hex = ""

if base == 2 or base == 4 or base == 8:
    
    while n > 0:
        
        z = n
        r = z % base
        n = z / base
        m = m + (fact * r)
    print(f"el número {n} en base {base} es {m}")
    
elif base == 16:
    
    while n > 0:
        
        z = n
        r = z % base
        
        if r < 10:
            
            hex = str(r) + hex
            
        elif r == 10:
        
            hex = "A" + hex
            
        elif r == 11:
            
            hex = "B" + hex
            
        elif r == 12:
            
            hex = "C" + hex
            
        elif r == 13:
            
            hex = "D" + hex
            
        elif r == 14:
            
            hex = "E" + hex
            
        elif r == 15:
            
            hex = "F" + hex
            
        n = z // base
        
    print(hex)
    
else:
    print("ingrese una base válida")