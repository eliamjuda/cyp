CATE = int(input("Introduce la categoría: "))
SUE = float(input("Introduce una categoría: "))

if CATE == 1:
    SUE = SUE * 1.15;
elif CATE == 2:
    SUE = SUE * 1.10;
elif CATE == 3:
    SUE = SUE * 1.08;
elif CATE == 4:
    SUE = SUE * 1.07;

# # Selección múltiple (switch)
# En python no existe la estructura de selección switch, en su lugar se emplea la palabra reservada:
# - elif

# Por ejemplo en el lenguaje C y Java sería de la forma:
# float SUE= 0.0;
# int CATE = 0;

# printf("Introduce la categoría")
# scanf("%i", &CATE);

# switch(CATE){
#     case 1:
#         SUE = SUE * 1.15;
#         break;
#     case 2:
#         SUE = SUE * 1.15;
#         break;   
#     case 3:
#         SUE = SUE * 1.15;
#         break;
#     case 4:
#         SUE = SUE * 1.15;
#         break;
#     case 5:
#         SUE = SUE * 1.15;
#         break;
# }

# printf("Categoría = %i, Sueldo= %f")

# A = float(input("Escribe un valor: "))
# B = float(input("Escribe un valor: "))
# C = float(input("Escribe un valor: "))

# if A > B:
#     if A > C:
#         if B > C:
#             print(A,B,C)
#         else:
#             print(A,C,B)
#     else:
#         print(C,A,B)
# else:
#     if B > C:
#         if A > C:
#             print(B,A,C)
#         else:
#             print(B,C,A)
#     else:
#         print(C,B,A)

TIPOENF = int(input("Ingresa el tipo de enfermedad: "))
EDAD = int(input("Introduce la edad: "))
DIAS = int(input("Introduce el número de días: "))
COSTO = 0.0

if TIPOENF == 1:
    COSTO = DIAS * 25.0
elif TIPOENF == 2:
    COSTO = DIAS * 16.0
elif TIPOENF == 3:
    COSTO = DIAS * 20.0
elif TIPOENF == 4:
    COSTO = DIAS * 32.0

if EDAD >= 14 and EDAD <= 22:
    COSTO = COSTO*1.10

print(f"Costo total = ${COSTO} ")
