import numpy as np


N = int(input())
K = int(input())
x = list(map(int, input().split()))


def find_outlier_optimized(N, K, x):
    x_arr = np.array(x)
    # Инициализация кэша для хранения уже вычисленных значений перцентиля
    percentile_cache = {}

    for day in range(K, N):
        if day not in percentile_cache:
            # Вычисление и кэширование перцентиля, если он еще не был вычислен для данного дня
            percentile_cache[day] = np.percentile(x_arr[:day], 90)

        threshold = percentile_cache[day]
        if x_arr[day] > threshold:
            # Проверка условия выхода, используя кэшированное значение перцентиля
            return day + 1

    # Если ни одно значение не превысило порог, возвращаем -1
    return -1


print(find_outlier_optimized(N, K, x))