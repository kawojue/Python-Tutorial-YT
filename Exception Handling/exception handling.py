try:
    num = int(input("Number: "))
    print(num)
except ValueError:
    print("Invalid Input.")
except ZeroDivisionError:
    print("Indeterminate!")
print("Thanks!")