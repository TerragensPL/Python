# OPERADORES LOGICOS

# Sirven para poder comprobar si se cumple una determinada condición

numero = 5

# AND
# El operador AND devuelve True si ambas condiciones son verdaderas si no False
print(numero > 0 and numero < 10) # Devuelve True porque ambas condiciones son verdaderas

#----------------------------------


# OR
# El operador OR devuelve True si al menos una de las condiciones es verdadera si no False
print(numero > 0 or numero < 4) # Devuelve True porque la primera condición es verdadera


#----------------------------------

# NOT
# Se usa para invertir el valor de una condición. 
# Si una condición es True, not la convierte en False, 
# y si es False, la convierte en True.

verdadero = True

print(not (numero > 0 and numero < 10)) # Devuelve False porque la condición es verdadera
print(not numero > 7) # Devuelve True porque la condición es falsa
print(not verdadero) # Devuelve False porque la condición es verdadera


