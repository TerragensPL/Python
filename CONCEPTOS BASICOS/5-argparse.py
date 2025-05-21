# ARGPARSE: Entrada de datos por argumentos con argparse

###
# Hemos visto que con Input podemos pedirle información al usuario.
# Pero tambien hay una manerad de introducir informacion com parametros
# en la línea de comandos al ejecutar el programa.
# Para ello utilizamos la libreria argparse
###



# Para utilizar argparse tenemos que importarlo ya que no es una libreria nativa de Python
import argparse


# Crea un objeto ArgumentParser, que se usa para definir y analizar argumentos de línea de comandos. 
# La opción description="Suma dos numeros" proporciona una breve descripción del programa 
# cuando el usuario ejecuta --help.
parse = argparse.ArgumentParser(description="Suma dos numeros")

# Creamos el numero de parametros que quiero recibir en mi caso 2
parse.add_argument("numero1", type=int, help="Primer numero") 
parse.add_argument("numero2", type=int, help="Segundo numero")


argumentos = parse.parse_args() # En esta variable guardamos los argumentos que nos da el usuario


primer_numero = argumentos.numero1 # Guardamos el primer valor de argumentos en la variable primer_numero
segundo_numero = argumentos.numero2 # Guardamos el segundo valor de argumentos en la variable segundo_numero

print(f"El primer numero es {primer_numero} y el segundo numero es {segundo_numero}") # Imprimimos los dos numeros

resultado = primer_numero + segundo_numero # Sumamos los dos numeros
print(f"La suma de ambos numeros es: {resultado}") # Imprimimos el resultado
