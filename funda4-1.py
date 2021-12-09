# Argumento por defecto

from typing import DefaultDict


# Notación donde no se envía argumento, entonces se asgina el que el programador asignó como Default

# def dividir(op1, op2=1):
#     c = op1 / op2
#     return c

# print(dividir(25))

# Este concepto se puede ejemplificar con la función print 
# nombre = "José";
# edad = 18;
# print(nombre, edad, sep='++-++-+-+-+-');

# Argumentos posicionales


# def sumar(op1, op2):
#     return print(op1+op2)
# sumar(2,2)

# def comanda(comensal=1, primer="Consomé", segundo="Arroz rojo", tercero="Enchiladas"):
#     print(f"El comensal {comensal} quiere: ");
#     print("\t Entrada: ",primer);
#     print("\t Medio: ",segundo);
#     print("\t Plato fuerte: ", tercero)

# comanda(3, "Ensalada", "Arroz blanco", "Espárragos al horno")

# Argumentos enviados en grupo en una tupla
# Esto sirve para enviar múltiples argumentos a una función empleando el comodín *.

# def mifun( args* ):
#     <cuerpo de la func>

# def comanda2( *opciones ):
#     print( opciones )
#     print(f"El comensal {opciones[0]} pidió: ")
#     print("\t Entrada: ",opciones[1])
#     print("\t Segundo: ",opciones[2])
#     print("\t Plato juerte: ",opciones[3])
#     for instruccion in opciones[4::]:
#         print(instruccion)

# comanda2( 1, "Sopa de fideo", "Arroz", "Pechuga asada" )

# Argumentos enviados en grupo en un diccionario
# Es el mismo concepto que anterior pero se usa el comodín ** y se mapea a un diccionario

# def comanda3( **opciones ):
#     print(opciones)
#     print(f"El comensal {opciones['comensal']} pidió: ")

# comanda3(segundo="arroz blanco",tercero="Esparragos al horno",primer="Ensalada",comensal=3)


# def comanda3(**opciones):
#     ops = opciones.keys()
#     for key in ops:
#         print(f"{key} = {opciones[key]}")
        
# comanda3(segundo="arroz blanco",tercero="Esparragos al horno",primer="Ensalada",comensal=3)

# # Modularidad y bibliotecas
# Todos los lenguajes de programación tienen la capacidad de compartir código entre la comunidad de programadores.
# Para ello cada lenguaje establece un mecanismo para escribir y compartir bibliotecas

# from simple_chalk import chalk, yellow
# print(chalk.yellow("Hola en color amarillo"))

# martes y jueves 11 a 1
# los demas de 11:30 a 12:50
# miguel angel sanchez hernandez

# ¿Cómo escribo un módulo? (biblioteca)

# Se define en un archivo de biblioteca.

# import mi_modulo

# res = mi_modulo.sumar(7,5)
# print(res)


archivo = open("salida.txt", "wt")
archivo.write("Hola mion")