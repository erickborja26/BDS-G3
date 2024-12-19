class Usuario:
    __email = 'cesar@gmail.com' ## con doble _ al principio de la variable lo encapsulamos, lo protegemos
    __password = 'qwerty123'
    
    def __init__(self):
        pass
    
    def set_password(self, password): # con esto si podriamos cambiar la variable desde afuera
        self.__password = password
    
    def login(self, email, password):
        if(self.__email ==email and self.__password == password):
            print(f"Bienvenido {self.__email}")
        else:
            print("datos incorrectos")

print('LOGIN DE USUARIOS')
email = input('Ingrese Email : ')
password = input('Ingrese Password : ')

usuario = Usuario()
#usuario.password = password  (cambia la variable interna de la clase si no hay doble _)
usuario.__password = password #no cambia, no sirve
usuario.set_password(password) #si lo cambia
usuario.login(email,password)
