def how_are_you(function_to_decorate):
    def wrapped_func(*args):
        print("Как дела? Хорошо\nА у меня не очень! Ладно, держи свою функцию.")
        function_to_decorate(*args)
    return wrapped_func


@how_are_you
def test():
    print('<Тут что-то происходит...>')

@how_are_you
def helloWorld(mess):
    print(mess)


test()
helloWorld("Hello world")
