cadena0 = "texto de ejemplo hola mundo" #Se pueden usar estos comandos dentro de cadenas entre ""
cadena1 = 'Texto \'de\' ejemplo' #Usar la diagonal invertida para agregar signos
cadena2 = 'Texto \nde ejemplo de salto de linea' #Usar la diagonal invertida y n para realizar un salto de linea
cadena3 = 'Texto de \t ejemplo de tabulacion' #uso de diagonal invertida y t para tabular
cadena4 = 'Hola '
cadena5 = 'Mundo'

print("Ejemplos de comandos: ", cadena3)

#Suma aritmetica con cadenas 
print("Combinacion de cadenas: ", cadena4 + cadena5)

#Multiplicacion aritmetica con cadenas
print("Multiplicacion: ",cadena5 * 5)

#Debanado de cadenas 
print("Debanado de cadena: ", cadena0[0 : 5]) #permite asignar la poscicion de 0 a X depende de la cantidad de la cadena y obtiene el valor como tambien los espacios
print("Debanado de cadena: ", cadena0[-5 : ]) #se asigna una pocision negativa de la cadena 
#Metodos aplicados en cadenas 
print("Minuscula: ", cadena0.lower()) #Convierte en minusculas a la cadena
print("Mayuscula: ", cadena0.upper()) #Convierte en Mayusculas a la cadena
print("Conversion: ", cadena0.capitalize()) #convierte la primera letra de la cadena en mayuscula 
print("Titulo: ", cadena0.title()) #en cada letra inicial de una palabra los convierte en mayuscula
