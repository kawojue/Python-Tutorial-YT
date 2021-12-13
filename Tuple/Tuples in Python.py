newTuple = (2, 3, 5, 4.3, "Hello", False) # It is always immutable
# newTuple[0] = 6 -> Error
for i in newTuple:
    #print(i)
    pass

j = 0
while j < len(newTuple):
    # print(newTuple[j])
    j += 1

fruit1 = tuple(("Apple", "Banana", "Mango"))
fruit2 = ("Orange", "Grape")
fruits = fruit1+fruit2

number = (1, 4, 2, 3, 4, 3, 3, 5)
print(number[2: 5])

print(number[-1])

print(number.count(4))

num1 = (1, 2, 3)
num1 = list(num1)
num1.remove(3)
num1 = tuple(num1)
print(num1)

del num1

# print(num1)

num1 = (1, 2, 3, 4, 5)
print(num1.index(4))


(green, yellow, red) = ("Apple", "Banana", "Grape")

print(green)
print(yellow)
print(red)

num1 = (1, 2, 3, 4, 5)
(one, two, three, *numbers) = num1

print(one)
print(two)
print(three)
print(tuple(numbers))
