palabra = input("Palabra a convertir: ")        #Se solicita la variable "palabra" que es una sola palabra
n = len(palabra)                                #calcula la longitud de la varaiable "palabra"
piglatin = ""                                   #Define una variable sin valor o vacía

for i in range(n):                              #Bucle "for" que recorre "palabra" caracter por caracter
    if i == 0:                                 
        l1 = palabra[i]                         #Variable que almacena el primer caracter de "palabra"
    else:
        piglatin = piglatin + palabra[i]        #Código que va formando la palabra sin contar el primer caracter

print(piglatin + l1 + "ay")                     #Resultado final del código