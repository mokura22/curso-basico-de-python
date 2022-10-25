class Animal():
    def __init__(animal, especie, habitat, alimentacion) :
        animal.especie = especie
        animal.habitat = habitat
        animal.alimentacion= alimentacion
    
    def __str__ (animal):
        return f"El animal : es {animal.especie}, su habitat es: {animal.habitat} y su  tipo de alimentacion es: {animal.alimentacion}" 
     
perro = Animal("Perro", "Terrestre", "omnivoro")
print (perro)        
        
