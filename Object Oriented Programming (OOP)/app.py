class Person:
    def getInfo(self):
        return f"My name is {self.name} and I am {self.age}years old."

    def walk(self):
        if self.age < 2:
            print(f"{self.name} cannot walk yet because he/she is {self.age}years")
        else:
            print(f"{self.name} can walk because he/she is {self.age}")


person1 = Person()
person1.name = "Always Appear"
person1.age = 18
person1.walk()
print(person1.getInfo())


person2 = Person()
person2.name = "Mary Alice"
person2.age = 1.5
person2.walk()
print(person2.getInfo())
