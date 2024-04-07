K = int(input())

x = []
y = []
for i in range(K):
    xi, yi = list(map(int, input().split()))
    x.append(xi)
    y.append(yi)

print(f'{min(x)} {min(y)} {max(x)} {max(y)}')