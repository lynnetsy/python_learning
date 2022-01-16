import time

class owners():
    id = None
    name = None
    email = None
    
    def register_owner(self):
        self.name = input('Introduce tu nombre con el que deseas registrarte:\n')
        self.email = input('Introduce tu email:\n')
        self.id = input('Introduce tu id:\n')
        

    def keep_owner(self):
        diccionario = {'id':self.id,'Name':self.name,'Email:':self.email}
        
        
        
        
        # ESTO SIRVE PARA LISTAR LOS VALORES DE DICCIONARIOS CON FORMATO
        # for indice, valor in diccionario.items():
          #  print(indice, valor)

class pets():
    name = None
    animal_specie = None
    age = 0
    energy_level = 0
    hunger_level = 0 
    hydration_level = 0
    diversion_level = 0
    state_life = None
    id_owner = 0

    def register_pet(self):
        self.name = input('Introduce el nombre de la mascota que deseas registrar:\n')
        self.animal_specie = input('Introduce su especie:\n')
        self.age = input('Introduce su edad: \n')
       

    def records_pet(self):
        diccionario=[]
        for valores in regis:
            diccionario.append(valores)

            



    


chucha = pets()
chucha.register_pet()
chucha.records_pet()