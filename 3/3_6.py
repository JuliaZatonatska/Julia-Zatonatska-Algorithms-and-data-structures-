import bisect

n = int(input())
a = list(map(int, input().split()))
m = int(input())
q = list(map(int, input().split()))

for x in q:
    i = bisect.bisect_left(a, x)
    if i < n and a[i] == x:
        print("YES")
    else:
        print("NO")