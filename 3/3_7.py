n = int(input())
a = list(map(int, input().split()))

d = {}
for x in a:
    d[x] = d.get(x, 0) + 1

m = int(input())
q = list(map(int, input().split()))

for x in q:
    print(d.get(x, 0))