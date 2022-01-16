## Atributos o propiedades: se le llama así a las características de un objeto
## por ejemplo: color, tamaño, material, etc...

#Acciones que pueden realizar los objetos se llaman METODOS 

#Clase: son propiedades y métodos que describen a un objeto, encapsulados
# y se declara con la palabra reservada class 

class celular():
    numero_pantalla = 1
    color = None
    camara = False
    chip = False
    mi_numero = None
    numero_llamada = None
    marca_celular = None
    def __init__(self, marca_celular):
        self.marca_celular = marca_celular
        print('Bienvenido a tu %s' % self.marca_celular)
    def __str__(self):
        return 'este celular es de la marca %s' % self.marca_celular
    def tomar_fotos(self):
        if self.camara == False:
            print('No tengo camara')
            return
        orden = input('Presiona Y para tomar foto\n')
        disparador = False
        if orden == 'Y':
            disparador = True
        if disparador == True:
            print('tomo foto')
        else:
            print('no tomo foto')

    def llamar(self):
        self.recibe_numeros()
        if self.chip == True and self.numero_llamada != None:
            print('usted esta llamando a %s desde %s' %(self.numero_llamada, self.mi_numero,))
        else:
            print('introduzca chip')
    def recibe_numeros(self):
        self.numero_llamada = int(input('dame el numero de telefono: \n'))
    def mandar_mensaje(self):
        pass
    def introducir_chip(self):
        self.chip = True
        self.mi_numero = int(input('Introduce tu numero de telefono:\n'))
    def quitar_chip(self):
        self.chip = False
        self.mi_numero = None


ejemplo = celular('nokia azul')
print(ejemplo)
print(ejemplo.camara)
ejemplo.tomar_fotos()


ejemplo2 = celular('iphone')
print(ejemplo2)
ejemplo2.camara = True
print(ejemplo2.camara)
ejemplo2.tomar_fotos()

ejemplo3 = celular('samsung')
ejemplo3.llamar()
ejemplo3.introducir_chip()
ejemplo3.llamar()


##TAREA CREAR UNA CLASE MASCOTA QUE AL ADOPTARLA 
##ME PIDA UN NOMBRE, COLOR, Y QUE ANIMAL VA A SER
## Y QUE MI MASCOTA SEA CAPAZ DE DECIRME SU NOMBRE
## Y DE JUGAR CONMIGO, QUE PUEDA COMER Y BEBER Y ME DIGA
## SI TIENE HAMBRE O SED

class mascota():
    nombre = None
    color = None
    especie = None
    hambre = 0
    sed = 0
    diversion = 0

    def decir_nombre(self):
        pass

    def jugar(self):
        pass

