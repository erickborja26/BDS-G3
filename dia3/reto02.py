#RETO2 . HACER UN CRUD DE EMPRESA CON RUC, RAZON SOCIAL Y DIRECCION

import os
from time import sleep

dic_empresas= {
    '12345678912': {
        'razon social': 'PEPSICO INC.',
        'direccion': 'av los tulipanes cuadra 30'
    }
}

ANCHO=50
opcion=0

while(opcion<5):
    os.system("clear")
    print("="*ANCHO)
    print(" "*10 + "EMPRESAS")
    print("="*ANCHO)
    print("""
          [1] REGISTRAR EMPRESA
          [2] MOSTRAR EMPRESAS
          [3] ACTUALIZAR EMPRESAS
          [4] ELIMINAR EMPRESA
          [5] SALIR
          """)
    print("="* ANCHO)
    opcion = int(input("INGRESE OPCION: "))
    os.system("clear")
    if opcion==1:
        print("="*ANCHO)
        print(" "*10 + "[1] REGISTRAR EMPRESA")
        print("="*ANCHO)
        ruc = input("RUC    :")
        razon_social = input("RAZON SOCIAL  :")
        direccion = input("DIRECCION    :")
        dic_nueva_empresa = {
            ruc: {
                'razon social' : razon_social,
                'direccion' : direccion
            }
        }
        dic_empresas.update(dic_nueva_empresa)
        print("Se registro la empresa con exito")
    elif opcion==2:
        print("="*ANCHO)
        print(" "*10 + "[2] MOSTRAR EMPRESAS")
        print("="*ANCHO)
        for ruc,datos in dic_empresas.items():
            print(f"RUC  : {ruc}")
            print(f"RAZON SOCIAL : {datos['razon social']}")
            print(f"DIRECCION: {datos['direccion']}")
            print("*"*ANCHO)
            
    elif opcion==3:
        print("="*ANCHO)
        print(" "*10 + "[3] ACTUALIZAR EMPRESAS")
        print("="*ANCHO)
        ruc= input("Ingrese el RUC de la empresa: ")
        if ruc in dic_empresas:
            print(f"ALUMNO A ACTUALIZAR {dic_empresas[ruc]['razon social']}")
            nueva_razon = input('NUEVA RAZON SOCIAL : ')
            nuevo_ruc = input('NUEVO RUC : ')
            nueva_direccion= input('NUEVA DIRECCION : ')
            dic_empresas.pop(ruc)
            empresa_actualizada= {
                nuevo_ruc: {
                    'razon social': nueva_razon,
                    'direccion' : nueva_direccion
                }
            }
            dic_empresas.update(empresa_actualizada)
            print("ALUMNO ACTUALIZADO CON EXITO")
        else:
            print("NO SE ENCONTRO LA EMPRESA")
            
    elif opcion==4:
        print("="*ANCHO)
        print(" "*10 + "[4] ELIMINAR EMPRESA")
        print("="*ANCHO)
        
        ruc= input("Ingrese el RUC de la empresa a eliminar: ")
        if ruc in dic_empresas:
            dic_empresas.pop(ruc)
            print("EMPRESA ELIMINADA")
        else:
            print("NO SE ENCONTRO EMPRESA")
        
    elif opcion==5:
        print("="*ANCHO)
        print(" "*10 + "[1] SALIR")
        print("="*ANCHO)
    else:
        print("="*ANCHO)
        print(" "*10 + "OPCION INCORRECTA!!!")
        print("="*ANCHO)
    sleep(1)