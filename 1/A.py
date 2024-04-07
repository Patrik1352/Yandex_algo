x1, y1 = list(map(int, input().split(':')))
x2, y2 = list(map(int, input().split(':')))
home = int(input())
gool = 0

def soccer_sucks(x1, y1, x2, y2, home):
    new_x2 = x2
    while x1+new_x2 < y1 + y2:
        new_x2 += 1
    # счет сравняли

    if home == 2:
        if y1<=y2:
            return new_x2+1
        else:
            return new_x2
    else:
        return new_x2 + 1


print(soccer_sucks(x1, y1, x2, y2, home))