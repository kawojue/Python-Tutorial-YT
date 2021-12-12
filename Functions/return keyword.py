def info(name: str, age: int):
    return f"My name is {name} and I am {age} years old."


print(info("Mary", 19))


def division(x, y):
    if y == 0:
        return "Cannot Divide by Zero"
    return x / y


print(division(5, 0))


def remDup(array: list):
    newArray = []
    for element in array:
        if element not in newArray:
            newArray.append(element)
    return newArray


print(remDup([2, 3, 4, 2, 5, 4, 3]))
print(remDup([6, 7, 8, 3, 7, 8, 7]))


def is_prime(num: int):
    count = 0
    for i in range(1, num+1):
        if num % i == 0:
            count += 1
    if count == 2:
        return True
    return False


# print(is_prime(1000000001))
print(is_prime(57))
