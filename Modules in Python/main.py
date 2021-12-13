class Set:
    def __init__(self, string1, string2):
        self.string1 = string1
        self.string2 = string2

    @staticmethod
    def remDup(string):
        newString = ""
        for i in string:
            if i not in newString:
                newString += i
        return newString

    def intersection(self):
        intersect = ""
        for s in self.string1:
            if s in self.string2:
                intersect += s
        return self.remDup(intersect)

    def union(self):
        return "".join(sorted(self.remDup(self.string1 + self.string2)))

    def is_subset(self):
        count = 0
        for i in self.string1:
            if i in self.string2:
                count += 1
        return count == len(self.string1)

    def is_superset(self):
        count = 0
        for i in self.string2:
            if i in self.string1:
                count += 1
        return count == len(self.string2)

    def difference(self):
        diff = ""
        for i in self.string1:
            if i not in self.string2:
                diff += i
        return self.remDup(diff)
