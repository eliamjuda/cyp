# - \\"   --> "
# - \\'   --> '
# - \n   --> Salto de linea (tecla enter)
# - \t   --> tabulador spacios a la izq.
# - \uxxxx  --> Caracteres unicode 
# - \Uxxxxxxxx --> unicode extendido
# - \\\   --> \\ 

print("\u0444")
print("\u0620")

print("\U00010057")
print("\U0001F602")

# Funcion Print
# Se emplea para desplegar información en la salida estándar.
# Normalmente un monitor.

nombre = "José"
edad = 18
casado = False
estatura = 1.67

# 1.Con comas : Concatena haciendo un casting, convirtiendo a string automáticamente
print(nombre, edad, casado, estatura)

# 2. Con el símbolo de + : Concatenación en crudo
print(nombre  +  str(edad) + str(casado) + str(estatura))

# 3. Dando formato con format
print("Nombre: {}\n\tEdad: {}\n\tEsta casado: {}\n\tEstatura en metros: {}\n\t".format(nombre,edad,casado,estatura))

# 4. Con el operador f" "
print("Con el operafor f\"\"")
print(f"Nombre: {nombre}\n\tEdad: {edad}\n\tEsta casado: {casado}\n\tEstatura en metros: {estatura}\n\t")

# Cómo manejar el argumento end
print(f"Hola {nombre} ", end="")
print(", Cómo estás?")

# Con un print, escribir su primer nombre 

# EEEE LL    II     AA     MMMM MMMM #
# E    LL    II    A  A    MM MM  MM #
# EEEE LL    II   AAAAAA   MM     MM #
# E    LL    II  A      A  MM     MM #
# EEEE LLLLL II A        A MM     MM #

print("Tarea - Nombre de pila: \n")
print("EEEE LL    II     AA     MMMM MMMM\nE    LL    II    A  A    MM MM  MM\nEEEE LL    II   AAAAAA   MM     MM\nE    LL    II  A      A  MM     MM\nEEEE LLLLL II A        A MM     MM")
print("\n")

