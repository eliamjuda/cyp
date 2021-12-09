# Para abrir un archivo ya sea para lectura o escritura se usa la función open

# from typing import final


# open( fileobj , 'XY' )

# Donde file object es el nombre del archivo a abrir, y el segundo argumento de la función, está formado
# por un par de letras. La primer letra establece el tipo de apertura del archivo:

# 1. r Lectura
# 2. w Escritura
# 3. x Escritura exclusiva, es decir, sólo en el caso que el archivo no exista.
# 4. a Append Datos al final

# El segundo caracter indica el formato del archivo:

# 1. t Formato del texto
# 2. b Formato binario

# archivo = open("ejemplo1.txt", "wt")

# for x in range( 10 ):
#     archivo.write("Hola mundo " + str(x) + "\n")


# cont = archivo.write("Otra cosa")
# archivo.close()


# La función write escribe datos en un archivo abierto para modificación o escritura,
# para ello utiliza un cursor al siguiente byte dentro del archivo.
# Cuando el archivo se abre, se crea este apuntador y se posiciona para moverse de forma automática cada vez que escribimos.

# La función write regresa un valor entero que indica el número de caracteres escritos en el archivo.


# Lectura de un archivo
# Para leer un archivo con programación
# se puede emplear una de tres opciones (funciones):

# 1. read() lee todo el archivo y lo regresa como texto.
# 2. readline() Lee una sola línea hasta encontrar el sig. salto de línea y la regresa como string.
# 3. readlines() lee todo el archivo y lo regresa como una lista de texto separada por saltos de línea


# archivo = open("ejemplo1.txt", "wt")

# for x in range( 10 ):
#     archivo.write("Hola mundo " + str(x) + "\n")


# cont = archivo.write("Otra cosa")
# archivo.close()

# archivo1 = open("ejemplo1.txt", "rt")
# datos = archivo1.read()
# separados = datos.split("\n")

# for index in range( len(separados) ):
#     if index % 2 == 0:
        # print(separados[index].upper())
    # else:
        # print(separados[index].lower())

# print("--> ",datos," <--")

# archivo2 = open("ejemplo1.txt", "rt")
# for x in range( 11 ):
#     if x % 2 == 0:
#         print(archivo2.readline().upper(), end="")
#     else:
#         print(archivo2.readline().lower())

# archivo3 = open("ejemplo1.txt", "rt")
# lineas = archivo3.readlines()
# print(lineas)

# for texto in lineas:
#     print( texto.rstrip() )

archivo4 = open("ejemplo2.txt", "rt")

lineas = archivo4.readlines()
suma = 0
for linea in lineas[:len(lineas)-1 :]:
    for numero in linea.strip().split(','):
        suma += int(numero.strip())

print(suma)