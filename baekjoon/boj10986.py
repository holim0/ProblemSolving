n, m = map(int, input().split())

num = list(map(int, input().split()))


acc= []

remain = [0] * m

for i in range(len(num)):
    if i==0:
        acc.append(num[0])

    else:
        acc.append(acc[-1] + num[i])

for i in range(len(acc)):
    mod = acc[i]%m

    remain[mod]+=1

answer = remain[0]

for r in remain:
    if r!=0:

        answer +=(r * (r-1))//2

print(answer)

