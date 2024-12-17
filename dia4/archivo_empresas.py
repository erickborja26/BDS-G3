# funcion para cargar el ruc, razon social, direccion de empresas de un archivo

dic_empresas= {}

def cargar_empresas(file_name):
    
    file= open(file_name, 'r')
    str_empresas= file.read()
    print(str_empresas)
    file.close()
    
    lista_empresas= str_empresas.splitlines()
    for empresa in lista_empresas:
        lista_fila= empresa.split(',') #se supone q sera [ruc, razon social, direccion]
        dic_empresa_nueva={
            lista_fila[0]: {
                'razon social' : lista_fila[1],
                'direccion' : lista_fila[2]
            }
        }
        dic_empresas.update(dic_empresa_nueva)
