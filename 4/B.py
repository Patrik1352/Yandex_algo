# количество клеток для n-палубных кораблей

def len_for_n(n):
    h = (n**3+6*n**2+5*n-6)//6
    return h

def lbinserch(k):
    R = 5 * 10 ** 6
    L = 1
    while L < R:
        M = (R + L) // 2
        if len_for_n(M) > k:
            R = M
        else:
            L = M + 1
    return L-1

k = int(input())
print(lbinserch(k))







# print(max_k(int(input())))
