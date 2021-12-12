def info(name: str, age: int):
    return f"My name is {name} and I am {age} years old."


print(info(age=19, name="Mary"))


def division(x, y):
    if y == 0:
        return "Cannot Divide by Zero"
    return x / y


print(division(y=5, x=10))
