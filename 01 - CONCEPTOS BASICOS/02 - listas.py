# LAS LISTAS
### Las listas son estructuras de datos que contiene varios elementos
# # Ejemplo lista de comida: naranja, zumo, marcarrones, etc,
###


# Para crear una lista se utiliza [] para contener los elementos
lista =["Pedro", 52, "Informatico"]


# Para accesder a un elemento de la lista se utiliza el nombre de la lista
# y entre corchetes el número del elemento que quiero acceder.
# Las listas empiezan en 0, por lo que el primer elemento es el 0
print(lista[0]) #Imprime Pedro
print(lista[1]) #Imprime 52
print(lista[2]) #Imprime Informatico


# Imprime "Informatico" porque -1 se refiere al último elemento de la lista, 
# cuando se accede de forma negativa de atras hacia adelante
print(lista[-1])


# Si queremos sber cuanto elementos tiene la lista utilizamos la función len()
print(len(lista)) #Imprime 3 ya que hay 3 elementos en la lista


# Eliminar un elemento de la lista se utiliza del lista[número del elemento]
del lista[2] # Elimina el tercer elemento de la lista que es "Informatico"
print(lista[2]) # Daria error porque ya no existe el tercer elemento

