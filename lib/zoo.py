from lib.animal import Animal

class Zoo:

    all = []

    def __init__(self, name, location):
        self.name = name
        self.location = location
        Zoo.all.append(self)

    @property
    def animals(self):
        return [animal for animal in Animal.all if animal.zoo == self]
        
    @property
    def animal_species(self):
        return list ({animal.species for animal in self.animals})
           
    @property
    def find_by_species(self,species):
        return [animal for animal in self.animals if animal.species == species]
    
    @property
    def animal_nicknames(self):
        return[animal.nickname for animal in self.animals]
    
    @classmethod
    def find_by_location(cls,location):
        return[zoo for zoo in cls.all if zoo.location == location]