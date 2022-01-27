import functools
from typing import Callable, Any

app = {}


def callback(key: str) -> Callable:
    def call_func(func: Callable) -> Callable:
        app[key] = func

        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            return func(*args, **kwargs)

        return wrapper

    return call_func


@callback('//')
def example() -> str:
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')

# зачтено
