n = int(input())

dis = []

for _ in range(n):
    s, e = map(int, input().split())
    dis.append((s, e))

dis = sorted(dis, key =lambda x: ((x[1], x[0])))
answer = 1

start, end = dis[0]

for i in range(1, len(dis)):
    cur_start, cur_end = dis[i]

    if cur_start>=end:
        answer+=1
        start = cur_start
        end= cur_end
print(answer)
