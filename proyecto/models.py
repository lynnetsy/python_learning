import time
#from db import Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import registry
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


#La clase owner hereda de Base en db.py
class Owner(Base):
    __tablename__ = 'owners'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    pets = relationship("Pet", back_populates='owner')

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return self.name

    # el metodo serialize convierte el objeto en un diccionario
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email}


class Pet(Base):
    __tablename__='pets'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    animal_specie = Column(String, nullable=False)
    age = Column(Integer, nullable = False)
    energy_level = Column(Integer)
    hunger_level = Column(Integer)
    hydration_level = Column(Integer)
    diversion_level = Column(Integer)
    state_life = Column(String, nullable=False)
    id_owner = Column(Integer, ForeignKey("owners.id"))
    owner = relationship("Owner", back_populates="pets")

    def __init__(self, name, animal_specie, age, id_owner):
        self.name = name
        self.animal_specie = animal_specie
        self.age = age
        self.energy_level = 5
        self.hunger_level = 5
        self.hydration_level = 5
        self.diversion_level = 5
        self.state_life = 'alive'
        self.id_owner = id_owner

    def __str__(self):
        return self.name
    

    def register_pet(self):
        self.name = input('Introduce el nombre de la mascota que deseas registrar:\n')
        self.animal_specie = input('Introduce su especie:\n')
        self.age = input('Introduce su edad: \n')
        self.energy_level = input('Introduce su nivel de energia: \n')
        self.hunger_level = input('Introduce su nivel de hambre: \n')
        self.hydration_level = input('Introduce su nivel de hidratacion: \n')
        self.state_life = input('Introduce su estado actual (vivo o muerto): \n')

    """def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "animal specie": self.animal_specie,
            "age": self.age,
            "energy_level": self.energy_level,
            "hunger_level": self.hunger_level,
            "hydration_level": self.hydration_level,
            "state_life": self.state_life
            }"""

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

    """def status(self):
        print(
Te hablo un poco de mi:
 Mi nombre es %s y soy un %s
 * Mi diversion es de: %s
 * Mi energia es de: %s 
 * Mi hidratacion es de: %s
         % (self.nombre, self.especie, self.diversion, self.energia, self.sed))




"""
        