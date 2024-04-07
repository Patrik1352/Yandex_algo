def transform_array_with_odd(arr):
    result = []  # Результирующий массив
    combination = []
    even_product = 1  # Для накопления произведения четных чисел
    odd_product = 1  # Для накопления произведения нечетных чисел
    for num in arr:
        if num % 2 == 0:  # Четное число
            if odd_product != 1:  # Если есть накопленное произведение нечетных чисел
                combination.append('+')
                result.append(odd_product)  # Добавляем его в результат
                odd_product = 1  # Сбрасываем произведение
            else:
                combination.append('x')
            even_product = 2  # Накапливаем произведение четных чисел
        else:  # Нечетное число
            if even_product != 1:  # Если есть накопленное произведение четных чисел
                combination.append('x')
                result.append(even_product)  # Добавляем его в результат
                even_product = 1  # Сбрасываем произведение
            else:
                combination.append('x')
            odd_product = 2  # Накапливаем произведение нечетных чисел
    # После окончания цикла проверяем, осталось ли ненулевое произведение
    if even_product != 1:  # Для четных чисел
        result.append(even_product)
    if odd_product != 1:  # Для нечетных чисел
        result.append(odd_product)


    f = (len(result) + arr[0]%2) % 4
    if f in [0, 1]:
        index_plas = combination.index('+')
        combination[index_plas] = 'x'


    return ''.join(combination[1:])

n = input()
a = list(map(int, input().split(' ')))

print(transform_array_with_odd(a))
