import sys 
input = sys.stdin.readline
r, c = map(int, input().split())

mapp = []

for _ in range(r):
    row = input()
    mapp.append(list(row))

check = [False for _ in range(100)]

answer = 0

def getSol(cx, cy, dist):

    global answer

    answer = max(answer, dist)


    for a, b in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        nx, ny = cx+a, cy+b

        if 0<=nx<r and 0<=ny<c:
            nxtValue = mapp[nx][ny]
            if not check[ord(nxtValue)]:
                check[ord(nxtValue)] = True
                getSol(nx, ny, dist+1)
                check[ord(nxtValue)] = False


start = mapp[0][0]

check[ord(start)] = True
getSol(0, 0, 1)

print(answer)