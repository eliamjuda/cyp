
#include <stdio.h>

# int main()
# {
#     int valor = 0;
    
#     printf("---------- con do-while -----------");
#     do{
#         printf("Dame un valor entero: ");
#         scanf("%i",&valor);
#     } while( valor != 0 );

#     return 0;
# }

# ------------------------------------ MODULARIDAD (Funciones) ----------------------------

# Una función es una unidad de código reutilizable
# además de ser un mecanismo para organizar código.

# La gran ventaja de emplear funciones es simplificar la programación

# Estructura 

# Una función puede tomar cualquier cantidad de parámetros de entrada (de cualquier tipo) y retorna únicamente
# un sólo valor.
# Un parámetro de entrada es un valor que recibe la función para realizar sus operaciones.

# def multiplica(val1, val2):
#   return val1 * val2
# multiplica(3, 5)

# nombre = input("¿Cuál es tu nombre? ")
# def saludos(val1):
#     return print(f"¡Hola {val1} !")
# saludos(nombre)

# Con una función se pueden hacer 2 cosas:
# 1. Definirla
# 2. Invocarla
# La gran ventaja de tener una función declarada es que la podemos reutilizar cuando se desee.

# def sumar(op1, op2):
#     return print(op1+op2)
# sumar(2,2)

# def imprimeCuadro():
#     print("*********")
#     print("*********")
#     print("*********")
#     print("*********")

# imprimeCuadro()

# Regla de oro: Una función siempre retorna un sólo valor. Inclusive si ese valor es el vacío.

# La palabra reservada None de python
# Ésta palabra reservada significa vacío
# equivalente a la palabra reservada void del lenguaje C, C++ y Java.
# Se usa para indicar ya sea un return vacío o que se recibe como parámetro un vacío.

# def multiplicar( valor , veces ):
#     if valor == None:
#         return print(-1)
#     else:
#         return print(valor * veces)

# multiplicar(5,5)

# Parámetros y argumentos.
# Son conceptos relacionados y su diferencia está centrada en el momento que se emplea en una función.

# Es decir en la función sumar de arriba cuando se declara se le llama parámetro y cuando se invoca se le llama argumento.

# Arumentos posicionales
# En python es posible determinar a qué parámetros están dirigidos los argumentos según su posición.
num1 = 25
num2 = 5

def dividir( op1, op2 ):
    return print(op1 / op2)
    
dividir(num1, num2)