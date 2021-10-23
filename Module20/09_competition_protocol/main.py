protocol = {}

N = int(input("N = "))

for i in range(N):
    game = input("{0}: ".format(i + 1))
    result, name = game.split(" ")

    if name in protocol.keys() and protocol[name] < result:
        protocol.pop(name)
        # TODO: Количество баллов нужно переводить в тип int
        protocol[name] = result
    else:
        protocol[name] = result

sorted_protocol_keys = sorted(protocol, key=protocol.get)

print("")
for i in range(3):
    name = sorted_protocol_keys[i]
    print("{0} level. {1} ({2})".format(i + 1, name, protocol[name]))

# TODO: Соритровка работает неверно:
"""
N = 4
1: 69485 Jack
2: 95715 qwerty
3: 95715 Alex
4: 197128 qwerty

1 level. qwerty (197128)
2 level. Jack (69485)
3 level. Alex (95715)
"""