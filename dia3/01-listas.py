dias= ['lunes', 'martes', 'miercoles', 'jueves', 'viernes']
print(dias)
print(dias[-2])
print(dias[1:3])

#AGREGAR VALORES A LA LISTA

dias.append('sabado')
dias.append('domingo')
print(dias)

#ELIMINAR UN VALOR DE LA LISTA

dias.pop(3)
print(dias)
del dias[2:4]

#ACTUALIZAR UN DATO

dias[3]= 'jueves'
print(dias)

#RECORRER VALORES
for i in range(len(dias)):
    print(dias[i])
print("-----------------")
for dia in dias:
    print(dia)