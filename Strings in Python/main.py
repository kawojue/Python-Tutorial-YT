name = "Always Appear"
age = 17

print("My name is", name, "and i am", age, "years old")

print(len(name))
print()

s = "Subscribe"

print(s[0:1])  # [begin:end:step]
print(s[0:12:2])
print(s[::-1])
print()
sentence = "this is python Course"

lower = sentence.lower()  # lowercase
upper = sentence.upper()  # uppercase

print(lower, upper)

title = sentence.title()
print(title)

capitalize = sentence.capitalize()
print(capitalize)

index = sentence.index("C")
print(index)

sent2 = "python "

print(sent2.find("o"))

print(sent2.replace("Course", "Tutorial"))

print(sent2.endswith("e")) # True, False

print(sent2.startswith("p".upper()))

print(sent2.isupper())

print(sent2.islower())

t = " python tutorial "
print(t.strip())

print(t.lstrip())

print(t.rstrip())