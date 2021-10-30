site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def find_key(dictionary, key, depth, now = 0):
    if depth != -1 and depth < now:
        return

    if key in dictionary:
        return dictionary[key]

    for new_dictionary in dictionary.values():
        if isinstance(new_dictionary, dict):
            result = find_key(new_dictionary, key, depth, now + 1)

            if result:
                break

    else:
        result = None

    return result


user_key = input("Key: ")
depth = int(input("Input depth (if not need, write 0)"))
result = find_key(site, user_key, depth - 1)
if result:
    print(result)
else:
    print("Not found")