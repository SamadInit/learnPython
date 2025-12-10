"""
my_dictionnary={}

my_dictionnary["abdessamad"]="audiA4"
my_dictionnary["mohammed amine"]="audirs6"
my_dictionnary["taha"]="mercedes classA"

print(len(my_dictionnary))
print(my_dictionnary)
print(my_dictionnary[taha])
"""

def rUinTheList(d:dict):
    user=input("ennter ur id ")
    if id in d:
        print("u're r registred ")
    else :
        print("we coudn't find you")

my_dict={"id1":"abdessmad", "id2":"mohammed amine", "id3":"ahlam"}

rUinTheList(my_dict)