n, e, w, s, N = map(int, input().split())

answer = 0

possible = {
    "E": e/100,
    "W": w/100,
    "S": s/100,
    "N": N/100
}

moveDir = {
    "E": (0, 1),
    "W": (0, -1),
    "S": (1, 0),
    "N": (-1, 0)
}

visit = [[False for _ in range(30)] for _ in range(30)]


def solve(cx, cy, curMove, curPossible):
    global answer
    if len(curMove) == n:
        answer+=curPossible
        return 
    

    for dir in ["E", "W", "S", "N"]:
        a, b = moveDir[dir]
        nx, ny = cx+a, cy+b

        if not visit[nx][ny]:
            visit[nx][ny] = True
            solve(nx, ny, curMove+dir, curPossible*possible[dir])
            visit[nx][ny] = False

    


visit[n][n] = True
solve(n, n, "", 1)

print(answer)