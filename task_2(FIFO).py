"""Модуль для реализации циклического буфера FIFO"""

from collections import deque
from typing import Union, Type, Any


class FirstCustomFIFO:
    """Класс для реализации FIFO при помощи list"""

    def __init__(self, queue_size: int) -> None:
        self.__max_size: int = queue_size
        self.__current_size: int = 0
        self.__last_add_position: int = 0
        self.__first_to_delete_position: int = self.__last_add_position - 1
        self.__handmade_queue: list = [None for _ in range(queue_size)]

    @property
    def max_size(self) -> int:
        """Геттер для получения максимального размера очереди"""
        return self.__max_size

    @property
    def current_size(self) -> int:
        """Геттер для получения текущего размера очереди"""
        return self.__current_size

    @property
    def handmade_queue(self) -> list:
        """Геттер для получения значений элементов очереди"""
        return self.__handmade_queue

    def put_in_queue(self, user_info: Any):
        """Метод для добавления данных в очередь"""
        if self.__current_size == self.__max_size:
            raise IndexError('Очередь заполнена, добавление невозможно.')
        else:
            self.__handmade_queue[self.__last_add_position] = user_info
            self.__current_size += 1
            self.__last_add_position = (self.__last_add_position + 1) % self.__max_size

    def pick_up_from_queue(self) -> Any:
        """Метод для безвозвратного извлечения данных из очереди"""
        if self.__current_size == 0:
            raise IndexError('Очередь пуста, извлекать нечего.')
        else:
            self.__first_to_delete_position = (self.__first_to_delete_position + 1) % self.__max_size
            self.__current_size -= 1
            info: Any = self.__handmade_queue[self.__first_to_delete_position]
            self.__handmade_queue[self.__first_to_delete_position] = None
            return info


class SecondCustomFIFO:
    """Класс для реализации FIFO при помощи deque"""

    def __init__(self, queue_size: int) -> None:
        self.__max_size: int = queue_size
        self.__current_size: int = 0
        self.__handmade_queue: deque = deque([], maxlen=queue_size)

    @property
    def current_size(self) -> int:
        """Геттер для получения текущего размера очереди"""
        return self.__current_size

    @property
    def handmade_queue(self) -> deque:
        """Геттер для получения значений элементов очереди"""
        return self.__handmade_queue

    def put_in_queue(self, user_info: Any):
        """Метод для добавления данных в очередь"""
        if len(self.__handmade_queue) == self.__max_size:
            raise IndexError('Очередь заполнена, добавление невозможно.')
        else:
            self.__handmade_queue.append(user_info)
            self.__current_size += 1

    def pick_up_from_queue(self) -> Any:
        """Метод для безвозвратного извлечения данных из очереди"""
        if len(self.__handmade_queue) == 0:
            raise IndexError('Очередь пуста, извлекать нечего.')
        else:
            some_info: Any = self.__handmade_queue.popleft()
            self.__current_size -= 1
            return some_info


def show_and_test(chosen_way: Union[Type[FirstCustomFIFO], Type[SecondCustomFIFO]], queue_size: int):
    """Функция для демонстрации работы классов 'FirstCustomFIFO' и 'SecondCustomFIFO'"""

    test_queue = chosen_way(queue_size)

    for _num in range(queue_size + 1):
        print(f'Текущая очередь: {test_queue.handmade_queue}.'
              f'Она состоит из {test_queue.current_size} элеметов.\n')
        print(f'>> Добавим элемент №{_num + 1}')
        try:
            test_queue.put_in_queue(f'test_data__{_num + 1}')
        except IndexError as e:
            print(e)
    print('-' * 20)
    for _num in range(queue_size + 1):
        print(f'Текущая очередь: {test_queue.handmade_queue}.'
              f'Она состоит из {test_queue.current_size} элеметов.\n')
        print(f'>> Заберем элемент')
        try:
            data = test_queue.pick_up_from_queue()
            print(f'Полученный элемент: {data}')
        except IndexError as e:
            print(e)


if __name__ == '__main__':
    show_and_test(FirstCustomFIFO, 4)
    print('=' * 100)
    show_and_test(SecondCustomFIFO, 4)
