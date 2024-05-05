N = int(input())

building = list(map(int, input().split()))
answer = 0

for i in range(N):
    cnt = 0
    for j in range(i + 1, N):
        isOk = True
        for k in range(i + 1, j):
            if (building[k] - building[i]) * (j - i) >= (((building[j] - building[i]) * (k-i))):
                isOk = False
                break
        if isOk:
            cnt+=1
    for j in range(0, i):
        isOk= True
        for k in range(j + 1, i):
            if (building[k] - building[j]) * (i-j) >= (building[i] - building[j]) * (k - j):
                isOk = False
                break
        if isOk:
            cnt+=1
    answer = max(cnt, answer)
print(answer)