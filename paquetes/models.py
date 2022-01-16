import time

class mascota():
    nombre = None
    especie = None
    diversion = 0
    energia = 0
    sed = 0

    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie
        self.diversion = 5
        self.energia = 5
        self.sed = 5
        print('Gracias por adoptarme')

    def dar_energia(self):
        self.energia+=1
        
    def quitar_energia(self):
        self.energia-=2

    def dar_diversion(self):
        self.diversion+=1
        
    def quitar_diversion(self):
        self.diversion-=1

    def dar_sed(self):
        self.sed+=1
        
    def quitar_sed(self):
        self.sed-=2

    def jugar(self):
        if self.diversion >= 10:
            print('Ya me aburri')
            return False

        self.dar_diversion()
        self.quitar_energia()
        self.quitar_sed()
        print('Oh :)')
        time.sleep(20)
        print('Que divertido\n\n')
        return True
    
    def comer(self):
        if self.energia >= 10:
            print('No tengo hambre\n\n')
            return False
        
        self.dar_energia()
        self.quitar_diversion()
        print('Yummy\n\n')
        return True

    def hidratarse(self):
        if self.sed >= 10:
            print('No tengo sed\n\n')
            return False
        
        self.dar_sed()
        print('Que refrescante!!\n\n')
        return True

    def status(self):
        print("""
 Te hablo un poco de mi:
 Mi nombre es %s y soy un %s
 * Mi diversion es de: %s
 * Mi energia es de: %s 
 * Mi hidratacion es de: %s
        """ % (self.nombre, self.especie, self.diversion, self.energia, self.sed))
