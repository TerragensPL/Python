# INPUT: Entrada de información por parte del usuario
### Mediante el uso de input podemos pedirle al usuario que ingrese un dato


# Introcimos el nombre que nos da el usuario en la variable
variable = input("Introduce tu nombre: ") 

print("El nombre insertado es: ",variable) #Imprimimos el nombre que nos dio el usuario

#----------------------------------------------------



numero1 = int(input("Introduce un numero entero: ")) # Le indicacamos con int que el dato que se introduce es un entero
numero2 = int(input("Introduce otro numero entero: ")) # Le indicacamos con int que el dato que se introduce es un entero

# Para que se haga esta suma Python debe saber que los dos numeros son enteros, por eso usamos int
resultado = numero1 + numero2 #Sumamos los dos numeros

print("La suma de ambos numeros es: ",resultado)

#----------------------------------------------------



print("¿Que pasaria si no hubiramos expecificado que los datos son enteros (int)?")

numero1 = (input("Introduce un numero entero: ")) # Piensa que es un string
numero2 = (input("Introduce otro numero entero: ")) # Piensa que es un string

# Al no especificar que son enteros piensa que son cadenas de texto (string) y los junta.
resultado = numero1 + numero2 # En este caso no se suman, sino que se concatenan

print("La suma de ambos numeros es sin expecificar que son enteros: ",resultado)



#----------------------------------------------------

print("Vamos a pedirle al usuario que ingrese un numero decimal")
# Usamos float para que el usuario pueda ingresar un numero decimal
# los decimales se deben escribir con punto (.) y no con coma (,)


numero1 = float(input("Introduce un numero decimal: "))
numero2 = float(input("Introduce otro numero decimal: "))

resultado = numero1 + numero2 #Sumamos los dos numeros decimales

print("La suma de ambos numeros decimales es: ",resultado)



#----------------------------------------------------

nombre= input("Introduce tu nombre: ") #como esperamos un string no es necesarrio especificar el tipo de dato
edad= int(input("Introduce tu edad: ")) 

print(f"Tu nombre es {nombre} y tu edad es {edad} años")


#----------------------------------------------------
