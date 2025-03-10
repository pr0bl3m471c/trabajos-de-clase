frase = input("Ingresa la frase a separar: ")                   #Solicita una frase completa que cuenta como una variable

n = len(frase)                                                  #Calcula la cantidad de caracteres en la frase ingresada
separador = " "                                                 #Define una variable que vale un " " (espacio)
palabra = ""                                                    #Define una variable vacía para que acumule caracteres

for i in range(n):                                              #Bucle "for" que recorre caracter por caracter usando un índice "i"
    if frase[i] == separador:                                   #Condicional "if" que hace que si "frase" termina en un espacio la imprima
        print(palabra)                                          #Imprime la variable "palabra"
        palabra = ""                                            #Resetea el valor de "palabra"
    else:                                                       #Si el caracter actual no es un espacio une los anteriores caractes, formando palabras
        palabra = palabra + frase[i]                            #Operación encargada de ir formando las palabras
print(palabra)                                                  #Imprime el resultado final