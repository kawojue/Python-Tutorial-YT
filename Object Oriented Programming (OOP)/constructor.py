class Student:
    def __init__(self, name, id, level):
        self.name = name
        self.lvl = level
        self.no = id

    def getStudentInfo(self):
        return f"[{self.no}] -> {self.name} -> {self.lvl}"

    def __str__(self):
        return f"Welcome {self.name}!"


student1 = Student("Always Appear", 5, "Grade 12")
print(student1.getStudentInfo())
print(student1)

student2 = Student("Mary Alice", 3, "Grade 10")
print(student2.getStudentInfo())
print(student2)
