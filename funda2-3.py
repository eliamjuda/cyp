pelicula = {
    "nombre": {
        "ingles": "Fight Club",
        "espanol": "Club de la Pelea"
    },
    "año":{ 
        "1999" 
    },
    "genero":{ 
        "drama "
    },
    "duracion": {
        "2h 19m"
    },
    "estreno":{
        "5 de noviembre 1999"
    },
    "calificacion":{
        "imdb": 8.8,
        "rottenTomatoes": "79%",
        "google": "92%"
    },
    "personajes":{
        "Narrador": ["Brad Pitt", "Edward Norton"],
        "Marla Singer": "Helena Bonham",
        "Cara de Ángel": "Jared Leto",
        "Meat Loaf": "Robert Paul",
        "El Mecánico": "Holt McCallany"
    },
    "director":{
        "David Fincher"
    },
    "sinopsis":{
        "Un empleado de oficina insomne, harto de su vida, se cruza con un vendedor peculiar. Ambos crean un club de lucha clandestino como forma de terapia y, poco a poco, la organización crece y sus objetivos toman otro rumbo."
    }
}

# print(pelicula["personajes"])

# Estructuras de control de programación 
# Se puede crear cualquier tipo de algoritmo empleando sólamente 3 estructuras de control:

#     1. Secuencia:
#         - La representación de la memoria de programa (Arquitectura Vonn Newman)
#     2. Selección:
#         - Es la estructura de control que decide si un bloque de programa se ejecuta o no.
#           También permite seleccionar, ejecutar un bloque entre un conjunto de opciones.
#           En resumen tenemos: Selección simple, selección con bifurcación y selección múltiple.
#     3. Repetición:
#         - Este tipo de estructuras nos permite automatizar la ejecución repetitiva de código
#           mientras ciertas condiciones se cumplan, tenemos 3 variantes de ésta estructura en 
#           todos los lenguajes de programación:
#          
#           - Desde... hasta (estructura for)
#           - haz mientras (while)
#           - haz y luego validas (do-while)


# Estructura de selección simple

# CAL = float(input("Calificación: "))

# if CAL > 8 :
#     print("Aprobado")
# else:
#     print("No eres mayor de edad")

SUE = float(input("Escribe el sueldo: "))
AUM = 0 
MSUE = 0

if SUE < 1000 :
    AUM = SUE* 0.15
    MSUE = SUE + AUM
    print(MSUE)



