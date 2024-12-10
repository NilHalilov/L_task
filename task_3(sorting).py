"""Модуль для реализации алгоритма сортировки"""


def quick_sort_handmade(user_list: list) -> list:
    """Реализация быстрой сортировки"""

    if len(user_list) == 0:
        return []
    else:
        pivot = user_list[(len(user_list) // 2)]
        less_pivot = [nums for nums in user_list if nums < pivot]
        more_pivot = [nums for nums in user_list if nums > pivot]
        left_part = quick_sort_handmade(less_pivot)
        right_part = quick_sort_handmade(more_pivot)
        central_part = []
        duplicates = user_list.count(pivot)
        if duplicates > 1:
            for _ in range(duplicates):
                central_part.append(pivot)
        else:
            central_part = [pivot]

        return left_part + central_part + right_part


if __name__ == '__main__':
    print(
        "Отсортированный список:",
        quick_sort_handmade([33, 1, 45, -1, 78, 23, 1005, 20, 49, 17, 23, 54, 76, 2, 33, 0, 98])
    )
