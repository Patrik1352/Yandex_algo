# n, m = list(map(int, input().split()))
#
# tabel = []
# first = 0
# second = -1
# index_first = [-1,-1]
# index_second = [-1,-1]
# for i in range(n):
#     f = list(map(int, input().split()))
#     tabel.append(f)
#     iter_max = max(f)
#     if iter_max>second:
#         new_max_index = [i, f.index(iter_max)]
#         if iter_max>=first:
#             first, second = iter_max, first
#             index_first, index_second = new_max_index, index_first[:]
#         else:
#             second = iter_max
#             index_second = new_max_index
#     elif iter_max==second:
#         pass
#
#
# tabel[index_second[0]][index_second[1]] = 0
# tabel[index_first[0]][index_first[1]] = 0
#
#
# if index_second[0]==index_first[0]:
#     for col in range(n):
#
# elif index_second[1]==index_first[1]:
#     for row in range(m):
#         iter_max = max(row)
#         if iter_max > second:
#
#
# a = max([tabel[i][index_first[1]] for i in range(n)]+tabel[index_second[0]])
# b = max([tabel[i][index_second[1]] for i in range(n)]+tabel[index_first[0]])
#
# if b>a:
#     print(f'{index_first[0]+1} {index_second[1]+1}')
# else:
#     print(f'{index_second[0]+1} {index_first[1]+1}')
#
#
#
#
def forbid_race_and_class(races_strengths):
    # Поиск максимальной силы персонажа для каждой расы
    max_strength_per_race = [max(race) for race in races_strengths]
    # Поиск максимальной силы персонажа для каждого класса
    max_strength_per_class = [max(strength) for strength in zip(*races_strengths)]

    # Определение расы и класса к запрету
    race_to_forbid = max_strength_per_race.index(max(max_strength_per_race)) + 1
    class_to_forbid = max_strength_per_class.index(max(max_strength_per_class)) + 1

    return race_to_forbid, class_to_forbid


# Пример 1
n, m = 2, 2
strengths_1 = [
    [1, 2],
    [3, 4]
]
# Пример 2
n2, m2 = 4,5
strengths_2 = [[999999997, 1, 2, 3, 4],
 [10, 2, 1000000000, 1, 7],
 [3, 9, 999999999, 5, 10],
 [1, 7, 3, 999999998, 6]]

result_1 = forbid_race_and_class(strengths_1)
result_2 = forbid_race_and_class(strengths_2)

print(result_1, result_2)
