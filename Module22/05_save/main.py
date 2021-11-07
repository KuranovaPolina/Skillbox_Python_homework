import os

string = input("Input string: ")
path_list = input("Input path (use " "): ").split(" ")
file_name = input("Input file name: ")
path = "C:" + os.path.sep + os.path.sep.join(path_list) + os.path.sep + file_name + ".txt"
print(path)
if os.path.exists(path):
    answer = input("Rewrite file? (True / False)")
    if answer == "True":
        file = open(path, 'w')
        file.write(string)
        file.close()
        print("Rewrited")
else:
    file = open(path, 'w')
    file.write(string)
    file.close()
    print("writed")

# зачтено
