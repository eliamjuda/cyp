# for x in range(1, 20, 1):
#     print(x)
# print("Fin del programa")

# for x in range(19,0,-1):
#     print(x)
# print("Fin del programa")

# Ejemplo 3.3

# CUECER = 0;
# NUM = 0;
# N = int(input("Introduce un valor numérico mayor que 1: "))

# for i in range( 1, N+1 , 1 ):
#     N = int(input("Introduce un valor numérico mayor que 1: "))
#     if N == 0:
#         CUECER += 1

# print("CUECER = ", CUECER)

# for i in range( 0, 11, 1 ):
#     print(f"7 x {i} = ", 7*i)


# N1 = int(input("Dame un número entre 1 y 5: "))
# if N1 > 0 and N1 <= 5:
#     N2 = int(input(f"Dame un número entre {N1} y 10: "))
#     if N2 >= N1 and N2 <= 10:
#         for i in range( N1, N2+1):
#             for j in range(1,11):
#                 print(f"{i} x {j} = ", i*j)
#     else:
#         print(f"Elige un valor entre {N1} y 10")
# else:
#     print("Elige un valor entre el 1 y el 5")


# numeros = [ x for x in range(10,101,10)]
# print(numeros)


# ejercicio: calcular promedio de edad

# edades = [0 for x in range(5)]
# suma = 0
# for i in range(len(edades)):
#     edades[i] = int(input("Ingresa una edad: "))

# print(len(edades))

# for j in range(len(edades) + 1):
#     print(j)
#     suma = suma + edades[j]
#     promedio = suma/5
        
# print(suma)


import random 
N = [round(random.uniform(5,11),2)]
print(N)

valores = [N for x in range(20)]
print(valores)

for i in range(len(valores)):
    print(i)