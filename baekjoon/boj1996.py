n = int(input())

d = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

mapp = []
answer_map = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(n):
    line = list(input())
    mapp.append(line)

for i in range(n):
    for j in range(n):
        if mapp[i][j] == ".":
            cnt = 0
            for x, y in d:
                nx, ny = i+x, j+y
                if 0<=nx<n and 0<=ny<n and mapp[nx][ny] != ".":
                    cnt += int(mapp[nx][ny])
            
            if cnt >=10:
                answer_map[i][j] = "M"
            else:
                answer_map[i][j] = str(cnt)
        else:
            answer_map[i][j] = "*"

for i in range(n):
    print("".join(answer_map[i]))