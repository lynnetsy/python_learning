from models import Owner, Pet
from db import session

class OwnerRepository():
    def save(self, name, email):
        owner = Owner(name, email)
        #creamos una instancia de owner
        session.add(owner)
        session.commit()

    def find_by_email(self, email):
        owner = session.query(Owner).filter(Owner.email==email).first()
        return owner


class PetRepository():
    def save(self, name, animal_specie, age, owner):
        id_owner = owner.id
        pet = Pet(name, animal_specie, age, id_owner)
        session.add(pet)
        session.commit()
    
    def get_by_owner(self, owner):
        pets = session.query(Pet).filter(Pet.id_owner==owner.id).all()
        return pets








