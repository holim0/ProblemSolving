import sys
input = sys.stdin.readline
n = int(input())

for _ in range(n):
    t = list(map(int, input().split()))
    cnt = {}

    half = t[0]/2
    answer = "SYJKGW"
    for i in range(1, len(t)):
        cur =t[i]
        if cur not in cnt:
            cnt[cur] = 1
        else:
            cnt[cur]+=1
            if cnt[cur]>half:
                answer = cur

    print(answer)