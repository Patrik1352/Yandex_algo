n = int(input())


def A(n):
    input()
    repaets = input().split()
    new_repaets = []
    for _ in range(n-1):
        input()
        for k in input().split():
            if k in repaets:
                new_repaets.append(k)
            else:
                continue
        if len(new_repaets) == 0:
            return 0,''
        repaets = new_repaets[:]
        new_repaets = []
    return len(repaets),' '.join(sorted(repaets))
# time-limit-exceeded 22

def A_2(n):
    repaets = {}
    for _ in range(n):
        input()
        for k in input().split():
            repaets[k] = repaets.get(k,0)+1

    anser = sorted([key for key, values in repaets.items() if values == n])
    return len(anser), ' '.join(anser)

a,b = A_2(n)
print(a)
print(b)



