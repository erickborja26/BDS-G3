file = open('alumnos.txt', 'w') #para escribir
file.write('100,cesar,cesar@gmail.com')
file.close()

file = open('alumnos.txt', 'a') #para agregar
file.write('\n')
file.write('200,ana,anar@gmail.com')
file.close()

file_read= open('alumnos.txt', 'r') #para leer
alumnos= file_read.read()
print(alumnos)
print(type(alumnos))
file_read.close()