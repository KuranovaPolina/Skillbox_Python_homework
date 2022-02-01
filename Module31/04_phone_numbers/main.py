import re


numbers = ['9999999999', '999999-999', '99999x9999']

for i in range(len(numbers)):
    if len(numbers[i]) == 10 and re.search(r'[89]\d{9}', numbers[i]):
        print(f"{i+1} number: ok")
    else:
        print(f"{i+1} number: not ok")
