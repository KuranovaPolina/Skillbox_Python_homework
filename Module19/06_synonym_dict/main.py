N = int(input("N = "))

synonym_dict = {}

for i in range(N):
    pair = input("{0} pair: ".format(i+1)).lower().split(" - ")
    synonym_dict[pair[0]] = pair[1]
    synonym_dict[pair[1]] = pair[0]

while True:
    word = input("Input word: ").lower()

    if word in synonym_dict.keys():
        print("Synonym:", synonym_dict[word])
        break
    else:
        print("Word not find")