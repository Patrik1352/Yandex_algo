def max_square_plus(a: list) -> int:
    """Какой размерности можно построить крест
    a - исходный массив
    возвращает максималную размерность"""
    n = 0
    for row in a:
        n += row.count('#')
    n = int((n/5)**(0.5))

    return min(n, len(a)//3, len(a[0])//3)



def plus(n):
    """Создает крест в массиве a рамером n"""
    a = ['.' * n * 3] * n * 3
    for i in range(n):
        a[i] = '.' * n + '#' * n + '.' * n

    for i in range(n, n * 2):
        a[i] = '#' * 3 * n

    for i in range(n * 2, n * 3):
        a[i] = '.' * n + '#' * n + '.' * n

    return a


def get_part(a,i,j,n):
    """Создает массив с нужным крестом, ненужные углы заменет на '.'
    a - искходный массив
    i, j - координаты верхрего левого угла,
        i - по длине
        j - по глубине
    n - сколько сторона плюса"""

    b = []


    for y in range(j, n+j):
        b.append('.' * n +a[y][i+n:i+n*2] + '.'*n)

    for y in range(n+j, n*2+j):
        b.append('#'*n*3)

    for y in range(n*2+j, n*3+j):
        b.append('.' * n + a[y][i + n :i + n * 2] + '.' * n)

    return b


# какой максимальный размер крест в теории можно посмотрить из данного массива
def anser(a):
    n = max_square_plus(a)

    while n > 1:
        # крест размером n
        b = plus(n)

        # от куда можно начать поиск
        for i in range(len(a)-n*3+1):
            for j in range(len(a[0]) - n*3+1):

                part = get_part(a,j,i,n)

                if part == b:
                    print(n)
                    return

        n -= 1
    print(1)


a = []
h, w = list(map(int, input().split()))
for g in range(h):
    a.append(input())

anser(a)


