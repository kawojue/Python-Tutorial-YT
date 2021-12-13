array = []

for a in range(1, 11):
    array.append(a)
print(array)

l = [i for i in range(1, 11)]
print(l)

k = [j for j in range(1, 11, 2)]
print(k)


def isEven(n):
    if n % 2 == 0:
        return True
    return False


even = [e for e in range(1, 21) if not isEven(e)]
print(even)
