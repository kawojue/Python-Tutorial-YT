# Map & Filter

# map(func, list) likewise filter.

def positive(n):
    return n >= 0


li = [2, 4, -2, -4, 6, -7, 9]

p = filter(positive, li)
print(list(p))


def add(n):
    return n+5


m = sorted(list(map(add, li)), reverse=True)
print(m)

square = list(map(lambda a: a**2, li))  # Square each element in the List.
print(square)

filt = list(filter(lambda j: j % 2 == 0, li))  # Filters out odd numbers in the list.
print(filt)
