# BUCLE WHILE

###
# Un Bucle While se utiliza para repetir un bloque de codigo siempre y cuando una condicion se verdadera es decir mientras
# se cumpla una determinada condicion se va a estar repitiendo el bloque de codigo que este dentro del bucle.
###

contador = 0

while contador < 10: # El bucle whire se ejecuta mientras la condicion sea verdadera. Contador sea menor que 10
    print("Voy a imprimir este mensage mientras la variable contador sea inferior a 10")
    print(f"En esta vuelta voy a sumar 1 a la variable contador que ahora vale {contador}")
    contador += 1 # Incrementamos la variable contador en 1



#-------------------------------

condicion = True
contador = 0

while condicion == True: # Bucle infinito, se ejecuta hasta que se rompa el bucle
    contador += 1 # Incrementamos el contador en 1
    if contador == 10: # Si el contador llega a 10, cambiamos la condicion a False
        condicion = False # Cambiamos la condicion a False para salir del bucle
    else:
        print("La condicion se esta cumpliendo, seguimos dentro del bucle")


#-------------------------------

#BUBLE INFINITO
'''
while True: # Bucle infinito, se ejecuta hasta que se rompa el bucle
    print("Este bucle se ejecuta infinitamente")
'''


