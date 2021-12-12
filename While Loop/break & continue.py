guess = "12345"
guess_limit = 5
guess_count = 0
while guess_count < guess_limit:
    password = input("Password: ")
    if password == guess:
        print("You're right.")
        guess_count = 5
    guess_count += 1
