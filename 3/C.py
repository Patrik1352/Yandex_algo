n = int(input())
a = list(map(int, input().split()))


def min_numbers_to_remove_correct(a):
    # Сортируем массив
    a.sort()

    # Инициализируем переменные для подсчета
    counts = {}
    # Подсчитываем количество каждого числа в массиве
    for number in a:
        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1

    # Находим два самых частых соседних числа (разность которых не превышает 1)
    max_pair_count = 0
    sorted_keys = sorted(counts.keys())
    for i in range(len(sorted_keys) - 1):
        if sorted_keys[i + 1] - sorted_keys[i] <= 1:
            max_pair_count = max(max_pair_count, counts[sorted_keys[i]] + counts[sorted_keys[i + 1]])
        else:
            max_pair_count = max(max_pair_count, counts[sorted_keys[i]])
    max_pair_count = max(max_pair_count, counts[sorted_keys[-1]])  # Убедимся, что учли последний элемент

    # Возвращаем количество чисел для удаления
    return len(a) - max_pair_count


print(min_numbers_to_remove_correct(a))

