
left = 0.0
right = 2.0

for _ in range(100):
    mid = (left + right) / 2
    if mid**3 + 4 * mid**2 + mid - 6 > 0:
        right = mid
    else:
        left = mid

print(f"Корінь рівняння x: {left:.6f}")