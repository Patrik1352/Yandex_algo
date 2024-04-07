input()
a = input().split()
input()
b = input().split()
input()
c = input().split()

all_set = set(a+b+c)
rez = []
for i in all_set:
    if sum([i in a, i in b, i in c]) > 1:
        rez.append(int(i))

print(' '.join([str(i) for i in sorted(rez)]))