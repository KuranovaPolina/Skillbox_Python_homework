import time


def slower(function_to_decorate):
    def wrapped_func(*args, **kwargs) -> None:
        time.sleep(3)
        return function_to_decorate(*args, **kwargs)

    return wrapped_func


@slower
def test() -> None:
    print('<Тут что-то происходит...>')


print("1")
test()
