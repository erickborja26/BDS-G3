capitales = {
        'Perú' : 'Lima',
        'Ecuador' : 'Quito',
        'Chile': 'Santiago',
        'Colombia': 'Bogota'
    }

#RECORRIDO POR CLAVES

for clave in capitales.keys():
    print(clave)
    
print('='*50)

#RECORRIDO POR VALORES

for valor in capitales.values():
    print(valor)
    
print('='*50)
    
#recorrido por calve, valor
for clave,valor in capitales.items():
    print(f"La capital de {clave} es {valor}")
    