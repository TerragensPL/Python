
# VARIABLES
# Variables en Python no hace falta poner el tipo de dato dentro de la variable


nombre ="Pedro"  # Si yo quiero guardar un texto es un String y se pone entre comillas
edad = 52  # Si yo quiero guardar un número es un entero

print(nombre) # Para imprimir una variable se usa la función print poniendo el nombre de la variable nombre
print(edad) # Para imprimir una variable se usa la función print poniendo el nombre de la variable edad

# No se puede imprimir una variable sin comillas porque lo toma como un texto
print("Hola soy: nombre")

# Para imprimir un texto y una variable. El texto entre comillas, una coma y la variable sin comillas
print("Hola soy: ", nombre)

# Si ponemos la variable entre llaves y la letra f antes de las comillas, se imprime el valor de la variable
print(f"Hola soy: {nombre}")

# Se pueden poner varias variables dentro de las llaves
print(f"Hola soy: {nombre} y tengo {edad} años") 

#-------------------------------------------


numero1 = 5
numero2 = 2

#Puedo guardar el resultado de una operación entre dos variable en una variable final
resultado= numero1 + numero2

print("El resultado es: ", resultado)
print(f"El resultado es: {resultado}")


