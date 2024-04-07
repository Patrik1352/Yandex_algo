def true(n, m, platoons, raids):
    def optimize_raid_planning(n, platoons, counts, summ):
        for start_serch in range(n - counts):
            # print(start_serch)
            summm = sum(platoons[start_serch:start_serch + counts])
            if summm == summ:
                return start_serch + 1
            elif summm > summ:
                return -1
    rez = []
    for counts, summ in raids:
        counts = int(counts)
        summ = int(summ)
        # counts, summ = map(int, input().split())
        rez.append(optimize_raid_planning(n, platoons, counts, summ))
    return rez

def find_starting_platoon(n, m, platoons, raids):
    """
    Finds the starting platoon for each raid if possible.

    :param n: Number of platoons
    :param m: Number of raids
    :param platoons: Number of orcs in each platoon
    :param raids: List of tuples (l, s) for each raid
    :return: List of starting platoon numbers or -1 if not possible
    """
    results = []
    # Precompute the prefix sums for quick range sum calculation
    prefix_sums = [0]
    for orc_count in platoons:
        prefix_sums.append(prefix_sums[-1] + orc_count)

    for l, s in raids:
        l, s = int(l), int(s)
        found = False
        for start in range(n - l + 1):
            sum_orcs = prefix_sums[start + l] - prefix_sums[start]
            if sum_orcs == s:
                found = True
                results.append(start + 1)  # Arrays are 0-indexed, platoons are 1-indexe
                break
            if sum_orcs > s:
                results.append(-1)
                found = True
                break
        if not found:
            results.append(-1)



    return results

# with open('input.txt', 'r') as file:
#     lines = file.readlines()
#
# n, m = map(int, lines[0].rstrip().split())
# platoons = list(map(int, lines[1].rstrip().split()))
# raids =  list(map(lambda x: x.rstrip().split(), lines[2:]))
# for i in find_starting_platoon(n, m, platoons, raids):
#     print(i)


def find_starting_platoon_optimized(n, m, platoons, raids):
    results = []
    prefix_sums = [0]
    for orc_count in platoons:
        prefix_sums.append(prefix_sums[-1] + orc_count)

    for l, s in raids:
        found = False
        left, right = 0, n - l
        while left <= right:
            mid = (left + right) // 2
            sum_orcs = prefix_sums[mid + l] - prefix_sums[mid]
            if sum_orcs == s:
                results.append(mid + 1)  # Найдено точное совпадение
                found = True
                break
            elif sum_orcs < s:
                left = mid + 1
            else:
                right = mid - 1

        if not found:
            results.append(-1)

    return results

# Поскольку входные данные для функции raids уже должны быть в целочисленном формате,
# убедитесь, что они преобразуются корректно перед вызовом функции.
with open('input.txt', 'r') as file:
    lines = file.readlines()

n, m = map(int, lines[0].rstrip().split())
platoons = list(map(int, lines[1].rstrip().split()))
raids =  list(map(lambda x: x.rstrip().split(), lines[2:]))
raids = [(int(l), int(s)) for l, s in raids]


# Теперь можно вызвать оптимизированную функцию
for i in find_starting_platoon_optimized(n, m, platoons, raids):
    print(i)
