nombre = input("Ingresa tu nombre")
print("Tecleaste:", nombre)

# ¿Cómo capturar datos numéricos? 
# Para ello se hace una conversión entre tipos (casting)
# Consiste en llamar al constructor de la clase deseada.
# Ejemplo: Convertir el string "2" en número
# int("2")

entrada = input("Dame tu edad: ")
edad = int(entrada)
edad += 1 
print("Tu edad es:", edad)

# Esto se puede hacer con menos código:
estatura = int(input("Dame tu edadestatura: "))
print("Tu estatura es: ", estatura)

# inputs booleanos
casado = bool(int(input("Soltero (0) casado (1)")))
print("casado =", casado )