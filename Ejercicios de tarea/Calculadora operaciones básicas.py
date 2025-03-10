salir = False                                            #Define una variable "salir" como falsa

while salir == False:                                    #Bucle "while" mientras "salir" continue como falsa
 
    
    #Estas líneas representan un menú interactivo que demuestra los caracteres para cada operación
    print("¿Qué operación desea realizar?")              
    print("Suma: +")
    print("Resta: -")
    print("Producto: *")
    print("División: /")
    print("Salir: x")
    operación = input()
    
    #Bloques de código para cada operación
    
    if operación == "+":                                #Bloque de códigos de suma
        n1 = float(input("Primer número: "))            
        n2 = float(input("Segundo número: "))
        print(n1 + n2)
    elif operación == "-":                              #Bloque de códigos de resta
        n1 = float(input("Primer número: "))
        n2 = float(input("Segundo número: "))
        print(n1 - n2)
    elif operación == "*":                              #Bloque de códigos de multiplicación
        n1 = float(input("Primer número: "))
        n2 = float(input("Segundo número: "))
        print(n1 * n2) 
    elif operación == "/":                              #Bloque de códigos de división
        n1 = float(input("Primer número: "))
        n2 = float(input("Segundo número: "))
        print(n1 / n2)
    elif operación == "x" or operación == "X":          #Código que permite la salida del programa
        salir = True
    else:
        print("[SELECIÓN INVÁLIDA] [VUELVA A INTENTAR]")#Código que sale cuando no se cumple ninguna condición anterior