# * EJERCICIO:
#  - Crea un comentario en el código y coloca la URL del sitio web oficial del
#    lenguaje de programación que has seleccionado.
#  - Representa las diferentes sintaxis que existen de crear comentarios
#    en el lenguaje (en una línea, varias...).
#  - Crea una variable (y una constante si el lenguaje lo soporta).
#  - Crea variables representando todos los tipos de datos primitivos
#    del lenguaje (cadenas de texto, enteros, booleanos...).
#  - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!"
# 
#  ¿Fácil? No te preocupes, recuerda que esta es una ruta de estudio y
#  debemos comenzar por el principio.


# COMENTARIOS
# https://www.python.org/
# Este es el comentario para una linea
"""
comentario para varia lineas
aunque no es oficial, el interprete ignorá los caracteres que no esten
asignados a una variable
"""
'''
Este tambien sería un comentario de varias lineas
'''

# VARIABLES Y CONSTANTES
variable_1 = 4
CONSTANTE = 3.1416 # En Python no hay constantes, pero usando una variable en mayusculas la comunidad entendera que es una constante

#VARIABLES CON DATOS PRIMITIVOS
v_int = 1 #Entero
v_str = "variable" # String
v_bool = True # Boolean
v_float = 1.5 # Float
v_none = None # Sin valor
v_complex = 1+2j



print(type(v_int))
print(type(v_str))
print(type(v_bool))
print(type(v_float))
print(type(v_none))
print(type(v_complex))

# HOLA MUNDO EN PYTHON
print("Hola mundo desde Python")

import os
print(f'Hola mundo, {os.getlogin()}! How are you?')

# LISTAS
lista = [1,2,3,4,5]
print(type(lista))

# TUPLAS
tupla = (1,2,3,4,5)
print(type(tupla))
# DICCIONARIOS
diccionario ={"Nombre":"Juan","DNI":"12345", "Edad":23}
print(type(diccionario))

# SET
set = {1,2,3,4,5}
print(type(set))
