import os
from time import sleep
conversion1= 3.7
conversion2= 3.8
bandera = "si"
while(bandera=="si"):
    print("=======CONVERSOR (SOLES|DOLARES)=======")
    
    opcion= int(input("""
                  1) DE SOLES A DOLARES
                  2) DE DOLARES A SOLES
                  ESCOJA UNA OPCION: 
                  """))
    os.system("clear")
    if(opcion==1):
        soles= float(input("Ingrese los soles a convertir: "))
        print(f"{soles} soles son {soles/conversion2} dolares")
    elif(opcion==2):
        dolares= float(input("Ingrese los dolares a convertir: "))
        print(f"{dolares} dolares son {dolares*conversion1} soles")
    bandera= input("¿Desea continuar? ...(si|no): ")
    sleep(2)
    os.system("clear")