IP_string = input("Input IP: ")
IP_list = IP_string.split(".")

if len(IP_list) != 4:
    print("IP is 4 numbers separated by dots")
else:
    IP_is_rightIP = True
    for number in IP_list:
       if not number.isdigit():
           print("{0} is not a number".format(number))
           IP_is_rightIP = False
           break
       elif int(number) > 255:
           print("{0} exceeds 255".format(number))
           IP_is_rightIP = False
           break
    if IP_is_rightIP == True:
        print("IP address is correct")