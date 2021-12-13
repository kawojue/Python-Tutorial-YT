array = [1, 2, 3]
List = ["Hello", 1, 2.3]

for num in List:
    pass

l = list(range(1, 5))
print(l)

fruits = ["Apple", "Orange", "Mango"]
for fruit in fruits:
    #print(fruit + " is a fruit")
    pass

number = list(range(1, 6)) # 5(6)/2 = 5(3) = 15
i, j = 0, 0
while i < len(number):
    j += number[i]
    i += 1
print(j)


num = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]
k, n = 0, 0
while k < len(num):
    if num[k] < 0:
        n = n + num[k]
    k += 1
print(n)

a, b = 0, 0
while a < len(num):
    if num[a] > 0:
        b += num[a]
    a += 1
print(b)
