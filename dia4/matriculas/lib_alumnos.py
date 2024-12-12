def menu(ANCHO):
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
    
    
def registrar(ANCHO):
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
    return dic_nuevo_alumno

def mostrar(ANCHO, dic_alumnos):
    print("="*ANCHO)
    print(" "*10 + "[2] MOSTRAR ALUMNO")
    print("="*ANCHO)
    for dni,datos in dic_alumnos.items():
        print(f"DNI : {dni}")
        print(f"Nombre : {datos['nombre']}")
        print(f"Email: {datos['email']}")
        print("*"*ANCHO)

def actualizar(ANCHO, dic_alumnos):
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

def eliminar(ANCHO, dic_alumnos):
    print("="*ANCHO)
    print(" "*10 + "[4] ELIMINAR ALUMNO")
    print("="*ANCHO)
    
    dni= input("Ingrese el dni del alumno a eliminar: ")
    if dni in dic_alumnos:
        dic_alumnos.pop(dni)
        print("ALUMNO ELIMINADO")
    else:
        print("NO SE ENCONTRO EL ALUMNO")
        
def salir(ANCHO):
    print("="*ANCHO)
    print(" "*10 + "[1] SALIR")
    print("="*ANCHO)

def opcion_invalida(ANCHO):
    print("="*ANCHO)
    print(" "*10 + "OPCION INCORRECTA!!!")
    print("="*ANCHO)