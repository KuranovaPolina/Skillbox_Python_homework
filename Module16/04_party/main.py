guests = ['Petya', 'Vanya', 'Sasha', 'Liza', 'Katya']

while True:
    lenght = len(guests)
    print(f"Now there are {lenght} at the party: {guests}")
    action = input("The guest has come/left: ")

    if action == "go bad":
        print("The party was finished, everyone are sleeping")
        break
    else:
        name = input("Guest's name: ")
        if action == 'left':
            print(f"Bye, {name}\n")
            guests.remove(name)
        elif action == 'come' and lenght < 6:
            print(f"Hi, {name}\n")
            guests.append(name)
        else:
            print(f"Sori, {name}, there are not places\n")