n = int(input())
b = bin(n)[2:]
k = len(b)
m = 0

for i in range(k):
    b = b[1:] + b[0]
    m = max(m, int(b, 2))

print(m)