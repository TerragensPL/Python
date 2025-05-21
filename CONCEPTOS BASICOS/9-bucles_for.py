# BUCLES FOR
# Un bucle for se utiliza para iterar sobre una secuencia (lista, tupla, diccionario, conjunto o cadena).   

for variable in "Hola Mundo": # Dara tantas vueltas como caracteres tenga la cadena de texto "Hola Mundo"
    print(variable) # Imprimira cada letra de la cadena de texto "Hola Mundo"

#----------------------------------


lista =['naranja', 'limon', 'manzana']

for fruta in lista:
    print('En esta vuelta la variable fruta vale: ',fruta) # Imprimira cada fruta de la lista


#----------------------------------


correo = False # Inicializa la variable correo como False

# Pide al usuario que introduzca su correo electronico y recorre cada letra dl correo electronico
for caracter in input('Introduce tu correo electronico: '):
    print('En esta vuelta la variable caracter vale: ',caracter) # Imprimira cada letra del correo electronico
    if caracter == '@': # Si encuentra un arroba en el correo electronico, cambia el valor de la variable correo a True
        correo = True

if correo == True:#
    print('El correo es valido, tiene un arroba')
else:
    print('ERROR: El correo no es valido, no tiene una arroba')


#----------------------------------

lista = ['naranja', 'limon', 'melon', 'manzana', 'pera', 'sandia']

bucle = [_ for _ in lista] # Crea una lista con los componentes de la lista original
print(bucle) # Imprime la lista creada


#----------------------------------


numeros = [1,2,3,4,5,]

for _ in numeros: # _ para no imprimir el valor de la variable
    print('En estas vueltas no se imprime el contenido de la lista que estamos recorriendo') # Se imprime tantas veces como elementos tenga la lista


#----------------------------------

for numero in range(1, 100): # range(1, 100) puedo recorrer una lista de 1 a 100
    print('Se ejecutara 100 veces, la variable vale: ',numero) # Se imprime tantas veces como elementos tenga la list