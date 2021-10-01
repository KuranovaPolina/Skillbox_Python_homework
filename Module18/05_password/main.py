def NumberCount(string):
    count = 0
    string_list = list(string)

    for letter in string_list:
        if letter.isdigit():
            count += 1

    return count

while True:
    password = input("Password: ")

    if len(password) < 8 or password.islower() or NumberCount(password) < 3:
        print("Try again")

    else:
        print("Reliable password")
        break