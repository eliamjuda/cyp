
# -------------------- 2.1 --------------------------------------

# N = int(input("Número de sonidos emitidos por minuto: "))
# T = 0

# if N > 0:
#     T = N/4 + 40
#     print(f"Temperatura: {T}")
# print("FIN")

# ---------------------------------------------------------------
# ////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////
# -------------------- 2.2 --------------------------------------

# P = int(input("Escribe un valor entero: "))
# Q = int(input("Escribe un valor entero: "))
# EXP = P**3 + Q**4 - 2*P**2

# if EXP < 680:
#     print(f"P: {P}, Q: {Q}")
# print("FIN")


# ---------------------------------------------------------------
# ////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////
# -------------------- 2.3 --------------------------------------

# A = float(input("Escribe un valor numérico: "))
# B = float(input("Escribe un valor numérico: "))
# C = float(input("Escribe un valor numérico: "))
# DIS = B**2 - 4*A*C

# if DIS >= 0:
#     X1 = ((-B)+DIS**0.5)/2*A
#     X2 = ((-B)-DIS**0.5)/2*A
#     print(f"Raíces reales: {X1},{X2}")

# ---------------------------------------------------------------
# ////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////
# -------------------- 2.4 --------------------------------------


# MAT = float(input("Escribe un valor numérico de tu matrícula: "))
# CAL1 = float(input("Escribe tu calificación: "))
# CAL2 = float(input("Escribe tu calificación: "))
# CAL3 = float(input("Escribe tu calificación: "))
# CAL4 = float(input("Escribe tu calificación: "))
# CAL5 = float(input("Escribe tu calificación: "))
# PRO = (CAL1+CAL2+CAL3+CAL4+CAL5)/5

# if PRO >= 6:
#     print(f"{MAT},{PRO}, APROBADO")
# else:
#     print(f"{MAT},{PRO}, NO APROBADO")
# print("FIN")



# ---------------------------------------------------------------
# ////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////
# -------------------- 2.5 --------------------------------------

# NUM = float(input("Ingresa un número: "))

# if NUM > 0:
#     print("Positivo")
# else:
#     if NUM == 0:
#         print("NULO")
#     else:
#         print("NEGATIVO")
# print("FIN")

# ---------------------------------------------------------------
# ////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////
# -------------------- 2.6 --------------------------------------


# A = int(input("Ingresa un número entero: "))

# if A == 0:
#     print("NULO")
# else:
#     if -1**A > 0:
#         print("PAR")
#     else:
#         print("IMPAR")

# print("FIN")


# ---------------------------------------------------------------
# ////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////
# -------------------- 2.7 --------------------------------------


# A = int(input("Ingresa un número entero: "))
# B = int(input("Ingresa un número entero diferente al anterior: "))
# C = int(input("Ingresa un número entero diferente al anterior: "))

# if A < B:
#     if B < C:
#         print("Los números están en orden creciente.")
#     else:
#         print("Los números no están en orden creciente.")
# else:
#     print("Los números no están en orden creciente.")

# print("FIN")



# ---------------------------------------------------------------
# ////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////
# -------------------- 2.8 --------------------------------------

# NUM = int(input("Ingresa el número: "))
# COMPRA = 0
# PAGAR = 0

# if COMPRA < 500:
#     PAGAR = COMPRA
# else:
#     if COMPRA <= 1000:
#         PAGAR = COMPRA - (COMPRA * 0.05)
#     else:
#         if COMPRA <= 7000:
#             PAGAR = COMPRA - (COMPRA*0.11)
#         else:
#             if COMPRA <= 1500:
#                 PAGAR = COMPRA - (COMPRA*.18)
#             else:
#                 PAGAR = COMPRA - (COMPRA*.25)
# print(PAGAR)
# print("FIN")

# ---------------------------------------------------------------
# ////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////
# -------------------- 2.9 --------------------------------------

# PREBAS = float(print("Precio básico del producto: "))
# IMP = 0

# if PREBAS > 500:
#     IMP = 20*.30+(PREBAS-40)*.5
# else:
#     if PREBAS > 40:
#         IMP = 20*.30+(PREBAS-40)*.40
#     else:
#         if PREBAS > 20:
#             IMP (PREBAS-20)*.30
#         else: 
#             IMP = 0

# PRETOT = PREBAS + IMP
# print(PREBAS, PRETOT)

# ---------------------------------------------------------------# 
# ////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////
# -------------------- 2.10 --------------------------------------


# A = float(input("Ingresa un número real: "))
# B = float(input("Ingresa un número real: "))
# C = float(input("Ingresa un número real: "))

# if A > B:
#     if A > C:
#         print("A es el mayor")
#     else:
#         if A == C:
#             print("A y C son los mayores")
#         else:
#             print("C es el mayor")
# else:
#     if A == B:
#         if A > C:
#             print("A y B son los mayores")
#         else:
#             if A == C:
#                 print("A,B y C son iguales")
#             else: print("C es el mayor")
#     else:
#         if B > C:
#             print("B es el mayor")
#         else:
#             if B == C:
#                 print("B y C son los mayores")
#             else:
#                 print("C es el mayor")

# print("FIN")

# ---------------------------------------------------------------
# ////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////
# -------------------- 2.11 --------------------------------------


# CLAVE = int(input("Ingresa tu clave de la zona geográfica a la que se llamó: "))
# NUMIN = int(input("Ingresa un número entero de la duración de llamada: "))
# CLAVE = 0

# if CLAVE == 12:
#     COST = NUMIN*2
# elif CLAVE == 15:
#     COST = NUMIN*2.2
# elif CLAVE == 18:
#     COST = NUMIN*4.5
# elif CLAVE == 19:
#     COST = NUMIN*3.5
# elif CLAVE == 23 or CLAVE == 25:
#     COST = NUMIN*6
# elif CLAVE == 29:
#     COST = NUMIN*5

# print("Costo total de la llamada: ", COST)

# ---------------------------------------------------------------
# ////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////
# -------------------- 2.12 --------------------------------------

# SUE = float(print("Escribe tu sueldo: "))
# CATE = int(print("Escribe tu categoría: "))
# HE = int(print("Escribe tus horas extras trabajadas: "))
# NSUE = 0;
# PHE = 0;

# if  CATE == 1:
#     PHE = 30
# elif CATE == 2:
#     PHE = 38
# elif CATE == 3:
#     PHE = 50
# elif CATE == 4:
#     PHE = 70
# else:
#     PHE = 0

# if HE > 30:
#     NSUE = SUE + 30*PHE
# else:
#     NSUE = SUE + HE*PHE

# print("NSUE")

# ////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////
# -------------------- 2.13--------------------------------------

# MAT = int(print("Escribe tu matrícula: "))
# CARR = print("Escribe tu carrera: ")
# SEM = int(print("Escribe el número de tu semestre: "))
# PROM = float(print("Escribe tu proemdio: "))

# if CARR == "Economía":
#     if SEM >= 6 and PROM >= 8.8:
#         print(f"{MAT}, {CARR}, ACEPTADO")
#     else:
#         print("FIN DEL PROGRAMA")

# elif CARR == "Contabilidad" or CARR == "Administración":
#     if SEM > 5 and PROM > 8.5:
#         print(f"{MAT}, {CARR}, ACEPTADO")
#     else:
#         print("FIN DEL PROGRAMA")

# elif CARR == "Computación":
#     if SEM > 6 and PROM > 8.5:
#         print(f"{MAT}, {CARR}, ACEPTADO")
#     else:
#         print("FIN DEL PROGRAMA")

# ////////////////////////////////////////////////////////////////
# ////////////////////////////////////////////////////////////////
# -------------------- 2.14--------------------------------------

TIPOENF = int(print("Tipo de enfermedad: "))
EDAD = int(print("Edad del pasiente: "))
DIAS = int(print("Días que estuvo internado: "))

if TIPOENF == 1:
    COSTOT = DIAS*25
elif TIPOENF == 2:
    COSTOT = DIAS*16
elif TIPOENF == 3:
    COSTOT = DIAS*20
elif TIPOENF == 4:
    COSTOT = DIAS*32

if EDAD >= 14 and EDAD <= 22:
    COSTOT = COSTOT*1.10

print(f"Costo total: {COSTOT}")    



