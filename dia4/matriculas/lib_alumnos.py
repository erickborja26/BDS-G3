
ANCHO=50
dic_alumnos =  {}

def mostrar_mensaje(mensaje):
    print("*"*ANCHO)
    print(" "*10 + mensaje)
    print("*"*ANCHO)

def menu():
    mostrar_mensaje("GESTION DE ALUMNOS")
    print("""
          [1] REGISTRAR ALUMNO
          [2] MOSTRAR ALUMNOS
          [3] ACTUALIZAR ALUMNO
          [4] ELIMINAR ALUMNO
          [5] SALIR
          """)
    print("="* ANCHO)
        
def registrar():
    mostrar_mensaje("[1] REGISTRAR ALUMNO")
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

def mostrar():
    mostrar_mensaje("[2] MOSTRAR ALUMNO")
    for dni,datos in dic_alumnos.items():
        print(f"DNI : {dni}")
        print(f"Nombre : {datos['nombre']}")
        print(f"Email: {datos['email']}")
        print("*"*ANCHO)

def actualizar():
    mostrar_mensaje("[3] ACTUALIZAR ALUMNO")
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

def eliminar():
    mostrar_mensaje("[4] ELIMINAR ALUMNO")
    
    dni= input("Ingrese el dni del alumno a eliminar: ")
    if dni in dic_alumnos:
        dic_alumnos.pop(dni)
        print("ALUMNO ELIMINADO")
    else:
        print("NO SE ENCONTRO EL ALUMNO")
        