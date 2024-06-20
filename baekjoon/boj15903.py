import heapq as hp
n, m = map(int, input().split())

card = list(map(int, input().split()))



hp.heapify(card)

for _ in range(m):

    a = hp.heappop(card)
    b = hp.heappop(card)

    s = a+b

    hp.heappush(card, s)
    hp.heappush(card, s)

print(sum(card))

