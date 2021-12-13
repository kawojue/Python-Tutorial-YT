subjects = ["Mathematics", "English", "Physics"]
subjects.append("Basic Electricity")
subjects.append("Chemistry")
subjects.pop()
subjects.pop()
subjects.insert(2, "Economics")

courses = ["Computer", "Petroleum", "Medicine"]

subjects.extend(courses)
print(subjects)

numbers = [-1, 0, 1, 2, 3, 4, 4, 3, 5, 2, 4, 5, -2, 200, 100]
print(sum(numbers))  # Add all numbers in an array

print(min(numbers))  # Get the lowest number in an array

print(max(numbers))  # Get the largest number in an array

print(sorted(numbers))  # sort the array in ascending order

print(sorted(numbers, reverse=True)) # sort array in descending order

print(numbers.count(4))  # occurrence of an element in an array

# numbers.sort()

print(numbers)

# numbers.remove(0)

# del numbers[1]

print(numbers.index(5))

print(numbers)