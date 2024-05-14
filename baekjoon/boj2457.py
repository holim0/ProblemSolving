n = int(input())

flower = []

for _ in range(n):
    a, b, c, d = map(int, input().split())
    flower.append((a, b, c, d))

cnt = 1