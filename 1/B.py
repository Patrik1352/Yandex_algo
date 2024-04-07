X1, Y1 = list(map(int, input().split(':')))
X2, Y2 = list(map(int, input().split(':')))
home = int(input())

if home == 1:
    X1 = X1 * 100
    X2 = X2 * 101
    Y1 = Y1 * 101
    Y2 = Y2 * 100
    if X1+X2>Y1+Y2: print(0)
    else:
        print(((Y1+Y2)-(X1+X2)+101)//101)


else:
    X1 = X1 * 101
    X2 = X2 * 100
    Y1 = Y1 * 100
    Y2 = Y2 * 101
    if X1 + X2 > Y1 + Y2:
        print(0)
    else:
        print(((Y1 + Y2) - (X1 + X2)+100) // 100)