t = int(input())

for _ in range(t):
    n = int(input())

    order = []
    answer = 0
    for _ in range(n):
        a, b = map(int, input().split())
        order.append((a, b))

    order.sort(key = lambda x: x[0])
    cnt = 0
    cur = 1e10

    for a, b in order:
        if b<cur:
            cnt+=1
            cur = b
    answer = max(answer, cnt)

    print(answer)