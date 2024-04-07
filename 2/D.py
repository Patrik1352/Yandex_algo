K = int(input())

tabel = []
for _ in range(10):
    tabel.append([0]*10)


dx = (0,1,0,-1)
dy = (1,0,-1,0)
coord = []
for _ in range(K):
    x, y = list(map(int, input().split()))
    coord.append((x,y))
    for neq_x, neq_y in zip(dx,dy):
        tabel[neq_x+x][neq_y+y] += 1

for x,y in coord:
    tabel[x][y] = 0

print(sum([sum(x) for x in tabel]))
