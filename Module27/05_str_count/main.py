def counter(func):
    def wrapper(*args, **kwargs) -> None:
        wrapper.count += 1
        func(*args, **kwargs)  # TODO: Не забываем возвращать результат

    wrapper.count = 0
    return wrapper


@counter
def f() -> None:
    print("Doing something")


f()
f()
f()

print(f.count)
