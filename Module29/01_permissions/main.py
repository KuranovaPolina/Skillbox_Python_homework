import functools
from collections.abc import Callable


def check_permission(user: str) -> Callable:
    def check(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            if user in user_permissions:
                return func(*args, **kwargs)
            else:
                print(f"PermissionError:"
                      f" У пользователя недостаточно прав, "
                      f"чтобы выполнить функцию {func.__name__}")
        return wrapped
    return check


user_permissions = ['admin']


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()
