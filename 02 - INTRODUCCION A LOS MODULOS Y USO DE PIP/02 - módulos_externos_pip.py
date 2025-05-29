# Instalación de módulos externos - Uso de Pip



import requests 
# requests es un módulo externo que no viene instalado por defecto en Python.
# Portanto, debemos instalarlo antes de poder usarlo.

###
# Cuando queremos encontrar modulos que no vienen instalados en Python por defecto 
# podemos buscar en la web de PyPI (Python Package Index) que es el repositorio oficial de paquetes de Python.
# https://pypi.org/
# Para instalar un módulo externo, utilizamos el gestor de paquetes pip.
# pip install nombre_del_modulo
# Por ejemplo, para instalar el módulo requests, que se utiliza para hacer peticiones HTTP:
# 
# En una consola de comandos, ejecutamos:
# pip install requests
# Una vez instalado, podemos importarlo en nuestro código Python:
# import requests
###

###
# Si queremos ver los modulos intalados podemos usar el comando en una consola de comandos:
# pip list
###

###
# Si queremos desinstalar un modulo podemos usar el comando:
# pip uninstall nombre_del_modulo
###

# El siguiente verifica si podemos conectarnos a una URL utilizando el módulo requests:
url = "https://google.com" # URL a la que queremos hacer una petición HTTP

response = requests.get(url) # Hacemos una petición GET a la URL especificada

if response.status_code == 200: # Verificamos si la respuesta fue exitosa (código 200)
    print("Conexión exitosa a") # Imprimimos un mensaje de éxito
else: # si la respuesta no fue exitosa
    print("Error al conectar a", url) # Imprimimos un mensaje de error si la conexión falla


