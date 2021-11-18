# Estructura de selección con bifurcación (if-else)
# Esta estructura selecciona una de dos opcioner de ejecución,
# se ejecuta un bloque si la condición se cumple o se ejecuta otro bloque si la
# condición no se cumple (else).

# if (condicion) :
#     //Bloque de ejecución
# else:
#     //Bloque de ejecución alterno


# edad = int (input("Dame tu edad:"))
# dinero = float (input("¿Cuánto dinero tienes?"))
# if edad >= 18:
#     if dinero >=35:
#         print("Eres mayor de edad y tienes dinero, ten tu cheve")
#     else:
#         print("No tienes suficiente dinero")
# else:
#     print("Eres menor de edad, ten tu Boing")
# print("Fin del programa")


# CAL = float(input("Escribe tu calificación"))
# if CAL >= 8:
#     print("Aprobado")
# else:
#     print("Reprobado")


# SUE = float(input("Escribe el sueldo: "))
# AUM = 0 
# NSUE = 0


# if SUE<1000:
#     NSUE=SUE*1.15
# else:
#     NSUE=SUE*1.12
# print(f"Tu nuevo sueldo es: {NSUE}")

# # Ejercicio if-else
# dia = int(input("Ingresa un número entre 1 y 7: "))
# print(f"Capturaste el número { dia }")

# if dia >= 1 and dia <= 7:
#     if dia == 1:
#         print("Lunes")
#     else:
#         if dia == 2:
#             print("Martes")
#         else:
#             if dia == 3:
#                 print("Miércoles")
#             else:
#                 if dia == 4:
#                     print("Jueves")
#                 else:
#                     if dia == 5:
#                         print("Viernes")
#                     else:
#                         if dia == 6:
#                             print("Sábado")
#                         else:
#                             print("Domingo")
                        
            



# Selección múltiple

# ejemplo 2.7

NUM = int(input("Dame un número entre 1 y 3: "))
V = float(input("Dame un valor float: "))
VAL = 0

if NUM == 1:
    VAL = 100 * V
elif NUM == 2:
    VAL = 100 ** V
elif NUM == 3:
    VAL == 100 / V
else:
    VAL = 0
print(VAL)
