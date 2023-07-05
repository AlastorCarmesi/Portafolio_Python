'''
En este programa se creara la formula general
'''

#importamos 
from math import sqrt #Esta funcion permite sacar las raices cuadradas

#print(sqrt(100)) #daremos la funcion de raiz cuadrada

A = int(input("Ingresa el digita A: "))
B = int(input("Ingresa el digita B: "))
C = int(input("Ingresa el digita C: "))
x1 = 0
x2 = 0

#Crearemos una condicional IF donde analizamos si la ecuacion es correcta para su proceso 
if((B**2)-(4*A*C)) < 0:
    print("Los datos proporcionados imposibilitan resolver la ecuacion")

else:
    x1 = (-B + sqrt((B**2)-(4*A*C))/(2*A))
    x2 = (-B - sqrt((B**2)-(4*A*C))/(2*A))
    #Se muestra 
    print("La solucion es: \nX1=", x1, "\nX2=",x2)