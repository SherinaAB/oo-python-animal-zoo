class Animal:
    
    def __init__(self,species,weight,nickname,zoo_instance):
        self.species = species
        self.weight = weight
        self.nickname = nickname
        self.zoo_instance = zoo_instance
        Animal.all.append(self)

    @classmethod
    def find_by_species(cls, species):
        return[animal.nickname for animal in cls.all if animal.species == species]