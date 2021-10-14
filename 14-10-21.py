carrera = "Ingeniería en Computación"

print(carrera)
print(carrera[-1])
print(carrera[-25])

# A la sintáxis escrita para elegir un elemento de un grupo de datos 
# se le llama selector
# En el caso de Strngs y listas (lst) se usan los caracteres []

# 1.- En todos los lenguajes los arreglos inician en 0
# 2.- En python no existe el tipo de dato arreglo, el concepto se sustituye por listas
# 3.- Los strings se comportan como un arreglo en la mayoría de los lenguajes
# 4.- En python se acepta el indexado negativo, en otros


# Slicing (rebanado) de cadenas
# Permite seleccionar subcadenas con el operador:
    # [inicio : stop : incremento]
    # - El stop no se incluye, por eso debemos agregar una posición extra

print(carrera[-11::])

#otro ejercicio de incremento

print(carrera[0:10:2])
print(carrera[-1:-12:-1])

# dir() y help() funciones para obtener ayuda del lenguaje python
#  dir muestra las funciones de un tipo de dato como resumen
# help muestra la misma ayuda pero a detalle

frutas = "limon , fresa, manzana  , aguacate  "
print(frutas)
print(frutas[0::1].upper())

frutas2 = frutas[0::1].upper()
print(frutas2)
print(frutas)

print(frutas.split(","))
print(frutas.index("n"))

print('"jose"')


