left = 0.0
right = 10.0

for _ in range(100):
    mid = (left + right) / 2
    if mid**3 + mid + 1 > 5:
        right = mid
    else:
        left = mid

print(f"Найменше x: {left:.6f}")