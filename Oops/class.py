class Dog:
    species = "Canine"
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
dog1 = Dog("Buddy", 3)
dog2 = Dog("Charlie", 5)

print(dog1.name)
print(dog1.age)
print(dog1.species)
print(Dog.species)
print(f"Name of the dog2 is {dog2.name} and age is {dog2.age}")