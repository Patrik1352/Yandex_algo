# N = 6
# a = sorted(list(map(int, '3 10 1 10 3 4'.split())))
# a.append(a[-1]+1)
# a.insert(0,a[0]-1)
# b = a[::-1]
#
#
#
# def lbinary_search(a, num):
#     left = 0
#     rigth = len(a)-1
#     while left < rigth:
#         mid = (left + rigth) // 2
#
#         if a[mid] >= num:
#             rigth = mid
#         else:
#             left = mid + 1
#     return left
#
# def rbinary_search(a, num):
#     left = 0
#     rigth = len(a)-1
#     while left < rigth:
#         mid = (left + rigth ) // 2
#         if a[mid] > num:
#             rigth = mid
#         else:
#             left = mid + 1
#     return left
#
# print(a)
# anser = []
# for i in range(int(input())):
#     L, R = map(int, input().split())
#     print(lbinary_search(a, L))
#     # print(rbinary_search(a, R))
#
# print(*anser)

def count_in_range(arr, queries):
    arr.sort()
    prefix_sums = [0]  # Начинаем с 0 для удобства расчётов
    for num in arr:
        prefix_sums.append(prefix_sums[-1] + 1)  # Каждый раз добавляем 1, т.к. это индивидуальные числа

    # Бинарный поиск для нахождения индекса начала и конца диапазона
    def binary_search(arr, x, left):
        lo, hi = 0, len(arr) - 1
        result = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if arr[mid] < x:
                lo = mid + 1
            elif arr[mid] > x:
                hi = mid - 1
            else:
                result = mid
                if left:
                    hi = mid - 1  # Ищем самое левое вхождение
                else:
                    lo = mid + 1  # Ищем самое правое вхождение
        return lo if left else hi

    # Ответы на запросы
    answers = []
    for L, R in queries:
        left_idx = binary_search(arr, L, True)
        right_idx = binary_search(arr, R, False)
        if right_idx < left_idx:  # Если правый индекс меньше левого, значит чисел в диапазоне нет
            answers.append(0)
        else:
            answers.append(prefix_sums[right_idx + 1] - prefix_sums[left_idx])

    return answers

# Тестовые данные
N = int(input())
numbers = list(map(int, input().split()))
K = int(input())
queries = [list(map(int, input().split())) for i in range(K)]

# Решение
print(*count_in_range(numbers, queries))
