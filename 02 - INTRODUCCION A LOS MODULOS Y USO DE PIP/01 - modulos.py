# MODULOS

###
# Un modulo es un archivo de Python que contiene funciones o codigo que puedo utilizarlo en cualquier momento.
# Hay modulos instalados en Pytjon por defecto que es lo que se conoce como la libreria estandar de Python.
# tambien puedo crear mis propios modulos.
###

# Vamos a crearnos dos archivos modulo.py y script.py
# En el modulo.py vamos a escribir una funcion que nos permita saludar.
# En el script.py vamos a importar el modulo y a utilizar la funcion que hemos creado.

# En el archivo modulo.py vamos a escribir lo siguiente:
"""
def saludar():
    print("Hola, mensaje desde el modulo.py")
"""

# En el archivo script.py vamos a escribir lo siguiente:
"""
import modulo

modulo.saludar()
"""
# Como vemos primero debemos importar el modulo y luego llamamos a l funcion.


#--------------------------------


###
# Tambien podemos utilizar modulos que no estan instalados por defecto en Python.
# Ejemplo, si yo quiero gestionar numeros aleatorios, puedo utilizar el modulo random.
###

import random # Importamos el modulo random

numero_aleatorio = random.randint(1, 100) # Generamos un numero aleatorio entre 1 y 100
print(f"El numero aleatorio generado es: {numero_aleatorio}") # Imprimimos el numero aleatorio generado



#----------------------------------

#Para ver la lista de modulos que tengo instalados en mi sistema.

help("modules")

"""
# Lista de modulos instalados en Python
_statistics         errno               random
__future__          _string             faulthandler        re
__hello__           _strptime           filecmp             reprlib
__phello__          _struct             fileinput           rlcompleter
_abc                _suggestions        fnmatch             runpy
_aix_support        _symtable           fractions           sched
_android_support    _sysconfig          ftplib              script
_apple_support      _testbuffer         functools           secrets
_ast                _testcapi           gc                  select
_asyncio            _testclinic         genericpath         selectors
_bisect             _testclinic_limited getopt              shelve
_blake2             _testconsole        getpass             shlex
_bz2                _testimportmultiple gettext             shutil
_codecs             _testinternalcapi   glob                signal
_codecs_cn          _testlimitedcapi    graphlib            site
_codecs_hk          _testmultiphase     gzip                smtplib
_codecs_iso2022     _testsinglephase    hashlib             socket
_codecs_jp          _thread             heapq               socketserver
_codecs_kr          _threading_local    hmac                sqlite3
_codecs_tw          _tkinter            html                sre_compile
_collections        _tokenize           http                sre_constants
_collections_abc    _tracemalloc        idlelib             sre_parse
_colorize           _typing             imaplib             ssl
_compat_pickle      _uuid               importlib           stat
_compression        _warnings           inspect             statistics
_contextvars        _weakref            io                  string
_csv                _weakrefset         ipaddress           stringprep
_ctypes             _winapi             itertools           struct
_ctypes_test        _wmi                json                subprocess
_datetime           _zoneinfo           keyword             symtable
_decimal            abc                 linecache           sys
_elementtree        antigravity         locale              sysconfig
_functools          argparse            logging             tabnanny
_hashlib            array               lzma                tarfile
_heapq              ast                 mailbox             tempfile
_imp                asyncio             marshal             test
_interpchannels     atexit              math                textwrap
_interpqueues       base64              mimetypes           this
_interpreters       bdb                 mmap                threading
_io                 binascii            modulefinder        time
_ios_support        bisect              modulo              timeit
_json               builtins            msvcrt              tkinter
_locale             bz2                 multiprocessing     token
_lsprof             cProfile            netrc               tokenize
_lzma               calendar            nt                  tomllib
_markupbase         cmath               ntpath              trace
_md5                cmd                 nturl2path          traceback
_multibytecodec     code                numbers             tracemalloc
_multiprocessing    codecs              opcode              tty
_opcode             codeop              operator            turtle
_opcode_metadata    collections         optparse            turtledemo
_operator           colorsys            os                  types
_osx_support        compileall          pathlib             typing
_overlapped         concurrent          pdb                 unicodedata
_pickle             configparser        pickle              unittest
_py_abc             contextlib          pickletools         urllib
_pydatetime         contextvars         pip                 uuid
_pydecimal          copy                pkgutil             venv
_pyio               copyreg             platform            warnings
_pylong             csv                 plistlib            wave
_pyrepl             ctypes              poplib              weakref
_queue              curses              posixpath           webbrowser
_random             dataclasses         pprint              winreg
_sha1               datetime            profile             winsound
_sha2               dbm                 pstats              wsgiref
_sha3               decimal             pty                 xml
_signal             difflib             py_compile          xmlrpc
_sitebuiltins       dis                 pyclbr              xxsubtype
_socket             doctest             pydoc               zipapp
_sqlite3            email               pydoc_data          zipfile
_sre                encodings           pyexpat             zipimport
_ssl                ensurepip           queue               zlib
_stat               enum                quopri              zoneinfo
"""
