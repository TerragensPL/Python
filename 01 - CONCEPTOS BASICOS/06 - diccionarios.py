# DICCIONARIOS

# Un diccionario es un tipo de dato que almacena pares claves y valor
# Se definen con llaves {}

diccionario = {'Nombre':'Pedro', 'Edad': 52, 'Profesion':'Docente'}


# Tambien podemos definirlo de esta manera
diccionario2 = {'Nombre':'Pedro',
                'Edad': 52,
                'Profesion':'Docente'
                }


# Cunado quiero imprimir el valor de un elemento del diccionario
# tengo que usar la clave entre corchetes
print(diccionario['Nombre']) # Imprime el valor de la clave 'Nombre'
print(diccionario['Edad']) # Imprime el valor de la clave 'Edad'



# Para elminar una clave y su valor del diccionario
del diccionario['Profesion'] # Elimina la clave 'Profesion' y su valor

"""
print(diccionario['Profesion']) # Imprime un error porque la clave 'Profesion' no existe
"""

# Podemos verificar si una clave existe en el diccionario con el operador in
print('Nombre' in diccionario) # Imprime True porque la clave 'Nombre' existe
print('Profesion' in diccionario) # Imprime False porque la clave 'Profesion' no existe



