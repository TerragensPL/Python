# FUNCIONES

###
# Las funciones son bloques de código que se pueden reutilizar en cualquier punto del codigo.
# se definen con la palabra clave 'def' seguida del nombre de la función y los paréntesis.
###


# Esta funcion la estamos definiendo. No se va a ejecutar hasta que la llamemos
def saludar (): # Definimos la funcion saludar
    print("Hola. Te mando saludos, Pedro")


saludar() # Llamamos a la funcion saludar, se ejecuta el bloque de codigo que esta dentro de la funcion



#---------------------------------

# A una funcion le podemos pasar parametros, que son variables que se definen dentro de la funcion
def saludar(nombre): # Definimos la funcion saludar con un parametro nombre
    print("Hola, Buenos días ",nombre)

saludar("Pedro") # Llamamos a la funcion saludar y le pasamos el parametro "Pedro"



#---------------------------------

def saludar(nombre, edad):
    print(f"Hola, {nombre}. Tienes {edad} años")

saludar("Pedro", 52) # los parametros se pasan en el orden en que se definen en la funcion
                     # Si no pasamos un parametro, nos va a dar un error


#---------------------------------

###
# Todo lo que haga dentro de una funcion, fuera de la funcion no va a funcionar. (variables, operaciones, etc.)
# Por ejemplo, si definimos una variable dentro de la funcion, no podremos acceder a ella fuera de la funcion
# Por eso usamos return para devolver un valor desde la funcion
###

def sumar(numero1, numero2):
    return numero1+numero2 # La palabra clave 'return' nos permite devolver un valor desde la funcion

resultado = sumar(2, 4) # Llamamos a la funcion sumar y guardamos el resultado en la variable resultado
print("El resultado de la suma es: ",resultado) # Imprimimos el resultado de la suma



#---------------------------------

def verificar_edad(nombre, edad):
    if edad >=18:
        print(f"{nombre} es mayor de edad")
    else:
        print(f"{nombre} es menor de edad")


verificar_edad("Juan", 16)
verificar_edad("Pedro", 52)