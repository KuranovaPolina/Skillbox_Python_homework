def how_are_you(function_to_decorate):
    # TODO: Не забываем передавать ещё и **kwargs
    def wrapped_func(*args):
        print("Как дела? Хорошо\nА у меня не очень! Ладно, держи свою функцию.")
        function_to_decorate(*args)  # TODO: Не забываем передавать ещё и **kwargs и возвращать результат

    return wrapped_func


@how_are_you
def test() -> None:
    print('<Тут что-то происходит...>')


@how_are_you
def helloWorld(mess: str) -> None:
    print(mess)


test()
helloWorld("Hello world")
