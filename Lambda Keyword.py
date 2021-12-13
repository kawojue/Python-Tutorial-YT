# Lambda Keyword or Anonymous Function

def add(x):
    return x+1


print(add(7))

func = lambda x: x+1
print(func(7))

secFunc = lambda x, y: x+y
print(secFunc(4, 5))

thirdFunc = lambda a: a % 3 == 0

li = [t for t in range(1, 21) if thirdFunc(t)]
print(li)
