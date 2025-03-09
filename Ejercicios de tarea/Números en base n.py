n = int(input("Número a representar (entero): "))                          #El número a representar
b = int(input("Base nueva en la que se desea representar: "))              #La base con la que se trabaja
m = 0                                                                      #La respuesta del programa
fact = 1                                                                   #Variable que se encargará de las posiciones de los números
if 2 <= b < 10:                                                            #La base ingresada debe estar entre 2 y 9
    print(n)                                                               #Demuestra el proceso de conversión en la consola
    while n > 0:                                                           #Función "mientras" para operar
        z = n                                                              #Define una variable entera "z" a partir de "n" para poder operar
        r = z % b                                                          #Define variable a partir del residuo entre "z" y "b"
        print(r)                                                           #Demuestra la evolución del programa
        n = z // b                                                         #Va convirtiendo "n" dependiendo del valor de "b"
        m = m + (fact * r)                                                 #Se encarga de construir el número en la base deseada
        fact = fact * 10                                                   #Se encarga de la posición de cada dígito convertido
    print (f"Número final convertido: {m}")                                #La respuesta final del programa
else:                                                                      #Si no escoje variable entre 2 y 9 mostrar aviso
    print("La base debe ser un número de 2 a 9")