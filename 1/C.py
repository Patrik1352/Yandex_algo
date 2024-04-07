n = int(input())

s = 0
for _ in range(n):
    a = int(input())
    if a == 0:
        s+=0
    hui = 0
    if  a%4 == 1:
        hui = 1
    elif a%4 == 2 or a%4 == 3:
        hui = 2
    s += a//4+hui

print(s)