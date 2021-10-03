file_name = input("Input file name: ")

if file_name.startswith("@" or "№" or "$" or "%" or "^" or "&" or "*" or "(" or ")"):
    print("Wrong start")
elif not file_name.endswith(".txt" or ".docx"):
    print("Wrong end")
else:
    print("Right file's name")

# TODO: .startswith() если вы хотите передать несколько символов, их нужно передавать в виде кортежа.
