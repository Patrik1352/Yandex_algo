n, k = list(map(int,input().split()))
a = input().split()

def repeat_number(a,k):
    for i in range(len(a)-k):
        if len(set(a[i:i+k+1])) != k+1:
            return 'YES'
    return 'NO'

def repeat_number_2(a,k):
    for i in range((len(a)-k)//2):
        if a[i:i+k+1].count(a[i]) != 1:
            return 'YES'
        if a[-(i+k+2):-(i+1)].count(a[-i-1]) != 1:
            return 'YES'
    if a[-(k+1):].count(a[-1]) != 1: return 'YES'
    return 'NO'


from collections import defaultdict
def repeat_number_optimized(a, k):
    window_count = defaultdict(int)

    # Заполняем начальное окно и счетчик
    for i in range(k + 1):
        window_count[a[i]] += 1

    # Проверяем начальное окно
    if len(window_count) != k + 1:
        return 'YES'

    # Проходим по оставшимся элементам
    for i in range(k + 1, len(a)):
        # Удаляем элемент, который "вышел" из окна
        window_count[a[i - k - 1]] -= 1
        if window_count[a[i - k - 1]] == 0:
            del window_count[a[i - k - 1]]

        # Добавляем новый элемент, который "вошел" в окно
        window_count[a[i]] += 1

        # Проверяем условие наличия дубликатов
        if len(window_count) != k + 1:
            return 'YES'

    return 'NO'

def find_repeated_within_k(n, k, sequence):
    last_indexes = {}  # Словарь для хранения последних индексов каждого числа
    for i, num in enumerate(sequence):
        if num in last_indexes and i - last_indexes[num] <= k:
            # Нашли повторяющееся число на расстоянии не более k
            return "YES"
        last_indexes[num] = i  # Обновляем последний индекс для текущего числа
    return "NO"

print(find_repeated_within_k(n,k,a))