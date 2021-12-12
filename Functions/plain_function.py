def greet(name: str):
    print(f"Hello {name}")

greet("Alice")
greet("Bob")

def add7(num: int):
    n = num + 7
    print(n)

add7(5)
add7(6)
add7(7)


def greet_user(firstname, lastname):
    print(f"Hello I am {firstname} {lastname}")

greet_user(lastname = "Alice", firstname = "Bob")