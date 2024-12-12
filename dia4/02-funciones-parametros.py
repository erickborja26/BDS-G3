#parametros args y kargs

def sumar_infinitos(*args): #se ingresa k parametros(los q quieras) y se ingresan en una lista
    resultado = 0
    for numero in args: #recorre la lista y suma todos los valores de la lista
        resultado= resultado + numero
    return resultado

suma1 = sumar_infinitos(3,4,5,3,41,34,34)
print(suma1)

print(sumar_infinitos(1,2,3,4,5))

def calculadora(**kwargs): #recibe parametros y lo decompone en un diccionario
    ope= kwargs.get('ope')
    n1= kwargs.get('n1')
    n2= kwargs.get('n2')
    
    if ope == 'suma':
        resultado= n1 + n2
        print(f'La {ope} de {n1} + {n2} es {resultado}')
    elif ope == 'resta':
        resultado= n1 - n2
        print(f'La {ope} de {n1} - {n2} es {resultado}')
    elif ope== 'multiplicacion':
        resultado= n1 * n2
        print(f'La {ope} de {n1} * {n2} es {resultado}')
    elif ope== 'division':
        resultado= n1 / n2
        print(f'La {ope} de {n1} / {n2} es {resultado}')
    else:
        print('operacion desconocida')


calculadora(ope='division', n1=8, n2=3)