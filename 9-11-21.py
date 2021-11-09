# Características de las tuplas
#  - Son datos agrupados
#  - Puede tener 0 a n elementos
#  - No son mutables (no se eliminan o cambian)
#  - Son buenas para almacenar información de consulta
#  - Pueden estar anidadas
#  - Tienen métodos útiles
#  - Se declara usando () ó tuple()

info = ("juan23", "dios1234", "123.232.1.12")
print(info)
print(info[1])

numeros = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
print(numeros[5:11])

cosas = (info, numeros)
print(cosas)
print(cosas[0][2][4:7])

# Métodos de las tuplas
# Son los mismos de las listas pero los que no involucren mutabilidad

# Diccionarios
#     Características de los diccionarios
#     - Agrupan datos per de forma no lineal.
#     - Formado por pares del tipo llave: valor , donde: 
#         -  llave es de tipo string (Siempre)
#         - valor puede ser de cualquier tipo de datos, incluyendo diccionarios
#     - Se seleccionan con la llave de la forma: ["id_llave"]
#     - Son mutables
#     - Son equivalentes al tipo de dato JSON del lenguaje javascript

alumno = {"nombre": "José"}
print(alumno["nombre"])

alumno = {"nombre": "José",
          "nc": "21929392",
          "edad": 18
         }

print(alumno["nombre"].upper())

alumno2 = dict()
alumno2["nombre"] = "josé"

print(alumno2)
alumno2["nc"] = "49129839"
alumno2["edad"] = 18
print(alumno2)

alumno2["edad"] += 1
print(alumno2)

cliente = { "id" : "CT2121",
            "nombre": {
                "nombre_pila": ["José","Eduardo"],
                "paterno": "Pedroza",
                "materno": "Rosales"
            },
            "telefonos": {
                "casa" : 238123912,
                "trabajo" : 2912931,
                "celular" : 9192939919
            },
            "productos": {
                    "ahorros": { "numero_cuenta": "7788", "ahorro": 2500},
                    "tarjetas":[
                        {"tipo": "debito", "saldo": 10000.5},
                        {"tipo": "credito preferente" , "limite": 2500000.5},
                        {"tipo": "lite", "limite": 15000.5}
                    ]
            },
            "direccion":{
                "calle": "Av. central" ,
                "numero": 12345,
                "colonia": "Impulsora",
                "delegacion": "neza",
                "estado": {
                    "clave": 15,
                    "nombre_corto": "EdoMex",
                    "nombre_completo": "Estado de México"
                }
            }
            
}

print(cliente["productos"]["ahorros"]["ahorro"])
print(cliente["direccion"]["estado"]["nombre_completo"].upper())