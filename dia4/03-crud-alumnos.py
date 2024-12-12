import os
from time import sleep
from matriculas.lib_alumnos import *

"""
CRUD
 - CREATE
 - READ
 - UPDATE
 - DELETE
"""

opcion= 0

while(opcion<5):
    os.system("clear")
    menu()
    opcion = int(input("INGRESE OPCION: "))
    os.system("clear")
    if opcion==1:
        registrar()
    elif opcion==2:
        mostrar()
        input("Presione enter para contiuar ...")
    elif opcion==3:
        actualizar()
            
    elif opcion==4:
        eliminar()
        
    elif opcion==5:
        mostrar_mensaje("[5] SALIR")
    else:
        mostrar_mensaje("OPCION INVALIDA!!! ...")
    sleep(1)