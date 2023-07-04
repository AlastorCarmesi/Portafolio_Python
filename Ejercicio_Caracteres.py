'''
Crear un programa, que tenga una variable con la cadena “Te quiero solo como amigo”, 
y muestre la siguiente información:

• Imprima los dos primeros caracteres.

• Imprima los tres últimos caracteres.

• Imprima dicha cadena cada dos caracteres. Ej.: Si la cadena fuera “recta” 
debería imprimir rca

• Dicha cadena en sentido inverso. Ej.: Si la cadena fuera hola mundo! 
debe imprimir !odnum aloh

• Imprima la cadena en un sentido y en sentido inverso. 
Ej: Si la cadena es “reflejo” imprime reflejoojelfer.

'''

Cadena = "Te quiero como amigo"

print("Debanado de caracteres mostrando los dos primeros caracteres: ", Cadena[0:2])
print("Debanado de caracteres mostrando los tres ultimos caracteres: ", Cadena[-3: ])
print("Debanado de caracteres en dos en dos: ", Cadena[: : 2])
print("Al revez:", Cadena[: : -1])
print("Reflejo: ", Cadena+Cadena[: : -1])

'''

Ejercicio 2:
Crear un programa que tenga una variable con la cadena “Separado” y un carácter de coma (,); 
e inserte el carácter entre cada letra de la cadena. 
Ej: separar y , debería devolver s,e,p,a,r,a,r
'''
Cadena1 = "Hola Mundo"
Rem = Cadena1.replace("",",")
print("Separacion mediante replace: ", Rem)
