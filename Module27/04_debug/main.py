def args_out(args: list) -> str:
    res = ''
    for a in args:
        if isinstance(a, str):
            res += '"' + str(a) + '"'
        else:
            res += str(a)
        res += ", "
    return res


def kwargs_out(kwargs: dict) -> str:
    res = ''
    for key, k in kwargs.items():
        if isinstance(k, str):
            k = '"' + str(k) + '"'
        res += str(key) + '=' + str(k) + ", "
    return res[:-2]


def debug(function):
    def wrapped_func(*args, **kwargs):
        a_line = args_out(args)
        k_line = kwargs_out(kwargs)
        if k_line == "":
            print(f"Вызывается {function.__name__}({a_line[:-2]})")
        else:
            print(f"Вызывается {function.__name__}({a_line}{k_line})")
        print(f"'{function.__name__}' вернула значение {function(*args, **kwargs)}")
        print(function(*args, **kwargs))
        return function(*args, **kwargs)

    return wrapped_func


@debug
def greeting(name: str, age=None) -> str:
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растешь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)


greeting("Том")
greeting("Миша", age=100)
greeting(name="Катя", age=16)

# зачтено
