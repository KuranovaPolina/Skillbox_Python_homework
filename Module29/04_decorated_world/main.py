from typing import Callable, Any


def decorator_with_args_for_any_decorator(decorator: Callable) -> Callable:
    def decorator_args(*args, **kwargs) -> Callable:
        def wrapper(func) -> Any:
            return decorator(func, *args, **kwargs)

        return wrapper

    return decorator_args


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args, **kwargs) -> Callable:
    def wrapper(*fargs, **fkwargs) -> Any:
        print("Переданные арги и кварги в декоратор:", args, kwargs)
        return func(*fargs, **fkwargs)

    return wrapper


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)

# зачтено
