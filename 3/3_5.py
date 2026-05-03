while True:
    try:
        n = int(input())
        h = list(map(int, input().split()))
        a, b = map(int, input().split())

        cnt = [0]*101

        for x in h:
            cnt[x - 150] += 1

        s = 0
        for i in range(a, b+1):
            s += cnt[i - 150]

        print(s)
    except:
        break