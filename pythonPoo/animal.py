class Animals():
    numberOfAnimals=0

    def __init__(self, name):
        self.name=name
        self._weight=0.0
        self.__age=0
        Animals.numberOfAnimals+=1

    
    def setWeight(self,weight):
        self._weight=weight
    
    def setAge(self,age):
        self.__age=age

    def incNmbrOfAanimals():
        Animals.numberOfAnimals+=1

    def __str__(self):
        
        return f"name :{self.name} the weight : {self._weight} the age : {self.__age}"