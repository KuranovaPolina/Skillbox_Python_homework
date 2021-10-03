file_name = input("Input file name: ")
wrong_start_letter = tuple("@№$%^&*()")

if file_name.startswith(wrong_start_letter):
    print("Wrong start")
elif not file_name.endswith(".txt" or ".docx"):
    print("Wrong end")
else:
    print("Right file's name")
