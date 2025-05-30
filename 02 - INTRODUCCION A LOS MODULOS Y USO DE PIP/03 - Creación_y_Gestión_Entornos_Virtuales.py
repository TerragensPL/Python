# Creación y Gestión de Entornos Virtuales

###
# Vamos intalar librerias utilizando entornos aislados.
# Haciendo esto  tenemos más ordenadas las librerias por que se encuentran
# de forma aislada para cada uno de los proyectos que tengamos.S
###

import requests
response = requests.get('https://www.google.com')
print("codigo de estado:", response.status_code)



###
# Para crear un entorno virtual, utilizamos el módulo venv que viene incluido en Python.
# En un terminal, navegamos al directorio donde queremos crear el entorno virtual y ejecutamos:
# python -m venv nombre_del_entorno
# Por ejemplo, para crear un entorno virtual llamado "mi_entorno":
# python -m venv mi_entorno
# Esto creará un directorio llamado "mi_entorno" que contendrá una copia aislada de Python y pip.
#
# Para activar el entorno virtual, utilizamos el siguiente comando:
# En Windows en CMD:
# mi_entorno\Scripts\activate
#
# En macOS y Linux:
# source mi_entorno/bin/activate
#
# Una vez activado, el prompt de la terminal cambiará para indicar que estamos dentro del entorno virtual.
# Ahora, cualquier paquete que instalemos con pip se instalará en este entorno virtual y no afectará 
# al sistema global de Python.
#
# Para desactivar el entorno virtual, simplemente ejecutamos:
# deactivate
#
#
# Si queremos eliminar todo el entorno virtual sol tendremos que borrar la carpeta que se creó 
# al crear el entorno virtual.
#
# Tod esto se hace para evitar posibles conflitos entre librerias en un futuro 
# cuando tengamos muchas librerias instaladas y así tener un sistema mas limpio y ordenado.
###
