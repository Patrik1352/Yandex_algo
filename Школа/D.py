T = int(input())
K = list(map(int, input().split()))

def divide_round_up(dividend, divisor):
    result = dividend // divisor  # Целая часть от деления
    remainder = dividend % divisor  # Остаток от деления

    if remainder > 0:  # Если остаток больше нуля, добавляем единицу к результату
        result += 1

    return result

def fed(T,K):
    if len(K) == T: return max(K)
    for speed in range(1,max(K)+1):
        need_time = sum(map(lambda x: divide_round_up(x,speed), K))
        if need_time<=T:
            return speed

# T = int(input())
# K = list(map(int, input().split()))

def is_possible(speed, T, K):
    total_days_needed = sum((task + speed - 1) // speed for task in K)
    return total_days_needed <= T

def find_min_speed(T, K):
    left, right = 1, max(max(K), sum(K) // T + 1)
    while left < right:
        mid = (left + right) // 2
        if is_possible(mid, T, K):
            right = mid
        else:
            left = mid + 1
    return left

print(find_min_speed(T, K))

# print(fed(T,K))