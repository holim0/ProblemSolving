import sys

sys.setrecursionlimit(10 ** 5)

input = sys.stdin.readline


def solve(i):
    global answer
    visit[i] = True
    group.append(i)
    nxt = number[i]

    if visit[nxt]:
        if nxt in group:
            answer += len(group[group.index(nxt):])
        return
    else:
        solve(nxt)


t = int(input())

for _ in range(t):
    n = int(input())
    number = [0] + list(map(int, input().split()))
    visit = [False] * (n + 1)
    answer = 0

    for i in range(1, n + 1):
        if not visit[i]:
            group = []
            solve(i)

    print(n - answer)