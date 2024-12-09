bandera= "si"

while(bandera=="si"):
    print("=================CALCULADORA DE PYTHON=================")
    num1= input("Numero 1: ")
    num2= input("Numero 2: ")
    operacion = int(input("""
                    1) SUMA
                    2) RESTA
                    3) MULTIPLICACION
                    4) DIVISION
                    INGRESE OPCION: """))
    if(operacion== 1):
        resultado = int(num1) + int(num2)
    elif(operacion==2):
        resultado = int(num1) - int(num2)
    elif(operacion==3):
        resultado = int(num1) * int(num2)
    elif(operacion==4):
        resultado = float(num1) / float(num2)
    else:
        print("ESA OPERACION NO EXISTE")
    print(f"La respuesta es {resultado}")
    bandera= input(f"¿Desea realizar otra operacion?(si|no)")