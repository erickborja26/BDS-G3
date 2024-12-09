conversion1= input("Ingrese la conversión actual de sol a dolar: ")
conversion2= input("Ingrese la conversión actual de dolar a sol: ")
bandera = "si"
while(bandera=="si"):
    print("=======CONVERSOR (SOLES|DOLARES)=======")
    
    opcion= int(input("""
                  1) DE SOLES A DOLARES
                  2) DE DOLARES A SOLES
                  ESCOJA UNA OPCION: 
                  """))
    if(opcion==1):
        soles= float(input("Ingrese los soles a convertir: "))
        print(f"{soles} soles son {soles*float(conversion1)} dolares")
    elif(opcion==2):
        dolares= float(input("Ingrese los dolares a convertir: "))
        print(f"{dolares} dolares son {dolares*(1/float(conversion2))} soles")
    bandera= input("¿Desea continuar? ...(si|no): ")