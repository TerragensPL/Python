# SENTENCIAS CONDICIONALES

# Las sentencias condicionales son estructuras de control que permiten ejecutar un bloque de código
# dependiendo de si se cumple o no una determinada condición.
# En Python, las sentencias condicionales más comunes son if, elif y else.

edad = 19

if edad > 18:# Si la edad es mayor a 18
    print("Eres mayor de edad, puedes pasar")
elif edad < 18: # Si la edad es menor a 18
    print("Eres menor de edad, NO PUEDES PASAR")
else: # No se cumple ninguna de las condiciones anteriores
    print("dato incorrecto, debes introducir la edad")


#----------------------------------


edad = -1

if edad > 18 and edad < 30:# Si la edad es mayor a 18 y menor a 30
    print("Eres mayor de edad y tienes menos de 30 años, puedes pasar")
elif edad < 18 and edad > 0: # Si la edad es menor a 18 y mayor a 0
    print("Eres menor de edad, NO PUEDES PASAR")
else: # No se cumple ninguna de las condiciones anteriores
    print("Dato incorrecto, debes proporcinar una edad valida")


#----------------------------------

texto = "Mi numero de telefono es 123456789"
patron = "123456789" # Definimos el patron a buscar

if patron in texto: # Si el patron se encuentra en el texto
    print("El el numero de telefono esta presente ene le texto")
else: # Si el patron no se encuentra en el texto
    print("El numero de telefono no esta presente en el texto") 


#----------------------------------

contraseña = "La contraseña es: 123456789"
patron = input("Dime la contraseña: ") # Pedimos al usuario que introduzca la contraseña

if patron in contraseña:
    print("La contraseña es correcta, puedes pasar")
else:
    print("La contraseña es incorrecta, NO PUEDES PASAR")   


