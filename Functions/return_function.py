def exponent(n1:int = 3, n2:int = 4, n3=5):
    num = n1**n2**n3
    return num

print(exponent(5, 2, 4))


def rem_dup(array: list = [2, 3, 4, 5, 6]):
    arr = []
    for i in array:
        if i not in arr:
            arr.append(i)
    return sorted(arr)

#l = input("Array seperated with comma: ").split(",")
#print(rem_dup())
#print(rem_dup([1, 7, 4, 4, 6, 5]))


def is_prime(num: int):
    n = 0
    for i in range(1, num+1):
        if num % i == 0:
            n += 1
    if n == 2:
        return True
    return False

print(is_prime(2))