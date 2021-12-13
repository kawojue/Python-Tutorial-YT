# w -> write mode
# a -> append mode
# r -> read mode
file = open("pswd.txt", "r")
print(file.readline())
print(file.readlines())
file.close()


with open("code.txt", "r") as code:
    # # code.write("Numbers: \n")
    # for i in range(1, 11):
    #     code.write(f"{i}\n")
    print(code.readlines())
