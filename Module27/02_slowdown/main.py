import time


def slower(function_to_decorate):
    def wrapped_func(*args) -> None:
        time.sleep(3)
        function_to_decorate(*args)
    return wrapped_func


@slower
def test() -> None:
    print('<Тут что-то происходит...>')


print("1")
test()
