n = int(input())

object = []

for _ in range(n):
    cur = list(map(int, input().split()))
    object.append(set(cur[1:]))

m = int(input())

students = []

for _ in range(m):
    tmp = list(map(int, input().split()))
    students.append(set(tmp[1:]))

for s in students:
    cnt = 0

    for o in object:
        if set.intersection(s, o) == o:
            cnt+=1

    print(cnt)