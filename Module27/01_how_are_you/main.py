def how_are_you(function_to_decorate):
    def wrapped_func(*args, **kwargs):
        print("Как дела? Хорошо\nА у меня не очень! Ладно, держи свою функцию.")
        return function_to_decorate(*args, **kwargs)

    return wrapped_func


@how_are_you
def test() -> None:
    print('<Тут что-то происходит...>')


@how_are_you
def helloWorld(mess: str) -> None:
    print(mess)


test()
helloWorld("Hello world")
