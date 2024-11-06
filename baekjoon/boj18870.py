import heapq as hp

n = int(input())
number = list(map(int, input().split()))

q = []

answer = [-1] * n

for i in range(len(number)):
    cur = number[i]

    hp.heappush(q, (cur, i))


curIdx = -1
curValue = 1e10

while q:
    cur, targetIdx = hp.heappop(q)
    
    if cur == curValue:
        answer[targetIdx] = curIdx
    else:
        curIdx+=1
        answer[targetIdx] = curIdx
        curValue = cur
for a in answer:
    print(a, end=" ")