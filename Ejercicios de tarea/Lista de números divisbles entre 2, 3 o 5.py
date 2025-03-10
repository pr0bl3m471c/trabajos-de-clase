n = int(input("número hasta el que debe llegar la lista: "))                 #Solicita el ingreso de un número entero "n"

for i in range (n+1):                                                        #Bucle "for" para iterar hasta que llegue al valor de n
    if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:                               #Condicional "if" que evalúa que el número ingresado sea divisble entre 2, 3 o 5
        print(i)                                                             #Imprime la respuesta en la consola