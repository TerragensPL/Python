# Manipulación de archivos en python

###
# El bjetivo es entender como podemos leer, escribir  o agregar informacion y editar un archivo.
# Para esto vamos a utilizar la funcion open() que nos permite abrir un archivo y realizar diferentes operaciones.
###

###
# Creamos un archivo de texto llamados datos.txt y escribimos en el siguiente texto:
# Hola esto es una linea de prueba
###


# Para leer el archivo.
# Abrimos el archivo en modo lectura y su contenido se guarda en la variable archivo
with open('datos.txt', 'r') as archivo: # r significa read (lectura)
    contenido = archivo.read()  # Leemos todo el contenido del archivo y lo guardamos en la variable contenido
    print(contenido)  # Imprimimos el contenido del archivo


# Para escribir en el archivo borrando su contenido.
with open('datos.txt', 'w') as archivo: # w significa write (escritura)
    archivo.write('Escribimos en el archivo (borrando lo anterior)')  # Escribimos en el archivo, esto borra el contenido anterior


# Para escribir en el archivo agregando contenido al final del archivo.
with open('datos.txt', 'a') as archivo: # a significa append (agregar)
    # Agregamos una nueva linea al final del archivo. agregamos un salto de linea con \n
    archivo.write('\nAgregamos una nueva linea al final del archivo\n')  


# Para leer el archivo nuevamente line por linea.
with open('datos.txt', 'r') as archivo:  # Abrimos el archivo en modo lectura
    for linea in archivo:  # Iteramos sobre cada linea del archivo
        print(linea)  # Imprimimos cada linea



# Escribimos en el archivo
with open('datos.txt', 'w') as archivo:
    archivo.write('Primera linea\n')
    archivo.write('Segunda linea\n')

# leemos el archivo completo
with open('datos.txt', 'r') as archivo:
    contenido = archivo.read()
    print("Contenido del archivo:")
    print(contenido)

# Agregamos más líneas al archivo
with open('datos.txt', 'a') as archivo:
    archivo.write('Tercera linea añadida\n')
    archivo.write('Cuarta linea añadida\n')

# leemos el archivo line por linea
with open('datos.txt', 'r') as archivo:
    print("leyendo línea por línea:")
    for linea in archivo:
        print(linea)