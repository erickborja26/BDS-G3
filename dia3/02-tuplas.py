#TUPLAS : IGUAL A LISTAS PERO INMUTABLES
dias = ('lunes', 'martes', 'jueves')
print(type(dias))

#PARA AGREGAR DATOS CONVERTIMOS LA TUPLA A LISTA
dias = list(dias)
print(type(dias))

dias= tuple(dias)
print(type(dias))

#RECORRER TUPLAS
for dia in dias:
    print(dia)
    