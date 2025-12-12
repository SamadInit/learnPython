# this is the main class
from animal import Animals
print(" here are some theree diffrent animals :")


a1=Animals("yane")
a2=Animals("moriss")
a3=Animals("jack")

print(Animals.numberOfAnimals)

print(a1.__str__())
Animals.incNmbrOfAanimals()
print(Animals.numberOfAnimals)
