is_cool = True
if is_cool is True:
    print("Go and Code")
elif is_cool is False:
    print("Play games or \n Read some PDFs")
else:
    print("Take a Nap")

#0 - Fasle, 1 - True

# num > 0 -> Positive, num < 0 Negative, num = 0 -> Zero

num = int(input("Number: "))
if num > 0:
    print(f"{num} is Positive")
elif num < 0:
    print(f"{num} is Negative")
else:
    print(f"{num} is Neutral")