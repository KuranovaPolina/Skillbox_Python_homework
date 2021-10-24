protocol = {}

N = int(input("N = "))

for i in range(N):
    game = input("{0}: ".format(i + 1))
    result, name = game.split(" ")
    result = int(result)

    if name in protocol.keys() and protocol[name] < result:
        protocol.pop(name)
        protocol[name] = result
    else:
        protocol[name] = result

sorted_protocol_keys = sorted(protocol, key=protocol.get, reverse=True)

print("")
for i in range(3):
    name = sorted_protocol_keys[i]
    print("{0} level. {1} ({2})".format(i + 1, name, protocol[name]))

# зачтено
