# N, K = list(map(int, input().split()))
# prices = list(map(int, input().split()))

def fast_but_not_work(N,K,prices):
    if N == 1:
        return 0
    max_stoncs = 0
    for i in range(len(prices)-K):
        stonc = max(prices[i+1:i+K+1]) - prices[i]
        if stonc > max_stoncs:
            max_stoncs = stonc

    for i in range(i+1,i+K+1):
        stonc = prices[i] - max(prices[i:])
        if stonc > max_stoncs:
            max_stoncs = stonc

    return max_stoncs

def slow_but_work(N,K,prices):
    if N == 1:
        return 0
    max_stoncs = 0
    prices = prices+[0]*K
    for i in range(len(prices)-K):
        stonc = max(prices[i + 1:i + K + 1]) - prices[i]
        if stonc > max_stoncs:
            max_stoncs = stonc
    return max_stoncs

# print(slow_but_work(N,K,prices))

assert slow_but_work(5 ,2,[1, 2, 3, 4, 5]) == 2
assert slow_but_work(5 ,2,[5, 4 ,3 ,2 ,1]) == 0
assert slow_but_work(10,2,[8 ,3, 2, 3, 2, 1, 10, 5, 4 ,2]) == 9
