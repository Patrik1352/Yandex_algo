o = int(input())
for i in range(o):
    n = int(input())
    a = list(map(int, input().split()))
# if True:
#     n = 9
#     a = list(map(int,'1 1 9 2 9 9 9 5 8'.split()))
    rez = []
    min_len = n+1
    now_len = 1
    for i in a:


        if min_len > i:
            min_len = i

        if min_len == now_len:
            rez.append(now_len)
            min_len = n+1
            now_len = 0
        elif now_len > min_len:
            rez.append(now_len-1)
            now_len = 1
            min_len = i

        now_len += 1

    if now_len-1:
        rez.append(now_len-1)

    print(len(rez))
    print(' '.join(map(str, rez)))
