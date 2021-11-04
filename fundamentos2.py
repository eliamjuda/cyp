# Tipos de datos estructurados de python

# 1. Listas
# 2. Tuplas
# 3. Diccionarios
# 4. Conjuntos(opcional)

# Listas
# - Tipo de dato que agrupa variables o valores.
# - Estructura secuencial (indexados o empezando por 0)
# - Se declara de dos formas
#     - usando []
#     - usando list()
# - Puede contener tipos de dato diversos (En otros lenguajes de prog. eso no esposible de forma directa)
# - Los elementos internos se seleccionan con []
# - Soporta slicing
# - Son mutables

numeros = [10, 5,2,3,1]
print(numeros)

numeros2 = list()
numeros2.append(10)
numeros2.append(5)
numeros2.append(2)
numeros2.append(3)
numeros2.append(1)
print(numeros2)

# Tipos diversos
cosas = [12,2,True,"José", 1.57, ["pera", "kiwi", "uva"]]
print(cosas)
print(cosas[3][1:3])
cosas[3] = cosas[3].upper()

numeros = [1,2,3,4,5,6,7,8,9,10,11]
print(numeros)
print(numeros[3:8])
print(numeros[8:10])
print(numeros[::-1])

#Crear una lista con un generador
numeros = [ x for x in range(101) ]

numeros = [4,1,15,8,22,34,50]
numeros.append(99)
print(numeros)

frutas = ["uvas", "kiwi", "manzana"]
copia = frutas.copy()
print(frutas)
print(copia)

nombres = ["jose", "pedro", "karina"]
otrosNombres = [ "josue", "diana", "dalia"]

nombres.extend(otrosNombres)
print(nombres)

nombres.insert(4, "Eliam")
print(nombres)

nombres.pop()
print(nombres)