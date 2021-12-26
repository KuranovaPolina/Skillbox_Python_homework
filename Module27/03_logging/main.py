import datetime


def logging(function_to_decorate):
    def wrapped_func(*args, **kwargs) -> None:
        try:
            print(f"{function_to_decorate.__name__}")
            print(f"{function_to_decorate.__doc__}")
            return function_to_decorate(*args, **kwargs)
        except Exception as err:
            file_name = 'function_errors.log'
            file = open(file_name, 'a')
            file.write(f"{function_to_decorate.__name__} - {err}: {datetime.datetime.now()}\n")
            file.close()

    return wrapped_func


@logging
def first(x: int, y: int) -> None:
    """Some doc"""
    print(x / y)


first(1, 10)
print()
first(1, 0)
print()
first(0, 0)
print()

# зачтено
