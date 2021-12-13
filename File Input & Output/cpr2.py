def totalZeros(nth: int):
    re, k = 0, 1
    while True:
        y, z = divmod(nth, k)
        x, y = divmod(y, 10)

        if x == 0:
            return re

        if y == 0:
            re += (x-1) * k + z + 1
        else:
            re += x * k
        k *= 10


print(totalZeros(10))  # 1
print(totalZeros(89))  # 8
print(totalZeros(9898))  # 343
