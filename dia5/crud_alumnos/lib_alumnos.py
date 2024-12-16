from tabulate import tabulate

ANCHO=50
TABLE_STYLE= 'simple_grid'

dic_alumnos =  {}

def cargar_alumnos(file_name):
    file = open(file_name, 'r')
    str_alumnos = file.read()
    file.close()
    lista_alumnos = str_alumnos.splitlines() #crea una lista que separa por salto de linea al string
    for str_fila in lista_alumnos:
        lista_fila = str_fila.split(',') #se crea lista que separa por comas al string
        dic_fila= {
            'nombre': lista_fila[1],
            'email': lista_fila[2]
        }
        dic_nuevo_alumno= {
            lista_fila[0]: dic_fila
        }
        dic_alumnos.update(dic_nuevo_alumno)

def grabar_alumnos(file_name):
    str_alumnos= ""
    for clave,valor in dic_alumnos.items():
        str_alumnos += clave +","+ valor['nombre'] +"," + valor['email'] +"\n"
    file= open(file_name, 'w')
    file.write(str_alumnos)
    file.close

def mostrar_mensaje(mensaje):
    tabla = [[mensaje]]
    print(tabulate(tabla, tablefmt=TABLE_STYLE, stralign ="center"))

def menu():
    mostrar_mensaje("GESTION DE ALUMNOS")
    menu_principal = [["[1] REGISTRAR ALUMNO"],
                      ["[2] MOSTRAR ALUMNOS"],
                      ["[3] ACTUALIZAR ALUMNO"],
                      ["[4] ELIMINAR ALUMNO"],
                      ["[5] SALIR"]]
    print(tabulate(menu_principal, headers=["GESTIÓN DE ALUMNOS"], tablefmt= TABLE_STYLE))
        
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
    data= []
    columnas= ["DNI", "NOMBRE", "EMAIL"]
    for dni,datos in dic_alumnos.items():
        data.append([dni,datos['nombre'],datos['email']])
    print(tabulate(data, headers=columnas, tablefmt= TABLE_STYLE))

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
        