'''
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. 
Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete, 
así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. 
Cada payaso pesa 112 g y cada muñeca 75 g. Un cliente frecuente pide la cantidad de 23 payasos y 54 muñecas, 
realiza un programa que muestre el peso total de toda la venta.
'''
Payaso = 112 #Peso de los payasos
Muñeca = 75 #Peso de las muñecas

#Operaciones necesarias
Cant_Payasos = Payaso * 23  
Cant_Dolls =  Muñeca * 54
print("Resultados:",
      Cant_Payasos,"Peso total de Payasos",
      Cant_Dolls, "Peso total de Muñecas")

#Sumatoria
Sum = Cant_Payasos + Cant_Dolls
print("Total del peso del paquete:", Sum)