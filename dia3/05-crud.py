import os
from time import sleep

"""
CRUD
 - CREATE
 - READ
 - UPDATE
 - DELETE
"""

dic_alumnos =  {
    '12345678' :{
        'nombre' : 'CESAR',
        'email' : 'cesar@gmail.com'
    }
}

ANCHO= 50
opcion= 0

while(opcion<5):
    os.system("clear")
    print("="*ANCHO)
    print(" "*10 + "GESTION DE ALUMNOS")
    print("="*ANCHO)
    print("""
          [1] REGISTRAR ALUMNO
          [2] MOSTRAR ALUMNOS
          [3] ACTUALIZAR ALUMNO
          [4] ELIMINAR ALUMNO
          [5] SALIR
          """)
    print("="* ANCHO)
    opcion = int(input("INGRESE OPCION: "))
    os.system("clear")
    if opcion==1:
        print("="*ANCHO)
        print(" "*10 + "[1] REGISTRAR ALUMNO")
        print("="*ANCHO)
        dni = input("DNI    :")
        nombre = input("NOMBRE  :")
        email = input("EMAIL    :")
        dic_nuevo_alumno = {
            dni: {
                'nombre' : nombre,
                'email' : email
            }
        }
        dic_alumnos.update(dic_nuevo_alumno)
    elif opcion==2:
        print("="*ANCHO)
        print(" "*10 + "[2] MOSTRAR ALUMNO")
        print("="*ANCHO)
        for dni,datos in dic_alumnos.items():
            print(f"DNI : {dni}")
            print(f"Nombre : {datos['nombre']}")
            print(f"Email: {datos['email']}")
            print("*"*ANCHO)
            
    elif opcion==3:
        print("="*ANCHO)
        print(" "*10 + "[3] ACTUALIZAR ALUMNO")
        print("="*ANCHO)
        dni= input("Ingrese el dni del alumno a actualizar: ")
        if dni in dic_alumnos:
            print(f"ALUMNO A ACTUALIZAR {dic_alumnos[dni]['nombre']}")
            nuevo_nombre = input('NOMBRE : ')
            nuevo_dni = input('DNI : ')
            nuevo_email= input('EMAIL : ')
            dic_alumnos.pop(dni)
            alumno_actualizado= {
                nuevo_dni: {
                    'nombre': nuevo_nombre,
                    'email' : nuevo_email
                }
            }
            dic_alumnos.update(alumno_actualizado)
            print("ALUMNO ACTUALIZADO CON EXITO")
        else:
            print("NO SE ENCONTRO AL ALUMNO")
            
    elif opcion==4:
        print("="*ANCHO)
        print(" "*10 + "[4] ELIMINAR ALUMNO")
        print("="*ANCHO)
        
        dni= input("Ingrese el dni del alumno a eliminar: ")
        if dni in dic_alumnos:
            dic_alumnos.pop(dni)
            print("ALUMNO ELIMINADO")
        else:
            print("NO SE ENCONTRO EL ALUMNO")
        
    elif opcion==5:
        print("="*ANCHO)
        print(" "*10 + "[1] SALIR")
        print("="*ANCHO)
    else:
        print("="*ANCHO)
        print(" "*10 + "OPCION INCORRECTA!!!")
        print("="*ANCHO)
    sleep(1)