'''
Se desea tener un algoritmo que permita determinar y mostrar el promedio que 
ha obtenido un alumno en un determinado curso, 
conociendo las notas de: tres prácticas, el examen parcial y el examen final.

Considere:
PP = ( P1 + P2 +P3 ) / 3 
PROM = ( PP + 2*EP + 3*EF ) / 6

Donde: P1, P2, P3 : Practicas
PP: promedio de práctica
PROM: promedio
EP: examen parcial
EF: examen final
'''
#Importando modulos necesarios
import time

#Promedio de Practicas, ingresamos los datos siendo de tipo float 
P1 = float(input("Calificacion de la primera practica: "))
P2 = float(input("Calificacion de la segunda practica: "))
P3 = float(input("Calificacion de la tercera practica: "))

#Operacion de PP (Promedio de las practicas)
PP = (P1 + P2 + P3)/3
print("Promedio de las practicas:", PP)

#Promedio de los Examenes parcial y final aplicamos la misma funcion 
EP = float(input("Calificacion de examen parcial: "))
EF = float(input("Calificacion de examen final: "))

#Operacion del PROM (Promedio)
PROM = (PP + 2*EP + 3*EF)/6

#Barra de carga 
BAR_LEN = 24
elements = ['-', '\\', '|', '/']

for i in range(BAR_LEN + 1):
    frame = i % len(elements)
    print(f'\r[{elements[frame]*i:=<{BAR_LEN}}]', end='')
    time.sleep(0.2)
print("Calificacion final:", PROM)
