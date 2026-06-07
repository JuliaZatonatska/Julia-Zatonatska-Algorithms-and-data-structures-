import math

left = 1.6
right = 3.0

for _ in range(100):
    mid = (left + right) / 2
    if math.sin(mid) - mid / 3 < 0:
        right = mid
    else:
        left = mid

print(f"Корінь рівняння x: {left:.6f}")