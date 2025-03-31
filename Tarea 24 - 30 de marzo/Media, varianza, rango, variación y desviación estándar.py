# IMPORTES
import random as rnd

n = int(input("Ingresa la cantidad de números con los que operar "))
A = []

#Generar números aleatorios
for i in range(n):
    A.append(rnd.randint(0,100))
    
#DEFINICIÓN DE FUNCIONES:

#Media o Promedio
def media(e):
    media = sum(e) / len(e)
    return media

#Varianza
def varianza(e):
    
    sum = 0
    for i in e:
        sum = sum + ((i - media(e))**2)
    varianza = sum / (len(e) - 1)
    
    return varianza

#Desviación estandar
def desviacion(e):
    desviacion = varianza(e)**(1/2)
    
    return desviacion

#Rango
def rango(e):
    rango = max(e) - min(e)
    
    return rango


print(f"La lista generada es:{A}")
print("")
print(f"la media es: {media(A)}")
print("")
print(f"la varianza es: {varianza(A)}")
print("")
print(f"la desviación estandar es: {desviacion(A)}")
print("")
print(f"El rango es: {rango(A)}")

    
    