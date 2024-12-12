
def sumar(n1,n2):
    resultado= int(n1)+int(n2)
    return resultado

def sumar_con_mensaje(n1,n2):
    resultado= int (n1) + int(n2)
    print(f"SUMA CON MENSAJE: La suma de {n1} + {n2} es {suma}")

n1= input("Ingrese nro1: ")
n2= input("Ingrese nro2: ")
suma = sumar(int(n1),int(n2))

print(f"La suma de {n1} + {n2} es {suma}")
print(sumar(40,23))
print(sumar_con_mensaje(n1,n2))