#CLASE = MOLDE O RECETA
#Un objeto es el resultado de ese molde o receta
#atributos = caracteristicas de la clase
#metodos = funciones o cosas que puede hacer 
import random

class Cat:
    def __init__(self, name, last_name):
        self.patas = 4
        self.ojos = 2
        self.cola = 1
        self.bigotes = 10
        self.name = name
        self.last_name = last_name
        self.catched = False

    def saltar(self):
        print("saltar")

    def comer(self):
        print("comer")

    def get_full_name(self):
        return f"{self.name} {self.last_name}"

    def play(self, stats):
        if stats % 3 == 0:
            self.catched = True
            print(f"{self.get_full_name()} esta atrapado")
        else:
            self.catched = False
            print(f"{self.get_full_name()} se escapo")
        return self.catched



class Dog:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    def get_full_name(self):
        return f"{self.name} {self.last_name}"

    def run(self):
        print("Correr")

    def play(self, pet):
        print(f"{self.get_full_name()} Juega con {pet.get_full_name()}")
        rand = random.randint(0, 9)
        catched = pet.play(rand)
        if catched:
            print(f"{self.get_full_name()} Esta contento")
        else:
            print(f"{self.get_full_name()} Ladra")
      
   
class Bird:
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name
        self.catched = False
    
    def get_full_name(self):
        return f"{self.name} {self.last_name}"

    def play(self, stats):
        fly = random.randint(0, 100)
        if stats == fly:
            self.catched = True
            print(f"{self.get_full_name()} Se lo comieron")

        else:
            self.catched = False
            print(f"{self.get_full_name()} Voló muy lejos")
        return self.catched



cucu = Cat("Cucu", "Perez")
cucu.get_full_name()

bernie = Dog("Bernardo", "unknown")
bernie.get_full_name()
bernie.play(cucu)
bernie.play(cucu)
bernie.play(cucu)
bernie.play(cucu)
bernie.play(cucu)

print(cucu.catched)

coco = Bird("Coco", "Cacas")
bernie.play(coco)
bernie.play(coco)
bernie.play(coco)
bernie.play(coco)
bernie.play(coco)

