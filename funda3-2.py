# Estructura While

# while <condición>:
#     <Blque de sentencias a ejecutar>
# <Siguiente línea posterior a while>

# valor = int(input("Dame un valor entero"))

# while valor != 0:
#     print(valor)
#     valor = int(input("Dame un valor entero"))


# valor = int(input("Dame un valor"))

# while valor != 0:
#     print(valor)
#     print("Otras cosas")

# print("Fin del programa")

# comprobar = True

# while comprobar == True:
#     n = int(input("Ingrese un número entero positivo: "))
    
#     if n > 0:
#         print("Es correcto")
#         for i in range(10):
#             print(n, " x ", i+1, "Es igual a: ", n*(i+1))
#             comprobar = False
#     else:

#         print("El número ingresado no es correcto: ")


# comprobar = True

# while comprobar == True:
#     n = int(input("Ingrese un número entero positivo: "))
#     if n > 0:
#         i = 1
#         while i < 11:
#             print(f"{n} por {i} es igual a: {n*i}")
#             i += 1
#             comprobar = False
#     else: 
#         print("El número ingresado no es correcto. Intente de nuevo.")
comprobar = True

while comprobar == True:
    n = int(input("Ingresa un número entero positivo: "))

    if n > 0:
        comprobar = False
        resultado = 0
        for i in range(1, n+1):
            resultado += (1/i)
            print("El resultado de la serie es: ", resultado)

    else:
        print("El número ingresado no es correcto, intente de nuevo.")
