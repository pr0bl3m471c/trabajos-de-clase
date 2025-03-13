n = int(input("¿Cuántos valores numéricos desea ingresar? "))                       #Se solicita una variable entera

suma = 0                                                                            #Se define una variable "suma" en cero
a = 0                                                                               #Se define una variable "a"

for i in range(1,n+1):                                                              #Bucle "for" que llega hasta que i vale
    
    x = int(input(f"valor {i}: "))                                                  #Se solicitan los números pares que se promediaran

    if x % 2 == 0:                                                                  #Se calcula si el número ingresado es par o impar
        suma = suma + x                                                             #Se van sumando los números pares
        a = a + 1                                                                   #Se va aumentando el contador que cuenta los números pares

promedio = suma / a                                                                 #Se calcula el promedio
print ("El promedio de los números pares que ingresaste es: " + str(promedio))      #Se imprime el resultado del promedio