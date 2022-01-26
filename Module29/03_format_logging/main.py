from typing import Callable, Any
import functools
import datetime
import time


def format_converter(form: str) -> str:
    for sym in form:
        if sym.isalpha():
            form = form.replace(sym, '%' + sym)

    return form


def timer(cls, func: Callable, day_format: str) -> Callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print(f"- Запускается '{cls.__name__}.{func.__name__}'. "
              f"Дата и время запуска: {datetime.datetime.now().strftime(day_format)} ")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"- Завершение '{cls.__name__}.{func.__name__}', время работы = {round(end - start, 3)}s ")
        return result
    return wrapper


def log_methods(format: str) -> Callable:
    @functools.wraps(timer)
    def decorate(cls):
        for method in dir(cls):
            if not method.startswith('__'):
                current_method = getattr(cls, method)
                new_format = format_converter(format)
                decorated_method = timer(cls, current_method, new_format)
                setattr(cls, method, decorated_method)
        return cls
    return decorate


@log_methods("b d Y - H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
