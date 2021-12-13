class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return f"{self.name} makes sound."


class Dog(Animal):
    def __init__(self, name, age):
        self.age = age
        super().__init__(name)

    def sound(self):
        return f"{self.name} Barks at {self.age}."


class Cat(Dog):
    def sound(self):
        return f"{self.name} Meow at {self.age}."


myCat = Cat("Bella", 3)
print(myCat.sound())
print(myCat.make_sound())


myDog = Dog("Bingo", 5)
print(myDog.sound())
print(myDog.make_sound())

animal = Animal("Dog")
print(animal.make_sound())

animal2 = Animal("Cat")
print(animal2.make_sound())
