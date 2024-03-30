# pylint: disable=invalid-name
#   EJERCICIO:
#   - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
#     Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
#     (Ten en cuenta que cada lenguaje puede poseer unos diferentes)
#   - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
#     que representen todos los tipos de estructuras de control que existan
#     en tu lenguaje:
#     Condicionales, iterativas, excepciones...
#   - Debes hacer print por consola del resultado de todos los ejemplos.
#  
#   DIFICULTAD EXTRA (opcional):
#   Crea un programa que imprima por consola todos los números comprendidos
#   entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
#  
#   Seguro que al revisar detenidamente las posibilidades has descubierto algo nuevo.

# OPERADORES ARITMETICOS
operadorSuma = 9 + 3
operadorResta = 9 - 3
operadorMultiplicacion = 9 * 3
operadorDivision = 9 / 3
operadorModulo = 9 % 3
operadorPotencia = 9 ** 3
operadorDivisionEntera = 9//4

print("\nOperadores Aritmeticos")
print('Suma : ',operadorSuma)
print(f'Resta : {operadorResta}')
print("Multiplicacion : ", operadorMultiplicacion)
print("Division : ", operadorDivision)
print("Modulo : ", operadorModulo)
print("Potencia : ", operadorPotencia)
print("Division Entera : ", operadorDivisionEntera)

#OPERADORES RELACIONALES
print("\nOperadores relacionales")
print("12 > 3 : " ,12>3)
print("12 < 3 : " ,12<3)
print("12 == 3 : ",12==3)
print("12>=3", 12>=3)
print("12<=3", 12<=3)
print("12!=3", 12!=3) #Devuelve True si ambos operandos no son iguales
