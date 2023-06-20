#Operaciones con variables
Num1 = 2
Num2 = 3

#Operaciones
Sum = Num2 + Num1
Rest = Num1 - Num2
RestNeg = Num2 - Num1
Mult = Num1 * Num2
Div = Num2/Num1
Porc = Num1 % Num2

Oper_Compl = Num2+23*56+Num1

Exp = (Num1**3) #Este tipo de operacion pertenece al cubo o al cuadrado

Div_NoFloat = Num2 // Num1

#Resultados
print("Suma:", Sum, 
      "Rest", Rest, 
      "Resta con resultado negativo: ",RestNeg,
      "Multiplicacion: ",Mult, 
      "Division: ", Div,
      "Porcentaje:", Porc)

print("Resultado de operacion compleja:",Div_NoFloat)