class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.age} years old {self.name}."
    
cat1 = Cat('Persian cat', 3)
cat2 = Cat('Indian cat', 2)

print(cat1)
print(cat2)