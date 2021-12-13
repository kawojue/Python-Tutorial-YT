A = {2, 3, 4, 5}
B = {3, 2, 6, 7}

print(B.intersection(A))
print(A & B)

print(A.union(B))
print(A | B) # B | A

print(A.symmetric_difference(B))
print(A ^ B)

print(A.difference(B)) # diff(B-A) != diff(A-B)
print(A - B)

print(B.difference(A))
print(B - A)

x = {9, 10, 13}
y = {5, 8, 7, 2, 1, 4, 6, 3}

print(x.issubset(y))

print(y.issuperset(x))

print(y.isdisjoint(x))