def show_chat(user_name):
    try:
        with open('chat_text.txt', 'r') as file:
            file_text = file.read()
            if file_text == "":
                print("No message")
            else:
                for i_line in file_text.split("\n"):
                    i_line_list = i_line.split(" ")
                    if i_line_list[0] == (user_name + ":"):
                        mes = " ".join(i_line_list[1:])
                        print(f"You: {mes}")
                    else:
                        print(i_line)
    except FileNotFoundError:
        print("No message")


def write_message(user_name, message):
    file = open('chat_text.txt', 'a')
    file.write(f"{user_name}: {message}\n")
    file.close()


user = input("Input user name: ")

while True:
    action = input("\nSelect an action: (1 or 2)\n1. Chat text\n2. Send email\n")
    if action == "1":
        show_chat(user)
    elif action == "2":
        email = input("Message: ")
        write_message(user, email)
    else:
        print("Error. Try again")

# зачтено
