string1 = input("First string: ")
string2 = input("Second string: ")

if string1 == string2:
    print("Strings are equal. Shift: 0")
elif len(string1) != len(string2):
    print("Must not")
else:
    lens = len(string1)
    shift = 1
    must = False

    for i in range(lens):
        string2 = string2[lens - 1: lens - 2:-1] + string2[:lens - 1]
        if string2 == string1:
            print("Must. Shift:", shift)
            must = True
            break
        else:
            shift += 1

    if not must:
        print("Must not")

# зачтено
