from main import Set

a = "1372137154"
b = "234"

newSet = Set(a, b)
newSet2 = Set(b, a)
print(newSet.is_superset())
print(newSet2.is_subset())

print(newSet.difference())
print(newSet2.difference())

print(newSet.union())
