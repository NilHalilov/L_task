"""Модуль для определения четности целого числа"""

import os


def get_user_num() -> int:
    """Функция для запроса у пользователя проверяемого числа"""

    username: str = os.getlogin()
    if not username:
        username: str = 'Уважаемый разработчик из "Lesta Games"'

    while True:
        try:
            user_num: int = int(input(f'\n{username}, введите любое целое число: '))
            return abs(user_num)

        except ValueError as e:
            print(
                {
                    'Error': e.args[0],
                    'Message': 'Нужно ввести любое целое число! Попробуйте ещё раз!',
                }
            )


def check_num(num: int = None) -> bool:
    """
    Функция для определения четности целого числа
    :param num: Передаваемое целое число
    """

    if num is None:
        num = get_user_num()

    if num <= 0:
        return num == 0
    else:
        return check_num(num - 2)


if __name__ == '__main__':
    print(check_num())
