# enumerate & zip function

names = ["Python", "Always Appear", "JavaScript", "C#"]
uses = ["Data Science", "Learning", "Web", "Game"]

index = 0

for i, name in enumerate(names, start=1):
    print(i, name)
    # print(f"{name} is for {use}")

for use, name in zip(uses, names):
    print(f"{name} is for {use}")
