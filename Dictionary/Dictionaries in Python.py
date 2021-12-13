new_dict = {"key": "value"}

car = {"Brand": "Toyota",
       "Model": "Camry", 
       "Year": 2018,
       }

print(car.items())

print(car.keys())

print(car.values())

for x in car.values(): # key(), # items
    print(x)

car["Brand"] = "Tesla"
car["Model"] = "Model S"
car["Year"] = 2020
car["Color"] = "White"


print(car)

print("fruit" in car) # checking

car.update({"type": "SUV Shape"})

print(car)

# del car


# car2 = dict(car)
car2 = car.copy()

print(car2)

#car2.pop("Model")

# print(car2)

car2.popitem()

print(car2)

number = {"1": "One", "2": "Two", "3": "Three", "4": "Four", "5": "Five"}

result = ""

user = input("Phone: ")

for u in user:
    result += number.get(u, u) + " "
print(result)