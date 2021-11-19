
# ---------------------------------------------------------------------------------------------
# hacer un programa que pida dos numeros enteros y que imprima en pantalla lo siguiente:
# 1. cual de ellos es el numero mayor
# 2. cual de ellos es el numero menor
#  o en su defecto
# Imprimir que los valores son iguales

# NUM1 = int(input("Escribe un número entero: "))
# NUM2 = int(input("Escribe otro número entero: "))

# if NUM1 > NUM2:
#     print(f"El número {NUM1} es el mayor y el número {NUM2} es el menor")
# else:
#     if NUM1 < NUM2:
#         print(f"El número {NUM2} es el mayor y el número {NUM1} es el menor")
#     else:
#         print(f"Los números {NUM1} y {NUM2} son iguales.")
# ---------------------------------------------------------------------------------------------




# ---------------------------------------------------------------------------------------------
# Hacer un programa que solicite  3 numeros enteros diferentes 
# entre sí  y que imprima cual de los 3 es el mayor

# NUM1 = int(input("Ingresa un número entero: "))
# NUM2 = int(input("Ingresa otro número entero: "))
# NUM3 = int(input("Ingresa otro número entero: "))

# if NUM1 > NUM2 and NUM1 > NUM3:
#     print(f"El número {NUM1} es el mayor")
# else:
#     if NUM2 > NUM1 and NUM2 > NUM3:
#         print(f"El número {NUM2} es el mayor")
#     else:
#         if NUM3 > NUM1 and NUM3 > NUM2:
#             print(f"El número {NUM3} es el mayor")
#         else:
#             print("Los 3 números digitados son iguales.")
 
# ---------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------
# Hacer un programa que solicite  3 numeros enteros diferentes 
# entre sí  y que imprima cual de los 3 es el menor


# NUM1 = int(input("Ingresa un número entero: "))
# NUM2 = int(input("Ingresa otro número entero: "))
# NUM3 = int(input("Ingresa otro número entero: "))

# if NUM1 < NUM2 and NUM1 < NUM3:
#     print(f"El número {NUM1} es el menor")
# else:
#     if NUM2 < NUM1 and NUM2 < NUM3:
#         print(f"El número {NUM2} es el menor")
#     else:
#         if NUM3 < NUM1 and NUM3 < NUM2:
#             print(f"El número {NUM3} es el menor")
#         else:
#             print("Los 3 números digitados son iguales.")

# ---------------------------------------------------------------------------------------------




# ---------------------------------------------------------------------------------------------

# Hacer un programa que solicite 4 numeros enteros diferentes entre si
# e imprima a la salida cual de ellos es el menor y cual de ellos es el mayor


NUM1 = int(input("Ingrese un número entero: "))
NUM2 = int(input("Ingrese un número entero: "))
NUM3 = int(input("Ingrese un número entero: "))
NUM4 = int(input("Ingrese un número entero: "))

if(NUM1 > NUM2 and NUM1 > NUM3 and NUM1 > NUM4):
    MAYOR=NUM1
else:
    if(NUM2 > NUM1 and NUM2 > NUM3 and NUM2 > NUM4):
        MAYOR=NUM2
    else:
        if(NUM3 > NUM1 and NUM3 > NUM2 and NUM3 > NUM4):
            MAYOR=NUM3
        else:
            MAYOR=NUM4
            if(NUM1 < NUM2 and NUM1 < NUM3 and NUM1 < NUM4):
                MENOR=NUM1
            else:
                if(NUM2 < NUM1 and NUM2 < NUM3 and NUM2 < NUM4):
                    MENOR=NUM2
                else:
                    if(NUM3 < NUM1 and NUM3 < NUM2 and NUM3 < NUM4):
                        MENOR=NUM3
                    else:
                        MENOR=NUM4

print(f"El mayor es {MAYOR} y el menor es {MENOR}")
# ---------------------------------------------------------------------------------------------