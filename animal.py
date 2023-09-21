class animal:
    def __init__(self,especie,edad) :
        self.especie=especie
        self.edad=edad
    def hacer_sonido(onomatopella):
        return onomatopella
    
class perro(animal):
    def raza(raza):
        return raza
    def hacer_sonido(self):
        return "Guau"
    
class gato(animal):
    def color(colorgat):
        return colorgat
    def hacer_sonido(self):
        return "Miau"
    
dog=perro("canus_lupus",20)

print(dog.especie)

print(dog.hacer_sonido(),perro.raza("doberman"))

cat=gato("mirringo",10)

print(cat.especie)

print(cat.hacer_sonido(),gato.color("negro"))


def presentar_animal(animal):
    if animal=="gato":
        cati=gato("catus",20)
        return cati.especie,cati.edad,cati.hacer_sonido()
    if animal=="perro":
        perri=perro("cannus",200)
        return perri.especie,perri.edad,perri.hacer_sonido()

an=input("que animal es?")
print(presentar_animal(an))