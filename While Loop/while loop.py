"""
while condition is True:
    do_this
"""
"""
i = 0
while i < 6:
    print(i)
    i += 1  # i = i + 1
"""
"""
k = 1
while k <= 12:
    print(k * 3)
    k += 1  # k = k + 1
"""

word = "pneumococci"
vowel = "aeiou"
k = 0
count = 0
while k < len(word):
    if word[k] in vowel:
        count += 1
        print(word[k], end=" ")
    k += 1
print(count)
